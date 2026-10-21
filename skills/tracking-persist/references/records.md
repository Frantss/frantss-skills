# Logical records

These fields describe information to retain; the adapter chooses its physical representation.
All records have `schema_version: 1`, `record_type`, stable `id` (readable workspace ID; UUID otherwise), `key`, `title`, integer `revision`, `created_at`, and `updated_at`.
Start revisions at 1. Timestamps carry an offset; date-only values retain their precision. Unknown dates are null.
Relationships contain record IDs, including readable workspace strings. A returned durable reference supplements an ID without replacing it.
Use `<record_type>:<id>` keys unless the supplied schema defines a composite key; reuse identities during retries.
Composite keys use compact JSON strings with fixed element order, independent of backend serialization.

## Tasks and workspaces

Tasks retain `status: pending|done`, nullable `workspace`, `tags`, `evidence`, `history_complete`, and task `context`.
Optional `due_date` or `due_at` preserves the deadline's precision. A null workspace identifies the inbox.
The absence of `reviewed-by-frantss` means unreviewed. Preserve this state during unrelated changes.
Workspaces use `title` as their display name and retain `area: work|personal`, `sources`, `repositories`, and `local_paths`.
The backend record owns a unique readable workspace ID such as `frantss/frantssuy`; connection files and checkouts own no workspace identity.
`repositories` holds canonical remote strings; `local_paths` holds `{machine, path}` bindings. Missing lists read as empty without saving; workspaces need no repository.
Names and associations can change without changing IDs. Read [workspace resolution](workspaces.md) before matching or registering associations.
For source mappings, read [sources](sources.md) for their meaning, retained configuration, and use during collection.
An empty source list enables no collection. Semantic task deduplication and workspace creation decisions come from the caller.

## Evidence

Retain `workspaces`, `source_refs`, `source`, `account`, `source_scope`, `object_id`, `event_id`, `actor`, and `action`.
`source` is the provider identifier; `account` is its canonical native host/tenant/account namespace, independent of authenticated profiles.
`source_scope` is null for account-global object/event IDs; otherwise use the stable native container ID. Query filters never belong here.
Normalize connector wrappers to native object/event strings; unresolved identity requires clarification before saving or deduplication.
`source_refs` is a unique list of `{workspace: <workspace-id>, source_id: <configured-id>}` pairs, sorted by workspace/source ID, identifying contributing mappings.
Merge references/workspace IDs when multiple mappings find one event; these provenance fields do not participate in its key.
Retain `occurred_at`, `occurred_date`, `collected_at`, `timezone`, `source_url`, excerpt `content`, and attribution `context`.
Derive local occurrence date from a known occurrence time; preserve source-supported date-only evidence when time is unknown.
The key is `[source, account, source_scope, object_id, event_id]` encoded as a canonical JSON string, independent of access method and collection scope.
If no event ID exists, use an access-independent stable event discriminator; reconcile older matches by native identity without replacing their UUIDs.
Distinct actions on one object remain distinct observations. Source edits create revisions of the same evidence identity.

## Collection runs

Retain `workspaces`, `window_start`, `window_end`, `timezone`, `collected_at`, `capture: automatic|none`, `status: partial|complete`, `evidence`, and per-source `coverage`.
Coverage identifies each workspace/source-ID pair and access method, with scope, requested window, pages, cursor, limits, usage, gaps, and completed-through checkpoints.
Coverage retains the selected access descriptor with its cursor, not merely its position in the configured access list.
A run identifies one collection attempt. Preserve partial coverage and cursors even when some sources fail.
Advance a source checkpoint only after all pages and evidence writes for that scope/window are verified.

## Task events

Retain `task`, `kind`, `occurred_at`, `occurred_date`, `recorded_at`, `evidence`, and a `change` containing before/after field values.
Creation, categorization, acknowledgment, completion, reopening, and deadline/context edits each require a dated event.
One logical task change can update several fields in one event. Allocate event identity before writing.
Current state and its events must agree. Keep `history_complete: false` while events or earlier history are missing.
Known manual edits without events leave a gap; never invent their dates or claim a complete audit trail.

## Reports and revisions

Retain `report_type: daily|weekly`, `workspaces`, `window_start`, `window_end`, `timezone`, `generated_at`, `evidence`, `narrative`, and `manifest`.
The manifest includes collection IDs, exact input IDs/revisions, status cutoffs, coverage, and completeness at generation time.
The key is `[report_type, window_start, window_end, timezone, sorted_workspace_ids]` encoded as a canonical JSON string.
Normalize key timestamps to UTC; sort unique workspace ID strings lexicographically. Windows include the start and exclude the end.
Identical scope identifies one report with successive saved revisions. Retrieval returns its saved snapshot without regeneration.
Keep previous record revisions so a report's exact inputs remain retrievable after source edits.
Preserve human edits and earlier report narratives during regeneration. Missing input snapshots remain explicit gaps.
