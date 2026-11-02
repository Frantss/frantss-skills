"""Evaluate commit-a against executable local Git histories using an installed Codex plugin."""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
from textwrap import dedent

from ship_it import ROOT, configured_model, run_git, write
from ship_it_bare import install_plugin, turn
from ship_it_verifier import inventory
from atomic_commits_verifier import grade

CASES = ('decomposable', 'inseparable')
CHECK_COMMAND = ['node', '--test']
PROMPT = ('commit-a. Execute commits for all pending work. Do not change the implementation, '
          'rewrite existing history, or push. Use only the local repository and installed plugin files; '
          'do not contact external services.')


def decomposable():
    baseline = {
        'apps/dashboard/runtime.mjs': '''\
            export function dashboardSettings() {
              return { product: 'Field Notes', locale: 'en-GB', currency: 'GBP' };
            }
            ''',
        'tests/dashboard.test.mjs': '''\
            import assert from 'node:assert/strict';
            import test from 'node:test';
            import { dashboardSettings } from '../apps/dashboard/runtime.mjs';

            test('dashboard keeps its product and regional settings', () => {
              assert.deepEqual(dashboardSettings(), {
                product: 'Field Notes', locale: 'en-GB', currency: 'GBP',
              });
            });
            ''',
    }
    pending = {
        'packages/configs/index.mjs': '''\
            export const siteConfig = Object.freeze({
              product: 'Field Notes',
              locale: 'en-GB',
              currency: 'GBP',
            });
            ''',
        'apps/dashboard/runtime.mjs': '''\
            import { siteConfig } from '../../packages/configs/index.mjs';

            export function dashboardSettings() {
              return { ...siteConfig };
            }
            ''',
        'tests/configs.test.mjs': '''\
            import assert from 'node:assert/strict';
            import test from 'node:test';
            import { siteConfig } from '../packages/configs/index.mjs';
            import { dashboardSettings } from '../apps/dashboard/runtime.mjs';

            test('shared settings retain the existing dashboard defaults', () => {
              assert.deepEqual(siteConfig, {
                product: 'Field Notes', locale: 'en-GB', currency: 'GBP',
              });
              assert.deepEqual(dashboardSettings(), siteConfig);
            });

            test('a dashboard consumer cannot mutate shared settings', () => {
              assert.throws(() => { siteConfig.currency = 'USD'; }, TypeError);
              const settings = dashboardSettings();
              settings.product = 'My workspace';
              assert.equal(dashboardSettings().product, 'Field Notes');
            });
            ''',
        'docs/configuration.md': '''\
            # Shared configuration

            Import `siteConfig` from `packages/configs/index.mjs` for the product name,
            locale, and billing currency. These settings are frozen. The dashboard
            returns a separate settings object so workspace overrides stay local.
            ''',
        'apps/marketing/home.mjs': '''\
            import { siteConfig } from '../../packages/configs/index.mjs';

            export function marketingPage(title, content) {
              return {
                title: `${title} | ${siteConfig.product}`,
                brand: siteConfig.product,
                lang: siteConfig.locale,
                content,
              };
            }

            export function homePage() {
              return marketingPage('Home', {
                heading: 'Keep your fieldwork in one notebook',
                description: 'Record observations and share notes with your team.',
              });
            }
            ''',
        'tests/home.test.mjs': '''\
            import assert from 'node:assert/strict';
            import test from 'node:test';
            import { homePage } from '../apps/marketing/home.mjs';

            test('homepage publishes its content with the shared product identity', () => {
              assert.deepEqual(homePage(), {
                title: 'Home | Field Notes',
                brand: 'Field Notes',
                lang: 'en-GB',
                content: {
                  heading: 'Keep your fieldwork in one notebook',
                  description: 'Record observations and share notes with your team.',
                },
              });
            });

            test('each homepage request gets its own content', () => {
              homePage().content.heading = 'Changed by a caller';
              assert.equal(homePage().content.heading, 'Keep your fieldwork in one notebook');
            });
            ''',
        'docs/homepage.md': '''\
            # Marketing homepage

            `homePage()` in `apps/marketing/home.mjs` returns the homepage model.
            Its title, brand, and language use the shared site configuration.
            `marketingPage(title, content)` supplies the same page envelope for
            other marketing pages. Each homepage call returns fresh content.
            ''',
        'apps/marketing/pricing.mjs': '''\
            import { siteConfig } from '../../packages/configs/index.mjs';
            import { marketingPage } from './home.mjs';

            const plans = Object.freeze([
              Object.freeze({ name: 'Personal', monthly: 0, seats: 1 }),
              Object.freeze({ name: 'Team', monthly: 12, seats: 5 }),
            ]);

            export function pricingPage() {
              const format = new Intl.NumberFormat(siteConfig.locale, {
                style: 'currency', currency: siteConfig.currency,
                minimumFractionDigits: 0, maximumFractionDigits: 0,
              });
              return marketingPage('Pricing', {
                plans: plans.map(plan => ({ ...plan, price: format.format(plan.monthly) })),
                billingPeriod: 'month',
              });
            }
            ''',
        'tests/pricing.test.mjs': '''\
            import assert from 'node:assert/strict';
            import test from 'node:test';
            import { pricingPage } from '../apps/marketing/pricing.mjs';

            test('pricing uses the marketing envelope and shared billing currency', () => {
              assert.deepEqual(pricingPage(), {
                title: 'Pricing | Field Notes',
                brand: 'Field Notes',
                lang: 'en-GB',
                content: {
                  plans: [
                    { name: 'Personal', monthly: 0, seats: 1, price: '£0' },
                    { name: 'Team', monthly: 12, seats: 5, price: '£12' },
                  ],
                  billingPeriod: 'month',
                },
              });
            });

            test('pricing consumers cannot change the plan catalogue', () => {
              pricingPage().content.plans[1].monthly = 1;
              assert.equal(pricingPage().content.plans[1].monthly, 12);
            });
            ''',
        'docs/pricing.md': '''\
            # Pricing page

            `pricingPage()` in `apps/marketing/pricing.mjs` uses the homepage's
            marketing page envelope and the shared locale and currency.
            The Personal plan costs £0 per month for one seat; Team costs £12 per
            month for five seats. Returned plans are copies of the catalogue.
            ''',
    }
    bundles = [
        ['packages/configs/index.mjs', 'tests/configs.test.mjs', 'docs/configuration.md'],
        ['apps/dashboard/runtime.mjs'],
        ['apps/marketing/home.mjs', 'tests/home.test.mjs', 'docs/homepage.md'],
        ['apps/marketing/pricing.mjs', 'tests/pricing.test.mjs', 'docs/pricing.md'],
    ]
    return baseline, pending, bundles, [
        'packages/configs/index.mjs', 'apps/marketing/home.mjs', 'apps/marketing/pricing.mjs',
    ]


