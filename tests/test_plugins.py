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
        for directory in ('.claude-plugin', 'plugins'):
            shutil.copytree(SOURCE / directory, self.root / directory,
                            ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))

    def test_layout_has_only_three_plugins_and_one_copy_per_skill(self):
        self.assertFalse((self.root / 'skills').exists())
        self.assertFalse((self.root / '.plugins').exists())
        names = [path.parent.name for path in self.root.glob('plugins/*/skills/*/SKILL.md')]
        self.assertEqual(len(names), 17)
        self.assertEqual(len(set(names)), 17)
        self.assertFalse((self.root / '.claude-plugin/plugin.json').exists())
        self.assertFalse((self.root / '.codex-plugin').exists())
        market = json.loads((self.root / '.claude-plugin/marketplace.json').read_text())
        self.assertEqual({entry['name'] for entry in market['plugins']},
                         {'frantss-tracking', 'frantss-bdd', 'frantss-development'})
        self.assertEqual(len(market['plugins']), 3)
        self.assertEqual({p.name for p in (self.root / 'plugins/frantss-development/skills').iterdir()},
                         {'core-communicate', 'refactoring', 'atomic-commits'})
        self.assertEqual({p.name for p in (self.root / 'plugins/frantss-tracking/skills').iterdir()},
                         {'tracking-tasks', 'tracking-collect', 'tracking-report', 'tracking-team-digest',
                          'persistence-records', 'persistence-obsidian', 'core-configure', 'core-update'})

    @unittest.skipUnless(shutil.which('gh'), 'GitHub CLI is needed for skill discovery')
    def test_github_cli_discovers_skills_once(self):
        result = subprocess.run(['gh', 'skill', 'install', str(self.root), '--from-local'],
                                cwd=self.root, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        discovered = [line.split('\t')[0].rsplit('/', 1)[-1] for line in result.stdout.splitlines() if line]
        expected = [path.parent.name for path in self.root.glob('plugins/*/skills/*/SKILL.md')]
        self.assertCountEqual(discovered, expected)

    @unittest.skipUnless(shutil.which('codex'), 'Codex CLI is needed for plugin installation')
    def test_codex_installs_three_plugins_and_refreshes_without_sync(self):
        with tempfile.TemporaryDirectory() as runtime:
            env = {**os.environ, 'CODEX_HOME': runtime}

            def codex(*args):
                result = subprocess.run(['codex', 'plugin', *args, '--json'], cwd=runtime,
                                        env=env, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
                return json.loads(result.stdout)

            codex('marketplace', 'add', str(self.root))
            for source in sorted((self.root / 'plugins').iterdir()):
                name = source.name
                with self.subTest(plugin=name):
                    installed = Path(codex('add', f'{name}@frantss')['installedPath'])
                    self.assertTrue(installed.resolve().is_relative_to(Path(runtime).resolve()))
                    manifest = json.loads((installed / '.codex-plugin/plugin.json').read_text())
                    self.assertEqual(manifest['skills'], './skills/')
                    expected = source / 'skills'
                    actual = installed / 'skills'
                    self.assertEqual({p.relative_to(expected) for p in expected.rglob('*') if p.is_file()},
                                     {p.relative_to(actual) for p in actual.rglob('*') if p.is_file()})
                    for path in actual.rglob('*'):
                        if path.is_file():
                            self.assertEqual(path.read_bytes(), (expected / path.relative_to(actual)).read_bytes())
            skills = self.root / 'plugins/frantss-tracking/skills'
            (skills / 'tracking-added').mkdir()
            (skills / 'tracking-added/SKILL.md').write_text('---\nname: tracking-added\ndescription: Added.\n---\nTrack.\n')
            (skills / 'tracking-tasks/SKILL.md').write_text('Updated instruction.\n')
            shutil.rmtree(skills / 'tracking-collect')
            installed = Path(codex('add', 'frantss-tracking@frantss')['installedPath'])
            self.assertTrue((installed / 'skills/tracking-added/SKILL.md').is_file())
            self.assertEqual((installed / 'skills/tracking-tasks/SKILL.md').read_text(), 'Updated instruction.\n')
            self.assertFalse((installed / 'skills/tracking-collect').exists())


if __name__ == '__main__':
    unittest.main()
