#!/usr/bin/env python3
"""Validate and install ca77y-engineering custom Codex agents."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import tomllib


MARKER = "# managed-by: ca77y-engineering\n"
REQUIRED = {"name", "description", "manual"}
ALLOWED = REQUIRED


def resources() -> list[Path]:
    root = Path(__file__).resolve().parents[1] / "resources"
    return sorted(root.glob("*.toml"))


def plugin_root() -> Path:
    return Path(__file__).resolve().parents[3]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_revision() -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(plugin_root()), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unavailable"
    revision = result.stdout.strip()
    return revision or "unavailable"


def source_data(path: Path) -> dict[str, object]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith(MARKER):
        raise SystemExit(f"missing managed marker: {path}")
    data = tomllib.loads(raw)
    missing = REQUIRED - data.keys()
    if missing:
        raise SystemExit(f"missing {sorted(missing)}: {path}")
    extra = data.keys() - ALLOWED
    if extra:
        raise SystemExit(f"unsupported source settings {sorted(extra)}: {path}")
    return data


def resolve_manual(path: Path, value: object) -> Path:
    if not isinstance(value, str) or not value:
        raise SystemExit(f"invalid manual path: {path}")
    manual = (path.parent / value).resolve()
    plugin_root = path.resolve().parents[3]
    try:
        manual.relative_to(plugin_root)
    except ValueError:
        raise SystemExit(f"manual escapes plugin root: {path}") from None
    if not manual.is_file() or manual.name not in {"AGENT.md", "SKILL.md"}:
        raise SystemExit(f"missing agent manual: {manual}")
    return manual


def without_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0] == "---":
        try:
            end = lines.index("---", 1)
        except ValueError:
            raise SystemExit("unterminated manual frontmatter") from None
        lines = lines[end + 1 :]
    return "\n".join(lines).strip()


def compiled_instructions(manual: Path) -> str:
    sections = [
        "Your complete role procedure and required references are embedded in this custom-agent definition. Follow them directly; do not invoke or load a skill to define your role. When the procedure says to read a references/<file> path, use the matching embedded reference below. A reference that mentions SKILL.md means the embedded role procedure.",
        without_frontmatter(manual.read_text(encoding="utf-8")),
    ]
    reference_root = manual.parent / "references"
    if reference_root.is_dir():
        for reference in sorted(reference_root.rglob("*.md")):
            label = reference.relative_to(manual.parent).as_posix()
            sections.append(
                f"# Embedded reference: {label}\n\n"
                + reference.read_text(encoding="utf-8").strip()
            )
    return "\n\n".join(sections).strip() + "\n"


def compiled_agent(path: Path) -> str:
    data = source_data(path)
    name = data["name"]
    description = data["description"]
    if not isinstance(name, str) or not name:
        raise SystemExit(f"invalid agent name: {path}")
    if not isinstance(description, str) or not description:
        raise SystemExit(f"invalid agent description: {path}")
    manual = resolve_manual(path, data["manual"])
    instructions = compiled_instructions(manual)
    return (
        MARKER
        + f"name = {json.dumps(name)}\n"
        + f"description = {json.dumps(description)}\n"
        + f"developer_instructions = {json.dumps(instructions)}\n"
    )


def validate(paths: list[Path]) -> None:
    if not paths:
        raise SystemExit("no agent resources found")
    names: set[str] = set()
    for path in paths:
        data = source_data(path)
        name = data["name"]
        if not isinstance(name, str) or not name:
            raise SystemExit(f"invalid agent name: {path}")
        if name in names:
            raise SystemExit(f"duplicate agent name: {name}")
        names.add(name)
        installed = tomllib.loads(compiled_agent(path))
        if set(installed) != {"name", "description", "developer_instructions"}:
            raise SystemExit(f"invalid compiled agent settings: {path}")


def install(paths: list[Path]) -> list[dict[str, str]]:
    target = Path.home() / ".codex" / "agents"
    conflicts: list[Path] = []
    results: list[dict[str, str]] = []
    for source in paths:
        destination = target / source.name
        content = compiled_agent(source)
        if destination.exists():
            existing = destination.read_text(encoding="utf-8")
            if existing != content and not existing.startswith(MARKER):
                conflicts.append(destination)
    if conflicts:
        joined = "\n".join(str(path) for path in conflicts)
        raise SystemExit(f"refusing to overwrite unmanaged agent definitions:\n{joined}")

    target.mkdir(parents=True, exist_ok=True)
    for source in paths:
        destination = target / source.name
        content = compiled_agent(source)
        if destination.exists() and destination.read_text(encoding="utf-8") == content:
            print(f"unchanged {destination}")
            action = "unchanged"
        else:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=target, delete=False) as handle:
                handle.write(content)
                temporary = Path(handle.name)
            os.chmod(temporary, 0o644)
            os.replace(temporary, destination)
            print(f"installed {destination}")
            action = "installed"
        results.append(
            {
                "name": str(tomllib.loads(compiled_agent(source))["name"]),
                "source": str(source.resolve()),
                "destination": str(destination.resolve()),
                "action": action,
                "source_sha256": sha256(source),
                "compiled_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                "installed_sha256": sha256(destination),
            }
        )

    current = {source.name for source in paths}
    for destination in sorted(target.glob("*.toml")):
        if destination.name in current:
            continue
        if destination.read_text(encoding="utf-8").startswith(MARKER):
            destination.unlink()
            print(f"removed {destination}")
    return results


def validate_ledger_path(ledger_path: Path) -> None:
    if not ledger_path.is_absolute():
        raise SystemExit(f"ledger path must be absolute: {ledger_path}")
    if not ledger_path.parent.is_dir():
        raise SystemExit(f"ledger parent does not exist: {ledger_path.parent}")


def append_refresh_proof(ledger_path: Path, results: list[dict[str, str]]) -> None:
    validate_ledger_path(ledger_path)
    lines = [
        "",
        "## Agent-definition refresh proof",
        f"- source revision: `{source_revision()}`",
        f"- installer: `{Path(__file__).resolve()}`",
        "- `--check`: passed before installation",
        "- install: completed for every managed TOML",
        "- post-install new-task confirmation: pending replacement lead",
        "- managed agents:",
    ]
    for result in results:
        lines.extend(
            [
                f"  - `{result['name']}`: {result['action']}; source `{result['source']}`; installed `{result['destination']}`; source sha256 `{result['source_sha256']}`; compiled sha256 `{result['compiled_sha256']}`; installed sha256 `{result['installed_sha256']}`",
            ]
        )
    lines.append("")
    with ledger_path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    print(f"refresh proof written to {ledger_path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate without installing")
    parser.add_argument(
        "--ledger-path",
        type=Path,
        help="absolute story-worktree ledger path to receive the refresh proof",
    )
    args = parser.parse_args()
    paths = resources()
    validate(paths)
    if args.check:
        if args.ledger_path is not None:
            raise SystemExit("--ledger-path requires installation, not --check")
        print(f"validated {len(paths)} ca77y-engineering custom agents")
        return
    if args.ledger_path is not None:
        validate_ledger_path(args.ledger_path)
    results = install(paths)
    if args.ledger_path is not None:
        append_refresh_proof(args.ledger_path, results)


if __name__ == "__main__":
    main()
