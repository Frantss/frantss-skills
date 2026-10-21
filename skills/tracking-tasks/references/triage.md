# Triage

Read the inbox and existing workspaces. Clarify outcomes and workspace fit; preserve explicit user categorization.

Assign an existing workspace automatically when evidence clearly identifies it,
such as a named workspace or a unique configured source mapping. If several
workspaces fit, ask a focused question and leave the task in the inbox meanwhile.
If none fits, retain the task in the inbox and explain the gap.

An agent may suggest a new workspace. Mentioning a new name, approving a task,
or requesting assignment to a missing workspace is not a creation command.
On explicit creation, resolve the target workspace and reuse its `.frantss/workspace.yaml` UUID; ask for the workspace when unresolved.
Use `setup-frantss-skills` for identity setup when available; otherwise require a valid, Git-excluded profile. Never replace another workspace's identity.
Persist tracking data with that ID and resolved work/personal area; preserve supplied sources. Partial retries reuse the same ID.
