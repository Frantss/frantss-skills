import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]


class PluginTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for directory in ('.claude-plugin', '.codex-plugin', 'skills'):
            shutil.copytree(SOURCE / directory, self.root / directory,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))

    def test_marketplace_exposes_one_plugin_with_all_skills(self):
        self.assertFalse((SOURCE / 'plugins').exists())
        names = [path.parent.name for path in self.root.glob('skills/*/SKILL.md')]
        self.assertEqual(len(names), 17)
        self.assertEqual(len(set(names)), 17)
        market = json.loads((self.root / '.claude-plugin/marketplace.json').read_text())
        self.assertEqual(market['name'], 'frantss')
        self.assertEqual(len(market['plugins']), 1)
        entry = market['plugins'][0]
        self.assertEqual(entry['name'], 'frantss-skills')
        self.assertEqual((self.root / entry['source']).resolve(), self.root.resolve())
        shared = json.loads((self.root / '.claude-plugin/plugin.json').read_text())
        codex = json.loads((self.root / '.codex-plugin/plugin.json').read_text())
        self.assertEqual(shared['name'], entry['name'])
        self.assertEqual(codex.pop('skills'), './skills/')
        self.assertEqual(shared, codex)

    def assert_installed_skills(self, installed):
        expected = self.root / 'skills'
        actual = installed / 'skills'
        self.assertEqual({p.relative_to(expected) for p in expected.rglob('*') if p.is_file()},
                         {p.relative_to(actual) for p in actual.rglob('*') if p.is_file()})
        for path in actual.rglob('*'):
            self.assertFalse(path.is_symlink(), path)
            if path.is_file():
                self.assertEqual(path.read_bytes(), (expected / path.relative_to(actual)).read_bytes())

    @unittest.skipUnless(shutil.which('gh'), 'GitHub CLI is needed for skill discovery')
    def test_github_cli_discovers_skills_once(self):
        result = subprocess.run(['gh', 'skill', 'install', str(self.root), '--from-local'],
                                cwd=self.root, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        discovered = [line.split('\t')[0].rsplit('/', 1)[-1] for line in result.stdout.splitlines() if line]
        expected = [path.parent.name for path in self.root.glob('skills/*/SKILL.md')]
        self.assertCountEqual(discovered, expected)

    @unittest.skipUnless(shutil.which('gh'), 'GitHub CLI is needed for skill installation')
    def test_github_cli_installs_one_skill_with_bundled_resources(self):
        with tempfile.TemporaryDirectory() as destination:
            result = subprocess.run(
                ['gh', 'skill', 'install', str(self.root), 'bdd-design-solution',
                 '--from-local', '--dir', destination],
                cwd=self.root, capture_output=True, text=True, timeout=30)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual({p.name for p in Path(destination).iterdir()}, {'bdd-design-solution'})
            reference = Path('bdd-design-solution/references/run-record.md')
            self.assertEqual((Path(destination) / reference).read_bytes(),
                             (self.root / 'skills' / reference).read_bytes())

    @unittest.skipUnless(shutil.which('codex'), 'Codex CLI is needed for plugin installation')
    def test_codex_installs_all_skills_and_refreshes_without_sync(self):
        with tempfile.TemporaryDirectory() as runtime:
            env = {**os.environ, 'CODEX_HOME': runtime}

            def codex(*args):
                result = subprocess.run(['codex', 'plugin', *args, '--json'], cwd=runtime,
                                        env=env, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            codex('marketplace', 'add', str(self.root))
            installed = Path(codex('add', 'frantss-skills@frantss')['installedPath'])
            self.assertTrue(installed.resolve().is_relative_to(Path(runtime).resolve()))
            manifest = json.loads((installed / '.codex-plugin/plugin.json').read_text())
            self.assertEqual(manifest['skills'], './skills/')
            self.assert_installed_skills(installed)
            skills = self.root / 'skills'
            (skills / 'tracking-added').mkdir()
            (skills / 'tracking-added/SKILL.md').write_text('---\nname: tracking-added\ndescription: Added.\n---\nTrack.\n')
            (skills / 'tracking-tasks/SKILL.md').write_text('Updated instruction.\n')
            shutil.rmtree(skills / 'tracking-collect')
            installed = Path(codex('add', 'frantss-skills@frantss')['installedPath'])
            self.assert_installed_skills(installed)
            self.assertTrue((installed / 'skills/tracking-added/SKILL.md').is_file())
            self.assertEqual((installed / 'skills/tracking-tasks/SKILL.md').read_text(), 'Updated instruction.\n')
            self.assertFalse((installed / 'skills/tracking-collect').exists())

    @unittest.skipUnless(shutil.which('claude'), 'Claude Code CLI is needed for plugin installation')
    def test_claude_installs_all_skills_from_shared_marketplace(self):
        with tempfile.TemporaryDirectory() as runtime:
            env = {**os.environ, 'CLAUDE_CONFIG_DIR': runtime}
            for arguments in (('marketplace', 'add', str(self.root)),
                              ('install', 'frantss-skills@frantss'), ('list', '--json')):
                result = subprocess.run(['claude', 'plugin', *arguments], cwd=runtime,
                                        env=env, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            plugins = json.loads(result.stdout)
            self.assertEqual([plugin['id'] for plugin in plugins], ['frantss-skills@frantss'])
            plugin = plugins[0]
            self.assertTrue(plugin['enabled'])
            installed = Path(plugin.get('readFromFolder') or plugin['installPath'])
            self.assertTrue(installed.resolve().is_relative_to(Path(runtime).resolve())
                            or installed.resolve() == self.root.resolve())
            self.assert_installed_skills(installed)

    @unittest.skipUnless(shutil.which('copilot'), 'Copilot CLI is needed for plugin installation')
    def test_copilot_installs_from_shared_claude_marketplace(self):
        with tempfile.TemporaryDirectory() as runtime:
            env = {**os.environ, 'COPILOT_HOME': runtime,
                   'COPILOT_CACHE_HOME': str(Path(runtime) / 'cache')}
            for arguments in (('marketplace', 'add', str(self.root)),
                              ('install', 'frantss-skills@frantss')):
                result = subprocess.run(['copilot', 'plugin', *arguments], cwd=runtime,
                                        env=env, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            installed = Path(runtime) / 'installed-plugins/frantss/frantss-skills'
            self.assert_installed_skills(installed)


if __name__ == '__main__':
    unittest.main()