def inseparable():
    baseline = {
        'packages/accounts/index.mjs': '''\
            export function formatAccountName(account) {
              return account.name.trim() || account.email;
            }
            ''',
        'apps/portal/profile.mjs': '''\
            import { formatAccountName } from '../../packages/accounts/index.mjs';

            export function profileHeading(account) {
              return `Account: ${formatAccountName(account)}`;
            }
            ''',
        'tests/profile.test.mjs': '''\
            import assert from 'node:assert/strict';
            import test from 'node:test';
            import { formatAccountName } from '../packages/accounts/index.mjs';
            import { profileHeading } from '../apps/portal/profile.mjs';

            test('account names and portal headings trim surrounding whitespace', () => {
              const account = { name: ' Ada ', email: 'ada@example.invalid' };
              assert.equal(formatAccountName(account), 'Ada');
              assert.equal(profileHeading(account), 'Account: Ada');
            });
            ''',
        'docs/accounts.md': '''\
            # Account names

            `formatAccountName(account)` trims the account name and uses the email
            when the name is blank. The portal profile heading uses this API.
            ''',
    }
    pending = {
        'packages/accounts/index.mjs': '''\
            export function accountDisplayName(account) {
              return account.name.trim() || account.email;
            }
            ''',
        'apps/portal/profile.mjs': '''\
            import { accountDisplayName } from '../../packages/accounts/index.mjs';

            export function profileHeading(account) {
              return `Account: ${accountDisplayName(account)}`;
            }
            ''',
        'tests/profile.test.mjs': '''\
            import assert from 'node:assert/strict';
            import test from 'node:test';
            import { accountDisplayName } from '../packages/accounts/index.mjs';
            import { profileHeading } from '../apps/portal/profile.mjs';

            test('account names and portal headings trim surrounding whitespace', () => {
              const account = { name: ' Ada ', email: 'ada@example.invalid' };
              assert.equal(accountDisplayName(account), 'Ada');
              assert.equal(profileHeading(account), 'Account: Ada');
            });

            test('blank account names use email in both API and portal', () => {
              const account = { name: '  ', email: 'ada@example.invalid' };
              assert.equal(accountDisplayName(account), 'ada@example.invalid');
              assert.equal(profileHeading(account), 'Account: ada@example.invalid');
            });
            ''',
        'docs/accounts.md': '''\
            # Account names

            `accountDisplayName(account)` trims the account name and uses the email
            when the name is blank. The portal profile heading uses this API.
            The former `formatAccountName` export has been removed.
            ''',
    }
    return baseline, pending, [list(pending)], []


