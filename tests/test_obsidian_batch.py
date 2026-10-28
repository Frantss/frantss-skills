import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'skills/tracking-obsidian/scripts/batch.py'
NODE = shutil.which('node')
try:
    import yaml
except ImportError:
    yaml = None

# Execute the shipped JavaScript against a disk-backed fake vault, including CLI error text.
BRIDGE = r'''
const fs = require('fs');
const args = process.argv.slice(2);
const file = process.env.BATCH_STATE;
const state = JSON.parse(fs.readFileSync(file, 'utf8'));
state.calls.push(args);
const save = () => fs.writeFileSync(file, JSON.stringify(state));
const commands = args.slice(1);
if (commands[0] === 'vaults') console.log('Test vault\t' + process.env.BATCH_VAULT);
else if (commands[0] === 'help') console.log('eval read');
else if (commands[0] === 'vault') console.log(process.env.BATCH_VAULT);
else if (commands[0] === 'eval') {
  const app = {
    metadataCache: {getFileCache: f => ({frontmatter: state.notes[f.path].fields})},
    vault: {
      getMarkdownFiles: () => Object.keys(state.notes).map(path => ({path})),
      getFileByPath: path => state.notes[path] ? {path} : null,
      read: async f => state.notes[f.path].content,
      create: async (path, content) => {
        if (state.notes[path]) throw Error('Path occupied');
        state.notes[path] = {content, fields: {}};
        save();
        if (state.fail_after_write) {
          delete state.fail_after_write;
          save();
          throw Error('Unknown outcome after committed write');
        }
      },
      process: async (f, change) => {
        if (state.race) {
          state.notes[f.path].content += '\nConcurrent human edit\n';
          delete state.race;
          save();
        }
        state.notes[f.path].content = change(state.notes[f.path].content);
        save();
      }
    }
  };
  save();
  Promise.resolve(eval(commands[1].slice(5))).then(value => console.log('=> ' + value))
    .catch(error => console.log('Error: ' + error.message));
  if (state.hang) setInterval(() => {}, 60000);
} else { console.log('Error: Unsupported fixture command'); }
save();
'''


