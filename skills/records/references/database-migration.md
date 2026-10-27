# Database connection key migration

Use through explicitly requested `update`, with its backups, fixed commits, journal, and content checks.
Applies to top-level `backend` in `~/.frantss/persistance.yaml` version 1. Rename it to `database`; the path, schema version, records, and project registry stay unchanged.

1. Reject duplicate YAML keys, unsupported versions, or malformed connection mappings. Back up the original and journal expected content before mutation.
2. If only `backend` exists, move its complete mapping to `database`, preserving adapter, options, unknown fields, comments, and human edits.
3. If both keys exist, remove `backend` only when the complete mappings match; conflicting mappings require resolution before writing.
4. If only `database` exists, verify it without rewriting. If neither exists or the file is absent, leave storage unconfigured; create nothing.
5. Patch atomically after rechecking content. Verify `database`, absence of `backend`, preserved fields, and selected-adapter inspection/read access without initializing storage.
6. On retry, inspect journaled effects; reuse a verified rename and finish only missing checks. Changed content or unavailable adapter access leaves the update incomplete.
