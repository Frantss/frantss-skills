---
name: tracking-migrate
description: "Check, migrate, or resume changes to tracking configuration and stored records. Use for legacy tracking formats and interrupted data migrations; package updates and ordinary configuration edits belong to their installers and tracking-configure."
---

# Migrate tracking configuration and records

Check compatibility read-only; apply changes only for an explicitly requested tracking migration. Package managers own skill/plugin installation and updates.
Use the configured adapter for records and views; Obsidian requires its official CLI and conflict/recovery protocol. Missing access leaves affected work incomplete.

## Select the migration

- For legacy `backend` connection keys, read [connection migration](references/database-migration.md).
- For source selectors or database Settings notes, read [configuration migration](references/configuration-migration.md).
- For evidence/run/event/revision notes or legacy task/report fields, read [record migration](references/lean-migration.md).

1. Inspect affected configuration, record shapes, references, and views. Equal schema versions do not prove compatibility. Missing storage stays unconfigured; empty storage needs no conversion.
2. Read `~/.frantss/skills-state.yaml` independently of the working directory. Retain schema version 1, repository, `data_commit`, `pending`, and unknown fields; preserve legacy `installations` without managing them. Parse YAML as data; reject duplicate keys, unsupported versions, escaping symlinks, and conflicting writers.
3. Establish the data baseline from verified content and existing state, independently of installed packages. Pin migration instructions to one full source commit when available; otherwise journal their content hashes. Use Git and repository access for temporary source history from https://github.com/Frantss/frantss-skills.git only for missing mappings; unresolved baselines or mappings block affected writes.
4. Resume an existing pending journal with its original target, identities, backups, and expected content; inspect started-step effects before retrying. Stop on legacy journals with unfinished package-installation steps for separate resolution through the original updater or installer; never discard or execute those steps here.
5. Plan only applicable transformations in dependency order, including connection/settings changes before record cleanup. Identify all affected records, retained history, inbound references, and owned/custom views. Report conflicts and verification gaps. Checks/previews end here without writes; with no pending migration, already-current data needs no state rewrite.

## Apply and verify

6. Exclude concurrent migrations and affected workflow writes. Back up configuration and all affected records/history outside active storage and installer caches; verify restorable coverage. Preserve IDs, keys, relationships, dates, unknown fields, and human edits; resolve ambiguous or destructive mappings before mutation.
7. Before mutation, atomically record baseline, fixed target/mapping hashes, backup locations, and ordered steps in `pending`, with stable IDs, expected content/revisions, preconditions, postconditions, and `planned|started|verified` status. For new state, use schema version 1, repository, `data_commit: null`, and `pending`; create no installation registry.
8. Mark each step started before writing; recheck content, apply only its mapped changes, then read back every affected object before marking verified. Patch configuration atomically. Retired records/history may leave active storage only after replacements, inbound references, and external backups verify through the adapter.
9. On failure, retain the journal, original target, backups, and unsaved payloads; report persisted and missing work. Retry only missing effects with the same identities; restore only when safe against later edits. Unavailable historical revisions remain explicit gaps.
10. Require valid target configuration/record shapes, preserved identities and unrelated data, resolved references, required views, and successful target-adapter reads/queries. Missing coverage remains incomplete. Archive the verified journal alongside backups, advance only `data_commit` when a full target commit is verified, and clear `pending` atomically; preserve installation fields unchanged.

Report applied mappings, verified scope, gaps, backup/journal locations, and any workflows still blocked by incompatible data. A plugin refresh alone never proves data compatibility.
