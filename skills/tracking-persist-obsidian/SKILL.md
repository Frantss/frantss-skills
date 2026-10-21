---
name: tracking-persist-obsidian
description: "Read and write prepared personal tracking records in a selected Obsidian vault. Use when Obsidian is the configured persistence adapter or for explicit tracking-vault setup and Bases changes. General persistence policy and ordinary note editing belong elsewhere."
compatibility: Requires Obsidian 1.12.7+ with the official obsidian CLI enabled and registered, and access to the desktop app.
---

# Tracking persist Obsidian

Implement supplied logical storage requests through the official [Obsidian CLI](https://obsidian.md/help/cli).
If available, `tracking-persist` prepares those requests. Without it, accept complete caller-supplied record payloads and operation requirements.
Ask for missing payload fields rather than inferring ownership, triage, acknowledgment, or report content.

## Setup and routing

Use supplied backend options `vault` and `root` from `~/.frantss/tracking.yaml`, or read that user-wide connection directly.
Expand `~` to the current user's home; repository-local and ancestor configurations never select the vault.
Require schema version 1, this adapter, an existing absolute vault path, and a vault-relative root. Missing options leave storage unconfigured.
Check `obsidian help`; if unavailable, retain payloads and explain CLI activation under Settings → General and PATH registration.
The desktop app must run; CLI commands can launch it. This adapter is not a headless workflow.
Use `obsidian vaults verbose` to resolve the configured path to a unique vault name or ID; ask if unresolved.
Put `vault=<name-or-id>` before the command on every call; verify `obsidian vault=<id> vault info=path` matches the configured path.
Initialize only on explicit setup; offer `Tracking` as the default root. Preserve unrelated notes and `.obsidian` settings.
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

Decode note links to logical record IDs, including readable workspace IDs, and labeled JSON sections to structured fields.
Read Events and retained revisions for historical cutoffs; expose missing dates, history, access, or truncated results.
Return logical fields plus IDs, keys, revisions, note references, and per-operation verified/partial/failed/unsupported status.
