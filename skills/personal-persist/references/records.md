# Logical records

These fields describe information to retain; the adapter chooses its physical representation.
All records have `schema_version: 1`, `record_type`, UUID `id`, stable `key`, `title`, integer `revision`, `created_at`, and `updated_at`.
Start revisions at 1. Timestamps carry an offset; date-only values retain their precision. Unknown dates are null.
Relationships contain record UUIDs. A returned durable reference supplements an ID without replacing it.
Use `<record_type>:<uuid>` keys for allocated tasks, projects, runs, and events; reuse identities during retries.
Composite keys use compact JSON strings with fixed element order, independent of backend serialization.

## Tasks and projects

Tasks retain `status: pending|done`, nullable `project`, `tags`, `evidence`, `history_complete`, and task `context`.
Optional `due_date` or `due_at` preserves the deadline's precision. A null project identifies the inbox.
The absence of `reviewed-by-frantss` means unreviewed. Preserve this state during unrelated changes.
Projects retain `area: work|personal` and `sources` mappings.
Each mapping identifies provider, account, user identity, and source locations, branches, or query constraints.
An empty source list enables no collection. Semantic task deduplication and project creation decisions come from the caller.

## Evidence

Retain `projects`, `source`, `account`, `source_scope`, `object_id`, `event_id`, `actor`, and `action`.
Retain `occurred_at`, `occurred_date`, `collected_at`, `timezone`, `source_url`, excerpt `content`, and attribution `context`.
Derive local occurrence date from a known occurrence time; preserve source-supported date-only evidence when time is unknown.
The key is `[source, account, source_scope, object_id, event_id]` encoded as a canonical JSON string.
If no event ID exists, use the collector's stable event discriminator; unresolved identity requires clarification before deduplication.
Distinct actions on one object remain distinct observations. Source edits create revisions of the same evidence identity.

## Collection runs

Retain `projects`, `window_start`, `window_end`, `timezone`, `collected_at`, `status: partial|complete`, `evidence`, and per-source `coverage`.
Coverage includes scope, requested window, pages, continuation cursor, limits, usage when supplied, gaps, and completed-through checkpoints.
A run identifies one collection attempt. Preserve partial coverage and cursors even when some sources fail.
Advance a source checkpoint only after all pages and evidence writes for that scope/window are verified.

## Task events

Retain `task`, `kind`, `occurred_at`, `occurred_date`, `recorded_at`, `evidence`, and a `change` containing before/after field values.
Creation, categorization, acknowledgment, completion, reopening, and deadline/context edits each require a dated event.
One logical task change can update several fields in one event. Allocate event identity before writing.
Current state and its events must agree. Keep `history_complete: false` while events or earlier history are missing.
Known manual edits without events leave a gap; never invent their dates or claim a complete audit trail.

## Reports and revisions

Retain `report_type: daily|weekly`, `projects`, `window_start`, `window_end`, `timezone`, `generated_at`, `evidence`, `narrative`, and `manifest`.
The manifest includes collection IDs, exact input IDs/revisions, status cutoffs, coverage, and completeness at generation time.
The key is `[report_type, window_start, window_end, timezone, sorted_project_ids]` encoded as a canonical JSON string.
Normalize key timestamps to UTC; sort unique project UUIDs. Windows include the start and exclude the end.
Identical scope identifies one report with successive saved revisions. Retrieval returns its saved snapshot without regeneration.
Keep previous record revisions so a report's exact inputs remain retrievable after source edits.
Preserve human edits and earlier report narratives during regeneration. Missing input snapshots remain explicit gaps.
