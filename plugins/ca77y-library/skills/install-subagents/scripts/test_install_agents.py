"""Installer behavior uses temporary sources and destinations only."""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import tomllib
import unittest


SCRIPT = Path(__file__).with_name("install_agents.py")
PLUGIN = json.loads((SCRIPT.resolve().parents[3] / ".codex-plugin/plugin.json").read_text())["name"]


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.plugin = self.root / "plugin-cache-version"
        manifest = self.plugin / ".codex-plugin/plugin.json"
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({"name": PLUGIN}))
        copied = self.plugin / "skills/install-subagents/scripts/install_agents.py"
        copied.parent.mkdir(parents=True)
        shutil.copyfile(SCRIPT, copied)
        spec = importlib.util.spec_from_file_location("installer", copied)
        self.installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.installer)
        self.target = self.root / "installed"
        self.manual = self.plugin / "agents/sample/AGENT.md"
        self.manual.parent.mkdir(parents=True)
        self.manual.write_text("# Core procedure\nFor findings, read references/fix.md.\n")
        self.reference = self.manual.parent / "references/fix.md"
        self.reference.parent.mkdir()
        self.reference.write_text("# Exceptional case\nRare instructions stay out of context.\n")
        self.source = self.plugin / "skills/install-subagents/resources/sample.toml"
        self.source.parent.mkdir(parents=True)
        self.source.write_text(self.installer.MARKER + 'name = "sample"\ndescription = "Sample role"\nmanual = "../../../agents/sample/AGENT.md"\n')
        self.installed_reference = self.target / f".{PLUGIN}/sample/references/fix.md"

    def build(self):
        return self.installer.build(self.installer.resources(), self.target)

    def install(self, check=False):
        with contextlib.redirect_stdout(io.StringIO()):
            self.installer.install(self.build(), self.target, check=check)

    def test_lazy_core_and_references_survive_source_removal(self):
        self.install()
        instructions = tomllib.loads((self.target / "sample.toml").read_text())["developer_instructions"]
        self.assertIn("# Core procedure", instructions)
        self.assertNotIn("Rare instructions", instructions)
        self.assertIn(str(self.installed_reference.parents[1]), instructions)
        shutil.rmtree(self.plugin)
        self.assertIn("Rare instructions", self.installed_reference.read_text())

    def test_nested_reference_paths_are_preserved(self):
        nested = self.reference.parent / "details/extra.md"
        nested.parent.mkdir()
        nested.write_text("Additional detail")
        self.install()
        self.assertIn("Additional detail", (self.installed_reference.parent / "details/extra.md").read_text())

    def test_update_and_remove_only_owned_files(self):
        self.install()
        self.reference.write_text("Updated instructions")
        self.install()
        self.assertIn("Updated instructions", self.installed_reference.read_text())
        unmanaged = self.installed_reference.with_name("personal.md")
        unmanaged.write_text("User notes")
        other = self.target / "other.toml"
        other.write_text("# managed-by: another-plugin\n")
        old = self.target / "retired.toml"
        old.write_text(self.installer.MARKER + 'name = "old"\n')
        self.reference.unlink()
        self.install()
        self.assertFalse(self.installed_reference.exists())
        self.assertFalse(old.exists())
        self.assertEqual(unmanaged.read_text(), "User notes")
        self.assertTrue(other.exists())

    def test_removed_role_references_are_cleaned(self):
        self.install()
        self.source.rename(self.source.with_name("replacement.toml"))
        self.install()
        self.assertFalse((self.target / "sample.toml").exists())
        self.assertFalse(self.installed_reference.exists())
        self.assertTrue((self.target / f".{PLUGIN}/replacement/references/fix.md").exists())

    def test_unmanaged_conflicts_are_detected_before_any_write(self):
        for conflict in (self.target / "sample.toml", self.installed_reference):
            with self.subTest(conflict=conflict):
                conflict.parent.mkdir(parents=True, exist_ok=True)
                conflict.write_bytes(b"unmanaged\xff")
                with self.assertRaisesRegex(SystemExit, "refusing to overwrite"):
                    self.install()
                self.assertEqual(conflict.read_bytes(), b"unmanaged\xff")
                conflict.unlink()
        self.assertFalse((self.target / "sample.toml").exists())
        self.assertFalse(self.installed_reference.exists())

    def test_symlink_destination_is_not_followed(self):
        outside = self.root / "outside"
        outside.mkdir()
        self.target.mkdir()
        (self.target / f".{PLUGIN}").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(SystemExit, "unsafe"):
            self.install()
        self.assertEqual(list(outside.iterdir()), [])

    def test_check_installed_is_read_only_and_detects_drift(self):
        with self.assertRaisesRegex(SystemExit, "installed files differ"):
            self.install(check=True)
        self.assertFalse(self.target.exists())
        self.install()
        self.install(check=True)
        before = self.installed_reference.stat().st_mtime_ns
        self.reference.write_text("New reference")
        with self.assertRaisesRegex(SystemExit, "installed files differ"):
            self.install(check=True)
        self.assertEqual(self.installed_reference.stat().st_mtime_ns, before)
        self.install()
        self.install(check=True)

    def test_metadata_overrides_are_rejected(self):
        with self.source.open("a") as handle:
            handle.write('model = "custom"\n')
        with self.assertRaisesRegex(SystemExit, "unsupported source settings"):
            self.build()

    def test_manual_cannot_escape_plugin(self):
        outside = self.root / "AGENT.md"
        outside.write_text("External manual")
        self.source.write_text(self.source.read_text().replace("../../../agents/sample/AGENT.md", str(outside)))
        with self.assertRaisesRegex(SystemExit, "manual escapes"):
            self.build()

    def test_reference_cannot_escape_plugin(self):
        outside = self.root / "outside.md"
        outside.write_text("External reference")
        self.reference.unlink()
        self.reference.symlink_to(outside)
        with self.assertRaisesRegex(SystemExit, "reference escapes"):
            self.build()


    def test_orchestration_skill_cannot_be_a_core_manual(self):
        skill = self.manual.with_name("SKILL.md")
        self.manual.rename(skill)
        self.source.write_text(self.source.read_text().replace("AGENT.md", "SKILL.md"))
        with self.assertRaisesRegex(SystemExit, "missing agent manual"):
            self.build()


class ActualResourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source_root = SCRIPT.resolve().parents[3]
        self.plugin = self.root / PLUGIN
        shutil.copytree(self.source_root, self.plugin, ignore=shutil.ignore_patterns("__pycache__"))
        self.installer = self.load(self.plugin)
        self.target = self.root / "agents"
        self.roles = {
            "ca77y-engineering": {"coder", "qa", "writer", "auditor"},
            "ca77y-library": {"researcher", "librarian", "scribe", "clerk"},
        }[PLUGIN]

    @staticmethod
    def load(plugin):
        spec = importlib.util.spec_from_file_location("actual_installer", plugin / "skills/install-subagents/scripts/install_agents.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def install(self, module=None, check=False):
        module = module or self.installer
        with contextlib.redirect_stdout(io.StringIO()):
            module.install(module.build(module.resources(), self.target), self.target, check=check)

    def test_actual_inventory_core_and_reference_survival(self):
        sources = self.installer.resources()
        self.assertEqual({p.name for p in sources}, {f"{PLUGIN}-{role}.toml" for role in self.roles})
        self.install()
        self.install(check=True)
        self.assertEqual(len(list(self.target.glob("*.toml"))), 4)
        references = []
        for source in sources:
            data = self.installer.source_data(source)
            role = source.stem.removeprefix(PLUGIN + "-")
            self.assertEqual(data["manual"], f"../../../agents/{role}/AGENT.md")
            self.assertEqual(data["name"], (PLUGIN + "_" + role).replace("-", "_"))
            manual = self.plugin / "agents" / role / "AGENT.md"
            installed = tomllib.loads((self.target / source.name).read_text())
            self.assertEqual(set(installed), {"name", "description", "developer_instructions"})
            self.assertTrue(installed["developer_instructions"].endswith(self.installer.without_frontmatter(manual.read_text()) + "\n"))
            for ref in (manual.parent / "references").rglob("*.md"):
                target_ref = self.target / f".{PLUGIN}" / source.stem / ref.relative_to(manual.parent)
                self.assertEqual(target_ref.read_text(), self.installer.REFERENCE_MARKER + ref.read_text())
                self.assertIn(str(target_ref.parents[1]), installed["developer_instructions"])
                references.append((target_ref, target_ref.read_bytes()))
        self.assertTrue(references)
        shutil.rmtree(self.plugin)
        for ref, content in references:
            self.assertEqual(ref.read_bytes(), content)

    def test_actual_stale_cleanup_and_unmanaged_preservation(self):
        self.install()
        stale_role = self.target / f"{PLUGIN}-retired.toml"
        stale_role.write_text(self.installer.MARKER + 'name = "retired"\n')
        stale_ref = self.target / f".{PLUGIN}/retired/references/old.md"
        stale_ref.parent.mkdir(parents=True)
        stale_ref.write_text(self.installer.REFERENCE_MARKER + "Retired reference")
        personal = stale_ref.with_name("personal.md")
        personal.write_text("User-owned note")
        other = self.target / "another-plugin.toml"
        other.write_text('# managed-by: another-plugin\nname = "other"\n')
        before = {p: p.read_bytes() for p in (personal, other)}
        with self.assertRaisesRegex(SystemExit, "installed files differ"):
            self.install(check=True)
        self.assertTrue(stale_role.exists())
        self.assertTrue(stale_ref.exists())
        self.install()
        self.assertFalse(stale_role.exists())
        self.assertFalse(stale_ref.exists())
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_actual_conflict_refusal_before_partial_install(self):
        self.target.mkdir()
        conflict = self.target / self.installer.resources()[-1].name
        conflict.write_bytes(b"personal definition")
        with self.assertRaisesRegex(SystemExit, "refusing to overwrite"):
            self.install()
        self.assertEqual(list(self.target.iterdir()), [conflict])
        self.assertEqual(conflict.read_bytes(), b"personal definition")

    def test_actual_drift_check_does_not_repair(self):
        self.install()
        changed = self.target / self.installer.resources()[0].name
        changed.write_text(changed.read_text() + "# local drift\n")
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.target.rglob("*") if p.is_file()}
        with self.assertRaisesRegex(SystemExit, "installed files differ"):
            self.install(check=True)
        self.assertEqual(before, {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in before})

    def test_actual_plugins_coexist_when_both_sources_are_present(self):
        other_name = "ca77y-library" if PLUGIN == "ca77y-engineering" else "ca77y-engineering"
        other_source = self.source_root.parent / other_name
        if not other_source.is_dir():
            self.skipTest("Other plugin absent; this plugin installs independently")
        other = self.load(other_source)
        self.install(other)
        before = {p: p.read_bytes() for p in self.target.rglob("*") if p.is_file()}
        self.install()
        self.install(check=True)
        self.install(other, check=True)
        self.assertEqual(len(list(self.target.glob("*.toml"))), 8)
        self.assertEqual(before, {p: p.read_bytes() for p in before})


if __name__ == "__main__":
    unittest.main()
