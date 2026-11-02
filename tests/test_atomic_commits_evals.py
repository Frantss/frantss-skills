from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
import atomic_commits
from atomic_commits_verifier import grade
from ship_it import run_git, write
from ship_it_verifier import inventory


class AtomicCommitsEvalTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)

    def fixture(self, case='decomposable'):
        self.expected = atomic_commits.fixture(self.directory, case)
        self.seed = self.directory / 'environment/seed'
        return self.expected

    def commit(self, paths):
        run_git(self.seed, 'add', '--', *paths)
        run_git(self.seed, 'commit', '-m', 'record completed work')

    def complete(self):
        for bundle in self.expected['bundles']:
            self.commit(bundle)

    def grade(self):
        with redirect_stdout(StringIO()):
            return grade(self.seed, self.expected)

    def test_dependency_steps_pass_without_changing_the_trial_repository(self):
        self.fixture()
        self.complete()
        before = (run_git(self.seed, 'rev-parse', 'HEAD'), inventory(self.seed),
                  run_git(self.seed, 'status', '--porcelain=v1'))
        self.assertTrue(all(self.grade().values()))
        self.assertEqual(before, (run_git(self.seed, 'rev-parse', 'HEAD'), inventory(self.seed),
                                  run_git(self.seed, 'status', '--porcelain=v1')))

    def test_valid_config_extraction_and_adoption_may_share_a_commit(self):
        self.fixture()
        config, migration, home, pricing = self.expected['bundles']
        self.commit(config + migration)
        self.commit(home)
        self.commit(pricing)
        self.assertTrue(all(self.grade().values()))

    def test_decomposable_megacommit_is_rejected_even_when_all_tests_pass(self):
        self.fixture()
        self.commit([path for bundle in self.expected['bundles'] for path in bundle])
        checks = self.grade()
        self.assertTrue(checks['intermediate_trees_pass'])
        self.assertTrue(checks['pending_paths_committed_once'])
        self.assertTrue(checks['bundles_together'])
        self.assertFalse(checks['milestones_separate_and_ordered'])

    def test_inseparable_api_caller_regression_and_docs_pass_together(self):
        self.fixture('inseparable')
        self.complete()
        self.assertTrue(all(self.grade().values()))

    def test_passing_final_state_does_not_hide_a_broken_intermediate_tree(self):
        self.fixture()
        config, migration, home, pricing = self.expected['bundles']
        for bundle in (home, config, migration, pricing):
            self.commit(bundle)
        output = StringIO()
        with redirect_stdout(output):
            checks = grade(self.seed, self.expected)
        self.assertIn('ERR_MODULE_NOT_FOUND', output.getvalue())
        final = subprocess.run(self.expected['check_command'], cwd=self.seed, capture_output=True,
                               text=True, timeout=30)
        self.assertEqual(final.returncode, 0, final.stdout + final.stderr)
        self.assertTrue(checks['implementation_preserved'])
        self.assertTrue(checks['working_tree_clean'])
        self.assertTrue(checks['pending_paths_committed_once'])
        self.assertTrue(checks['bundles_together'])
        self.assertFalse(checks['intermediate_trees_pass'])

    def test_api_or_caller_rename_cannot_land_alone(self):
        parent = self.directory
        for index in (0, 1):
            with self.subTest(first=index):
                self.directory = parent / str(index)
                self.fixture('inseparable')
                bundle = self.expected['bundles'][0]
                first = bundle[index]
                self.commit([first])
                self.commit([path for path in bundle if path != first])
                checks = self.grade()
                self.assertTrue(checks['implementation_preserved'])
                self.assertTrue(checks['pending_paths_committed_once'])
                self.assertFalse(checks['bundles_together'])
                self.assertFalse(checks['intermediate_trees_pass'])

    def test_regression_and_documentation_cannot_be_peeled_off_their_bundle(self):
        parent = self.directory
        for suffix in ('.test.mjs', '.md'):
            with self.subTest(separated=suffix):
                self.directory = parent / suffix
                self.fixture()
                bundle = self.expected['bundles'][0]
                separated = next(path for path in bundle if path.endswith(suffix))
                self.commit([path for path in bundle if path != separated])
                self.commit([separated])
                for remaining in self.expected['bundles'][1:]:
                    self.commit(remaining)
                checks = self.grade()
                self.assertTrue(checks['intermediate_trees_pass'])
                self.assertTrue(checks['pending_paths_committed_once'])
                self.assertFalse(checks['bundles_together'])

    def test_missing_pending_implementation_is_rejected(self):
        self.fixture('inseparable')
        source = self.expected['bundles'][0][0]
        run_git(self.seed, 'restore', '--source=' + self.expected['base'], '--', source)
        self.complete()
        checks = self.grade()
        self.assertFalse(checks['implementation_preserved'])
        self.assertFalse(checks['pending_paths_committed_once'])

    def test_changed_implementation_is_rejected_even_if_behavior_still_passes(self):
        self.fixture()
        source = self.seed / self.expected['ordered_paths'][0]
        write(source, source.read_text() + '\n')
        self.complete()
        checks = self.grade()
        self.assertTrue(checks['intermediate_trees_pass'])
        self.assertFalse(checks['implementation_preserved'])

    def test_uncommitted_work_and_no_commits_are_rejected(self):
        self.fixture()
        checks = self.grade()
        self.assertTrue(checks['implementation_preserved'])
        self.assertTrue(checks['baseline_ancestor'])
        self.assertFalse(checks['working_tree_clean'])
        self.assertFalse(checks['commits_created'])
        self.assertFalse(checks['intermediate_trees_pass'])

    def test_new_untracked_file_after_committing_is_not_a_clean_result(self):
        self.fixture()
        self.complete()
        write(self.seed / 'leftover.txt', 'uncommitted work\n')
        checks = self.grade()
        self.assertFalse(checks['implementation_preserved'])
        self.assertFalse(checks['working_tree_clean'])

    def test_rewritten_baseline_is_rejected_despite_preserved_final_files(self):
        self.fixture()
        run_git(self.seed, 'checkout', '--orphan', 'rewritten')
        self.commit(list(self.expected['files']))
        checks = self.grade()
        self.assertTrue(checks['implementation_preserved'])
        self.assertTrue(checks['working_tree_clean'])
        self.assertFalse(checks['baseline_ancestor'])

    def test_out_of_scope_add_then_delete_is_rejected_despite_preserved_final_files(self):
        self.fixture()
        extra = self.seed / 'temporary.txt'
        write(extra, 'not part of the pending work\n')
        self.commit(['temporary.txt'])
        extra.unlink()
        self.commit(['temporary.txt'])
        self.complete()
        checks = self.grade()
        self.assertTrue(checks['implementation_preserved'])
        self.assertTrue(checks['intermediate_trees_pass'])
        self.assertFalse(checks['pending_paths_committed_once'])

    def test_repeated_edits_to_a_pending_path_are_rejected(self):
        self.fixture()
        self.complete()
        path = self.expected['ordered_paths'][0]
        source = self.seed / path
        original = source.read_text()
        write(source, original + '\n')
        self.commit([path])
        write(source, original)
        self.commit([path])
        checks = self.grade()
        self.assertTrue(checks['implementation_preserved'])
        self.assertTrue(checks['intermediate_trees_pass'])
        self.assertFalse(checks['pending_paths_committed_once'])
        self.assertFalse(checks['bundles_together'])

    def test_checks_have_a_finite_timeout_and_capture_partial_output(self):
        self.fixture('inseparable')
        self.complete()
        self.expected['check_command'] = [
            sys.executable, '-c',
            "import time; print('before timeout', flush=True); time.sleep(10)",
        ]
        output = StringIO()
        with patch('atomic_commits_verifier.CHECK_TIMEOUT', 1), redirect_stdout(output):
            checks = grade(self.seed, self.expected)
        self.assertFalse(checks['intermediate_trees_pass'])
        self.assertIn('before timeout', output.getvalue())
        self.assertIn('timed out', output.getvalue())


if __name__ == '__main__':
    unittest.main()
