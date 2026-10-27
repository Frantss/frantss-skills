---
name: persistence-obsidian
description: "Read and write prepared Frantss records through the Obsidian CLI. Use for the selected database, storage setup/access checks, and Bases view changes; ordinary note editing belongs elsewhere."
compatibility: Requires Python 3.9+ with PyYAML, Obsidian 1.12.7+ with its official CLI enabled and registered, and access to the desktop app.
---

# Persist records in Obsidian

Accept complete record payloads and operation requirements from the caller or `persistence-records`. Read [note mapping](references/notes.md) for record operations/setup, [write protocol](references/writes.md) before writes, and [Bases views](references/bases.md) for setup, authorized upgrades, or view changes.
Use `database.options` from `~/.frantss/persistance.yaml`, expanding `~` for the current OS account. Require schema version 1, `database.adapter: persistence-obsidian`, an existing absolute `vault` path, and vault-relative `root`. Legacy `backend` requires explicit `core-update` migration. Repository/ancestor settings never select storage; missing options leave it unconfigured.
For sandboxed access, read [CLI access](references/sandbox.md) before checks. Stop after its permitted retry fails; retain unsaved payloads without installing dependencies or switching databases/filesystem writes.

For record batches, use the [Python runner](scripts/batch.py) and its [interface](references/batch.md). It verifies the connection and reuses an in-memory lookup until process exit; independent calls rebuild it. Let the runner perform connection checks.
For manual CLI access, derive the selector from the canonical vault path's basename. Run `obsidian vault=<selector> vaults verbose` and require one exact path match. Prefix subsequent commands/help/retries with that registered `vault=<name-or-id>`. Require successful `help` and `vault info=path`, matching the canonical path. Setup/inspection also requires `files`; empty storage is valid and Settings.md is legacy migration input.

Initialize only on explicit setup; offer `Frantss` as the default root. Preserve configured roots, unrelated notes, and `.obsidian` settings; setup remains incomplete until required Bases verify. Keep destinations inside the root and reject traversal/escaping symlinks. Keep credentials in their tool's credential store.
Use discovered vault-relative `path=<root>/.../<readable name>.md`, including the extension. Omitted paths and `file=` can select unintended notes; UUIDs never determine filenames. Exclude History unless requested.
Treat metadata/search as candidate hints. Verify selected notes fresh; complete queries and absence checks require fresh scoped reads. Apply caller filters/limits to fresh records, reporting access/truncation gaps rather than claiming completeness.
For manual reads, use the [bounded reader](scripts/read_cli.py): `python3 <skill-dir>/scripts/read_cli.py vault=<name> <command> ...`. It captures output and requires process exit within five seconds. Give each host call at least ten seconds; preserve sandbox/approval handling. Require exit zero and error-free output; timeouts/background tasks are incomplete. Report failure before retrying.
Pass CLI arguments as a process argument array; preserve literal backslashes/multiline content across CLI escaping (`\n`, `\t`). Consult `obsidian vault=<selector> help <command>` for installed syntax; [official CLI documentation](https://obsidian.md/help/cli) supplies context.
Use saved summaries or dated sources for historical cutoffs; expose unavailable revisions, unsupported legacy data, missing dates, and coverage gaps. Return logical fields, IDs/keys/revisions, note references, and per-operation verified/partial/failed/unsupported status.
