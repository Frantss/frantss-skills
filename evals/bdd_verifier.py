"""Check BDD task outcomes against independent cases and preserved fixture state."""

import json
from pathlib import Path
import subprocess
import tempfile
import shutil

from ship_it_verifier import inventory, read_trace


def implementation_checks(root):
    script = """import assert from 'node:assert/strict';
import { validate } from './src/validator.mjs';
for (let input = -3; input <= 9; input++) {
  const state = { items: ['preserve'], nested: { count: 2 } };
  const before = JSON.stringify(state);
  assert.equal(validate(input, state), input >= 1 && input <= 5);
  assert.equal(JSON.stringify(state), before);
}
"""
    result = subprocess.run(['node', '--input-type=module', '-e', script], cwd=root,
                            capture_output=True, text=True, timeout=20)
    native = subprocess.run(['node', '--test'], cwd=root, capture_output=True,
                            text=True, timeout=20)
    checks = {'independent_acceptance_cases_pass': result.returncode == 0,
              'native_tests_pass': native.returncode == 0}
    mutants = ('true', 'false', 'value >= 1 && value <= 6',
               '(state.changed = true, value >= 1 && value <= 5)')
    with tempfile.TemporaryDirectory() as temporary:
        mutant_root = Path(temporary) / 'app'
        shutil.copytree(root, mutant_root, ignore=shutil.ignore_patterns('.git', '.agents'))
        for number, expression in enumerate(mutants):
            (mutant_root / 'src/validator.mjs').write_text(
                f'export function validate(value, state) {{ return {expression}; }}\n')
            mutant = subprocess.run(['node', '--test'], cwd=mutant_root,
                                    capture_output=True, text=True, timeout=20)
            checks[f'native_tests_reject_mutant_{number}'] = mutant.returncode != 0
    return checks


def grade(root, expected, report, commands, telemetry):
    case = expected['case']
    actual = inventory(root)
    checks = {'report_present': bool(report), 'actions_recorded': bool(commands)}
    immutable = expected['state']
    if case in ('stale', 'reuse', 'audit'):
        checks['subject_and_sources_preserved'] = all(actual.get(name) == digest
                                                     for name, digest in immutable.items())
        checks['only_requested_report_created'] = set(actual) - set(immutable) == {'report.json'}
    if case in ('direct', 'partial'):
        checks.update(implementation_checks(root))
        checks['reported_completion'] = report.get('status') == 'done'
        checks['checks_reported'] = bool(report.get('checks') or report.get('actual_checks'))
        checks['native_checks_executed_by_agent'] = any(
            'node --test' in command.get('command', '') and command.get('exit_code') == 0
            for command in commands)
        checks['agreements_preserved'] = actual.get('acceptance.md') == immutable['acceptance.md']
        checks['no_unrequested_gherkin'] = not list(root.rglob('*.feature'))
        checks['installed_skills_preserved'] = all(
            actual.get(name) == digest for name, digest in immutable.items() if name.startswith('.agents/'))
        if case == 'direct':
            checks['no_unrequested_planning'] = set(actual) - set(immutable) <= {'report.json'} | {
                name for name in actual if name.startswith(('src/', 'tests/'))}
        else:
            folder = '.scratch/bdd/upload-limits-001/'
            for filename in ('acceptance.md', 'tickets.md'):
                checks[filename + '_preserved'] = actual.get(folder + filename) == immutable[folder + filename]
            run = (root / folder / 'run.md').read_text()
            checks['run_identity_preserved'] = all(text in run for text in (
                'feature_name: Upload limits', 'feature_slug: upload-limits', 'run_id: upload-limits-001',
                'current_slice: S-001', 'current_ticket: TK-001',
                '## Documents', '## Validation', '## Next action'))
            checks['unrelated_decision_and_human_note_preserved'] = all(text in run for text in (
                'TK-002 | blocked | Duplicate policy is undecided',
                'Human note: preserve this note and the unresolved duplicate policy.'))
            checks['selected_ticket_recorded_done'] = any(
                'TK-001' in line and '| done |' in line for line in run.splitlines())
    elif case in ('stale', 'reuse'):
        checks['agreement_preserved'] = report.get('rule_id') == 'R-001' and report.get('agreed_expiry_days') == 7
        checks['current_inference_reported'] = report.get('implementation_expiry_days') == (14 if case == 'stale' else 7)
        checks['current_revision_reported'] = report.get('implementation_revision') == expected['revision']
        checks['unagreed_limit_left_open'] = 'resend_limit' in report and report['resend_limit'] is None
        checks['decision_question_returned'] = bool(report.get('questions'))
        if case == 'reuse':
            checks['sufficient_map_reused_without_helper_reload'] = not any(
                'break-down/SKILL.md' in command.get('command', '') for command in commands)
    else:
        cases = {item['input']: item for item in report.get('cases', [])}
        checks['all_boundary_cases_reported'] = all(value in cases for value in (0, 1, 5, 6))
        checks['actual_upper_bound_defect_reported'] = all(cases.get(6, {}).get(key) == value
                                                         for key, value in {
            'input': 6, 'expected': False, 'actual': True, 'status': 'failed'}.items())
        checks['boundary_cases_executed'] = {0, 1, 5, 6} <= set(telemetry)
    return checks


def main():
    output = Path('/logs/verifier')
    output.mkdir(parents=True, exist_ok=True)
    try:
        expected = json.loads(Path('/tests/expected.json').read_text())
        report = json.loads(Path('/app/report.json').read_text())
        _, commands = read_trace(Path('/tmp/bdd-evidence/trace.jsonl'))
        path = Path('/tmp/bdd-eval/inputs.jsonl')
        telemetry = [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []
        checks = grade(Path('/app'), expected, report, commands, telemetry)
        result = {'checks': checks, 'report': report}
    except Exception as error:
        checks = {'verifier_completed': False}
        result = {'checks': checks, 'error': str(error)}
    (output / 'checks.json').write_text(json.dumps(result, indent=2))
    (output / 'reward.txt').write_text('1\n' if all(checks.values()) else '0\n')
    print(json.dumps(checks, indent=2))


if __name__ == '__main__':
    main()
