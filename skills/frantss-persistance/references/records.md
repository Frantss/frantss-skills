# Logical records

These fields describe information to retain; the adapter chooses its physical representation.
All records have `schema_version: 1`, `record_type`, stable `id` (readable workspace ID; UUID otherwise), `key`, `title`, integer `revision`, `created_at`, and `updated_at`.
Start revisions at 1. Timestamps carry an offset; date-only values retain their precision. Unknown dates are null.
Relationships contain record IDs, including readable workspace strings. A returned durable reference supplements an ID without replacing it.
Use `<record_type>:<id>` keys unless the supplied schema defines a composite key; reuse identities during retries.
Composite keys use compact JSON strings with fixed element order, independent of backend serialization.

## Workspaces

Workspaces use `title` as their display name and retain `area: work|personal`, `sources`, `repositories`, and `local_paths`.
The backend record owns a unique readable workspace ID such as `frantss/frantssuy`; connection files and checkouts own no workspace identity.
`repositories` holds canonical remote strings; `local_paths` holds `{machine, path}` bindings. Missing lists read as empty without saving; workspaces need no repository.
Names and associations can change without changing IDs. Read [workspace resolution](workspaces.md) before matching or registering associations.
For source mappings, read [sources](sources.md) for their meaning, retained configuration, and use during collection.

For other record types, require caller-supplied field meanings, relationship fields, and history requirements; preserve unknown fields as data.
