# Evidence and run records

Supply the common persistence envelope; evidence/runs use UUIDs. Allocate a run ID before writes, provisional if unsaved.
Evidence fields: `workspaces`, `source_refs`, `source`, `account`, `source_scope`, `object_id`, `event_id`, `actor`, and `action`.
`source` is the provider; `account` its native host/tenant/account namespace, independent of authentication profiles.
`source_scope` is the stable native container, or null for account-global object/event IDs; query filters never form identity.
Normalize connector wrappers to native strings; unresolved identity needs clarification before saving/deduplication.
Key: compact canonical JSON `[source, account, source_scope, object_id, event_id]`, independent of tools, query scope, and configured mapping IDs.
Without an event ID, use a stable access-independent event discriminator; match native identity and retain existing UUIDs on retries.
`source_refs` is a sorted unique list of `{workspace, source_id}` pairs; merge references/workspace IDs across mappings without changing the key.
Also retain `occurred_at`, `occurred_date`, `collected_at`, `timezone`, `source_url`, excerpt `content`, and attribution `context`.
Derive local occurrence dates from known times; retain source-supported date-only precision and null unknowns, never substituting retrieval time.
Keep meaningful excerpts/metadata, not only links; preserve supplied URLs without fabrication. Separate actions remain separate observations; source edits retain revisions.

Run fields: `workspaces`, `window_start`, `window_end`, `timezone`, `collected_at`, `capture: automatic|none`, `status: partial|complete`, `evidence`, and `coverage`.
Default run key is `run:<id>`; one run represents one attempt, including retries/resume. Windows include start and exclude end.
Coverage identifies each workspace/source-ID pair, runtime method/query scope, requested window, pages, cursor, limits, usage, gaps, and completed-through checkpoints.
Advance a checkpoint only after all pages and evidence writes for that scope/window verify; retain partial cursors separately even when other sources fail.
Read back uncertain writes by stable key; retry missing work with the same identities and preserve incomplete payloads/coverage.
If storage is unavailable, return an unsaved evidence/run bundle rather than claiming completion.
