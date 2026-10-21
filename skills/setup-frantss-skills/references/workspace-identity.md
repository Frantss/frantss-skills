# Workspace identity

Use `<selected-workspace>/.frantss/workspace.yaml` for exactly that workspace; identity setup requires no tracking backend.
Resolve an explicit workspace or current Git root; ask outside Git when unresolved.
Never inherit another repository's identity or select identity from the tracking connection's location.
Require `schema_version: 1`, UUID `id`, and display `name`; missing/null fields mean an incomplete draft.
On explicit workspace setup/creation, resolve the name and reuse existing identity before allocating one UUIDv4.
Retain supplied adoption IDs; unresolved previous identity requires clarification before allocating a replacement.
Renaming, moving, changing sources, and switching backends preserve the ID; names remain mutable labels.
Preserve unknown fields; reject unsupported versions and malformed IDs. Read back updates by ID.
Inspection and ordinary skill use never initialize or repair identity. Each workspace owns one identity file shared across Frantss skills.
Tracking reuses this UUID; work/personal area and sources remain backend fields.
