# Backend connection

Use only `~/.frantss/persistance.yaml` for this connection:
```yaml
schema_version: 1
backend: {adapter: frantss-persistance-obsidian, options: {vault: /path/to/vault, root: Frantss}}
```
Resolve real options before saving; placeholders or missing capabilities leave partial drafts. Store no project definitions or credentials here.
Use the selected adapter's inspection/setup to verify access; Obsidian requires CLI/vault checks before backend writes. Report failures without installing/repairing dependencies.
Patch requested options with content checks/atomic replacement and read-back. Initialize storage only when requested; changing the connection leaves stored records untouched.
