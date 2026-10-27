from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from sync_bdd_references import BDD_SKILLS, CONTRACT, REFERENCE, SKILLS, reference_errors, sync_references


class BddReferencesTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = Path(__file__).resolve().parents[1]
        (self.root / SKILLS).mkdir(parents=True)
        (self.root / CONTRACT).parent.mkdir()
        shutil.copyfile(self.source / CONTRACT, self.root / CONTRACT)

    def add_skill(self, name):
        target = self.root / SKILLS / name
        target.mkdir()
        shutil.copyfile(self.source / SKILLS / name / "SKILL.md", target / "SKILL.md")
        return target

    def test_bundled_skills_are_independent_real_files(self):
        for name in BDD_SKILLS:
            self.add_skill(name)
        sync_references(self.root)
        self.assertEqual(reference_errors(self.root), [])
        for name in BDD_SKILLS:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as isolated:
                skill = Path(isolated) / name
                shutil.copytree(self.root / SKILLS / name, skill)
                reference = skill / REFERENCE
                self.assertFalse(reference.is_symlink())
                self.assertEqual(reference.read_bytes(), (self.root / CONTRACT).read_bytes())

    def test_template_changes_fail_validation_until_regenerated(self):
        skill = self.add_skill("design-solution")
        sync_references(self.root)
        entrypoint = (skill / "SKILL.md").read_bytes()
        reference = skill / REFERENCE
        original_reference = reference.read_bytes()
        with (self.root / CONTRACT).open("a") as output:
            output.write("\nPreserve accepted external source references.\n")
        self.assertTrue(any("stale or missing" in error for error in reference_errors(self.root)))
        self.assertEqual(reference.read_bytes(), original_reference)
        sync_references(self.root)
        self.assertEqual(reference_errors(self.root), [])
        self.assertEqual((skill / "SKILL.md").read_bytes(), entrypoint)

    def test_missing_reference_and_template_are_reported(self):
        self.add_skill("formulate-behavior")
        self.assertEqual(len(reference_errors(self.root)), 1)
        (self.root / CONTRACT).unlink()
        self.assertIn("missing shared BDD run contract", reference_errors(self.root)[0])

    def test_collection_without_bdd_skills_needs_no_template(self):
        (self.root / CONTRACT).unlink()
        self.assertEqual(reference_errors(self.root), [])

    def test_repository_references_match_contract(self):
        self.assertEqual(reference_errors(self.source), [])

    def test_sync_is_idempotent_and_rejects_symlink_destinations(self):
        skill = self.add_skill("frame-problem")
        sync_references(self.root)
        reference = skill / REFERENCE
        modified = reference.stat().st_mtime_ns
        sync_references(self.root)
        self.assertEqual(reference.stat().st_mtime_ns, modified)
        reference.unlink()
        reference.symlink_to(self.root / CONTRACT)
        with self.assertRaises(ValueError):
            sync_references(self.root)


if __name__ == "__main__":
    unittest.main()
