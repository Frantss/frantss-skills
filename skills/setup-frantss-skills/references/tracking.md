# Tracking setup

Resolve an explicit `tracking.yaml` or unique ancestor `.frantss/tracking.yaml`; ask on ambiguity or an unresolved connection.
```yaml
schema_version: 1
backend:
  adapter: tracking-persist-obsidian
  options: {vault: /path/to/your/vault, root: Tracking}
```
Resolve real adapter options; placeholders/missing values leave a partial draft. Obsidian requires an existing absolute vault and vault-relative root.
Every project uses this backend. Shared settings/accounts and project area/sources live there; this file holds only the connection.
Follow only requested backend, settings, workspace, or source steps; inspection remains read-only throughout.
For backend changes, prepare the directory, patch requested options, parse YAML as data, and read back schema version 1 and backend selection.
For requested storage initialization, use the selected adapter; a connection file alone does not establish working storage.
Save supplied shared settings; preserve existing values and resolve timezone/week start when required.
For explicitly requested project creation, resolve name and work/personal area; use `tracking-tasks` when available, otherwise persist an explicitly authorized payload.
For source updates, resolve exact existing projects; missing records require explicit project creation.
Retain provider, account, user identity, and bounded scope; patch only requested mappings and resolve ambiguous targets before writes.
Persist through `tracking-persist` and its adapter when available; otherwise retain unsaved payloads and report missing capabilities.
Read back settings/project/source changes. Report partial config/backend writes with saved locations and missing steps.
Backend changes do not migrate records; retain the previous selection and explain separate migration requirements.
Setup does not collect activity, capture tasks, or generate reports.
