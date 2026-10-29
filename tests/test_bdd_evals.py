import json
from pathlib import Path
import shutil
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
import bdd
from bdd_verifier import grade, implementation_checks
from ship_it_verifier import inventory


class BddEvalTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def seed(self, case):
        root = self.root / case
        bdd.fixture(root, case)
        return root, {'case': case, 'state': inventory(root), 'revision': 'current-revision'}

    def handoff(self, root, *, days=7, limit=None):
        report = {'rule_id': 'R-001', 'agreed_expiry_days': 7,
                  'implementation_expiry_days': days,
                  'implementation_revision': 'current-revision',
                  'resend_limit': limit, 'questions': ['What resend limit should apply?']}
        (root / 'report.json').write_text(json.dumps(report))
        return report

    def test_prepare_uses_matrix_requests_and_keeps_graders_out_of_agent_seed(self):
        destination = self.root / 'tasks'
        bdd.prepare(destination, bdd.CASES)
        matrix = bdd.requests()
        self.assertEqual(set(matrix), set(bdd.CASES))
        for case in bdd.CASES:
            with self.subTest(case=case):
                task = destination / case
                config = tomllib.loads((task / 'task.toml').read_text())
                self.assertEqual(config['verifier']['environment_mode'], 'separate')
                self.assertTrue((task / 'instruction.md').read_text().startswith(matrix[case]['request']))
                self.assertTrue((task / 'tests/bdd_verifier.py').is_file())
                self.assertFalse((task / 'environment/seed/tests/bdd_verifier.py').exists())
                expected = json.loads((task / 'tests/expected.json').read_text())
                self.assertEqual(expected['state'], inventory(task / 'environment/seed'))
                self.assertEqual(len(list((task / 'environment/seed/.agents/skills').iterdir())), 7)

    def test_stale_map_refresh_preserves_agreement_and_does_not_choose_limit(self):
        root, expected = self.seed('stale')
        report = self.handoff(root, days=14)
        commands = [{'command': 'git log -1 && cat src/invitations.mjs', 'exit_code': 0}]
        self.assertTrue(all(grade(root, expected, report, commands, []).values()))
        report['agreed_expiry_days'] = 14
        self.assertFalse(grade(root, expected, report, commands, [])['agreement_preserved'])
        report['agreed_expiry_days'] = 7
        report['resend_limit'] = 3
        self.assertFalse(grade(root, expected, report, commands, [])['unagreed_limit_left_open'])
        report['resend_limit'] = None
        report['implementation_expiry_days'] = 7
        self.assertFalse(grade(root, expected, report, commands, [])['current_inference_reported'])

    def test_sufficient_map_reuse_rejects_helper_reload_and_subject_changes(self):
        root, expected = self.seed('reuse')
        report = self.handoff(root)
        commands = [{'command': 'cat breakdown.md', 'exit_code': 0}]
        self.assertTrue(all(grade(root, expected, report, commands, []).values()))
        commands.append({'command': 'cat .agents/skills/break-down/SKILL.md', 'exit_code': 0})
        self.assertFalse(grade(root, expected, report, commands, [])[
            'sufficient_map_reused_without_helper_reload'])
        (root / 'specification.md').write_text('Changed agreement')
        self.assertFalse(grade(root, expected, report, commands, [])['subject_and_sources_preserved'])

    def test_audit_checks_runtime_inputs_and_preserves_the_bug(self):
        root, expected = self.seed('audit')
        cases = [{'input': value, 'expected': 1 <= value <= 5,
                  'actual': 1 <= value <= 6, 'status': 'failed' if value == 6 else 'passed'}
                 for value in (0, 1, 5, 6)]
        report = {'cases': cases}
        (root / 'report.json').write_text(json.dumps(report))
        commands = [{'command': 'node --input-type=module check.mjs', 'exit_code': 0}]
        self.assertTrue(all(grade(root, expected, report, commands, [0, 1, 5, 6]).values()))
        self.assertFalse(grade(root, expected, report, commands, [0, 1])['boundary_cases_executed'])
        report['cases'][-1]['status'] = 'passed'
        self.assertFalse(grade(root, expected, report, commands, [0, 1, 5, 6])[
            'actual_upper_bound_defect_reported'])

    @unittest.skipUnless(shutil.which('node'), 'Node is needed for independent acceptance cases')
    def test_acceptance_and_mutation_checks_detect_missing_coverage(self):
        root, _ = self.seed('direct')
        (root / 'src/validator.mjs').write_text(
            'export function validate(value, state) { return value >= 1 && value <= 5; }\n')
        incomplete = implementation_checks(root)
        self.assertTrue(incomplete['independent_acceptance_cases_pass'])
        self.assertTrue(incomplete['native_tests_pass'])
        self.assertFalse(incomplete['native_tests_reject_mutant_2'])
        self.assertFalse(incomplete['native_tests_reject_mutant_3'])
        (root / 'tests/validator.test.mjs').write_text(
            "import assert from 'node:assert/strict';\n"
            "import { validate } from '../src/validator.mjs';\n"
            'for (const value of [0, 1, 5, 6]) {\n'
            "  const state = { keep: ['value'] };\n"
            '  assert.equal(validate(value, state), value >= 1 && value <= 5);\n'
            "  assert.deepEqual(state, { keep: ['value'] });\n}\n")
        self.assertTrue(all(implementation_checks(root).values()))
        (root / 'src/validator.mjs').write_text(
            'export function validate(value, state) { state.changed = true; return value >= 1 && value <= 5; }\n')
        self.assertFalse(implementation_checks(root)['independent_acceptance_cases_pass'])

    def test_tracked_subset_preserves_unrelated_decision_and_human_note(self):
        root, expected = self.seed('partial')
        report = {'status': 'done', 'scope': 'size limits', 'checks': ['node --test']}
        (root / 'report.json').write_text(json.dumps(report))
        run = root / '.scratch/bdd/upload-limits-001/run.md'
        run.write_text(run.read_text().replace('TK-001 | pending | None', 'TK-001 | done | node --test'))
        commands = [{'command': 'node --test', 'exit_code': 0}]
        with patch('bdd_verifier.implementation_checks', return_value={'acceptance': True}):
            self.assertTrue(all(grade(root, expected, report, commands, []).values()))
            run.write_text(run.read_text().replace('Duplicate policy is undecided', 'Duplicate policy is settled'))
            self.assertFalse(grade(root, expected, report, commands, [])[
                'unrelated_decision_and_human_note_preserved'])

    def test_completed_direct_scope_accepts_actual_checks_report_field(self):
        root, expected = self.seed('direct')
        report = {'status': 'done', 'scope': 'integer validator',
                  'actual_checks': [{'command': 'node --test', 'exit_code': 0}]}
        (root / 'report.json').write_text(json.dumps(report))
        commands = [{'command': 'node --test', 'exit_code': 0}]
        with patch('bdd_verifier.implementation_checks', return_value={'acceptance': True}):
            self.assertTrue(all(grade(root, expected, report, commands, []).values()))


if __name__ == '__main__':
    unittest.main()
