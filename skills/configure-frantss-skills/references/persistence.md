# Persistence setup

Use only `~/.frantss/persistance.yaml` for the backend connection; resolve missing options during requested setup, never from repository-local files.
```yaml
schema_version: 1
backend: {adapter: frantss-persistance-obsidian, options: {vault: /path/to/your/vault, root: Frantss}}
```
Resolve real options; placeholders/missing values leave a partial draft. This file holds only the connection; shared settings/accounts live in the backend, workspace/source definitions in `~/.frantss/workspaces.yaml`.
For Obsidian setup or inspection, require an existing absolute vault path and vault-relative root; check `obsidian help` and `obsidian vaults verbose`.
For that adapter, resolve a unique vault name/ID by configured path; require `obsidian vault=<selector> vault info=path` to match its canonical path. Never rely on the active vault.
For its access check, put `vault=<selector>` before each command; require successful `files` and, if `<root>/Settings.md` is listed, `read path=<root>/Settings.md`. Empty/uninitialized storage is valid.
On a failed Obsidian check, mark dependency setup partial, retain drafts, and stop backend writes; report the missing CLI activation/PATH registration, desktop-app access, or vault requirement without installing or repairing it.
For backend changes, prepare the directory, patch requested options, parse YAML as data, and read back schema version 1 and backend selection.
For requested storage initialization, use the selected adapter; a connection file alone does not establish working storage.
Persist through `frantss-persistance` and its adapter when available; otherwise retain unsaved payloads and report missing capabilities.
Backend changes do not migrate records; retain the previous selection and explain separate migration requirements.
