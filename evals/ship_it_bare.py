"""Evaluate bare-command discovery and approval using an installed Claude Code plugin."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

from ship_it import CHECK, TEST, ROOT, fixture, run_git, write
from ship_it_verifier import grade_plan, shipping_workflow_read, snapshot

PREPARE = 'Verify the completed implementation using CONTRIBUTING.md and report the result.'
BARE_COMMAND = 'ship it'
APPROVE = 'I approve the proposed plan. Execute it.'
BOUNDARY = ('All delivery targets are local test mirrors. Use local repository and plugin files; '
            'do not contact external services or publish packages.')
AUTH_KEYS = ('ANTHROPIC_API_KEY', 'CLAUDE_CODE_OAUTH_TOKEN')
PLUGIN = 'frantss-skills@frantss'


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
    for name in ('.claude-plugin', 'skills'):
        shutil.copytree(ROOT / name, package / name,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    for arguments in (('marketplace', 'add', str(package)), ('install', PLUGIN), ('list', '--json')):
        result = subprocess.run(['claude', 'plugin', *arguments], cwd=runtime,
                                env=env, capture_output=True, text=True, timeout=60)
        if result.returncode:
            raise RuntimeError(result.stderr or result.stdout)
    plugin = next(plugin for plugin in json.loads(result.stdout) if plugin['id'] == PLUGIN)
    installed = Path(plugin.get('readFromFolder') or plugin['installPath']).resolve()
    if not (installed.is_relative_to(runtime.resolve()) or installed == package.resolve()):
        raise RuntimeError('Plugin installation escaped the isolated runtime')
    return installed


def text_of(content):
    if isinstance(content, str):
        return content
    return '\n'.join(block.get('text', '') for block in content or [] if block.get('type') == 'text')


def read_trace(path):
    """Return the final answer and tool calls as command, aggregated_output, and exit_code items."""
    answer, commands, calls = '', [], {}
    for line in path.read_text().splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get('type') == 'result':
            answer = event.get('result') or ''
        content = event.get('message', {}).get('content', [])
        if isinstance(content, str):
            content = [{'type': 'text', 'text': content}]
        for block in content:
            if block.get('type') == 'tool_use':
                arguments = block.get('input', {})
                calls[block.get('id')] = (arguments.get('command', '') if block.get('name') == 'Bash'
                                          else block.get('name', '') + ' ' + json.dumps(arguments))
            elif block.get('type') == 'tool_result' and block.get('tool_use_id') in calls:
                commands.append({'command': calls.pop(block['tool_use_id']),
                                 'aggregated_output': text_of(block.get('content')),
                                 'exit_code': 1 if block.get('is_error') else 0})
            elif block.get('type') == 'text' and event.get('type') == 'user' and commands:
                # Claude Code injects a loaded skill's body as a user message after the Skill result.
                commands[-1]['aggregated_output'] += '\n' + block.get('text', '')
    return answer, commands


def isolated_env(runtime):
    env = {key: value for key, value in os.environ.items() if key in (
        'PATH', 'HOME', 'USER', 'LOGNAME', 'SHELL', 'LANG', 'LC_ALL', 'TMPDIR', *AUTH_KEYS)}
    env['CLAUDE_CONFIG_DIR'] = str(runtime)
    return env


def turn(seed, remote, env, directory, phase, prompt, model, session=None):
    instructions = BOUNDARY + '\n\nRepository AGENTS.md:\n' + (seed / 'AGENTS.md').read_text()
    command = ['claude', '-p', '--output-format', 'stream-json', '--verbose',
               '--permission-mode', 'bypassPermissions', '--append-system-prompt', instructions,
               '--disallowedTools', 'WebFetch,WebSearch', '--add-dir', str(remote)]
    if model:
        command += ['--model', model]
    if session:
        command += ['--resume', session]
    trace = directory / (phase + '.jsonl')
    # The prompt goes through stdin because --disallowedTools and --add-dir take variadic arguments.
    with trace.open('w') as stdout, (directory / (phase + '.stderr')).open('w') as stderr:
        result = subprocess.run(command, cwd=seed, env=env, input=prompt, stdout=stdout,
                                stderr=stderr, text=True, timeout=240)
    if result.returncode:
        raise RuntimeError(f'{phase} exited {result.returncode}; inspect {trace}')
    events = [json.loads(line) for line in trace.read_text().splitlines() if line.strip()]
    final = next((event for event in reversed(events) if event.get('type') == 'result'), {})
    session = final.get('session_id') or session
    if not session or final.get('is_error', True):
        raise RuntimeError(f'{phase} did not complete; inspect {trace}')
    answer, commands = read_trace(trace)
    return session, answer, commands


def trial(directory, model):
    directory.mkdir(parents=True)
    fixture(directory, 'synced', 'unused', route_skill=False, local_skills=False)
    seed, remote = directory / 'environment/seed', directory / 'environment/remote.git'
    runtime = directory / 'runtime'
    runtime.mkdir(mode=0o700)
    env = isolated_env(runtime)
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
    parser.add_argument('--model', default=os.environ.get('EVAL_MODEL'))
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error('attempts must be positive')
    if not any(os.environ.get(key) for key in AUTH_KEYS):
        parser.error('set CLAUDE_CODE_OAUTH_TOKEN (from claude setup-token) or ANTHROPIC_API_KEY')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    workspace = ROOT / '.scratch/evals' / (stamp + '-bare-command')
    results = []
    for attempt in range(args.attempts):
        directory = workspace / str(attempt + 1)
        try:
            report = trial(directory, args.model)
        except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as error:
            report = {'passed': False, 'error': str(error)}
            write(directory / 'result.json', json.dumps(report, indent=2) + '\n')
        results.append(report['passed'])
        print(f'Attempt {attempt + 1}: {"PASS" if report["passed"] else "FAIL"} ({directory})', flush=True)
    print(f'Passed {sum(results)}/{len(results)} bare-command trials.')
    return 0 if all(results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
