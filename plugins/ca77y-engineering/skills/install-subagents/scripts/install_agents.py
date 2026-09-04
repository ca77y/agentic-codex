#!/usr/bin/env python3
"""Validate and install ca77y-engineering custom Codex agents."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import tomllib


MARKER = "# managed-by: ca77y-engineering\n"
REQUIRED = {"name", "description", "manual"}
ALLOWED = REQUIRED
PROOF_HEADING = "## Agent-definition refresh proof"
PROOF_CHECK = "- `--check`: passed before installation"
PROOF_INSTALL = "- install: completed for every managed TOML"
PROOF_CONFIRMATION = "- post-install new-task confirmation: pending replacement lead"
PROOF_AGENTS_HEADING = "- managed agents:"
PROOF_AGENTS_COMPLETE = "- managed-agent records: complete"
AGENT_PROOF_PATTERN = re.compile(
    r"  - `(?P<name>[^`]+)`: (?P<action>installed|unchanged); "
    r"source `(?P<source>[^`]+)`; installed `(?P<destination>[^`]+)`; "
    r"source sha256 `(?P<source_sha256>[0-9a-f]{64})`; "
    r"compiled sha256 `(?P<compiled_sha256>[0-9a-f]{64})`; "
    r"installed sha256 `(?P<installed_sha256>[0-9a-f]{64})`"
)


def resources() -> list[Path]:
    root = Path(__file__).resolve().parents[1] / "resources"
    return sorted(root.glob("*.toml"))


def plugin_root() -> Path:
    return Path(__file__).resolve().parents[3]


def identity_files() -> list[Path]:
    root = plugin_root()
    source_roots = [root / "agents", root / "skills" / "install-subagents"]
    missing = [path for path in source_roots if not path.is_dir()]
    if missing:
        joined = ", ".join(str(path) for path in missing)
        raise SystemExit(f"source identity unavailable; missing source roots: {joined}")
    files = {
        path
        for source_root in source_roots
        for path in source_root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    }
    if not files:
        raise SystemExit("source identity unavailable; no source files found")
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_digest() -> str:
    root = plugin_root()
    digest = hashlib.sha256()
    for path in identity_files():
        relative = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        digest.update(b"\0")
    return digest.hexdigest()


def git_revision() -> str:
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


def source_identity() -> str:
    package = package_digest()
    revision = git_revision()
    if revision == "unavailable":
        return f"package-sha256:{package}"
    return f"git:{revision}; package-sha256:{package}"


def expected_proof_agents(paths: list[Path]) -> dict[str, dict[str, str]]:
    expected: dict[str, dict[str, str]] = {}
    target = Path.home() / ".codex" / "agents"
    for source in paths:
        content = compiled_agent(source)
        name = str(tomllib.loads(content)["name"])
        compiled_sha256 = hashlib.sha256(content.encode("utf-8")).hexdigest()
        expected[name] = {
            "source": str(source.resolve()),
            "destination": str((target / source.name).resolve()),
            "source_sha256": sha256(source),
            "compiled_sha256": compiled_sha256,
            "installed_sha256": compiled_sha256,
        }
    return expected


def proof_value(line: str, label: str, ledger_path: Path) -> str:
    prefix = f"- {label}: `"
    if not line.startswith(prefix) or not line.endswith("`"):
        raise SystemExit(f"refresh proof has malformed {label}: {ledger_path}")
    return line[len(prefix) : -1]


def verify_refresh_proof(ledger_path: Path, identity: str, paths: list[Path]) -> None:
    validate_ledger_path(ledger_path)
    lines = ledger_path.read_text(encoding="utf-8").splitlines()
    headings = [index for index, line in enumerate(lines) if line == PROOF_HEADING]
    if not headings:
        raise SystemExit(f"refresh proof missing from ledger: {ledger_path}")
    start = headings[-1]
    end = next(
        (index for index in range(start + 1, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    section = lines[start + 1 : end]
    while section and not section[-1]:
        section.pop()
    expected_agents = expected_proof_agents(paths)
    expected_length = 6 + len(expected_agents) + 1
    if len(section) != expected_length:
        raise SystemExit(
            f"refresh proof schema is incomplete or has extra records: "
            f"expected {expected_length} lines, found {len(section)} in {ledger_path}"
        )

    recorded = proof_value(section[0], "source identity", ledger_path)
    if recorded != identity:
        raise SystemExit(
            f"refresh proof source identity does not match current sources: {recorded} != {identity}"
        )

    installer = proof_value(section[1], "installer", ledger_path)
    expected_installer = str(Path(__file__).resolve())
    if installer != expected_installer:
        raise SystemExit(
            f"refresh proof installer does not match current installer: "
            f"{installer} != {expected_installer}"
        )
    fixed_records = [PROOF_CHECK, PROOF_INSTALL, PROOF_CONFIRMATION, PROOF_AGENTS_HEADING]
    if section[2:6] != fixed_records:
        raise SystemExit(f"refresh proof has malformed check, install, or managed-agent records: {ledger_path}")
    if section[-1] != PROOF_AGENTS_COMPLETE:
        raise SystemExit(f"refresh proof has no managed-agent completion record: {ledger_path}")

    agent_lines = section[6:-1]
    actual_agents: dict[str, dict[str, str]] = {}
    for line in agent_lines:
        match = AGENT_PROOF_PATTERN.fullmatch(line)
        if match is None:
            raise SystemExit(f"refresh proof has malformed managed-agent entry: {line}")
        fields = match.groupdict()
        name = fields.pop("name")
        fields.pop("action")
        if name in actual_agents:
            raise SystemExit(f"refresh proof has duplicate managed agent: {name}")
        actual_agents[name] = fields

    if set(actual_agents) != set(expected_agents):
        missing = sorted(set(expected_agents) - set(actual_agents))
        extra = sorted(set(actual_agents) - set(expected_agents))
        raise SystemExit(
            f"refresh proof managed-agent set does not match current resources; "
            f"missing {missing}, extra {extra}"
        )
    for name, expected in expected_agents.items():
        actual = actual_agents[name]
        if actual != expected:
            raise SystemExit(
                f"refresh proof fields do not match current compiled agent {name}: "
                f"{actual} != {expected}"
            )
        destination = Path(expected["destination"])
        if not destination.is_file() or sha256(destination) != expected["compiled_sha256"]:
            raise SystemExit(f"installed agent does not match current compiled output: {destination}")
    print(f"refresh proof verified for {len(expected_agents)} managed agents: {ledger_path}")


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


def append_refresh_proof(ledger_path: Path, identity: str, results: list[dict[str, str]]) -> None:
    validate_ledger_path(ledger_path)
    lines = [
        "",
        PROOF_HEADING,
        f"- source identity: `{identity}`",
        f"- installer: `{Path(__file__).resolve()}`",
        PROOF_CHECK,
        PROOF_INSTALL,
        PROOF_CONFIRMATION,
        PROOF_AGENTS_HEADING,
    ]
    for result in results:
        lines.extend(
            [
                f"  - `{result['name']}`: {result['action']}; source `{result['source']}`; installed `{result['destination']}`; source sha256 `{result['source_sha256']}`; compiled sha256 `{result['compiled_sha256']}`; installed sha256 `{result['installed_sha256']}`",
            ]
        )
    lines.extend([PROOF_AGENTS_COMPLETE, ""])
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
    parser.add_argument(
        "--verify-ledger-path",
        type=Path,
        help="read-only absolute story-worktree ledger path whose refresh proof should be verified",
    )
    args = parser.parse_args()
    paths = resources()
    validate(paths)
    identity = source_identity()
    if args.verify_ledger_path is not None:
        if args.check or args.ledger_path is not None:
            raise SystemExit("--verify-ledger-path cannot be combined with installation options")
        verify_refresh_proof(args.verify_ledger_path, identity, paths)
        return
    if args.check:
        if args.ledger_path is not None:
            raise SystemExit("--ledger-path requires installation, not --check")
        print(f"validated {len(paths)} ca77y-engineering custom agents")
        return
    if args.ledger_path is not None:
        validate_ledger_path(args.ledger_path)
    results = install(paths)
    if args.ledger_path is not None:
        append_refresh_proof(args.ledger_path, identity, results)


if __name__ == "__main__":
    main()
