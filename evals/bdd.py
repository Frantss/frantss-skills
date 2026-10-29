"""Exercise selected BDD regression requests as isolated Harbor tasks."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

from ship_it import DEFAULT_IMAGE, configured_model, run_git, summarize, write
from ship_it_verifier import inventory

ROOT = Path(__file__).resolve().parents[1]
CASES = ('direct', 'stale', 'reuse', 'partial', 'audit')
SKILLS = ('break-down', 'frame-problem', 'design-solution', 'discover-behavior',
          'formulate-behavior', 'slice-work', 'implement-ticket')
DOCKERFILE = '''FROM __BASE_IMAGE__
RUN (command -v git && command -v python3) || \
    (apt-get update && apt-get install -y --no-install-recommends git python3 ca-certificates \
    && rm -rf /var/lib/apt/lists/*)
WORKDIR /app
COPY seed/ /app/
RUN git config --global --add safe.directory /app && mkdir -p /tmp/bdd-eval
'''
RUN_RECORD = '''---
feature_name: Upload limits
feature_slug: upload-limits
run_id: upload-limits-001
stage: implementation
current_slice: S-001
current_ticket: TK-001
---

## Documents
### S-001: Upload limits
Scope: Settled integer size limits only.
Members: acceptance.md#R-001; tickets.md#TK-001
Dependencies: None

| File | Status |
| --- | --- |
| acceptance.md | partial |
| tickets.md | partial |

## Validation
Implementation: Ticket | State | Evidence
TK-001 | pending | None
TK-002 | blocked | Duplicate policy is undecided

Behavior checks: Ticket | Cases | Check | Result
TK-001 | 0, 1, 5, 6 | node --test | not_run

Human note: preserve this note and the unresolved duplicate policy.

## Next action
Implement TK-001 only.
'''


def requests():
    rows = json.loads((ROOT / 'tests/fixtures/bdd-requests.json').read_text())
    selected = [row for row in rows if row.get('eval_case')]
    result = {row['eval_case']: row for row in selected}
    if len(result) != len(selected) or set(result) != set(CASES):
        raise ValueError('BDD eval_case values must identify each supported case once')
    return result


def fixture(seed, case):
    seed.mkdir(parents=True)
    write(seed / '.gitignore', '.agents/\n')
    write(seed / 'AGENTS.md',
          'Use the installed skills when their purpose fits. These fixture requests authorize '
          'the requested local implementation or report. Do not publish or contact external services.\n')
    write(seed / 'README.md', '# BDD fixture\n'
          'Node.js is available. Use node --test for native tests. '
          'Reports requested by the instruction are authorized output artifacts.\n')
    for name in SKILLS:
        shutil.copytree(ROOT / 'skills' / name, seed / '.agents/skills' / name)
    run_git(seed, 'init', '-b', 'main')
    run_git(seed, 'config', 'user.name', 'BDD Eval')
    run_git(seed, 'config', 'user.email', 'bdd@example.invalid')
    if case in ('direct', 'partial', 'audit'):
        write(seed / 'acceptance.md', '# Agreed behavior\n'
              'R-001: Inputs are integers. validate(value, state) returns true for integers '
              '1 through 5 inclusive, false otherwise, and leaves state unchanged. '
              'Boundary cases are 0, 1, 5, and 6.\n')
        implementation = 'export function validate(value, state) { return false; }\n'
        if case == 'audit':
            implementation = (
                "import { appendFileSync } from 'node:fs';\n"
                'export function validate(value, state) {\n'
                "  appendFileSync('/tmp/bdd-eval/inputs.jsonl', JSON.stringify(value) + '\\n');\n"
                '  return value >= 1 && value <= 6;\n}\n')
        write(seed / 'src/validator.mjs', implementation)
        write(seed / 'tests/validator.test.mjs',
              "import assert from 'node:assert/strict';\n"
              "import { validate } from '../src/validator.mjs';\n"
              "assert.equal(validate(1, {}), true);\n"
              "assert.equal(validate(0, {}), false);\n")
        if case == 'partial':
            folder = seed / '.scratch/bdd/upload-limits-001'
            write(folder / 'run.md', RUN_RECORD)
            shutil.copy2(seed / 'acceptance.md', folder / 'acceptance.md')
            with (folder / 'acceptance.md').open('a') as stream:
                stream.write('Q-001: Duplicate-upload policy is undecided.\n')
            write(folder / 'tickets.md', '# Tickets\n'
                  '## TK-001: Validate integer size\nAcceptance: acceptance.md#R-001. Dependencies: None.\n'
                  '## TK-002: Reject duplicate uploads\nBlocked by Q-001. Do not implement.\n')
        return ''
    write(seed / 'specification.md', '# Agreed invitation requirement\n'
          'R-001: Invitation expiry is seven days. Resend limit is undecided.\n')
    write(seed / 'src/invitations.mjs', 'export const expiryDays = 7;\n')
    run_git(seed, 'add', '.')
    run_git(seed, 'commit', '-m', 'feat: seed invitations')
    revision = run_git(seed, 'rev-parse', 'HEAD')
    write(seed / 'breakdown.md', '# Invitation breakdown\n'
          f'Sources inspected: specification.md and src/invitations.mjs at {revision}.\n'
          'R-001: Agreed expiry is seven days.\n'
          f'I-001: Code inference: expiryDays is 7, inspected revision {revision}.\n'
          'Q-001: Resend limit is undecided. No numeric limit has been agreed.\n')
    if case == 'stale':
        write(seed / 'src/invitations.mjs', 'export const expiryDays = 14;\n')
    return revision


def prepare(destination, cases, image=DEFAULT_IMAGE):
    matrix = requests()
    destination.mkdir(parents=True, exist_ok=False)
    for case in cases:
        task = destination / case
        seed = task / 'environment/seed'
        fixture(seed, case)
        run_git(seed, 'add', '.')
        run_git(seed, 'commit', '-m', 'test: prepare BDD case')
        state = inventory(seed)
        prompt = matrix[case]['request']
        if case in ('direct', 'partial'):
            prompt += (' The existing API is src/validator.mjs: validate(value, state). '
                       'Acceptance is in acceptance.md; run node --test. '
                       'Return report.json with fields status (done or blocked), scope, '
                       'and checks (actual commands and results).')
        elif case == 'audit':
            prompt += (' The existing API is src/validator.mjs: validate(value, state). '
                       'Acceptance is in acceptance.md. Its existing input telemetry writes only to '
                       '/tmp/bdd-eval; preserve it. Save report.json with cases: an array of '
                       'objects containing input, expected, actual, and status (passed or failed).')
        else:
            prompt += (' Use specification.md, breakdown.md, and relevant current sources. '
                       'Save a JSON handoff in report.json with rule_id, agreed_expiry_days, '
                       'implementation_expiry_days, implementation_revision, resend_limit '
                       '(null when undecided), and questions. Ask the consequential question '
                       'rather than choosing an unagreed limit; do not edit the subject software.')
        write(task / 'instruction.md', prompt + '\n')
        write(task / 'environment/Dockerfile', DOCKERFILE.replace('__BASE_IMAGE__', image))
        write(task / 'tests/expected.json', json.dumps({
            'case': case, 'state': state, 'revision': run_git(seed, 'rev-parse', 'HEAD')}, indent=2))
        for filename in ('bdd_verifier.py', 'ship_it_verifier.py'):
            shutil.copy2(ROOT / 'evals' / filename, task / 'tests' / filename)
        write(task / 'tests/test.sh', '#!/bin/bash\nset -eu\npython3 /tests/bdd_verifier.py\n')
        write(task / 'task.toml',
              'schema_version = "1.4"\nartifacts = ["/app", "/tmp/bdd-eval", "/tmp/bdd-evidence"]\n'
              f'\n[task]\nname = "local/bdd-{case}"\nversion = "1.0.0"\n'
              '\n[agent]\ntimeout_sec = 240\n'
              '\n[environment]\nbuild_timeout_sec = 300\n'
              '\n[verifier]\nenvironment_mode = "separate"\ntimeout_sec = 90\n'
              '\n[[verifier.collect]]\ncommand = "mkdir -p /tmp/bdd-evidence && '
              'cp /logs/agent/codex.txt /tmp/bdd-evidence/trace.jsonl"\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--case', action='append', choices=CASES)
    parser.add_argument('--attempts', type=int, default=1)
    parser.add_argument('--model', default=configured_model())
    parser.add_argument('--image', default=os.environ.get('EVAL_IMAGE', DEFAULT_IMAGE))
    args = parser.parse_args()
    if args.attempts < 1 or not args.image or any(c.isspace() for c in args.image):
        parser.error('attempts must be positive and image must be one Docker image reference')
    cases = args.case or CASES
    workspace = ROOT / '.scratch/evals' / ('bdd-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    prepare(workspace / 'tasks', cases, args.image)
    if args.prepare_only:
        print(workspace / 'tasks')
        return 0
    harbor = Path(sys.executable).parent / 'harbor'
    if not harbor.exists() or not args.model:
        parser.error('run make eval-setup and configure EVAL_MODEL or --model')
    for case in cases:
        subprocess.run([str(harbor), 'lint', str(workspace / 'tasks' / case)], check=True)
    env = dict(os.environ)
    if not any(env.get(key) for key in ('OPENAI_API_KEY', 'CODEX_API_KEY', 'CODEX_AUTH_JSON_PATH')):
        auth = Path(env.get('CODEX_HOME', Path.home() / '.codex')) / 'auth.json'
        if not auth.exists():
            parser.error('log in with codex login or provide an API key')
        env['CODEX_AUTH_JSON_PATH'] = str(auth)
    result = subprocess.run([
        str(harbor), 'run', '--path', str(workspace / 'tasks'), '--agent', 'codex',
        '--model', args.model, '--n-attempts', str(args.attempts), '--n-concurrent', '1',
        '--jobs-dir', str(workspace), '--job-name', 'job', '--quiet'], env=env)
    return summarize(workspace / 'job', len(cases) * args.attempts) if result.returncode == 0 else result.returncode


if __name__ == '__main__':
    raise SystemExit(main())
