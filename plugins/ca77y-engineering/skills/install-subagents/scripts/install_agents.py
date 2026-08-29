#!/usr/bin/env python3
"""Validate and install ca77y-engineering custom Codex agents."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import tempfile
import tomllib


MARKER = "# managed-by: ca77y-engineering\n"
REQUIRED = {"name", "description", "developer_instructions"}


def resources() -> list[Path]:
    root = Path(__file__).resolve().parents[1] / "resources"
    return sorted(root.glob("*.toml"))


def validate(paths: list[Path]) -> None:
    if not paths:
        raise SystemExit("no agent resources found")
    names: set[str] = set()
    for path in paths:
        raw = path.read_text(encoding="utf-8")
        if not raw.startswith(MARKER):
            raise SystemExit(f"missing managed marker: {path}")
        data = tomllib.loads(raw)
        missing = REQUIRED - data.keys()
        if missing:
            raise SystemExit(f"missing {sorted(missing)}: {path}")
        name = data["name"]
        if not isinstance(name, str) or not name:
            raise SystemExit(f"invalid agent name: {path}")
        if name in names:
            raise SystemExit(f"duplicate agent name: {name}")
        names.add(name)


def install(paths: list[Path]) -> None:
    target = Path.home() / ".codex" / "agents"
    conflicts: list[Path] = []
    for source in paths:
        destination = target / source.name
        if destination.exists():
            existing = destination.read_text(encoding="utf-8")
            if existing != source.read_text(encoding="utf-8") and not existing.startswith(MARKER):
                conflicts.append(destination)
    if conflicts:
        joined = "\n".join(str(path) for path in conflicts)
        raise SystemExit(f"refusing to overwrite unmanaged agent definitions:\n{joined}")

    target.mkdir(parents=True, exist_ok=True)
    for source in paths:
        destination = target / source.name
        content = source.read_text(encoding="utf-8")
        if destination.exists() and destination.read_text(encoding="utf-8") == content:
            print(f"unchanged {destination}")
            continue
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=target, delete=False) as handle:
            handle.write(content)
            temporary = Path(handle.name)
        os.chmod(temporary, 0o644)
        os.replace(temporary, destination)
        print(f"installed {destination}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate without installing")
    args = parser.parse_args()
    paths = resources()
    validate(paths)
    if args.check:
        print(f"validated {len(paths)} ca77y-engineering custom agents")
        return
    install(paths)


if __name__ == "__main__":
    main()
