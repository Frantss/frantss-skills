# Operation requirements

## Save

Find by key before creation; reconcile duplicate matches or changed expected revisions before replacement.
Preserve prior revisions and human edits. Identical retries create no new record, event, or logical revision.
Related records form one logical operation; the adapter owns ordering, verification, and recoverable partial writes.
Retain missing payloads/identities so recovery completes the operation rather than repeating its effects.

## Read, query, and history

Supply type and ID/key for lookup, or schema-defined filters and result limits; ordinary queries exclude archived revisions.
Historical queries require dated events and retained revisions at the cutoff; never infer occurrence from recording or modification time.
Return exact ID/revision pairs for snapshot inputs, plus missing history, unsupported filters, pagination, and inaccessible records.
Reads do not save defaults or repair records; missing history remains an explicit gap.

## Results

Return `verified`, `partial`, `failed`, or `unsupported` per operation, with IDs, keys, revisions, durable references, and coverage.
For partial/failed writes, identify persisted parts, missing steps, recoverable payload locations, and unsaved inputs.
Read back by stable identity after uncertain writes; retry only missing work with the same identities.
Stop after a repeated unresolved conflict or access failure and identify what requires resolution.
