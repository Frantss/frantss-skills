"""Run prepared record operations in one process; all vault access uses the CLI."""
import argparse
import base64
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys

import yaml
from read_cli import run_cli


class Batch:
    def __init__(self, vault_path, root):
        supplied = Path(vault_path).expanduser()
        if not supplied.is_absolute() or not supplied.is_dir():
            raise ValueError('Vault must be an existing absolute directory')
        self.vault = supplied.resolve()
        self.root = self._relative(root)
        self.selector = self.vault.name
        self.stats = {'scans': 0, 'read_batches': 0, 'notes_read': 0}
        registered = [line.split('\t', 1) for line in self._cli('vaults', 'verbose').splitlines()]
        matches = [name for name, path in registered if Path(path).resolve() == self.vault]
        if len(matches) != 1:
            raise ValueError('Vault registration is missing or ambiguous')
        self.selector = matches[0]
        self._cli('help')
        if Path(self._cli('vault', 'info=path')).resolve() != self.vault:
            raise ValueError('CLI selected a different vault')
        self.entries = None

    @staticmethod
    def _relative(value):
        path = PurePosixPath(value)
        if not value or path.is_absolute() or '..' in path.parts or '\\' in value or str(path) != value or value == '.' or '\0' in value:
            raise ValueError('Expected a normalized vault-relative path')
        return value

    def _path(self, value, kind=None):
        value = self._relative(value)
        folders = ['Tasks'] if kind == 'task' else ['Reports'] if kind == 'report' else ['Tasks', 'Reports']
        if not any(value.startswith(f'{self.root}/{folder}/') for folder in folders) or not value.endswith('.md') or 'History' in PurePosixPath(value).parts:
            raise ValueError('Record path is outside its configured folder')
        if not (self.vault / value).resolve().is_relative_to(self.vault / self.root):
            raise ValueError('Record path escapes through a symlink')
        return value

    def _cli(self, *args):
        try:
            result = run_cli(['vault=' + self.selector, *args])
        except subprocess.TimeoutExpired:
            raise RuntimeError('Obsidian CLI exceeded 5 seconds; outcome unverified') from None
        output, errors = result.stdout.decode().strip(), result.stderr.decode().strip()
        if result.returncode or errors or re.search(r'^Error:', output, re.M):
            raise RuntimeError(errors or output or 'CLI failed')
        return output

    def _eval(self, body, data=None):
        payload = json.dumps(data, ensure_ascii=False).encode()
        if len(payload) > 48000:
            raise ValueError('CLI payload exceeds 48000 bytes; split the batch')
        encoded = base64.b64encode(payload).decode()
        code = ('(async()=>{const p=JSON.parse(new TextDecoder().decode(Uint8Array.from(atob("' +
                encoded + '"),c=>c.charCodeAt(0))));' + body + '})()')
        output = self._cli('eval', 'code=' + code)
        if not output.startswith('=> '):
            raise RuntimeError('Unexpected CLI eval output: ' + output)
        return json.loads(output[3:])

    def _scan(self):
        rows = self._eval('return JSON.stringify(app.vault.getMarkdownFiles().filter(f=>'
                          'p.some(prefix=>f.path.startsWith(prefix))&&!f.path.split("/").includes("History")).map(f=>({path:f.path,'
                          'fields:app.metadataCache.getFileCache(f)?.frontmatter||{}})));',
                          [self.root + '/Tasks/', self.root + '/Reports/'])
        self.stats['scans'] += 1
        self.entries = {self._path(row['path']): row['fields'] for row in rows}
        self._index()

    def _index(self):
        self.lookup = {}
        self.unresolved = set()
        for path, fields in self.entries.items():
            if not all(isinstance(fields.get(k), str) and fields[k] for k in ('record_type', 'id', 'key')):
                self.unresolved.add(path)
                continue
            for field in ('id', 'key'):
                value = fields.get(field)
                if isinstance(value, str):
                    self.lookup.setdefault((fields.get('record_type'), field, value), set()).add(path)

    @staticmethod
    def decode(content):
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', content, re.S)
        fields = yaml.safe_load(match[1]) if match else None
        if not isinstance(fields, dict) or fields.get('record_type') not in ('task', 'report'):
            raise ValueError('Unsupported or missing record frontmatter')
        if type(fields.get('schema_version')) is not int or fields['schema_version'] != 1:
            raise ValueError('Unsupported record schema_version')
        if not all(isinstance(fields.get(k), str) and fields[k] for k in ('id', 'key')):
            raise ValueError('Record requires string id and key')
        if type(fields.get('revision')) is not int or fields['revision'] < 1:
            raise ValueError('Record requires a positive integer revision')
        return fields

    def _read(self, paths):
        result = []
        changed = False
        paths = sorted(set(paths))
        for offset in range(0, len(paths), 20):
            rows = self._eval('return JSON.stringify(await Promise.all(p.map(async path=>{'
                              'const f=app.vault.getFileByPath(path);if(!f)throw Error("Missing path: "+path);'
                              'return {path,content:await app.vault.read(f)};})));', paths[offset:offset + 20])
            self.stats['read_batches'] += 1
            self.stats['notes_read'] += len(rows)
            for row in rows:
                row['fields'] = self.decode(row['content'])
                old = self.entries.get(row['path'], {})
                changed |= any(old.get(k) != row['fields'][k] for k in ('record_type', 'id', 'key'))
                self.entries[row['path']] = row['fields']
            result.extend(rows)
        if changed:
            self._index()
        return result

    @staticmethod
    def _matches(fields, selector):
        return all(fields.get(key) == value for key, value in selector.items())

    @staticmethod
    def _selector(selector):
        if (not isinstance(selector, dict) or set(selector) - {'record_type', 'id', 'key'}
                or selector.get('record_type') not in ('task', 'report')
                or not any(selector.get(k) for k in ('id', 'key'))
                or not all(isinstance(v, str) and v for v in selector.values())):
            raise ValueError('Select by record_type and id/key')

    def read_many(self, selectors):
        for selector in selectors:
            self._selector(selector)
        if not selectors:
            return []
        if self.entries is None:
            self._scan()
        paths = {path for selector in selectors for field in ('id', 'key') if field in selector
                 for path in self.lookup.get((selector['record_type'], field, selector[field]), set())}
        paths.update(self.unresolved)
        rows = self._read(paths)
        matches = [[r for r in rows if self._matches(r['fields'], s)] for s in selectors]
        if any(not group for group in matches):
            rows = self.read_all()
            matches = [[r for r in rows if self._matches(r['fields'], s)] for s in selectors]
        if any(len(group) > 1 for group in matches):
            raise ValueError('Duplicate identity')
        return [group[0] if group else None for group in matches]

    def read_all(self):
        self._scan()
        return self._read(self.entries)

    def write(self, path, content, expected=None):
        fields = self.decode(content)
        self._path(path, fields['record_type'])
        if expected is None:
            rows = self.read_all()
        else:
            selectors = [{'record_type': fields['record_type'], k: fields[k]} for k in ('id', 'key')]
            rows = self.read_many(selectors)
        matches = {r['path']: r for r in rows if r and r['fields']['record_type'] == fields['record_type'] and
                   (r['fields']['id'] == fields['id'] or r['fields']['key'] == fields['key'])}
        if len(matches) > 1:
            raise ValueError('Duplicate identity')
        current = next(iter(matches.values()), None)
        if current and (current['path'] != path or any(current['fields'][k] != fields[k] for k in ('id', 'key'))):
            raise ValueError('Identity/path conflict')
        if current and current['content'] == content:
            return current
        if expected is None:
            if current or fields['revision'] != 1:
                raise ValueError('Create requires absent identity and revision 1')
        else:
            old = self.decode(expected)
            if not current or current['content'] != expected:
                raise ValueError('Expected content conflict')
            if any(old[k] != fields[k] for k in ('record_type', 'id', 'key')):
                raise ValueError('Identity changes are unsupported')
            if fields['revision'] != old['revision'] + 1:
                raise ValueError('Replacement must increment revision once')
        try:
            self._eval('const f=app.vault.getFileByPath(p.path);'
                       'if(p.expected===null){if(f)throw Error("Path occupied");'
                       'await app.vault.create(p.path,p.content);}else{'
                       'if(!f)throw Error("Missing path");await app.vault.process(f,current=>{'
                       'if(current!==p.expected)throw Error("Expected content conflict");return p.content;});}'
                       'return JSON.stringify(true);', {'path': path, 'content': content, 'expected': expected})
            verified = self._read([path])[0]
            if verified['content'] != content:
                raise RuntimeError('Readback differs from supplied content')
            return verified
        except Exception:
            self.entries.pop(path, None)
            self._index()
            raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--vault-path', required=True, help='vault path from approved backend options')
    parser.add_argument('--root', required=True, help='root from approved backend options')
    args = parser.parse_args()
    results = []
    try:
        operations = json.load(sys.stdin)
        if not isinstance(operations, list):
            raise ValueError('stdin must contain a JSON array of operations')
        batch = Batch(args.vault_path, args.root)
        for operation in operations:
            if operation['op'] == 'read':
                result = batch.read_many(operation['selectors'])
            elif operation['op'] == 'read_all':
                result = batch.read_all()
            elif operation['op'] in ('create', 'replace'):
                expected = operation['expected'] if operation['op'] == 'replace' else None
                result = batch.write(operation['path'], operation['content'], expected)
            else:
                raise ValueError('Unsupported operation')
            results.append(result)
        print(json.dumps({'status': 'verified', 'results': results, 'stats': batch.stats}, default=str))
    except Exception as error:
        print(json.dumps({'status': 'failed', 'results': results, 'failed_index': len(results),
                          'error': str(error), 'recovery': 'Fresh-read the failed write before retrying.'}, default=str))
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
