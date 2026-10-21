---
name: frantss-persistance-obsidian
description: "Read and write prepared Frantss records through the Obsidian CLI. Use when selected as the backend adapter, or for explicit storage setup, vault access checks, and Bases view changes; ordinary note editing belongs elsewhere."
compatibility: Requires Python 3 and Obsidian 1.12.7+ with the official obsidian CLI enabled and registered, and access to the desktop app.
---

# Frantss persistance Obsidian

Use the official [Obsidian CLI](https://obsidian.md/help/cli) with complete record payloads and operation requirements from the caller or `frantss-persistance` when available.

## Setup and routing

Use supplied backend options `vault` and `root` from `~/.frantss/persistance.yaml`, or read that connection file directly; expand `~` to the current OS account's home. Repository-local and ancestor configurations never select the vault.
Require schema version 1, this adapter, an existing absolute vault path, and a vault-relative root; missing options leave storage unconfigured. For sandboxed agents, read [CLI access](references/sandbox.md) before checks; after its permitted retry, stop on failure and retain partial setup/unsaved payloads without installing or repairing dependencies.

1. Before CLI checks, derive the vault name from the configured canonical path's basename. Run `obsidian vault=<name> vaults verbose`; match the exact configured path to a unique registered name/ID, clarifying missing or ambiguous matches.
2. Prefix every command, including help and sandbox retries, with `vault=<name-or-id>`. Require successful `obsidian vault=<name-or-id> help` and `obsidian vault=<name-or-id> vault info=path`; the returned path must match the configured canonical path.
3. For setup/inspection, require successful `files`; when Settings.md is listed, also require `read path=<root>/Settings.md`. Empty storage is valid.

Initialize only on explicit setup; offer `Frantss` as the default root and preserve configured roots, unrelated notes, and `.obsidian` settings. Keep destinations inside the root; reject traversal and escaping symlinks. Keep credentials in their tool's credential store.
For record operations or setup, read [note mapping](references/notes.md); before writes, also read [write protocol](references/writes.md). For requested view setup or changes, read [Bases views](references/bases.md).

## CLI operations

Use exact vault-relative `path=<root>/.../<id>.md`, including the extension; omitted paths and `file=` can target unintended notes.
List candidates with `files folder=<root>/<Folder>`, then `read path=<path>` and filter decoded records by exact keys or fields; exclude History unless requested. Use `search query=<text> path=<root> format=json` for discovery; results alone do not prove completeness or identity.
Pass arguments through a process argument array. Preserve literal backslashes and multiline payloads across CLI escape handling (`\n`, `\t`).
Run CLI reads through the [bounded reader](scripts/read_cli.py): `python3 <installed-skill-dir>/scripts/read_cli.py vault=<name> <command> ...`. It captures output locally and waits up to 5 seconds for process exit before returning it. Give the host tool at least 10 seconds and retain its sandbox/approval flow. Require exit zero and error-free output; a timeout or background task is incomplete, even when a full note was printed. Report failure before retrying.
Use `obsidian vault=<name-or-id> help <command>` for installed syntax. If CLI access fails, report blocked storage without switching to filesystem writes or connectors.
Read retained revisions for historical cutoffs and Events for task history; expose missing dates, history, access, or truncated results. Return logical fields plus IDs, keys, revisions, note references, and per-operation verified/partial/failed/unsupported status.
