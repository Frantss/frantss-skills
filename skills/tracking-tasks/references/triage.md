# Triage

Read the backend inbox and `~/.frantss/workspaces.yaml` registry. Clarify outcomes and workspace fit; preserve explicit user categorization.

Assign an existing workspace automatically when evidence clearly identifies it,
such as a named workspace or a unique configured source mapping. If several
workspaces fit, ask a focused question and leave the task in the inbox meanwhile.
If none fits, retain the task in the inbox and explain the gap.

An agent may suggest a new workspace. Mentioning a new name, approving a task,
or requesting assignment to a missing workspace is not a creation command.
On explicit creation, resolve title and area; check registry IDs/associations, then use kebab-case `org/repo` (e.g. `frantss/frantssuy`) or a chosen slug without a repository.
Use `setup-frantss-skills` for local registration when available; otherwise return an unsaved configuration request, never a backend workspace record.
Save only requested associations/sources in the local registry; preserve existing fields. Resolve ID collisions first; renames and retries retain the ID.