@unittest.skipUnless(NODE and yaml and os.name == 'posix', 'requires Node, PyYAML and POSIX fixture executable')
class ObsidianBatchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.vault = self.directory / 'Test vault'
        self.vault.mkdir()
        self.state_path = self.directory / 'state.json'
        executable = self.directory / 'obsidian'
        executable.write_text('#!' + NODE + '\n' + BRIDGE)
        executable.chmod(0o700)
        self.env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PATH=str(self.directory) + os.pathsep + os.environ.get('PATH', ''),
                        BATCH_STATE=str(self.state_path), BATCH_VAULT=str(self.vault))
        self.fields, self.content = self.note('one')
        self.path = 'Frantss/Tasks/Readable title.md'
        self.state_path.write_text(json.dumps({'calls': [], 'notes': {
            self.path: {'content': self.content, 'fields': self.fields}}}))

    def note(self, identity, revision=1, suffix=''):
        fields = dict(schema_version=1, record_type='task', id=identity, key='task:' + identity,
                      title='Readable title', revision=revision, status='inbox', custom='preserve')
        return fields, '---\n' + yaml.safe_dump(fields, sort_keys=False) + '---\n\nHuman café, 🚀, \\n, `ticks`, $(literal).\n' + suffix

    def run_batch(self, operations, code=0):
        result = subprocess.run([sys.executable, str(SCRIPT), '--vault-path', str(self.vault),
                                 '--root', 'Frantss'], input=json.dumps(operations), capture_output=True,
                                text=True, env=self.env, timeout=30)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        self.assertEqual(result.stderr, '')
        return json.loads(result.stdout)

    def state(self):
        return json.loads(self.state_path.read_text())

    def test_selected_reads_reuse_scan_and_preserve_literal_content(self):
        operation = dict(op='read', selectors=[dict(record_type='task', id='one')])
        result = self.run_batch([operation, operation])
        self.assertEqual(result['stats'], dict(scans=1, read_batches=2, notes_read=2))
        self.assertEqual([group[0]['content'] for group in result['results']], [self.content] * 2)
        self.assertTrue(all(args[0] == 'vault=Test vault' for args in self.state()['calls']))

    def test_full_scope_read_scans_once(self):
        result = self.run_batch([dict(op='read_all')])
        self.assertEqual(result['stats'], dict(scans=1, read_batches=1, notes_read=1))
        self.assertEqual(result['results'][0][0]['content'], self.content)

    def test_empty_reads_do_not_discover_or_read_notes(self):
        result = self.run_batch([dict(op='read', selectors=[])])
        self.assertEqual(result['results'], [[]])
        self.assertEqual(result['stats'], dict(scans=0, read_batches=0, notes_read=0))

    def test_timeout_discards_output_and_reports_unverified_outcome(self):
        state = self.state()
        state['hang'] = True
        self.state_path.write_text(json.dumps(state))
        result = self.run_batch([dict(op='read_all')], code=1)
        self.assertEqual(result['results'], [])
        self.assertEqual(result['error'], 'Obsidian CLI exceeded 5 seconds; outcome unverified')

    def test_missing_metadata_and_stale_identity_fall_back_to_fresh_notes(self):
        state = self.state()
        state['notes'][self.path]['fields'] = dict(self.fields, id='stale', key='stale')
        self.state_path.write_text(json.dumps(state))
        result = self.run_batch([dict(op='read', selectors=[dict(record_type='task', id='one')])])
        self.assertEqual(result['results'][0][0]['content'], self.content)
        self.assertEqual(result['stats']['scans'], 2)
        state['notes'][self.path]['fields'] = {}
        self.state_path.write_text(json.dumps(state))
        result = self.run_batch([dict(op='read', selectors=[dict(record_type='task', id='one')])])
        self.assertEqual(result['results'][0][0]['fields']['id'], 'one')

    def test_create_replace_and_retries_update_lookup_without_duplicates(self):
        _, initial = self.note('two')
        _, updated = self.note('two', revision=2, suffix='Updated\n')
        path = 'Frantss/Tasks/Second title.md'
        create = dict(op='create', path=path, content=initial)
        replace = dict(op='replace', path=path, expected=initial, content=updated)
        result = self.run_batch([create, create, replace, replace,
                                 dict(op='read', selectors=[dict(record_type='task', key='task:two')])])
        self.assertEqual(result['results'][-1][0]['content'], updated)
        self.assertEqual(len(self.state()['notes']), 2)
        self.assertEqual(self.state()['notes'][self.path]['content'], self.content)

    def test_duplicate_identity_fails_before_create(self):
        result = self.run_batch([dict(op='create', path='Frantss/Tasks/Different title.md',
                                      content=self.content)], code=1)
        self.assertIn('conflict', result['error'].lower())
        self.assertEqual(len(self.state()['notes']), 1)

    def test_uncertain_create_is_reconciled_on_retry(self):
        state = self.state()
        state['fail_after_write'] = True
        self.state_path.write_text(json.dumps(state))
        _, content = self.note('two')
        operation = dict(op='create', path='Frantss/Tasks/Second title.md', content=content)
        result = self.run_batch([operation], code=1)
        self.assertIn('Unknown outcome', result['error'])
        self.assertEqual(len(self.state()['notes']), 2)
        retry = self.run_batch([operation])
        self.assertEqual(retry['results'][0]['content'], content)
        self.assertEqual(len(self.state()['notes']), 2)

    def test_unresolved_metadata_does_not_hide_duplicate_identity(self):
        state = self.state()
        state['notes']['Frantss/Tasks/Duplicate.md'] = {'content': self.content, 'fields': {}}
        self.state_path.write_text(json.dumps(state))
        result = self.run_batch([dict(op='read', selectors=[dict(record_type='task', id='one')])], code=1)
        self.assertIn('Duplicate identity', result['error'])

    def test_unsupported_schema_cannot_be_created(self):
        _, content = self.note('two')
        self.run_batch([dict(op='create', path='Frantss/Tasks/Second title.md',
                             content=content.replace('schema_version: 1', 'schema_version: 2'))], code=1)
        self.assertEqual(set(self.state()['notes']), {self.path})

    def test_stale_expected_content_leaves_note_unchanged(self):
        _, updated = self.note('one', revision=2)
        result = self.run_batch([dict(op='replace', path=self.path, expected=self.content + 'stale',
                                      content=updated)], code=1)
        self.assertIn('Expected content conflict', result['error'])
        self.assertEqual(self.state()['notes'][self.path]['content'], self.content)

    def test_concurrent_edit_between_read_and_process_survives(self):
        state = self.state()
        state['race'] = True
        self.state_path.write_text(json.dumps(state))
        _, updated = self.note('one', revision=2)
        result = self.run_batch([dict(op='replace', path=self.path, expected=self.content,
                                      content=updated)], code=1)
        self.assertIn('Expected content conflict', result['error'])
        self.assertEqual(self.state()['notes'][self.path]['content'], self.content + '\nConcurrent human edit\n')

    def test_failure_returns_completed_results_and_stops_remaining_operations(self):
        _, content = self.note('two')
        operations = [dict(op='read', selectors=[dict(record_type='task', id='one')]),
                      dict(op='replace', path=self.path, expected=self.content, content=self.note('one', 3)[1]),
                      dict(op='create', path='Frantss/Tasks/Unsaved.md', content=content)]
        result = self.run_batch(operations, code=1)
        self.assertEqual(result['failed_index'], 1)
        self.assertEqual(len(result['results']), 1)
        self.assertEqual(set(self.state()['notes']), {self.path})

    def test_rejects_escaping_paths_and_symlinks(self):
        _, content = self.note('two')
        for path in ('../Escaping.md', 'Frantss/Tasks/../Escaping.md', '/Absolute.md',
                     'Frantss/Reports/Wrong type.md', 'Frantss/Tasks/History/Retired.md'):
            with self.subTest(path=path):
                self.run_batch([dict(op='create', path=path, content=content)], code=1)
        (self.vault / 'Frantss/Tasks').mkdir(parents=True)
        (self.vault / 'Frantss/Tasks/Escaping').symlink_to(self.directory, target_is_directory=True)
        self.run_batch([dict(op='create', path='Frantss/Tasks/Escaping/Note.md', content=content)], code=1)
        self.assertEqual(set(self.state()['notes']), {self.path})
