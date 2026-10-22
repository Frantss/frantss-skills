# Backend connection

Use only `~/.frantss/persistance.yaml` for this connection:
```yaml
schema_version: 1
backend: {adapter: <adapter-skill>, options: <connection-options>}
```
Use `frantss-persistance-obsidian` with `{vault: /path/to/vault, root: Frantss}`, or `frantss-persistance-fizzy` with `{profile: <name>, api_url: https://app.fizzy.do, board: <id>}`; resolve real options before saving. Store no project definitions or credentials here.
Use the selected adapter's inspection/setup to verify access; Obsidian requires CLI/vault checks, Fizzy requires CLI/profile/account/board checks. Missing capabilities leave partial drafts; report failures without installing/repairing dependencies.
Patch requested options with content checks/atomic replacement and read-back. Initialize storage only when requested; changing the connection leaves stored records untouched.
