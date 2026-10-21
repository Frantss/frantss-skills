---
name: tracking-persist
description: "Define what personal tracking must retain and retrieve: tasks, workspaces, evidence, collection coverage, task history, and report snapshots. Use for persistence handoffs from tracking, collection, or reporting, independent of the storage backend. Source scanning, triage decisions, and generic note editing belong elsewhere."
---

# Tracking persist

Prepare storage requests and assess their results. Keep the same logical records when the storage tool changes.
The calling workflow decides ownership, categorization, completion, and report content; this skill preserves those decisions and their evidence.

## Select the adapter

Read only `~/.frantss/tracking.yaml`, expanding `~` to the current user's home independently of the working directory.
Repository-local and ancestor configurations are not discovered. Missing or invalid connection data leaves requests unsaved; setup requires a request.
Require `schema_version: 1` and one `backend` with an `adapter` skill name and `options` mapping; treat YAML as data.
Every workspace uses this backend. Reject per-workspace backend overrides and pass connection options unchanged to the selected adapter.
Retrieve shared settings and workspace/source records as needed through that adapter; keep them out of the connection file.
Read [workspace resolution](references/workspaces.md) for registration, association updates, or identifying the current workspace through backend records.
Inbox and operations scoped by existing backend IDs require no checkout or local profile; ordinary reads/capture never create identity or associations.
For Obsidian, use `tracking-persist-obsidian` when available. Other backends must satisfy the same record and operation requirements.
The adapter owns physical locations, serialization, storage tools, and recovery mechanics.
If the selected adapter is unavailable, retain an unsaved request bundle and identify the missing capability. Never silently switch stores.
These are instructions for an agent using available tools, not installed functions or a background service.

## Prepare the request

Read [logical records](references/records.md) for the requested record types.
For settings or account references, read [shared settings](references/settings.md) for the backend-independent payload and defaults.
Read [operation requirements](references/operations.md) when saving, querying, or evaluating adapter results.
Only explicit workspace creation registers a readable ID after checking existing records; partial backend writes retain that ID for recovery.
Pass the operation, record types, stable identities, supplied fields, expected revisions, and requested scope to the adapter.
Use record IDs for relationships. Callers should not construct backend paths, note links, or database-specific queries.
Preserve existing IDs, keys, dates, unknown fields, and human edits when preparing an update.

## Preserve the meaning

New tasks enter one inbox, pending and without a workspace or review tag.
Only explicit user acknowledgment adds `reviewed-by-frantss`; workspace creation requires an explicit command for that workspace.
Store dated task changes alongside current state. Missing history or dates limit historical certainty.
Keep occurrence time separate from collection, recording, and generation times. Unknown occurrence dates remain unknown.
Retain evidence excerpts and report narratives, not only links or live query views.

## Return

Check the adapter's verified records and revisions against the requested changes and supporting records.
Return durable references with scope, coverage, missing steps, and unsaved inputs. Partial writes remain labeled partial.
Finish when required records are verified or explicitly unsaved, with enough identity and payload information for recovery.
