from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
import ship_it
from ship_it_verifier import grade_failure, grade_no_trigger, grade_plan, read_trace, snapshot
from github_fixture import response


PLAN = '''1. Run `node --check src/greet.mjs` and `node --test tests/test_greet.mjs`.
2. Create atomic commits:
   - `fix: trim greeting names` (`src/greet.mjs`, `tests/test_greet.mjs`).
   - `docs: add support contact` (`docs/usage.md`).
3. Push `main` to `origin`.
4. Verify remote `main` matches local `HEAD`.
'''
READS = [{'command': 'cat .agents/skills/ship-it/SKILL.md .agents/skills/atomic-commits/SKILL.md',
          'aggregated_output': (ROOT / 'skills/ship-it/SKILL.md').read_text()},
         {'command': 'git ls-remote origin refs/heads/main'}]


class ShippingEvalTests(unittest.TestCase):
    def test_github_fixture_reads_and_stores_pull_requests_offline(self):
        with tempfile.TemporaryDirectory() as temporary:
            store = Path(temporary) / 'pr.json'
            value, code = response(['repo', 'view', '--json', 'nameWithOwner'], 'abc', store)
            self.assertEqual((value['nameWithOwner'], code), ('guildara/eval-app', 0))
            value, code = response(['api', 'repos/guildara/eval-app/branches/main'], 'abc', store)
            self.assertEqual((value['commit']['sha'], code), ('abc', 0))
            self.assertEqual(response(['pr', 'list'], 'abc', store)[0], [])
            self.assertEqual(response(['pr', 'create'], 'abc', store)[1], 0)
            self.assertEqual(response(['pr', 'list'], 'abc', store)[0][0]['number'], 1)

    def test_valid_plan_passes(self):
        self.assertTrue(all(grade_plan(PLAN, READS, 'synced').values()))

    def test_nearby_and_quoted_requests_must_not_load_shipping_workflow(self):
        self.assertTrue(all(grade_no_trigger('A release plan includes checks and delivery.', []).values()))
        self.assertFalse(grade_no_trigger(PLAN, READS)['shipping_workflow_not_loaded'])
        checks = grade_no_trigger('Done.', [{'command': 'git commit -m test; npm publish'}])
        self.assertFalse(checks['no_early_mutations'])
        self.assertFalse(checks['no_early_delivery'])

    def test_workflow_loading_checks_returned_content_including_wildcard_reads(self):
        commands = [{'command': 'cat .agents/skills/*/SKILL.md',
                     'aggregated_output': READS[0]['aggregated_output']}]
        self.assertFalse(grade_no_trigger('Done.', commands)['shipping_workflow_not_loaded'])
        commands = [{'command': 'ls .agents/skills/ship-it/SKILL.md',
                     'aggregated_output': '.agents/skills/ship-it/SKILL.md'}]
        self.assertTrue(grade_no_trigger('Found a path.', commands)['shipping_workflow_not_loaded'])
        contents = READS[0]['aggregated_output'].splitlines(keepends=True)
        commands = [{'command': 'head -n 10 .agents/skills/ship-it/SKILL.md',
                     'aggregated_output': ''.join(contents[:10])},
                    {'command': 'tail -n +11 .agents/skills/ship-it/SKILL.md',
                     'aggregated_output': ''.join(contents[10:])}]
        self.assertFalse(grade_no_trigger('Done.', commands)['shipping_workflow_not_loaded'])

    def test_unrelated_plan_can_run_checks_without_invoking_shipping_workflow(self):
        commands = [{'command': 'node --check src/greet.mjs && node --test tests/test_greet.mjs',
                     'exit_code': 0, 'aggregated_output': 'Tests passed.'}]
        self.assertTrue(all(grade_no_trigger('Release plan prepared.', commands).values()))

    def test_pr_endpoint_and_approval_boundary_are_checked(self):
        plan = PLAN.replace('Push `main`', 'Push `feature/greeting`') + '5. Open a PR targeting `guildara/eval-app:main`.\n'
        self.assertTrue(all(grade_plan(plan, READS, 'guildara').values()))
        commands = READS + [{'command': 'gh pr create --title test'}]
        self.assertFalse(grade_plan(plan, commands, 'guildara')['no_early_delivery'])
        plan += '6. Run `git push origin main`.\n'
        self.assertFalse(grade_plan(plan, READS, 'guildara')['no_main_delivery'])

    def test_flattened_commits_and_conditional_rebase_fail(self):
        regression = PLAN.replace('   - ', '- ') + '5. Rebase if needed.\n'
        checks = grade_plan(regression, READS, 'synced')
        self.assertFalse(checks['nested_commit_subjects'])
        self.assertFalse(checks['no_conditional_actions'])
        self.assertFalse(checks['unnecessary_integration_omitted'])

    def test_saying_no_rebase_is_needed_is_not_a_rebase_action(self):
        answer = PLAN.replace('Push `main` to `origin`.', 'Push `main` to `origin`; no rebase or merge is needed.')
        self.assertTrue(grade_plan(answer, READS, 'synced')['unnecessary_integration_omitted'])

    def test_regression_test_must_share_the_code_commit(self):
        regression = PLAN.replace(', `tests/test_greet.mjs`', '')
        self.assertFalse(grade_plan(regression, READS, 'synced')['code_and_regression_together'])

    def test_unambiguous_regression_test_scope_is_accepted(self):
        concise = PLAN.replace('`tests/test_greet.mjs`)', 'its regression test)')
        self.assertTrue(grade_plan(concise, READS, 'synced')['code_and_regression_together'])
        concise = PLAN.replace('`src/greet.mjs`, `tests/test_greet.mjs`', 'source change and regression test')
        self.assertTrue(grade_plan(concise, READS, 'synced')['code_and_regression_together'])

    def test_documentation_correction_can_use_readme_without_extension(self):
        answer = PLAN + '\nOptional correction: README uses npm run tests; use npm test.\n'
        self.assertTrue(grade_plan(answer, READS, 'documentation')['documentation_suggestion'])

    def test_cached_remote_and_early_execution_fail(self):
        commands = READS[:1] + [{'command': 'git status; node --test tests/test_greet.mjs; git commit -m fix'}]
        checks = grade_plan(PLAN, commands, 'synced')
        for key in ('live_remote_checked', 'no_early_tests', 'no_early_mutations'):
            self.assertFalse(checks[key], key)

    def test_direct_local_mirror_query_is_a_live_remote_check(self):
        commands = READS[:1] + [{'command': 'git --git-dir=/remote.git show-ref'}]
        self.assertTrue(grade_plan(PLAN, commands, 'synced')['live_remote_checked'])

    def test_environment_error_is_not_the_expected_test_failure(self):
        commands = [{'command': 'node --test tests/test_greet.mjs', 'exit_code': 127,
                     'aggregated_output': 'node: command not found'}]
        self.assertFalse(grade_failure('Tests failed.', commands)['required_test_failed'])
        commands[0].update(exit_code=1, aggregated_output='Error: SHIP_IT_TEST_FAILURE')
        self.assertTrue(all(grade_failure('Tests failed.', commands).values()))

    def test_trace_reads_actual_actions_and_final_message(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / 'trace.txt'
            events = [{'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'Inspecting.'}},
                      {'type': 'item.completed', 'item': {'type': 'command_execution', 'command': 'git status'}},
                      {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': PLAN}}]
            path.write_text('runtime warning\n' + '\n'.join(json.dumps(event) for event in events))
            answer, commands = read_trace(path)
            self.assertEqual(answer, PLAN)
            self.assertEqual(commands[0]['command'], 'git status')

    def test_fixture_has_hidden_graders_and_detects_working_changes(self):
        with tempfile.TemporaryDirectory() as temporary:
            tasks = Path(temporary) / 'tasks'
            ship_it.prepare(tasks, ['synced', 'approval-failure'])
            task = tasks / 'synced'
            expected = json.loads((task / 'tests/expected.json').read_text())
            seed, remote = task / 'environment/seed', task / 'environment/remote.git'
            self.assertEqual(snapshot(seed, remote), expected['state'])
            self.assertFalse((seed / 'tests/verify.py').exists())
            with (seed / 'src/greet.mjs').open('a') as stream:
                stream.write('// changed after planning\n')
            self.assertNotEqual(snapshot(seed, remote), expected['state'])
            config = tomllib.loads((tasks / 'approval-failure/task.toml').read_text())
            self.assertEqual(config['verifier']['environment_mode'], 'separate')
            self.assertEqual([step['name'] for step in config['steps']], ['plan', 'approved'])
            frozen = tasks / 'approval-failure/environment/seed'
            self.assertEqual(ship_it.run_git(frozen, 'status', '--porcelain', 'tests/test_greet.mjs'), '')

    def test_incomplete_and_failed_jobs_cannot_pass(self):
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(StringIO()):
            job = Path(temporary)
            self.assertEqual(ship_it.summarize(job, 1), 1)
            result = job / 'trial/result.json'
            result.parent.mkdir()
            result.write_text(json.dumps({'task_name': 'local/ship-it-synced',
                                         'verifier_result': {'rewards': {'reward': 0}}}))
            self.assertEqual(ship_it.summarize(job, 1), 1)
            result.write_text(json.dumps({'task_name': 'local/ship-it-approval-failure',
                'verifier_result': {'rewards': {'reward': 1}}, 'step_results': [
                    {'verifier_result': {'rewards': {'reward': 1}}}]}))
            self.assertEqual(ship_it.summarize(job, 1), 1)


if __name__ == '__main__':
    unittest.main()
