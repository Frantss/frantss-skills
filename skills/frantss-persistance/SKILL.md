---
name: frantss-persistance
description: "Persist and retrieve shared Frantss workspace configuration and prepared workflow records through one backend. Use for save, read, query, history, and persistence handoffs, independent of the storage tool. Source scans, workflow decisions, and ordinary note editing belong elsewhere."
---

# Frantss persistance

Prepare storage requests and assess their results. Keep the same logical records when the storage tool changes.
The calling workflow defines field meanings, requested changes, and content; this skill preserves those decisions across storage backends.

## Select the adapter

Read only `~/.frantss/persistance.yaml`, expanding `~` to the current user's home independently of the working directory.
Repository-local and ancestor configurations are not discovered. Missing or invalid connection data leaves requests unsaved; setup requires a request.
Require `schema_version: 1` and one `backend` with an `adapter` skill name and `options` mapping; treat YAML as data.
Every workspace uses this backend. Reject per-workspace backend overrides and pass connection options unchanged to the selected adapter.
Retrieve shared settings, workspace configuration, and workflow records as needed through that adapter; keep them out of the connection file.
Read [workspace resolution](references/workspaces.md) for registration, association updates, or identifying the current workspace through backend records.
Operations scoped by existing IDs, including inbox queries, require no checkout; ordinary reads and saves never create workspace identity or associations.
For Obsidian, use `frantss-persistance-obsidian` when available. Other backends must satisfy the same record and operation requirements.
The adapter owns physical locations, serialization, storage tools, and recovery mechanics.
If the selected adapter is unavailable, retain an unsaved request bundle and identify the missing capability. Never silently switch stores.

## Prepare the request

Read [logical records](references/records.md) for shared fields and workspace configuration; require a supplied schema for other workflow types.
For `task`, `evidence`, `run`, `event`, or `report` records, read [tracking records](references/tracking.md).
For settings or account references, read [shared settings](references/settings.md) for the backend-independent payload and defaults.
Read [operation requirements](references/operations.md) when saving, querying, or evaluating adapter results.
Only explicit workspace creation registers a readable ID after checking existing records; partial backend writes retain that ID for recovery.
Pass the operation, record types, stable identities, supplied fields, expected revisions, and requested scope to the adapter.
Use record IDs for relationships. Callers should not construct backend paths, note links, or database-specific queries.
Preserve existing IDs, keys, dates, unknown fields, and human edits when preparing an update.

## Return

Check the adapter's verified records and revisions against the requested changes and supporting records.
Return durable references with scope, coverage, missing steps, and unsaved inputs. Partial writes remain labeled partial.
Finish when required records are verified or explicitly unsaved, with enough identity and payload information for recovery.
