import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate import packaging_errors


class ToolingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        source = Path(__file__).resolve().parents[1]
        for folder in (".claude-plugin", ".codex-plugin", "templates"):
            shutil.copytree(source / folder, self.root / folder)
        (self.root / "skills").mkdir()

    def finished_skill(self, name="tracking-example"):
        skill = (self.root / "skills") / name
        skill.mkdir()
        (skill / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: A fixture skill.\n---\n\n# Example\n\nComplete the fixture task.\n"
        )
        return skill

    def test_empty_collection_and_completed_skill(self):
        self.assertEqual(packaging_errors(self.root), [])
        self.finished_skill()
        self.assertEqual(packaging_errors(self.root), [])





    def test_links_from_nested_references_and_missing_files(self):
        skill = self.finished_skill()
        references = skill / "references"
        references.mkdir()
        (references / "details.md").write_text("[entry](../SKILL.md)\n[missing](missing.md)\n")
        errors = packaging_errors(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("broken local link: missing.md", errors[0])

    def test_external_symlinks_and_links_fail(self):
        skill = self.finished_skill()
        (self.root / "outside.md").write_text("Outside the package.")
        (skill / "escape.md").symlink_to(self.root / "outside.md")
        (skill / "links.md").write_text("[outside](../../outside.md)")
        errors = packaging_errors(self.root)
        self.assertTrue(any("installers may skip symlinks" in error for error in errors))
        self.assertTrue(any("link escapes" in error for error in errors))

    def test_internal_and_dangling_symlinks_fail(self):
        skill = self.finished_skill()
        (skill / "copy.md").symlink_to("SKILL.md")
        (skill / "missing.md").symlink_to("absent.md")
        errors = packaging_errors(self.root)
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("installers may skip symlinks" in error for error in errors))

    def test_manifest_drift_fails(self):
        path = self.root / ".claude-plugin/marketplace.json"
        market = json.loads(path.read_text())
        market["plugins"][0]["name"] = "wrong-name"
        market["plugins"][0]["version"] = "1.0.0"
        path.write_text(json.dumps(market))
        errors = packaging_errors(self.root)
        self.assertTrue(any("same name" in error for error in errors))
        self.assertTrue(any("versions" in error for error in errors))

    def test_codex_plugin_must_match_the_shared_package(self):
        path = self.root / ".codex-plugin/plugin.json"
        original = json.loads(path.read_text())
        for changes, message in (
            ({"name": "other-plugin"}, "plugin names must match"),
            ({"skills": "../another-directory/"}, "shared ./skills/ directory"),
            ({"skills": ["./skills/example-task/"]}, "shared ./skills/ directory"),
            ({"version": "1.0.0"}, "Codex plugin versions"),
        ):
            with self.subTest(changes=changes):
                path.write_text(json.dumps({**original, **changes}))
                self.assertTrue(any(message in error for error in packaging_errors(self.root)))

    def test_missing_codex_manifest_fails(self):
        (self.root / ".codex-plugin/plugin.json").unlink()
        self.assertTrue(any("invalid plugin manifests" in error for error in packaging_errors(self.root)))

    @unittest.skipUnless(shutil.which("codex"), "Codex CLI is needed for the plugin installation smoke test")
    def test_codex_installs_and_refreshes_shared_skills(self):
        skill = self.finished_skill()
        with tempfile.TemporaryDirectory() as runtime:
            env = {**os.environ, "CODEX_HOME": runtime}

            def codex(*args):
                result = subprocess.run(
                    ["codex", "plugin", *args, "--json"],
                    cwd=runtime, env=env, capture_output=True, text=True, timeout=30,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            market = codex("marketplace", "add", str(self.root))
            self.assertEqual(market["marketplaceName"], "frantss")
            result = codex("add", "frantss-skills@frantss")
            installed = Path(result["installedPath"])
            self.assertTrue(installed.resolve().is_relative_to(Path(runtime).resolve()))
            self.assertEqual((installed / "skills" / skill.name / "SKILL.md").read_bytes(),
                             (skill / "SKILL.md").read_bytes())

            with (skill / "SKILL.md").open("a") as output:
                output.write("\nA locally updated instruction.\n")
            added = self.finished_skill("second-task")
            result = codex("add", "frantss-skills@frantss")
            installed = Path(result["installedPath"])
            for source in (skill, added):
                self.assertEqual((installed / "skills" / source.name / "SKILL.md").read_bytes(),
                                 (source / "SKILL.md").read_bytes())

    def test_skills_outside_plugin_directories_fail(self):
        stray = self.root / "stray"
        stray.mkdir()
        (stray / "SKILL.md").write_text("An incorrectly placed skill.")
        self.assertTrue(any("directly under skills/" in error for error in packaging_errors(self.root)))

    def test_line_limit_counts_entrypoint_references_and_metadata(self):
        skill = self.finished_skill()
        initial = len((skill / "SKILL.md").read_text().splitlines())
        (skill / "references").mkdir()
        (skill / "references/details.md").write_text("\n" * (73 - initial))
        (skill / "agents").mkdir()
        metadata = skill / "agents/openai.yaml"
        metadata.write_text('policy:\n  allow_implicit_invocation: true\n')
        self.assertEqual(packaging_errors(self.root), [])
        with metadata.open("a") as output:
            output.write("\n")
        self.assertTrue(any("76 text lines exceeds the 75-line limit" in error for error in packaging_errors(self.root)))

    def test_line_limit_counts_helper_code_but_excludes_binary_assets(self):
        skill = self.finished_skill()
        (skill / "assets").mkdir()
        (skill / "assets/binary.dat").write_bytes(b"\0\xff\n" * 200)
        self.assertEqual(packaging_errors(self.root), [])
        (skill / "scripts").mkdir()
        (skill / "scripts/helper.py").write_text("pass\n" * 76)
        self.assertTrue(any("line limit" in error for error in packaging_errors(self.root)))

    def test_named_line_limits_include_references(self):
        for name, limit in (("atomic-commits", 50), ("core-communicate", 50), ("core-update", 50),
                            ("persistence-records", 100), ("persistence-obsidian", 350)):
            with self.subTest(name=name):
                skill = self.finished_skill(name)
                initial = len((skill / "SKILL.md").read_text().splitlines())
                (skill / "references").mkdir()
                reference = skill / "references/records.md"
                reference.write_text("\n" * (limit - initial))
                self.assertEqual(packaging_errors(self.root), [])
                with reference.open("a") as output:
                    output.write("\n")
                errors = packaging_errors(self.root)
                self.assertEqual(len(errors), 1)
                self.assertIn(f"{limit + 1} text lines exceeds the {limit}-line limit", errors[0])
                reference.write_text("\n" * (limit - initial))

    def test_line_limit_exceptions_require_exact_skill_names(self):
        for name in ("persistence-records-other", "core-communicate-other", "core-update-other"):
            with self.subTest(name=name):
                skill = self.finished_skill(name)
                initial = len((skill / "SKILL.md").read_text().splitlines())
                (skill / "details.txt").write_text("\n" * (76 - initial))
                self.assertTrue(any(f"skills/{name}: 76 text lines exceeds the 75-line limit" in error
                                    for error in packaging_errors(self.root)))


if __name__ == "__main__":
    unittest.main()
