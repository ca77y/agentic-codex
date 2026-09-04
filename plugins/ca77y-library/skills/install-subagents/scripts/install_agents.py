#!/usr/bin/env python3
"""Validate and install ca77y-library custom Codex agents."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import tempfile
import tomllib


MARKER = "# managed-by: ca77y-library\n"
REQUIRED = {"name", "description", "manual"}
ALLOWED = REQUIRED


def resources() -> list[Path]:
    root = Path(__file__).resolve().parents[1] / "resources"
    return sorted(root.glob("*.toml"))


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


def install(paths: list[Path]) -> None:
    target = Path.home() / ".codex" / "agents"
    conflicts: list[Path] = []
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
            continue
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=target, delete=False) as handle:
            handle.write(content)
            temporary = Path(handle.name)
        os.chmod(temporary, 0o644)
        os.replace(temporary, destination)
        print(f"installed {destination}")

    current = {source.name for source in paths}
    for destination in sorted(target.glob("*.toml")):
        if destination.name in current:
            continue
        if destination.read_text(encoding="utf-8").startswith(MARKER):
            destination.unlink()
            print(f"removed {destination}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate without installing")
    args = parser.parse_args()
    paths = resources()
    validate(paths)
    if args.check:
        print(f"validated {len(paths)} ca77y-library custom agents")
        return
    install(paths)


if __name__ == "__main__":
    main()
