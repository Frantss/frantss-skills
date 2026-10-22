# Common record fields

Backend records use `schema_version: 1`, `record_type`, UUID `id`, stable `key`, `title`, integer `revision`, `created_at`, and `updated_at`.
Stable IDs are record properties; adapters use human-readable note names and resolve identity independently of filenames.
Store only `task` and `report`. Settings belong to local configuration; retired settings/evidence/run/event records are migration inputs only.
Start revisions at 1; timestamps include offsets, date-only values retain precision, and unknown dates remain null.
Use `<record_type>:<id>` keys unless the supplied schema defines a composite key; reuse identities on retries.
Composite keys are compact JSON strings with fixed element order, independent of storage serialization.
Relationships use backend record IDs or readable project IDs, e.g. `frantss/frantssuy`; durable references supplement rather than replace IDs.
Missing project definitions leave labels/scope unresolved without deleting historical records or invalidating their references.
Store one current record per key; revision numbers detect conflicts, not separate history records.
The caller declares domain fields, relationship types, and key construction; preserve unknown fields as data and human edits.
Only the documented schema/version is supported; report incompatible data without rewriting it.
