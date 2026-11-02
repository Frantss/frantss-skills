"""Grade actual commit trees without modifying the evaluated repository."""

from collections import Counter, defaultdict
import hashlib
from pathlib import Path
import subprocess
import tempfile

from ship_it_verifier import git, inventory

CHECK_TIMEOUT = 30


def baseline_inventory(seed, base):
    files = {}
    for entry in git(seed, 'ls-tree', '-rz', base).split('\0'):
        if not entry:
            continue
        metadata, path = entry.split('\t', 1)
        _, kind, object_id = metadata.split()
        if kind == 'blob':
            content = subprocess.check_output(
                ['git', 'cat-file', 'blob', object_id], cwd=seed, stderr=subprocess.PIPE)
            files[path] = hashlib.sha256(content).hexdigest()
    return files


def commit_passes(seed, commit, check_command):
    with tempfile.TemporaryDirectory(prefix='atomic-commit-') as temporary:
        commands = [
            ['git', 'clone', '--quiet', '--no-local', '--no-checkout', str(seed.resolve()), temporary],
            ['git', '-c', 'core.fsmonitor=false', 'checkout', '--quiet', '--detach', commit],
            check_command,
        ]
        for command in commands:
            try:
                result = subprocess.run(command, cwd=temporary, capture_output=True,
                                        text=True, timeout=CHECK_TIMEOUT)
            except (OSError, subprocess.TimeoutExpired) as error:
                print(f'{commit}: {command!r}: {error}')
                if isinstance(error, subprocess.TimeoutExpired):
                    print(error.stdout or '', error.stderr or '', sep='\n')
                return False
            if result.returncode:
                print(f'{commit}: {command!r} exited {result.returncode}')
                print(result.stdout, result.stderr, sep='\n')
                return False
    return True


def grade(seed, expected):
    seed = Path(seed)
    checks = {
        'implementation_preserved': inventory(seed) == expected['files'],
        'working_tree_clean': not git(seed, 'status', '--porcelain=v1', '--untracked-files=all'),
        'baseline_ancestor': False,
        'commits_created': False,
        'pending_paths_committed_once': False,
        'bundles_together': False,
        'milestones_separate_and_ordered': False,
        'intermediate_trees_pass': False,
    }
    ancestor = subprocess.run(
        ['git', '-c', 'core.fsmonitor=false', 'merge-base', '--is-ancestor', expected['base'], 'HEAD'],
        cwd=seed, capture_output=True, text=True)
    checks['baseline_ancestor'] = ancestor.returncode == 0
    if not checks['baseline_ancestor']:
        return checks

    commits = git(seed, 'rev-list', '--reverse', '--topo-order', expected['base'] + '..HEAD').splitlines()
    checks['commits_created'] = bool(commits)
    if not commits:
        return checks

    before = baseline_inventory(seed, expected['base'])
    pending = {path for path in before.keys() | expected['files'].keys()
               if before.get(path) != expected['files'].get(path)}
    touched = Counter()
    positions = defaultdict(list)
    for index, commit in enumerate(commits):
        paths = set(git(seed, 'diff-tree', '--root', '-m', '--no-commit-id', '--name-only',
                        '--no-renames', '-r', '-z', commit).split('\0')) - {''}
        touched.update(paths)
        for path in paths:
            positions[path].append(index)
    checks['pending_paths_committed_once'] = bool(pending) and touched == Counter(dict.fromkeys(pending, 1))
    checks['bundles_together'] = all(
        bool(bundle) and all(len(positions[path]) == 1 for path in bundle)
        and len({positions[path][0] for path in bundle}) == 1
        for bundle in expected['bundles'])
    ordered = expected['ordered_paths']
    checks['milestones_separate_and_ordered'] = all(len(positions[path]) == 1 for path in ordered) and all(
        positions[left][0] < positions[right][0] for left, right in zip(ordered, ordered[1:]))
    results = [commit_passes(seed, commit, expected['check_command']) for commit in commits]
    checks['intermediate_trees_pass'] = all(results)
    return checks
