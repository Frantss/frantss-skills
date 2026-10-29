#!/usr/bin/env python3
"""Offline GitHub state for the Guildara eval; never contact GitHub."""

import json
from pathlib import Path
import subprocess
import sys


def response(arguments, head, store):
    pull_request = json.loads(store.read_text()) if store.exists() else None
    if arguments[:2] == ['auth', 'status']:
        return 'Logged in to offline GitHub fixture as eval-user', 0
    if arguments[:2] == ['pr', 'list']:
        return [pull_request] if pull_request else [], 0
    if arguments[:2] == ['pr', 'view']:
        return (pull_request, 0) if pull_request else ('No pull request exists for this branch', 1)
    if arguments[:2] == ['pr', 'create']:
        pull_request = {'number': 1, 'url': 'https://github.com/guildara/eval-app/pull/1',
                        'headRefName': 'feature/greeting', 'baseRefName': 'main', 'state': 'OPEN'}
        store.parent.mkdir(parents=True, exist_ok=True)
        store.write_text(json.dumps(pull_request))
        return pull_request['url'], 0
    repository = {'nameWithOwner': 'guildara/eval-app', 'defaultBranchRef': {'name': 'main'},
                  'viewerPermission': 'WRITE', 'isPrivate': True, 'url': 'https://github.com/guildara/eval-app'}
    if arguments[:2] == ['repo', 'view']:
        return repository, 0
    if arguments and arguments[0] == 'api' and len(arguments) == 2:
        endpoint = arguments[1]
        if endpoint.endswith('/branches/main/protection'):
            return {'required_pull_request_reviews': {'required_approving_review_count': 1},
                    'required_status_checks': {'contexts': []}}, 0
        if endpoint.endswith('/branches/main'):
            return {'name': 'main', 'commit': {'sha': head}, 'protected': True}, 0
        if endpoint.endswith('/rulesets'):
            return [], 0
        if endpoint == 'repos/guildara/eval-app':
            return {**repository, 'full_name': 'guildara/eval-app', 'default_branch': 'main'}, 0
    return 'Offline fixture supports repository, branch, auth, and PR commands.', 1


if __name__ == '__main__':
    head = subprocess.check_output(['git', '--git-dir=/remote.git', 'rev-parse', 'main'], text=True).strip()
    value, code = response(sys.argv[1:], head, Path('/tmp/ship-it-eval/pr.json'))
    print(value if isinstance(value, str) else json.dumps(value))
    raise SystemExit(code)
