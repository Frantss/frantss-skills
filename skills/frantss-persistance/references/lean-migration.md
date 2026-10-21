# Migration to task links and report summaries

Use only through an explicitly requested `frantss-update` migration, with its verified backups, fixed commits, journal, and adapter protocol.
Applies to tasks with `evidence`/`history_complete`/Pending events and reports with `evidence`/`manifest`; empty/current storage needs no conversion.
The common envelope remains version 1; domain shape, not that number alone, determines applicability. Configuration/settings formats remain unchanged.

1. Inspect current records, referenced evidence/events/runs, retained revisions, and affected views. Exclude concurrent legacy writers before conversion.
2. Resolve old Pending events with the baseline write protocol before mapping; ambiguous/missing dependencies leave the affected conversion incomplete.
3. Build source links from each referenced evidence record's `source_url`, or its native provider/instance/container/object/event locator when no URL exists.
   Never fabricate links or replace unknown identity with an excerpt; unresolved references remain migration blockers with recoverable old payloads.
4. Tasks: merge existing `source_urls` with relevant task/event evidence links, deduplicating targets. Preserve ID/key, project, state, tags, context, dates, blockers, and human edits.
   For a currently done task, derive optional `completed_date`/`completed_at` only from an unambiguous latest completion event or supported source; otherwise leave unknown.
   Remove owned `evidence`, `history_complete`, and finalized Pending events from the converted current task; new updates need only task revisions.
5. Reports: preserve narrative, scope, ID/key, generation time, and human edits. Resolve evidence to supporting `source_urls` and referenced task IDs to `tasks`.
   Map manifest cutoff to `status_cutoff` and coverage/completeness to brief text `coverage`; preserve uncertainty when an old cutoff or source scope is missing.
   Remove current `evidence`/`manifest`; observations, input revisions, collection IDs, and query/cursor details remain only in the archived original.
6. Archive each original before replacing it through the adapter protocol. Keep original History unchanged; legacy snapshots remain readable as archival data, with unsupported domain/history queries reported as gaps.
7. Update affected owned views to task/report inputs after replacements verify; preserve custom views and report any that still depend on retired types.
8. Verify IDs/keys, link resolution, mapped fields, report text, history preservation, and current task/report queries. Do not mark migration complete with unresolved references.
9. Retry by the journal's original identities and expected revisions; inspect started-step effects, reuse verified replacements/archives, and write only missing work.
Retired evidence/run/event notes remain read-only. Deleting them or their history requires a separately authorized cleanup after all references and backups verify.
