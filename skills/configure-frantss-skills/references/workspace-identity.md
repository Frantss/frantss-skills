# Workspace registry

Use `~/.frantss/workspaces.yaml`: `schema_version: 1` and a `workspaces` mapping keyed by readable IDs, shared across Frantss skills.
Each entry requires `title` and `area: work|personal`; `repositories`, `local_paths`, and `sources` are optional lists. Configuration entries need no backend record metadata.
Read and write through filesystem tools; backend configuration/access is not a prerequisite. Use `frantss-persistance` when available for registry resolution.
Resolve explicit readable ID or unique display title first; otherwise match registered repository remotes, then machine-scoped canonical local roots.
When inferring context, inspect the current Git root/remotes, not parents; unresolved matches require clarification and never imply workspace creation.
Only explicit workspace creation registers an ID: use kebab-case `org/repo` from the selected repository, e.g. `frantss/frantssuy`, or a user-chosen slug without a repository.
IDs have one or two slash-separated `[a-z0-9]+(?:-[a-z0-9]+)*` segments, never UUIDs; resolve owner/repository ambiguity and ID collisions before saving.
Default new `sources`, `repositories`, and `local_paths` to empty lists; read [source configuration](sources.md) only for requested source changes.
Register only established associations: canonical remote strings in `repositories`, or `{machine, path}` entries in `local_paths` with a stable device identifier and absolute canonical root.
Update associations only from explicit requests or lasting changes stated by the user; a discovered checkout/remote alone changes nothing.
Reject malformed registries, unsupported versions, duplicate keys/IDs, and missing required fields; a missing registry is unresolved during inspection or ordinary use.
An explicit workspace-creation command may initialize a missing registry with `schema_version: 1` and `workspaces: {}` before adding the requested entry.
Before replacement, recheck original content; use exclusive creation/atomic replacement when supported, preserve human edits and unknown fields, and read back the intended entry.
Reuse readable IDs on renames, moves, and retries; new registration requires the explicit creation command above. Stop after a repeated conflict or access failure with unsaved inputs.
For requested backend export, reconcile entries by ID and copy configuration fields, preserving recovery mappings; migrate UUID references explicitly and leave old records for separate cleanup.
