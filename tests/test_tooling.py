import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from new_skill import create_skill
from validate import packaging_errors


class ToolingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        source = Path(__file__).resolve().parents[1]
        for folder in (".claude-plugin", "templates"):
            shutil.copytree(source / folder, self.root / folder)
        (self.root / "skills").mkdir()

    def finished_skill(self):
        skill = create_skill(self.root, "example-task", 'Use when a task contains: "quotes".')
        path = skill / "SKILL.md"
        lines = path.read_text().splitlines()
        path.write_text("\n".join(line for line in lines if "<!-- scaffold:" not in line))
        return skill

    def test_empty_collection_and_completed_skill(self):
        self.assertEqual(packaging_errors(self.root), [])
        self.finished_skill()
        self.assertEqual(packaging_errors(self.root), [])

    def test_description_is_quoted_without_losing_content(self):
        skill = self.finished_skill()
        value = (skill / "SKILL.md").read_text().splitlines()[2].removeprefix("description: ")
        self.assertEqual(json.loads(value), 'Use when a task contains: "quotes".')

    def test_invalid_names_cannot_escape_skills(self):
        for name in ("../escape", "Uppercase", "two--hyphens", "-leading", "trailing-", "a" * 65, ""):
            with self.subTest(name=name), self.assertRaises(ValueError):
                create_skill(self.root, name, "A task.")
        self.assertEqual(list((self.root / "skills").iterdir()), [])

    def test_existing_skill_is_preserved(self):
        skill = self.finished_skill()
        original = (skill / "SKILL.md").read_bytes()
        with self.assertRaises(FileExistsError):
            create_skill(self.root, skill.name, "A different task.")
        self.assertEqual((skill / "SKILL.md").read_bytes(), original)

    def test_unfinished_scaffold_fails(self):
        create_skill(self.root, "draft", "A draft task.")
        self.assertTrue(any("scaffold" in error for error in packaging_errors(self.root)))

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

    def test_template_is_not_discovered_but_stray_skills_fail(self):
        (self.root / "templates/SKILL.md").write_text("An accidentally discoverable template.")
        self.assertTrue(any("directly under skills/" in error for error in packaging_errors(self.root)))


if __name__ == "__main__":
    unittest.main()
