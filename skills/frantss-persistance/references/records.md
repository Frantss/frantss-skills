# Logical records

Backend records have `schema_version: 1`, `record_type`, UUID `id`, stable `key`, `title`, integer `revision`, `created_at`, and `updated_at`.
Start revisions at 1. Timestamps carry an offset; date-only values retain their precision. Unknown dates are null.
Relationships contain backend record IDs or readable local workspace IDs. A returned durable reference supplements an ID without replacing it.
Reuse `<record_type>:<id>` keys on retries unless the schema defines a composite key: compact JSON with fixed element order, independent of backend serialization.

## Workspace references

Workspace definitions live only in `~/.frantss/workspaces.yaml`; read [workspace resolution](workspaces.md) for their schema and matching.
Records reference readable workspace IDs such as `frantss/frantssuy`, never backend workspace records or note links.
Missing definitions do not delete historical records or invalidate their IDs; report unavailable labels/scope rather than inventing configuration.
For source mappings, read [sources](sources.md); retain actual collection coverage and provenance in records, not duplicate configuration registries.

For other record types, require caller-supplied field meanings, relationship fields, and history requirements; preserve unknown fields as data.
