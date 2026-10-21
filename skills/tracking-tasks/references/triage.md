# Triage

Read Inbox or selected tasks, supporting evidence, and `~/.frantss/workspaces.yaml`. Explicit user categorization takes precedence over inference.
Apply clear decisions automatically; otherwise retain Inbox and ask about the uncertain outcome, ownership, commitment, timing, or workspace fit.

| State | Evidence |
| --- | --- |
| `inbox` | Captured; a material triage question remains |
| `next` | Committed and underway, explicitly near-term, assigned to the user in the current sprint, or due/expected today or this week |
| `later` | Committed work that can wait; a clear commitment without near-term evidence defaults here |
| `maybe` | A captured possibility without a commitment; a date alone never establishes commitment |
| `done` | User report or evidence satisfies the entire intended outcome |

Keep Next small and actionable, without inventing an order or quota. Conflicting timing evidence requires clarification.
An assigned current-sprint Jira ticket supports Next, not an inferred deadline or expected date from the sprint end.
A nonurgent physician appointment belongs in Later even without a date; reports must still surface that commitment weekly.
Use [date rules](content.md); approaching or overdue committed work supports Next during triage, never an automatic promotion of Maybe.
Keep blocked commitments in Next/Later with `blocker` naming the dependency and next actor when known; clear resolved blockers from evidence.
Assign an existing workspace when named or uniquely supported by configured source mappings; unresolved fit keeps Inbox without creating a workspace.
Workspace assignment and state are independent: a known workspace can coexist with Inbox; a null workspace alone never defines Inbox.
Record a brief `triage_reason` with supporting `evidence` IDs or `source_urls`; reevaluate on new evidence or subsequent triage, preserving user choices.

Suggest workspaces when useful; mentioning a name, approving a task, or requesting a missing workspace is not a creation command.
On explicit creation, resolve title and area; check registry IDs/associations, then use kebab-case `org/repo` (e.g. `frantss/frantssuy`) or a chosen slug without a repository.
Use `configure-frantss-skills` for local registration when available; otherwise return an unsaved configuration request, never a backend workspace record.
Save only requested associations/sources in the local registry; preserve existing fields. Resolve ID collisions first; renames and retries retain the ID.