def fixture(directory, case):
    if case not in CASES:
        raise ValueError(f'Unknown atomic-commits case: {case}')
    directory = Path(directory)
    seed = directory / 'environment/seed'
    remote = directory / 'environment/remote.git'
    seed.mkdir(parents=True)
    run_git(seed, 'init', '-b', 'main')
    run_git(seed, 'config', 'user.name', 'Skill Eval')
    run_git(seed, 'config', 'user.email', 'eval@example.invalid')
    write(seed / 'AGENTS.md',
          '# Repository instructions\n\n'
          'Use conventional commits and preserve all pending work.\n'
          'When the user issues `commit-a`, locate and read the installed '
          '`atomic-commits/SKILL.md` and follow it.\n')
    write(seed / 'README.md',
          '# Field Notes fixture\n\n'
          'This local Node project is an executable evaluation fixture. '
          'It has no package dependencies.\n')
    write(seed / 'CONTRIBUTING.md',
          '# Contributing\n\n'
          'Run `node --test` to execute every existing behavioral test.\n'
          'Keep implementation, its regression coverage, and its usage documentation together.\n'
          'Delivery for this task is local commits only. Do not push or rewrite existing history.\n')
    write(seed / 'package.json', json.dumps({
        'name': 'field-notes-fixture', 'private': True, 'type': 'module',
        'scripts': {'test': 'node --test'},
    }, indent=2) + '\n')
    baseline, pending, bundles, ordered_paths = (
        decomposable() if case == 'decomposable' else inseparable())
    for name, contents in baseline.items():
        write(seed / name, dedent(contents))
    run_git(seed, 'add', '.')
    run_git(seed, 'commit', '-m', 'feat: add existing application')
    base = run_git(seed, 'rev-parse', 'HEAD')
    run_git(seed, 'clone', '--bare', str(seed.resolve()), str(remote.resolve()))
    run_git(seed, 'remote', 'add', 'origin', str(remote.resolve()))
    run_git(seed, 'fetch', 'origin')
    for name, contents in pending.items():
        write(seed / name, dedent(contents))
    expected = {
        'base': base, 'files': inventory(seed), 'case': case,
        'check_command': list(CHECK_COMMAND), 'bundles': bundles, 'ordered_paths': ordered_paths,
    }
    write(directory / 'expected.json', json.dumps(expected, indent=2) + '\n')
    return expected


def trial(directory, case, auth, model):
    directory = Path(directory).resolve()
    report = {
        'case': case, 'model': model, 'passed': False,
        'artifacts': str(directory), 'checks': {},
    }
    try:
        expected = fixture(directory, case)
        seed, remote = directory / 'environment/seed', directory / 'environment/remote.git'
        remote_before = run_git(remote, 'show-ref')
        remote_head = run_git(remote, 'symbolic-ref', 'HEAD')
        runtime = directory / 'runtime'
        runtime.mkdir(mode=0o700)
        if auth.is_file():
            (runtime / 'auth.json').symlink_to(auth.resolve())
        write(runtime / 'config.toml', '[projects.' + json.dumps(str(seed)) + ']\ntrust_level = "trusted"\n')
        env = {key: value for key, value in os.environ.items() if key in (
            'PATH', 'HOME', 'USER', 'LOGNAME', 'SHELL', 'LANG', 'LC_ALL', 'TMPDIR',
            'OPENAI_API_KEY', 'CODEX_API_KEY')}
        env['CODEX_HOME'] = str(runtime)
        report['installed_plugin'] = str(install_plugin(runtime, env))
        session, answer, commands = turn(seed, remote, env, directory, 'commit-a', PROMPT, model)
        report.update(session=session, answer=answer)
        report['checks'] = grade(seed, expected)
        skill_output = '\n'.join(command.get('aggregated_output', '') for command in commands
                                 if command.get('exit_code') == 0)
        report['checks']['workflow_loaded'] = (
            '# Atomic commits' in skill_output and '## Group by purpose' in skill_output)
        report['checks']['remote_unchanged'] = (
            run_git(remote, 'show-ref') == remote_before
            and run_git(remote, 'symbolic-ref', 'HEAD') == remote_head)
        report['passed'] = all(report['checks'].values())
    except (OSError, RuntimeError, ValueError, subprocess.SubprocessError) as error:
        report['error'] = str(error)
    write(directory / 'result.json', json.dumps(report, indent=2) + '\n')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case', action='append', choices=CASES)
    parser.add_argument('--attempts', type=int, default=3)
    parser.add_argument('--model', default=configured_model())
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    if args.attempts < 1:
        parser.error('attempts must be positive')
    cases = list(dict.fromkeys(args.case or CASES))
    auth = Path(os.environ.get('CODEX_HOME', Path.home() / '.codex')) / 'auth.json'
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    workspace = ROOT / '.scratch/evals' / (stamp + '-atomic-commits')
    results = []
    for case in cases:
        for attempt in range(1, args.attempts + 1):
            directory = workspace / case / str(attempt)
            if args.prepare_only:
                fixture(directory, case)
                print(f'Prepared {case} attempt {attempt}: {directory}', flush=True)
                continue
            report = trial(directory, case, auth, args.model)
            results.append(report['passed'])
            failed = [key for key, passed in report['checks'].items() if not passed]
            detail = report.get('error') or ', '.join(failed)
            print(f'{case} attempt {attempt}: {"PASS" if report["passed"] else "FAIL"} '
                  f'({directory})' + (f' [{detail}]' if detail else ''), flush=True)
    if args.prepare_only:
        print(f'Fixtures and expected inventories: {workspace}')
        return 0
    write(workspace / 'summary.json', json.dumps({
        'passed': sum(results), 'trials': len(results), 'model': args.model,
    }, indent=2) + '\n')
    print(f'Passed {sum(results)}/{len(results)} atomic-commits trials. Artifacts: {workspace}')
    return 0 if all(results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
