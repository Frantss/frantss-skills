---
name: tracking-persist-obsidian
description: "Read and write prepared personal tracking records in a selected Obsidian vault. Use when Obsidian is the configured persistence adapter or for explicit tracking-vault setup and Bases changes. General persistence policy and ordinary note editing belong elsewhere."
---

# Tracking persist Obsidian

Implement supplied logical storage requests using real filesystem tools or an available Obsidian connector.
If available, `tracking-persist` prepares those requests. Without it, accept complete caller-supplied record payloads and operation requirements.
Ask for missing payload fields rather than inferring ownership, triage, acknowledgment, or report content.

## Setup and routing

Use supplied backend options `vault` and `root`, or read them from the selected `.frantss/tracking.yaml`.
Without an explicit selection, use a unique config found in the current directory or its ancestors; ask when ambiguous.
Require schema version 1, this adapter, an existing absolute vault path, and a vault-relative root. Missing options leave storage unconfigured.
Initialize only on explicit setup; offer `Tracking` as the default root. Preserve unrelated notes and `.obsidian` settings.
Keep every resolved destination inside the root; reject traversal and escaping symlinks. Keep credentials in their tool's credential store.
For record operations or setup, read [note mapping](references/notes.md); before writes, also read [write protocol](references/writes.md).
For requested view setup or changes, read [Bases views](references/bases.md).

## Reads and results

Search current record folders and Settings.md by key, ID, or supplied filters; exclude History unless a revision is requested.
Decode note links to logical UUID relationships and labeled JSON sections to structured fields.
Read Events and retained revisions for historical cutoffs; expose missing dates, history, access, or truncated results.
Return logical fields plus IDs, keys, revisions, note references, and per-operation verified/partial/failed/unsupported status.
If tools or access are unavailable, retain unsaved payloads and identify the missing requirement.
