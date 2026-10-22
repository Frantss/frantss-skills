---
name: core-update
description: "Update the installed Frantss skill set, check available updates, or resume an upgrade using commit hashes and configuration/database migrations. Editing skill instructions and ordinary configuration changes belong elsewhere."
compatibility: Requires Git, access to the private Frantss/frantss-skills repository, the original installer, and configured backend tools for data migrations.
---

# Update Frantss

Update requested installations from https://github.com/Frantss/frantss-skills.git and migrate their shared configuration/database.
Preserve installer, agent, scope, selected skills, explicit pins, and unrelated packages. Checks/previews perform no writes.

## Revision state

Use user-wide `~/.frantss/skills-state.yaml`, independently of the working directory; parse YAML as data.
Store `schema_version: 1`, `repository`, `data_commit` (full hash or null), `installations` (list), and `pending` (null or journal).
Each installation has canonical `path`, `installer`, `agent`, `scope`, `skills` (`all` or names), and verified full-hash `commit`.
`data_commit` tracks verified shared data separately from installed payloads. Never infer migrated data from an installed package.
In `pending`, retain baseline/target hashes, backups, and ordered steps with stable IDs, intended payloads/identities, preconditions, postconditions, and `planned|started|verified` status.
Use content checks and atomic state/configuration writes; preserve unknown fields and reject escaping symlinks or conflicting writers.

## Compare commits

1. Inspect installation provenance, local edits, and pending work. Verify installed files against recorded commits, excluding installer metadata.
   Without state, recover hashes from provenance or exact source-tree matches; establish the data baseline separately from schemas/preconditions. Clarify unresolved baselines.
2. Fetch history into a temporary checkout. Resolve remote default-branch HEAD, or the requested revision, to one fixed full target hash.
   Resolve conflicting pins or local edits before writes. Missing history/tools/access, divergent commits, or newer shared data leave the upgrade incomplete.
3. Read chronological, rename-aware diffs from each installation/data baseline to target, including changed schemas, adapters, installer docs, and migration guidance.
   Account for every changed config path/key, domain/common field, storage mapping, skill name, and install reference; equal schema numbers do not prove compatibility.
4. Derive ordered, lossless migration steps with applicability checks, transformations, verification, and partial-write recovery. Report hashes, changes, and conflicts.
   Inspect all affected settings, tasks, evidence, runs, reports, events, retained revisions, and views. End checks/previews here without writing state or backups.

## Apply migrations and installation

5. The update authorizes lossless migrations; resolve ambiguous/destructive changes with frantss. Preserve IDs, keys, relationships, dates, unknown fields, and human edits; retain retired history in verified external backups.
   Patch schema-owned fields, structured relationships, and views. Reconcile old/new fields or paths before removal; coordinate incompatible consumers before changing shared data.
6. Exclude concurrent updates/affected workflow writes. Back up configuration, installation, and affected backend data outside installer caches; verify restorable coverage.
   Record backups and steps in `pending` before mutation. Empty data needs no migration or backend/project initialization.
7. Use source-history schemas and adapter protocols for ordered migrations; back up retired records/history externally before removing them from active storage. Verify current identity lookups; unavailable past revisions remain explicit gaps.
   For Obsidian, use its official CLI and conflict/recovery protocol; unavailable CLI access never permits filesystem writes instead.
   Recheck preconditions, mark started before writing, then read back all affected objects before marking verified.
8. Use installed installer help to install the fixed target through the original installer; a checkout at that commit can serve local installs.
   Preserve subsets, map renamed skills through history, and include new skills for `all`. Remove obsolete owned files/names after replacements verify.
   If exact installation is unsupported, stop with staged source. Preserve unrelated/local edits; never substitute a moving target.
9. On failure, retain hashes, journal, backups, and unsaved payloads; report persisted/missing work and pause incompatible workflows.
   Resume the journal's fixed target; inspect started-step effects and execute only missing work with the same identities. Restore only when safe against later edits.

## Verify completion

Require target-matching files, valid migrated configuration/records/revisions, resolved references, preserved unrelated data, and target-adapter reads/queries; missing coverage remains incomplete.
Only then atomically advance installation/data hashes, archive the journal alongside backups, and clear `pending`. Report hashes, migrations, backups, and reload needs; skip writes when already current.
