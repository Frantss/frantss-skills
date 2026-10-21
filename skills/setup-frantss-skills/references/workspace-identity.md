# Workspace identity

Use the backend selected by `~/.frantss/tracking.yaml`; workspace identity and configuration are backend records, shared across Frantss skills.
Read [persistence setup](tracking.md) for connection/access checks; use `tracking-persist` when available for workspace schema and resolution.
Resolve explicit readable ID or unique display title first; otherwise match registered repository remotes, then machine-scoped canonical local roots.
When inferring context, inspect the current Git root/remotes, not parents; unresolved matches require clarification and never imply workspace creation.
Only explicit workspace creation registers an ID: use kebab-case `org/repo` from the selected repository, e.g. `frantss/frantssuy`, or a user-chosen slug without a repository.
IDs have one or two slash-separated `[a-z0-9]+(?:-[a-z0-9]+)*` segments, never UUIDs; resolve owner/repository ambiguity and ID collisions before saving.
Resolve display `title` and `area: work|personal`; default new `sources`, `repositories`, and `local_paths` to empty lists.
Register only requested associations: canonical remote strings in `repositories`, or `{machine, path}` entries in `local_paths` with a stable device identifier and absolute canonical root.
Keep association changes explicit; a new checkout or changed remote never rewrites registration automatically.
Reuse readable IDs across renames, moves, backend changes, and retries; legacy UUID import needs an explicit old→new mapping and migration of references, keys, paths, and history.
Persist and read back by workspace ID; preserve unknown fields. If backend access or schema guidance is unavailable, return unsaved inputs without local identity files.
