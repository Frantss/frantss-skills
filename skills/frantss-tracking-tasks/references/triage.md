# Triage

Read selected tasks/Inbox, evidence, and the project registry; frantss's explicit categorization overrides inference.
Apply clear decisions automatically; unresolved outcome, ownership, commitment, timing, or project fit keeps Inbox with a focused question.

| State | Evidence |
| --- | --- |
| `inbox` | Captured, with a material triage question remaining |
| `next` | Committed work underway, explicitly near-term, assigned to frantss in the current sprint, or due/expected today or this week |
| `later` | Committed work that can wait; default for commitments without near-term evidence |
| `maybe` | Captured possibility without commitment; dates alone never establish commitment |
| `done` | frantss's report or evidence satisfies the entire outcome |

Keep Next small without quotas/order; approaching/overdue committed work supports Next, while conflicting timing requires clarification.
A sprint ticket supplies no invented date; a nonurgent physician appointment belongs in Later even undated.
Keep blocked commitments in Next/Later with a blocker/next actor when known; clear resolved blockers from evidence.
Assign named or uniquely source-mapped projects; unresolved fit stays in Inbox. A known project can coexist with Inbox; null project never defines it.
Retain a brief `triage_reason` with `evidence`/`source_urls`; reevaluate on new evidence/subsequent triage, preserving frantss's choices.
A suggested/missing project name or task acknowledgment is not creation; explicit creation uses `frantss-configure` when available, otherwise returns an unsaved request.
