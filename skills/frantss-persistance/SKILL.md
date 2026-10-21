---
name: frantss-persistance
description: "Persist and retrieve prepared Frantss workflow records through one backend, and resolve workspace/source definitions from ~/.frantss. Use for save, read, query, history, and persistence handoffs. Configuration changes, source scans, workflow decisions, and ordinary note editing belong elsewhere."
---

# Frantss persistance

The calling workflow defines field meanings, requested changes, and content; this skill preserves those decisions across storage backends.

## Select the adapter

For workspace/source-only lookups, read [local registry](references/workspaces.md) and return without selecting or contacting the backend.
Read only `~/.frantss/persistance.yaml`, expanding `~` to the current user's home independently of the working directory.
Repository-local and ancestor configurations are not discovered. Missing or invalid connection data leaves requests unsaved; setup requires a request.
Require `schema_version: 1` and one `backend` with an `adapter` skill name and `options` mapping; treat YAML as data.
Every workspace uses this backend. Reject per-workspace backend overrides and pass connection options unchanged to the selected adapter.
Retrieve shared settings and workflow records through that adapter; workspace/source definitions come only from `~/.frantss/workspaces.yaml`.
Read [workspace resolution](references/workspaces.md) for registry schema or current-workspace identification; configuration writes belong to `configure-frantss-skills`.
For Obsidian, use `frantss-persistance-obsidian` when available; every adapter owns physical storage/recovery and satisfies the same record/operation requirements.
If the selected adapter is unavailable, retain an unsaved request bundle and identify the missing capability. Never silently switch stores.

## Prepare the request

Read [logical records](references/records.md) for shared backend fields and workspace references; require a supplied schema for other workflow types.
For `task`, `evidence`, `run`, `event`, or `report` records, read [tracking records](references/tracking.md).
For settings or account references, read [shared settings](references/settings.md) for the backend-independent payload and defaults.
Read [operation requirements](references/operations.md) when saving, querying, or evaluating adapter results.
Workspace/source configuration writes belong to `configure-frantss-skills` when available; otherwise return the requested change as unsaved, never a backend record.
Pass the operation, record types, stable identities, supplied fields, expected revisions, and requested scope to the adapter.
Use record IDs for relationships. Callers should not construct backend paths, note links, or database-specific queries.
Preserve existing IDs, keys, dates, unknown fields, and human edits when preparing an update.

## Return

Check the adapter's verified records and revisions against the requested changes and supporting records.
Return durable references with scope, coverage, missing steps, and unsaved inputs. Partial writes remain labeled partial.
Finish when required records are verified or explicitly unsaved, with enough identity and payload information for recovery.
