# Operation requirements

## Save

Supply the logical record or requested patch, stable key, existing ID/revision when known, and related events or evidence.
Find by key before creation. An identical retry must not create another record, event, or logical revision.
Conflicting matches or changes since the expected revision require reconciliation before replacement.
Preserve the prior revision before a content update. Preserve unknown fields and human edits.
Related records form one logical operation; require a result for every part, including task/events or run/evidence writes for tracking.
Partial results must retain the missing payloads and identities so recovery completes rather than repeats the logical change.
The adapter implements write ordering, verification, and recoverable storage appropriate to its backend.

## Read, query, and history

Supply record type and ID/key for lookup, or schema-defined filters and result limits for queries.
For tracking, inbox queries select pending tasks without a workspace. Ordinary queries select current records, excluding archived revisions.
Tracking activity queries use occurrence date; collection or file modification dates cannot establish when activity happened.
Tracking historical status requires dated events and retained revisions at the cutoff; other types follow their supplied history schema.
Request exact ID/revision pairs for report inputs. Return missing history, unsupported filters, inaccessible records, and pagination explicitly.

## Configure and return

Use `setup-frantss-skills` when available for explicit configuration: `~/.frantss/persistance.yaml` selects one backend for every workspace.
The adapter saves workspace configuration, shared settings, and caller-defined workflow records there and initializes only requested storage/views.
Setup alone creates no workspace records. Changing the backend selection does not migrate existing records.
Return `verified`, `partial`, `failed`, or `unsupported` per operation, with IDs, keys, revisions, durable references, and coverage.
For partial or failed writes, include persisted parts, missing steps, recoverable payload locations, and remaining unsaved inputs.
Stop after a repeated unresolved conflict or access failure and identify what needs resolution.
