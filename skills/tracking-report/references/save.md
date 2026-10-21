# Save a report snapshot

Persist the written report with these logical fields in the configured storage format:

| Field | Meaning |
| --- | --- |
| Report key | Report type, exact interval, timezone, and sorted workspace identities |
| Generation time | When the report was produced, distinct from its activity period |
| Evidence | Collection IDs, supporting evidence/task references, and source revisions when available |
| Status cutoffs | Whether pending work represents period end or current status, with the relevant timestamp |
| Coverage | Source windows, gaps, truncation, unsaved inputs, and completeness at generation time |
| Narrative | The saved account of outcomes, contributions, and pending work, with supporting links |

Keep the narrative as a dated snapshot. Live query views may supplement it but must not replace its saved evidence or conclusions.
Before saving, find an existing report with the same key. Retries must not create accidental duplicates.
On regeneration, retain the prior snapshot as a revision and preserve human edits; identify the revised evidence cutoff.
If storage cannot preserve a revision, resolve replacement of existing content before overwriting it.
Read back by key after an uncertain write. Return a verified reference or an explicit partial/unsaved result.
