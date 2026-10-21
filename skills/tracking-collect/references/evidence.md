# Evidence and persistence

Store one meaningful observation per source event. Preserve these logical fields in the persistence layer's actual format:

| Field | Meaning |
| --- | --- |
| Evidence key | Stable source/account/scope/object/event identity; distinct reviews or replies on one PR remain distinct |
| Workspace links | Existing workspace identities; reuse one observation when several workspace mappings include it |
| Source | Provider, account, location, original IDs, and returned permalink when available |
| Actor and event | Who did what, their relationship to the user, and the basis for attribution |
| Occurred time and local date | Source-supported occurrence time and date in the selected timezone; unknown when unsupported |
| Collected time | Actual retrieval timestamp, separate from occurrence time |
| Content | Relevant excerpt or transcript passage with enough context to understand the contribution |

Deduplicate by evidence key before saving. Preserve separate actions even when they support one task or outcome.
Keep source revisions distinguishable; a changed message must not silently erase previously collected evidence.
Give each run a stable ID, provisional if unsaved. Link its observations and retain scope, timezone, collection time, and per-source coverage.
Coverage includes queried windows, completed pages, gaps, truncation, and continuation cursors.

Persist through configured storage. If unavailable, return an explicitly unsaved evidence bundle and identify the missing capability.
Store excerpts and metadata rather than only remote links. Preserve supplied links; never fabricate source URLs.
Before retrying an uncertain write, read back by stable evidence identity; report partial or failed persistence explicitly.
Reserve calls needed for verification; when the budget cannot finish another item, leave it pending.
Save partial-run cursors separately. Advance a completed-through checkpoint only after all pages and evidence writes for that scope/window succeed.
For incremental scans, overlap the prior checkpoint to catch late updates and deduplicate repeated events.
