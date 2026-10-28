# Operation requirements

## Save

Find by key before creation; reconcile duplicate matches or changed expected revisions before replacement.
Preserve human edits; replace the current record without creating revision archives. Identical retries create no new record or logical revision.
Related records form one logical operation; the adapter owns ordering, verification, and recoverable partial writes.
Retain missing payloads/identities so recovery completes the operation rather than repeating its effects.

## Read, query, and history

Supply type and ID/key for lookup, or schema-defined filters and result limits; ordinary queries exclude archived revisions.
Historical state requires saved report summaries or dated sources; unavailable prior revisions return unsupported. Never infer occurrence from modification time.
Return requested IDs/revisions plus missing history, unsupported legacy shapes/filters, pagination, and inaccessible records.
Reads do not save defaults or repair records; missing history remains an explicit gap.

## Results

Return `verified`, `partial`, `failed`, or `unsupported` per operation, with IDs, keys, revisions, durable references, and coverage.
For partial/failed writes, identify persisted parts, missing steps, recoverable payload locations, and unsaved inputs.
Read back by stable identity after uncertain writes; retry only missing work with the same identities.
Stop after a repeated unresolved conflict or access failure and identify what requires resolution.
