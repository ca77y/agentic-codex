#!/usr/bin/env python3
"""Install core agent procedures and on-demand references (Python 3.11+)."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import tempfile
import tomllib


PLUGIN = json.loads((Path(__file__).resolve().parents[3] / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))["name"]
MARKER = f"# managed-by: {PLUGIN}\n"
REFERENCE_MARKER = f"<!-- managed-by: {PLUGIN} -->\n"
REQUIRED = {"name", "description", "manual"}


def resources() -> list[Path]:
    return sorted((Path(__file__).resolve().parents[1] / "resources").glob("*.toml"))


def source_data(path: Path) -> dict[str, object]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith(MARKER):
        raise SystemExit(f"missing managed marker: {path}")
    data = tomllib.loads(raw)
    if REQUIRED - data.keys():
        raise SystemExit(f"missing {sorted(REQUIRED - data.keys())}: {path}")
    if data.keys() - REQUIRED:
        raise SystemExit(f"unsupported source settings {sorted(data.keys() - REQUIRED)}: {path}")
    for field in REQUIRED:
        if not isinstance(data[field], str) or not data[field].strip():
            raise SystemExit(f"invalid {field}: {path}")
    return data


def resolve_manual(path: Path, value: str) -> Path:
    manual = (path.parent / value).resolve()
    if not manual.is_relative_to(path.resolve().parents[3]):
        raise SystemExit(f"manual escapes plugin root: {path}")
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


def build(paths: list[Path], target: Path) -> dict[Path, str]:
    if not paths:
        raise SystemExit("no agent resources found")
    files: dict[Path, str] = {}
    names: set[str] = set()
    for source in paths:
        data = source_data(source)
        if data["name"] in names:
            raise SystemExit(f"duplicate agent name: {data['name']}")
        names.add(data["name"])
        manual = resolve_manual(source, data["manual"])
        base = target / f".{PLUGIN}" / source.stem
        instructions = (
            "Your core role procedure follows. Follow it directly; do not load a skill to define your role. "
            f"Read references only when the procedure calls for them. Resolve references/<file> under {base}. "
            "Resolve relative links inside a reference from that reference's directory. "
            "A reference to AGENT.md or SKILL.md as the role procedure means the core procedure below.\n\n"
            + without_frontmatter(manual.read_text(encoding="utf-8")) + "\n"
        )
        for reference in sorted((manual.parent / "references").rglob("*.md")):
            if not reference.resolve().is_relative_to(source.resolve().parents[3]):
                raise SystemExit(f"reference escapes plugin root: {reference}")
            files[base / reference.relative_to(manual.parent)] = (
                REFERENCE_MARKER + reference.read_text(encoding="utf-8")
            )
        files[target / source.name] = (
            MARKER
            + f"name = {json.dumps(data['name'])}\n"
            + f"description = {json.dumps(data['description'])}\n"
            + f"developer_instructions = {json.dumps(instructions)}\n"
        )
    return files


def safe_destination(path: Path, target: Path) -> bool:
    for ancestor in (path, *path.parents):
        if ancestor.is_symlink() or (ancestor != path and ancestor.exists() and not ancestor.is_dir()):
            return False
        if ancestor == target:
            break
    return not path.exists() or path.is_file()


def owned(path: Path, target: Path) -> bool:
    marker = MARKER if path.parent == target else REFERENCE_MARKER
    return path.read_bytes().startswith(marker.encode())


def stale_files(files: dict[Path, str], target: Path) -> list[Path]:
    candidates = [*target.glob("*.toml"), *(target / f".{PLUGIN}").rglob("*")]
    return sorted(path for path in candidates if path not in files
                  and safe_destination(path, target) and path.is_file() and owned(path, target))


def install(files: dict[Path, str], target: Path, check: bool = False) -> None:
    conflicts = [path for path in files if not safe_destination(path, target)
                 or (path.exists() and not owned(path, target))]
    if conflicts:
        raise SystemExit("refusing to overwrite unmanaged or unsafe paths:\n" + "\n".join(map(str, conflicts)))
    stale = stale_files(files, target)
    changed = [path for path, content in files.items()
               if not path.exists() or path.read_bytes() != content.encode("utf-8")]
    if check:
        if changed or stale:
            raise SystemExit("installed files differ:\n" + "\n".join(map(str, changed + stale)))
        print(f"installed {PLUGIN} agents and references are current")
        return
    for destination, content in files.items():
        if destination not in changed:
            print(f"unchanged {destination}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=destination.parent, delete=False) as handle:
            handle.write(content)
            temporary = Path(handle.name)
        os.chmod(temporary, 0o644)
        os.replace(temporary, destination)
        print(f"installed {destination}")
    for destination in stale:
        destination.unlink()
        print(f"removed {destination}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="validate sources without installing")
    mode.add_argument("--check-installed", action="store_true", help="report installation drift without writes")
    parser.add_argument("--target", type=Path, default=Path.home() / ".codex" / "agents", help="installation directory")
    args = parser.parse_args()
    target = args.target.expanduser().absolute()
    paths = resources()
    files = build(paths, target)
    if args.check:
        print(f"validated {len(paths)} {PLUGIN} custom agents")
        return
    install(files, target, check=args.check_installed)


if __name__ == "__main__":
    main()
