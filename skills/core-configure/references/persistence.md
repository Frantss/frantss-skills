# Database connection

Use only `~/.frantss/persistance.yaml` for this connection; legacy `backend` requires an explicit `core-update` migration, never inspection-time rewriting or replacement setup:
```yaml
schema_version: 1
database: {adapter: persistence-obsidian, options: {vault: /path/to/vault, root: Frantss}}
```
Resolve real options before saving; placeholders or missing capabilities leave partial drafts. Store no project definitions or credentials here.
Use the selected adapter's inspection/setup to verify access; Obsidian requires CLI/vault checks before database writes. Setup completes only after the adapter verifies its required views. Report failures without installing/repairing dependencies.
Patch requested options with content checks/atomic replacement and read-back. Initialize storage only when requested; changing the connection leaves stored records untouched.
