# Acknowledge

Absence of `reviewed-by-frantss` means unreviewed; natural-language acknowledgment requires clear task/batch scope, not general workflow agreement.
Preserve acknowledgment during other changes; remove the tag only on an explicit request to mark unreviewed.

## Update

Resolve the exact task; clarify ambiguous targets. Preserve unrelated fields, evidence, and human edits; apply [content/date rules](content.md).
Reassess states using [triage](triage.md); reopening restores the appropriate unfinished state from evidence, not automatically Next.

Record Done only from an explicit user report or evidence satisfying the outcome; a merged subtask PR does not complete a broader release.
Persist dated before/after events for state, workspace, acknowledgment, dates, blockers, triage reasons, and context changes, including reopening.
Separate occurrence and recording times; unknown dates stay unknown. Repeated triage with no change creates no event.

## Retrieve

Inbox queries select `inbox` or legacy `pending`, regardless of workspace. Pending queries return Next/Later plus Inbox awaiting triage; show Maybe separately when requested.
Respect workspace/area scope; without scope, include the inbox and all workspaces. Include references, dates, blockers, and acknowledgment where useful.
Identify inaccessible/incomplete results rather than presenting them as empty; legacy `pending` needs triage, preserving its workspace and history.
