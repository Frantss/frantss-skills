# Workspace resolution

Read the selected backend's current workspace records; unavailable or incomplete lookup is unresolved, not an empty registry.
Resolve explicit workspace IDs or exact, unique display titles first; a missing explicit selection never falls back to the current checkout.
Only resolve the current workspace when requested; all-workspace queries and inbox capture need no checkout association.
For Git, inspect the current repository root and all its remotes; worktrees with matching remotes select the same registered workspace.
Match canonical remotes against `repositories`; one matching workspace selects it, multiple matches require clarification.
If no remote matches, match an exact canonical root in `local_paths` on the current machine; for non-Git folders use the explicit root or current directory.
Use a stable device identifier from host tools or the caller for `machine`; if unavailable, ask or skip path matching, never infer it from a shared hostname.
Path bindings never match another machine or ancestor folder. Nested repositories resolve using their own root/remotes.
A failed lookup never creates a workspace. Keep unassigned task candidates in the inbox; resolve requested query scope instead of silently widening it.

## Associations and identity

Canonical remote format is `host[:port]/repository-path`, without credentials, query, fragment, trailing slash, or terminal `.git`.
Normalize SSH/scp and HTTPS spellings, lowercase the host, and preserve repository-path case; retain nondefault ports and resolve SSH aliases before matching.
File/local Git remotes require machine-scoped path bindings rather than inventing a host-based remote identity.
Unresolved aliases or conflicting canonicalization require clarification. Do not persist credentials or guess distinct hosts are equivalent.
Canonicalize local roots to absolute resolved paths; register them only with an established device identifier.
Association writes require explicit setup/update instructions; discovery alone never registers a checkout or changes bindings.
Only explicit workspace creation registers an ID after reconciling existing IDs, titles, and association matches.
For repository-backed creation, derive `org/repo` from the selected repository's owner and name, e.g. `frantss/frantssuy`; kebab-case each component.
Allow one or two slash-separated segments matching `[a-z0-9]+(?:-[a-z0-9]+)*`; reject UUID-shaped IDs and unsafe path segments.
Without a repository, use a user-chosen slug. Clarify missing owners, multiple candidate repositories, or normalization/host collisions; never invent disambiguating suffixes.
Reuse readable IDs on retries/imports; legacy UUIDs require explicit old→new mapping and migration of references, keys, note paths, and history, preserving recovery mappings and report narratives.
Renaming, moving, and changing sources/backends preserve identity. A backend switch does not migrate its registry or other records automatically.
