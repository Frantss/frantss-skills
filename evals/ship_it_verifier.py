"""Grade captured Codex actions and fixture state in Harbor's verifier container."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def git(root, *arguments):
    return subprocess.check_output(
        ['git', '-c', 'core.fsmonitor=false', *arguments], cwd=root, text=True,
        stderr=subprocess.PIPE).strip()


def inventory(root):
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob('*'))
        if path.is_file() and '.git' not in path.relative_to(root).parts
    }


def snapshot(root, remote):
    return {
        'head': git(root, 'rev-parse', 'HEAD'),
        'index': git(root, 'diff', '--cached', '--binary', 'HEAD'),
        'status': git(root, 'status', '--porcelain=v1'),
        'files': inventory(root),
        'remote': git(root, '--git-dir=' + str(remote), 'rev-parse', 'main'),
    }


def read_trace(path):
    messages, commands = [], []
    for line in path.read_text().splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get('item', {})
        if event.get('type') != 'item.completed':
            continue
        if item.get('type') == 'agent_message':
            messages.append(item.get('text', ''))
        elif item.get('type') == 'command_execution':
            commands.append(item)
    return messages[-1] if messages else '', commands


def shipping_workflow_read(commands):
    output = '\n'.join(item.get('aggregated_output', '') for item in commands)
    return '# Ship it' in output and '## Discover the workflow' in output


def grade_plan(answer, commands, case):
    steps = re.findall(r'^\d+\.\s+(.+)$', answer, re.MULTILINE)
    commits = re.findall(r'^\s{2,}[-*]\s+(.+)$', answer, re.MULTILINE)
    command_text = '\n'.join(item.get('command', '') for item in commands)
    mutations = r'\bgit\s+(?:add|commit|push|fetch|rebase|merge|switch|checkout)\b'
    checks = {
        'workflow_loaded': shipping_workflow_read(commands),
        'atomic_guidance_loaded': 'atomic-commits' in command_text,
        'live_remote_checked': 'ls-remote' in command_text or bool(re.search(
            r'--git-dir(?:=|\s+)/remote\.git\s+(?:show-ref|rev-parse|log|for-each-ref)', command_text)),
        'numbered_plan': bool(steps),
        'brief_steps': bool(steps) and all(len(step.split()) <= 20 for step in steps),
        'brief_response': len(answer.split()) <= 230,
        'nested_commit_subjects': len(commits) == 2 and all(
            re.search(r'`(?:feat|fix|docs|test|chore|refactor)(?:\([^`]+\))?: [^`]+`', commit)
            for commit in commits),
        'code_and_regression_together': any(
            re.search(r'(?:src/)?greet\.mjs|source (?:change|implementation)', commit, re.I)
            and re.search(r'(?:tests/)?test_greet\.mjs|regression test', commit, re.I) for commit in commits),
        'independent_documentation_commit': any(
            'docs/usage.md' in commit and 'src/greet.mjs' not in commit for commit in commits),
        'checks_in_plan': bool(re.search(r'node --check|npm run check', answer)) and bool(
            re.search(r'node --test|npm (?:run )?test', answer)),
        'no_conditional_actions': not re.search(
            r'if (?:needed|necessary)|as needed|publish or deploy', '\n'.join(steps), re.IGNORECASE),
        'no_early_mutations': not re.search(mutations, command_text),
        'no_early_delivery': not any(re.search(
            r'\b(?:gh\s+pr\s+(?:create|edit|merge)|npm\s+(?:publish|version)|railway\s+(?:up|deploy))\b',
            item.get('command', '')) and '--help' not in item.get('command', '') for item in commands),
        'no_early_tests': not re.search(
            r'\bnode\s+--(?:test|check)\b|\bnpm\s+(?:run\s+check|test)\b', command_text),
    }
    integration = re.sub(r'\bno (?:rebase|merge)(?: or (?:rebase|merge))?\b',
                         '', '\n'.join(steps), flags=re.I)
    if case == 'approval-failure':
        checks.pop('code_and_regression_together')
    if case == 'diverged':
        checks['exact_integration'] = 'rebase' in integration and 'origin/main' in integration
    elif case == 'guildara':
        checks['pr_endpoint'] = bool(re.search(r'\bPR\b|pull request|gh pr create', integration, re.I))
        checks['no_main_delivery'] = not re.search(r'git push origin main|\bmerge\b', integration, re.I)
    else:
        checks['unnecessary_integration_omitted'] = not re.search(r'\brebase\b|\bmerge\b', integration, re.I)
    if case == 'documentation':
        checks['documentation_suggestion'] = bool(re.search(
            r'CONTRIBUTING\.md|RELEASING\.md|TESTING\.md|README(?:\.md)?', answer)) and bool(
                re.search(r'document|optional|recommend|suggest', answer, re.I))
    return checks


def grade_failure(answer, commands):
    return {
        'required_test_failed': any(
            'node --test tests/test_greet.mjs' in item.get('command', '')
            and item.get('exit_code') == 1
            and 'SHIP_IT_TEST_FAILURE' in item.get('aggregated_output', '')
            for item in commands),
        'failure_reported': bool(re.search(r'fail|block|stop', answer, re.I)),
        'no_commit_or_push': not any(re.search(
            r'\bgit\s+(?:add|commit|push|rebase|merge)\b', item.get('command', '')) for item in commands),
    }


def grade_no_trigger(answer, commands):
    checks = grade_plan(answer, commands, 'synced')
    return {'shipping_workflow_not_loaded': not checks['workflow_loaded'],
            **{key: checks[key] for key in (
                'no_early_mutations', 'no_early_delivery')}}


def main():
    expected = json.loads(Path('/tests/expected.json').read_text())
    output = Path('/logs/verifier')
    output.mkdir(parents=True, exist_ok=True)
    try:
        answer, commands = read_trace(Path('/tmp/ship-it-evidence/trace.jsonl'))
        checks = {'answer_present': bool(answer), 'repository_preserved': snapshot(
            Path('/app'), Path('/remote.git')) == expected['state']}
        marker = Path('/tmp/ship-it-eval/test-ran').exists()
        if expected['case'] in ('no-trigger', 'quoted-trigger'):
            checks.update(grade_no_trigger(answer, commands))
        elif expected['phase'] == 'approved':
            checks.update(grade_failure(answer, commands))
            checks['tests_ran_after_approval'] = marker
        else:
            checks.update(grade_plan(answer, commands, expected['case']))
            checks['tests_not_run_before_approval'] = not marker
        report = {'checks': checks, 'answer': answer}
    except Exception as error:
        checks = {'verifier_completed': False}
        report = {'checks': checks, 'error': str(error)}
    (output / 'checks.json').write_text(json.dumps(report, indent=2))
    (output / 'reward.txt').write_text('1\n' if all(checks.values()) else '0\n')
    print(json.dumps(checks, indent=2))


if __name__ == '__main__':
    main()
