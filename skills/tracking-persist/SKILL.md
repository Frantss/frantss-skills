---
name: tracking-persist
description: "Define what personal tracking must retain and retrieve: tasks, workspaces, evidence, collection coverage, task history, and report snapshots. Use for persistence handoffs from tracking, collection, or reporting, independent of the storage backend. Source scanning, triage decisions, and generic note editing belong elsewhere."
---

# Tracking persist

Prepare storage requests and assess their results. Keep the same logical records when the storage tool changes.
The calling workflow decides ownership, categorization, completion, and report content; this skill preserves those decisions and their evidence.

## Select the adapter

Read the explicitly selected `.frantss/tracking.yaml`; otherwise search the current directory and its ancestors for a unique config.
Only tracking configuration selects this backend; `.frantss/workspace.yaml` identifies one workspace, independently of tracking storage.
Ask which configuration to use if several exist. Missing or invalid configuration leaves requests unsaved; use `setup-frantss-skills` only for requested setup.
Require `schema_version: 1` and one `backend` with an `adapter` skill name and `options` mapping; treat YAML as data.
Every workspace uses this backend. Reject per-workspace backend overrides and pass connection options unchanged to the selected adapter.
Retrieve shared settings and workspace/source records as needed through that adapter; keep them out of the connection file.
Resolve existing workspace IDs through backend records; read local `.frantss/workspace.yaml` only when identifying the current workspace.
Inbox and backend-scoped operations require no local profile; never initialize identity for an ordinary read or capture.
For Obsidian, use `tracking-persist-obsidian` when available. Other backends must satisfy the same record and operation requirements.
The adapter owns physical locations, serialization, storage tools, and recovery mechanics.
If the selected adapter is unavailable, retain an unsaved request bundle and identify the missing capability. Never silently switch stores.
These are instructions for an agent using available tools, not installed functions or a background service.

## Prepare the request

Read [logical records](references/records.md) for the requested record types.
Read [operation requirements](references/operations.md) when saving, querying, or evaluating adapter results.
For explicit workspace creation, initialize/reuse its workspace identity first. Partial backend writes retain that UUID for recovery.
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
