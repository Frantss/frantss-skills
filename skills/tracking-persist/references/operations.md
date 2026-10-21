# Operation requirements

## Save

Supply the logical record or requested patch, stable key, existing ID/revision when known, and related events or evidence.
Find by key before creation. An identical retry must not create another record, event, or logical revision.
Conflicting matches or changes since the expected revision require reconciliation before replacement.
Preserve the prior revision before a content update. Preserve unknown fields and human edits.
Task state and events, and run coverage and evidence, form related writes; require a result for every part.
Partial results must retain the missing payloads and identities so recovery completes rather than repeats the logical change.
The adapter implements write ordering, verification, and recoverable storage appropriate to its backend.

## Read, query, and history

Supply record type and ID/key for lookup, or workspace, area, date, state, and result limits for queries.
An inbox query selects pending tasks without a workspace. Ordinary queries select current records, excluding archived revisions.
Activity queries use occurrence date; collection or file modification dates cannot establish when activity happened.
Historical status requires dated events and retained revisions at the requested cutoff; distinguish it from current status.
Request exact ID/revision pairs for report inputs. Return missing history, unsupported filters, inaccessible records, and pagination explicitly.

## Configure and return

Use `setup-frantss-skills` when available for explicit configuration: `~/.frantss/tracking.yaml` selects one backend for every workspace.
The adapter saves shared settings and workspace identities, associations, and sources in that backend and initializes requested storage/views.
Setup alone creates no workspace records. Changing the backend selection does not migrate existing records.
Return `verified`, `partial`, `failed`, or `unsupported` per operation, with IDs, keys, revisions, durable references, and coverage.
For partial or failed writes, include persisted parts, missing steps, recoverable payload locations, and remaining unsaved inputs.
Stop after a repeated unresolved conflict or access failure and identify what needs resolution.
