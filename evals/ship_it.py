"""Prepare and run disposable Harbor tasks against the current ship-it skill."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import tomllib

from ship_it_verifier import snapshot

ROOT = Path(__file__).resolve().parents[1]
CASES = ('synced', 'diverged', 'documentation', 'guildara', 'approval-failure',
         'no-trigger', 'quoted-trigger')
DEFAULT_IMAGE = 'node:22.21.0-bookworm-slim'
CHECK = 'node --check src/greet.mjs'
TEST = 'node --test tests/test_greet.mjs'
PROMPT = ('ship it. Dry run only: inspect and propose the exact plan, '
          'then stop for approval. During this dry run, use only local test mirrors and repository '
          'metadata; do not execute external service requests. Include the full project delivery workflow in the plan.')
DOCKERFILE = '''FROM __BASE_IMAGE__
RUN (command -v git && command -v python3 && command -v curl) || \\
    (apt-get update && apt-get install -y --no-install-recommends git python3 ca-certificates curl \\
    && rm -rf /var/lib/apt/lists/*)
WORKDIR /app
COPY seed/ /app/
COPY remote.git/ /remote.git/
COPY service-bin/ /usr/local/bin/
RUN git config --global --add safe.directory /app \\
    && git remote set-url origin /remote.git && mkdir -p /tmp/ship-it-eval
'''


def run_git(root, *arguments):
    env = dict(os.environ, GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull,
               GIT_AUTHOR_DATE='2026-01-01T00:00:00Z', GIT_COMMITTER_DATE='2026-01-01T00:00:00Z')
    return subprocess.check_output(['git', *arguments], cwd=root, env=env,
                                   stderr=subprocess.PIPE, text=True).strip()


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def fixture(task, case, image):
    seed = task / 'environment/seed'
    seed.mkdir(parents=True)
    (task / 'environment/service-bin').mkdir()
    run_git(seed, 'init', '-b', 'main')
    run_git(seed, 'config', 'user.name', 'Skill Eval')
    run_git(seed, 'config', 'user.email', 'eval@example.invalid')
    write(seed / '.gitignore', '.agents/\n')
    routing = next(line for line in (ROOT / 'AGENTS.md').read_text().splitlines()
                   if line.startswith('- When the user issues `ship it` as a command,'))
    write(seed / 'AGENTS.md', 'Use conventional commits and atomic commits. Preserve unrelated work.\n'
          + routing + '\n')
    readme = '# Greeting fixture\nPersonal project. Source is distributed through the main branch in Git.\n'
    conventions = (f'# Contributing\nRun `{CHECK}` and `{TEST}` before committing or delivering. '
                   'On main, ship directly to origin/main. On a feature branch, rebase onto origin/main, '
                   'fast-forward main, and push main. No npm publication, tags, or deployment.\n')
    if case == 'guildara':
        readme = '# Guildara greeting fixture\nThe PR destination is guildara/eval-app, targeting main.\n'
        conventions = (f'# Contributing\nThis is Guildara. Run `{CHECK}` and `{TEST}`. '
                       'Commit, push the feature branch, and open a PR targeting main. Stop at the PR. '
                       'The local origin is an offline mirror of guildara/eval-app; pushes to origin '
                       'represent GitHub delivery in this fixture. The gh command provides authoritative '
                       'offline results and stores PRs locally. No PR exists yet; use the repository PR template.\n')
        write(seed / '.github/pull_request_template.md', '## Change\n\n## Validation\n')
        shutil.copy2(ROOT / 'evals/github_fixture.py', task / 'environment/service-bin/gh')
        (task / 'environment/service-bin/gh').chmod(0o755)
    if case == 'documentation':
        readme += 'Run `npm run tests` to check the project.\n'
    else:
        write(seed / 'CONTRIBUTING.md', conventions)
    write(seed / 'README.md', readme)
    write(seed / 'package.json', json.dumps({'name': 'greeting-fixture', 'private': True,
          'scripts': {'check': CHECK, 'test': TEST}}, indent=2) + '\n')
    write(seed / 'src/greet.mjs', 'export const greet = name => `Hello ${name}`;\n')
    regression = "assert.equal(greet(' Ada '), 'Hello Ada');\n"
    tests = ("import assert from 'node:assert/strict';\n"
             "import { greet } from '../src/greet.mjs';\nassert.equal(greet('Ada'), 'Hello Ada');\n")
    if case == 'approval-failure':
        tests += (regression + "import { appendFileSync } from 'node:fs';\n"
                  "appendFileSync('/tmp/ship-it-eval/test-ran', 'ran\\n');\n"
                  "throw new Error('SHIP_IT_TEST_FAILURE');\n")
    write(seed / 'tests/test_greet.mjs', tests)
    write(seed / 'docs/usage.md', '# Usage\nImport greet and supply a name.\n')
    run_git(seed, 'add', '.')
    run_git(seed, 'commit', '-m', 'feat: add greeting')
    remote = task / 'environment/remote.git'
    run_git(seed, 'clone', '--bare', str(seed), str(remote))
    run_git(seed, 'remote', 'add', 'origin', str(remote))
    run_git(seed, 'fetch', 'origin')
    if case in ('diverged', 'guildara'):
        run_git(seed, 'switch', '-c', 'feature/greeting')
    if case == 'diverged':
        write(seed / 'branch-context.txt', 'Existing feature work.\n')
        run_git(seed, 'add', 'branch-context.txt')
        run_git(seed, 'commit', '-m', 'docs: record branch context')
        with tempfile.TemporaryDirectory() as other:
            run_git(seed, 'clone', str(remote), other)
            other = Path(other)
            run_git(other, 'config', 'user.name', 'Remote Eval')
            run_git(other, 'config', 'user.email', 'remote@example.invalid')
            write(other / 'remote-context.txt', 'Remote main advanced.\n')
            run_git(other, 'add', '.')
            run_git(other, 'commit', '-m', 'docs: record remote context')
            run_git(other, 'push', 'origin', 'main')
    write(seed / 'src/greet.mjs', 'export const greet = name => `Hello ${name.trim()}`;\n')
    if case != 'approval-failure':
        with (seed / 'tests/test_greet.mjs').open('a') as stream:
            stream.write(regression)
    with (seed / 'docs/usage.md').open('a') as stream:
        stream.write('Send support requests to help@example.invalid.\n')
    for name in ('ship-it', 'atomic-commits'):
        shutil.copytree(ROOT / 'skills' / name, seed / '.agents/skills' / name,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    write(task / 'environment/Dockerfile', DOCKERFILE.replace('__BASE_IMAGE__', image))
    return snapshot(seed, remote)


def prepare(destination, cases, image=DEFAULT_IMAGE):
    destination.mkdir(parents=True, exist_ok=False)
    for case in cases:
        task = destination / case
        state = fixture(task, case, image)
        config = ('schema_version = "1.4"\n'
                  'artifacts = ["/app", "/remote.git", "/tmp/ship-it-evidence", "/tmp/ship-it-eval"]\n'
                  f'\n[task]\nname = "local/ship-it-{case}"\nversion = "1.0.0"\n'
                  '\n[agent]\ntimeout_sec = 180\n'
                  '\n[environment]\nbuild_timeout_sec = 300\n'
                  '\n[verifier]\nenvironment_mode = "separate"\ntimeout_sec = 60\n'
                  '\n[[verifier.collect]]\ncommand = "mkdir -p /tmp/ship-it-evidence && '
                  'cp /logs/agent/codex.txt /tmp/ship-it-evidence/trace.jsonl"\n')
        phases = ('plan', 'approved') if case == 'approval-failure' else ('plan',)
        for phase in phases:
            folder = task if len(phases) == 1 else task / 'steps' / phase
            if len(phases) > 1:
                config += f'\n[[steps]]\nname = "{phase}"\nmin_reward = 1.0\n'
            prompt = PROMPT if phase == 'plan' else (
                'I approve the proposed plan. Execute it. Do not alter the test commands or test fixtures. '
                'All remotes are local test mirrors; do not access external services.')
            if case == 'no-trigger':
                prompt = ('Prepare a release plan for the current changes. Dry run only; '
                          'use local repository metadata and do not execute external service requests.')
            elif case == 'quoted-trigger':
                prompt = 'What does the phrase "ship it" mean in software development? Answer briefly.'
            if case == 'approval-failure' and phase == 'plan':
                prompt += ' Test commands and fixtures are maintained separately and must remain unchanged throughout this task.'
            write(folder / 'instruction.md', prompt + '\n')
            write(folder / 'tests/expected.json', json.dumps(
                {'case': case, 'phase': phase, 'state': state}, indent=2))
            shutil.copy2(ROOT / 'evals/ship_it_verifier.py', folder / 'tests/verify.py')
            write(folder / 'tests/test.sh', '#!/bin/bash\nset -eu\npython3 /tests/verify.py\n')
        write(task / 'task.toml', config)


def configured_model():
    if os.environ.get('EVAL_MODEL'):
        return os.environ['EVAL_MODEL']
    config = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'config.toml'
    return tomllib.loads(config.read_text()).get('model') if config.exists() else None


def summarize(job, expected_trials):
    rows = []
    for path in sorted(job.glob('*/result.json')):
        result = json.loads(path.read_text())
        reward = (result.get('verifier_result') or {}).get('rewards', {}).get('reward')
        steps = result.get('step_results') or []
        expected_steps = 2 if result['task_name'].endswith('approval-failure') else 0
        passed = reward == 1 and not result.get('exception_info') and all(
            (step.get('verifier_result') or {}).get('rewards', {}).get('reward') == 1
            and not step.get('exception_info') for step in steps) and len(steps) == expected_steps
        rows.append({'case': result['task_name'], 'passed': passed, 'reward': reward,
                     'evidence': str(path)})
    summary = {'passed': sum(row['passed'] for row in rows), 'expected': expected_trials, 'trials': rows}
    write(job / 'summary.json', json.dumps(summary, indent=2))
    print(f"Passed {summary['passed']}/{expected_trials} trials. Results: {job / 'summary.json'}")
    return 0 if len(rows) == expected_trials and all(row['passed'] for row in rows) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--case', action='append', choices=CASES)
    parser.add_argument('--attempts', type=int, default=3)
    parser.add_argument('--concurrency', type=int, default=2)
    parser.add_argument('--model', default=configured_model())
    parser.add_argument('--image', default=os.environ.get('EVAL_IMAGE', DEFAULT_IMAGE))
    args = parser.parse_args()
    if args.attempts < 1 or args.concurrency < 1:
        parser.error('attempts and concurrency must be positive')
    if not args.image or any(character.isspace() for character in args.image):
        parser.error('image must be a single Docker image reference')
    cases = args.case or CASES
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    workspace = ROOT / '.scratch/evals' / stamp
    prepare(workspace / 'tasks', cases, args.image)
    if args.prepare_only:
        print(workspace / 'tasks')
        return 0
    if not args.model:
        parser.error('set EVAL_MODEL or pass --model; no Codex model was configured')
    harbor = Path(sys.executable).parent / 'harbor'
    if not harbor.exists():
        parser.error('run make eval-setup first')
    for case in cases:
        subprocess.run([str(harbor), 'lint', str(workspace / 'tasks' / case)], check=True)
    env = dict(os.environ)
    auth = Path(env.get('CODEX_HOME', Path.home() / '.codex')) / 'auth.json'
    if not any(env.get(key) for key in ('OPENAI_API_KEY', 'CODEX_API_KEY', 'CODEX_AUTH_JSON_PATH')):
        if not auth.exists():
            parser.error('log in with codex login or provide an API key')
        env['CODEX_AUTH_JSON_PATH'] = str(auth)
    command = [str(harbor), 'run', '--path', str(workspace / 'tasks'), '--agent', 'codex',
               '--model', args.model, '--resume-trajectory', '--n-attempts', str(args.attempts),
               '--n-concurrent', str(args.concurrency), '--jobs-dir', str(workspace),
               '--job-name', 'job', '--quiet']
    result = subprocess.run(command, env=env)
    return summarize(workspace / 'job', len(cases) * args.attempts) if result.returncode == 0 else result.returncode


if __name__ == '__main__':
    raise SystemExit(main())
