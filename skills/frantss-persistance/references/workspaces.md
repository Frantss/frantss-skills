# Workspace resolution

Read `~/.frantss/workspaces.yaml` as data: `schema_version: 1` and a `workspaces` mapping keyed by readable ID; no backend access is required.
Each entry has `title`, `area: work|personal`, `repositories` (canonical remotes), `local_paths` (`{machine, path}`), and `sources`; absent optional lists read as empty without saving.
Reject unsupported versions, invalid IDs, duplicate keys, or malformed entries; missing/unreadable config is unresolved, not an empty registry or backend fallback.
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
Only explicit workspace creation registers an ID through setup after reconciling existing IDs, titles, and association matches; ordinary use never edits this file.
For repository-backed creation, derive `org/repo` from the selected repository's owner and name, e.g. `frantss/frantssuy`; kebab-case each component.
Allow one or two slash-separated segments matching `[a-z0-9]+(?:-[a-z0-9]+)*`; reject UUID-shaped IDs and unsafe path segments.
Without a repository, use a user-chosen slug. Clarify missing owners, multiple candidate repositories, or normalization/host collisions; never invent disambiguating suffixes.
Requested backend-to-config exports preserve readable IDs, reconcile conflicts, and verify local entries before separate cleanup; UUID conversion also migrates references/history explicitly.
Renaming, moving, and backend changes preserve registry IDs. Switching the backend does not move or rewrite this local registry or migrate workflow records automatically.
