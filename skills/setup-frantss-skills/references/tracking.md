# Tracking setup

Resolve an explicit `tracking.yaml` or unique ancestor `.frantss/tracking.yaml`; ask on ambiguity or an unresolved connection.
```yaml
schema_version: 1
backend: {adapter: tracking-persist-obsidian, options: {vault: /path/to/your/vault, root: Tracking}}
```
Resolve real options; placeholders/missing values leave a partial draft. This file holds only the shared backend connection; settings/accounts and workspace area/sources live in that backend.
For Obsidian setup or inspection, require an existing absolute vault path and vault-relative root; check `obsidian help` and `obsidian vaults verbose`.
For that adapter, resolve a unique vault name/ID by configured path; require `obsidian vault=<selector> vault info=path` to match its canonical path. Never rely on the active vault.
For its access check, put `vault=<selector>` before each command; require successful `files` and, if `<root>/Settings.md` is listed, `read path=<root>/Settings.md`. Empty/uninitialized storage is valid.
On a failed Obsidian check, mark dependency setup partial, retain drafts, and stop backend writes; report the missing CLI activation/PATH registration, desktop-app access, or vault requirement without installing or repairing it.
For backend changes, prepare the directory, patch requested options, parse YAML as data, and read back schema version 1 and backend selection.
For requested storage initialization, use the selected adapter; a connection file alone does not establish working storage.
Save supplied shared settings using the `tracking-persist` logical schema; preserve existing values and resolve required timezone/week start.
Explicit workspace creation reads [identity setup](workspace-identity.md), initializes/reuses its UUID, and resolves work/personal area before backend writes.
For source setup or inspection, read [source configuration](sources.md). Resolve an existing workspace record by UUID; missing records require explicit creation.
Persist through `tracking-persist` and its adapter when available; otherwise retain unsaved payloads and report missing capabilities.
Read back settings/workspace/source changes. Report partial identity/backend writes; reuse UUIDs on retry.
Backend changes do not migrate records; retain the previous selection and explain separate migration requirements.
Setup does not collect activity, capture tasks, or generate reports.
