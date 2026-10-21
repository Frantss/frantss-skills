---
name: frantss-persistance-obsidian
description: "Read and write prepared Frantss records through the Obsidian CLI. Use when selected as the backend adapter, or for explicit storage setup, vault access checks, and Bases view changes; ordinary note editing belongs elsewhere."
compatibility: Requires Obsidian 1.12.7+ with the official obsidian CLI enabled and registered, and access to the desktop app.
---

# Frantss persistance Obsidian

Use the official [Obsidian CLI](https://obsidian.md/help/cli) with complete record payloads and operation requirements from the caller or `frantss-persistance` when available.

## Setup and routing

Use supplied backend options `vault` and `root` from `~/.frantss/persistance.yaml`, or read that user-wide connection directly.
Expand `~` to the current user's home; repository-local and ancestor configurations never select the vault.
Require schema version 1, this adapter, an existing absolute vault path, and a vault-relative root. Missing options leave storage unconfigured.
Stop on a failed check; return partial setup/unsaved payloads and missing dependencies without installing or repairing them.

1. Require successful `obsidian help`; otherwise retain payloads and explain CLI activation under Settings → General and PATH registration.
2. Resolve the configured path to a unique vault name/ID using `obsidian vaults verbose`; clarify unresolved matches.
3. Put `vault=<name-or-id>` before every command; require `vault info=path` to match the configured canonical path.
4. For setup/inspection, require successful `files`; when Settings.md is listed, also require `read path=<root>/Settings.md`. Empty storage is valid.

Initialize only on explicit setup; offer `Frantss` as the default root and preserve configured roots, unrelated notes, and `.obsidian` settings.
Keep every resolved destination inside the root; reject traversal and escaping symlinks. Keep credentials in their tool's credential store.
For record operations or setup, read [note mapping](references/notes.md); before writes, also read [write protocol](references/writes.md).
For requested view setup or changes, read [Bases views](references/bases.md).

## CLI operations

Use exact vault-relative `path=<root>/.../<id>.md`, including the extension; omitted paths and `file=` can target unintended notes.
List candidates with `files folder=<root>/<Folder>`, then `read path=<path>` and filter decoded records by exact keys or fields; exclude History unless requested.
Use `search query=<text> path=<root> format=json` for discovery; search results alone do not prove completeness or identity.
Pass arguments through a process argument array. Preserve literal backslashes and multiline payloads across CLI escape handling (`\n`, `\t`).
Use `obsidian help <command>` for installed syntax. If CLI access fails, report blocked storage without switching to filesystem writes or connectors.

## Reads and results

Read retained revisions for historical cutoffs and Events for task history; expose missing dates, history, access, or truncated results.
Return logical fields plus IDs, keys, revisions, note references, and per-operation verified/partial/failed/unsupported status.
