"""Evaluate bare-command discovery and approval using an installed Codex plugin."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

from ship_it import CHECK, TEST, ROOT, configured_model, fixture, run_git, write
from ship_it_verifier import grade_plan, read_trace, shipping_workflow_read, snapshot

PREPARE = 'Verify the completed implementation using CONTRIBUTING.md and report the result.'
BARE_COMMAND = 'ship it'
APPROVE = 'I approve the proposed plan. Execute it.'
BOUNDARY = ('All delivery targets are local test mirrors. Use local repository and plugin files; '
            'do not contact external services or publish packages.')


def checks_passed(commands):
    successful = '\n'.join(item.get('command', '') + '\n' + item.get('aggregated_output', '')
                           for item in commands if item.get('exit_code') == 0)
    return all(command in successful for command in (CHECK, TEST))


def grade_bare_plan(answer, commands):
    checks = grade_plan(answer, commands, 'synced')
    # Verify actual commit contents after approval instead of requiring paths in the prose.
    for key in ('code_and_regression_together', 'independent_documentation_commit'):
        checks.pop(key)
    return {**checks,
            'approval_requested': bool(re.search(r'approv|confirm|permission', answer, re.I))}


def grade_delivery(seed, remote, before, commands):
    after = snapshot(seed, remote)
    commits = run_git(seed, 'rev-list', '--reverse', before['head'] + '..HEAD').splitlines()
    scopes = [set(run_git(seed, 'diff-tree', '--no-commit-id', '--name-only', '-r', commit).splitlines())
              for commit in commits]
    return {
        'required_checks_passed': checks_passed(commands),
        'implementation_preserved': after['files'] == before['files'],
        'working_tree_clean': not after['status'] and not after['index'],
        'commits_created': after['head'] != before['head'],
        'atomic_commit_scopes': scopes == [{'src/greet.mjs', 'tests/test_greet.mjs'}, {'docs/usage.md'}],
        'remote_matches_head': after['remote'] == after['head'],
        'remote_advanced': after['remote'] != before['remote'],
    }


def install_plugin(runtime, env):
    package = runtime.parent / 'plugin-source'
    for name in ('.codex-plugin', '.claude-plugin', 'skills'):
        shutil.copytree(ROOT / name, package / name,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    for arguments in (('marketplace', 'add', str(package)), ('add', 'frantss-skills@frantss')):
        result = subprocess.run(['codex', 'plugin', *arguments, '--json'], cwd=runtime,
                                env=env, capture_output=True, text=True, timeout=60)
        if result.returncode:
            raise RuntimeError(result.stderr or result.stdout)
    installed = Path(json.loads(result.stdout)['installedPath']).resolve()
    if not installed.is_relative_to(runtime.resolve()):
        raise RuntimeError('Plugin installation escaped the isolated runtime')
    return installed


def turn(seed, remote, env, directory, phase, prompt, model, session=None):
    command = ['codex', 'exec', '--json', '--approve-for-me',
               '--cd', str(seed), '--add-dir', str(remote),
               '-c', 'sandbox_workspace_write.network_access=false',
               '-c', 'developer_instructions=' + json.dumps(BOUNDARY)]
    if model:
        command += ['--model', model]
    if session:
        command += ['resume', session]
    command += [prompt]
    trace = directory / (phase + '.jsonl')
    with trace.open('w') as stdout, (directory / (phase + '.stderr')).open('w') as stderr:
        result = subprocess.run(command, cwd=seed, env=env, stdin=subprocess.DEVNULL, stdout=stdout,
                                stderr=stderr, timeout=240)
    if result.returncode:
        raise RuntimeError(f'{phase} exited {result.returncode}; inspect {trace}')
    events = [json.loads(line) for line in trace.read_text().splitlines() if line.strip()]
    session = next((event['thread_id'] for event in events
                    if event.get('type') == 'thread.started'), session)
    if not session or any(event.get('type') in ('error', 'turn.failed') for event in events):
        raise RuntimeError(f'{phase} did not complete; inspect {trace}')
    answer, commands = read_trace(trace)
    return session, answer, commands


def trial(directory, auth, model):
    directory.mkdir(parents=True)
    fixture(directory, 'synced', 'unused', route_skill=False, local_skills=False)
    seed, remote = directory / 'environment/seed', directory / 'environment/remote.git'
    runtime = directory / 'runtime'
    runtime.mkdir(mode=0o700)
    if auth.is_file():
        (runtime / 'auth.json').symlink_to(auth.resolve())
    write(runtime / 'config.toml', '[projects.' + json.dumps(str(seed)) + ']\ntrust_level = "trusted"\n')
    env = {key: value for key, value in os.environ.items() if key in (
        'PATH', 'HOME', 'USER', 'LOGNAME', 'SHELL', 'LANG', 'LC_ALL', 'TMPDIR',
        'OPENAI_API_KEY', 'CODEX_API_KEY')}
    env['CODEX_HOME'] = str(runtime)
    installed = install_plugin(runtime, env)
    before = snapshot(seed, remote)
    session, answer, commands = turn(seed, remote, env, directory, 'implementation', PREPARE, model)
    phases = {'implementation': {
        'answer_present': bool(answer), 'required_checks_passed': checks_passed(commands),
        'shipping_workflow_not_loaded': not shipping_workflow_read(commands),
        'repository_preserved': snapshot(seed, remote) == before}}
    if all(phases['implementation'].values()):
        session, answer, commands = turn(seed, remote, env, directory, 'plan', BARE_COMMAND, model, session)
        phases['plan'] = {**grade_bare_plan(answer, commands),
                          'repository_preserved': snapshot(seed, remote) == before}
        if all(phases['plan'].values()):
            _, answer, commands = turn(seed, remote, env, directory, 'approved', APPROVE, model, session)
            phases['approved'] = {**grade_delivery(seed, remote, before, commands),
                                  'answer_present': bool(answer)}
    report = {'installed_plugin': str(installed), 'phases': phases,
              'passed': len(phases) == 3 and all(all(checks.values()) for checks in phases.values())}
    write(directory / 'result.json', json.dumps(report, indent=2) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--attempts', type=int, default=3)
    parser.add_argument('--model', default=configured_model())
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error('attempts must be positive')
    auth = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'auth.json'
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    workspace = ROOT / '.scratch/evals' / (stamp + '-bare-command')
    results = []
    for attempt in range(args.attempts):
        directory = workspace / str(attempt + 1)
        try:
            report = trial(directory, auth, args.model)
        except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as error:
            report = {'passed': False, 'error': str(error)}
            write(directory / 'result.json', json.dumps(report, indent=2) + '\n')
        results.append(report['passed'])
        print(f'Attempt {attempt + 1}: {"PASS" if report["passed"] else "FAIL"} ({directory})', flush=True)
    print(f'Passed {sum(results)}/{len(results)} bare-command trials.')
    return 0 if all(results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
