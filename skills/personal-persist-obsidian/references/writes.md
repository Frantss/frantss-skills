# File writes and recovery

1. Find current notes by key before creation; reuse the supplied UUID/key. Return a conflict for multiple matches.
2. Read content/revision before patching. Reconcile changed content; preserve unknown fields and human sections.
3. Archive the previous revision before replacement. Verify an existing archive instead of overwriting it.
4. Recheck current content against the read version. Use exclusive creation and atomic replacement when supported.
   Atomic replacement does not prevent concurrent edits; disclose limited protection when conditional writes are unavailable.
5. Increment revision for a logical content change, not an identical retry. Read back fields, revision, and links.

## Related records

Before changing a task, recover its pending events. Stop with partial status if recovery cannot finish.
Write desired task fields, `history_complete: false`, and a Pending events fenced JSON section in one task save.
The section stores prior history completeness and each supplied event's UUID/key, fields, dates, evidence, and before/after changes.
Create or verify Events notes by those keys. On retries, recover payloads from the task instead of repeating the transition.
After verification, remove pending payloads and restore prior completeness; new tasks become complete, earlier gaps stay incomplete.
Journal finalization keeps the same logical task revision and still requires a content check and read-back.
Write evidence before advancing the corresponding run's coverage checkpoint; retain partial-run cursors separately.

## Partial failures

Multi-file saves are not transactions. Inspect current notes, History, and pending event payloads after an uncertain write.
Retry only missing steps using the same identities. Preserve unsaved inputs when no recoverable note was written.
Return persisted parts, missing steps, and recovery locations; stop after a repeated unresolved conflict or access failure.
