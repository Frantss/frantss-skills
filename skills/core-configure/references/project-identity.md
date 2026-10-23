# Project registry and resolution
Use filesystem tools on `~/.frantss/projects.yaml`: `schema_version: 1` and `projects` keyed by readable IDs; projects may be ongoing or bounded; no database access is required.
Entries require `title` and `area: work|side-projects|personal` (`side-projects`: independent projects; `personal`: real-world matters); optional lists `local_paths` and `sources` read as empty without saving defaults.
Reject unsupported versions, malformed entries, duplicate keys/IDs, and missing required fields; missing/unreadable configuration is unresolved.
Resolve explicit ID or exact unique title first; an unresolved explicit selection never falls back to the checkout.
Only for current-context requests, inspect the current Git root/all remotes; match repository locations from [sources](sources.md), including canonical Git common directories for local sources, otherwise an exact machine-scoped canonical root. Multiple project matches require clarification.
For non-Git folders use the supplied root/current directory. Match no ancestors; nested repositories resolve independently, and worktrees may share identity.
Use `host[:port]/repository-path` remotes: normalize SSH/scp/HTTPS, lowercase host, preserve path case/nondefault port, and strip credentials/query/fragment/trailing slash/terminal `.git`.
Resolve SSH aliases; ambiguous equivalence requires clarification. File/local remotes use path bindings, not invented host identities.
Path entries are `{machine, path}` with absolute resolved roots and a stable device identifier; unavailable identity requires clarification or skipping path matching.
Paths never match another machine or ancestors; a shared hostname alone cannot establish device identity.
A failed lookup never creates a project. Reads are read-only; discovery alone never changes registrations or associations.
Only explicit creation registers a new ID: kebab-case owner/repository such as `frantss/frantssuy`, or a slug chosen by frantss without a repository.
Allow one/two slash-separated `[a-z0-9]+(?:-[a-z0-9]+)*` segments, excluding UUIDs; clarify owner/normalization/host collisions without invented suffixes.
Explicit creation may initialize a missing version-1 empty registry; default new optional lists to empty. Renames, moves, and retries retain IDs.
Patch only established associations/sources; preserve human edits/unknown fields. Recheck original content, use exclusive creation/atomic replacement, and read back.
Stop after a repeated conflict/access failure with unsaved inputs. Database selection leaves this registry unchanged.
