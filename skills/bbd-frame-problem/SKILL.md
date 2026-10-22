---
name: bbd-frame-problem
description: "Frame an unclear problem through a guided conversation about needs, evidence, intended outcomes, scope, and constraints. Use before choosing a solution or when the problem itself needs reframing. Routine implementation, detailed behavior discovery, and Gherkin conversion do not activate it."
---

# Frame a problem

Establish what needs solving, for whom, why it matters, and what a useful outcome would be.
Apply to problems of any kind. Deliver a problem brief; solution comparison, detailed behavior, and delivery planning belong to later work.
Accept existing context and agreements without requiring another skill or repeating settled discussions.
Default to a small coherent slice of the problem; use the whole scope when it is small or its decisions are tightly coupled.

## Maintain the live problem brief

Read supplied material and relevant evidence before asking questions those sources can answer.
Use the workspace's `.scratch/bdd/<run_id>/` for one feature across sessions and slices.
On creation, fix `feature_name`, lowercase kebab-case `feature_slug`, and `run_id: <feature_slug>-<NNN>` in `run.md` YAML frontmatter; choose the next per-feature ordinal, padded to at least three digits.
Resume the identified run by reading `run.md`; ask if the run is ambiguous. Create another only for a different feature or an explicit new-run request.
Create exactly `run.md`, `problem.md`, `discovery.md`, `behavior.feature`, and `design.md` for a new run, even standalone. On resume, preserve existing contents and initialize only missing files.
`run.md` adds `stage` and `current_slice` to its YAML frontmatter and uses exactly `## Documents` (file/status), `## Validation` (latest checks and limits), and `## Next action`; update current state after substantive exchanges. Initialize every required section as pending when unvisited, with a Gherkin comment for pending formulation.
Use `<feature_name>: <document role>` Markdown titles and `Feature: <feature_name>`; keep names stable when solutions change.
Keep only current content in these five files. Replace changed text and remove obsolete entries and resolved questions; use `None` for empty current sections. Retain no transcripts, revisions, superseded entries, change logs, audit files, or extra files/subfolders.
Use these exact level-two sections in `problem.md`: `Problem`, `Context and evidence`, `People`, `Goals and success criteria`, `Scope and constraints`, `Open questions`.
Use these exact level-two sections in `discovery.md`: `Boundary and vocabulary`, `Area map`, `Area details`, `Coverage gaps`, `Open questions`; each area uses `### <id>: <name>` with `Boundary`, `Rules`, and `Examples` fields.
Use these exact level-two sections in `design.md`: `Context`, `Approach`, `Structure`, `Decisions`, `Open questions`; describe each part's purpose, boundary, interfaces, and dependencies under `Structure`.
`behavior.feature` contains one named `Feature`, a scope description, `Rule` groups, tagged scenarios with Given/When/Then outcomes, and `Examples` for outlines.
Keep the current focus and review status visible. Distinguish observed facts, reported claims, assumptions, proposals, and agreements.
Give substantive points stable IDs, such as CO-001 context, G-001 goals, CN-001 constraints, P-001 subproblems, Q-001 questions, D-001 decisions; preserve existing identities and one authoritative entry per point.
Preserve IDs of current points; update definitions and references in place, and remove obsolete entries without replacement logs.
After each substantive exchange, update relevant points before asking the next round; record reasoning and sources, not a transcript.
Show focused changes and link the brief instead of repeatedly presenting the full document.

## Establish the problem

Identify the current situation, what prompted the request, previous attempts, and evidence of the difficulty.
Establish who is affected and the consequences for them. Separate the problem from symptoms and suspected causes.
If the request names a solution, establish the need it serves and distinguish a suggestion from an explicitly fixed choice.
Preserve choices the user has already authorized; reopen them only when relevant evidence challenges their fit.
Existing arrangements are context, not automatic requirements. Identify which constraints are actual obligations and which are assumptions.
State the intended outcome and why it matters; distinguish goals from proposed features or technical construction.
Define how progress or success could be recognized, keeping unknown baselines or targets visibly unknown rather than inventing them.
Establish overall scope, the current slice and its dependencies, relevant constraints, and the intended next decision or activity.
Challenge unclear goals, unsupported causal claims, or a mismatch between the proposed solution and the stated need.
Proceed when the problem, affected people, outcome, scope, and consequential uncertainty can be stated without choosing a new solution.

## Clarify through a focused conversation

Summarize the current interpretation and identify uncertainties that could change the problem or its boundaries.
Investigate available facts through permitted sources; ask the user for missing facts and choices evidence cannot resolve.
Ask independent questions together using available feedback interfaces; leave dependent questions until their prerequisite answers are known.
Give each question its stable ID and explain what its answer will determine.
For a decision, recommend an answer with its reason and main trade-off; present credible alternatives when they exist.
Apply answers only to the points addressed. User agreement establishes acceptance; silence leaves other points open.
Update the brief and recompute the unanswered questions after each exchange.

## Bound a broad problem when needed

If one problem contains distinct needs, propose outcome-focused subproblems and their relationships before expanding one.
Keep subproblems at comparable depth and review the map with the user; select a useful slice while other subproblems remain pending.
Use only the depth needed to clarify the problem. Behavior cases, technical modules, and implementation tasks belong to their respective later work.
Preserve behavior requirements that emerge, with their sources and agreement status, as inputs to behavioral discovery.
Keep early solution ideas and technical details as linked notes for solution design, rather than treating them as accepted directions.
When evidence changes an agreed goal or boundary, review the affected points while preserving unaffected agreements.
Check linked discovery, specifications, and designs for affected conclusions; update authorized records or identify required updates, keeping affected conclusions pending review.

## Review and handoff

Review the current slice within the overall brief for a coherent problem statement, evidence, people, outcomes, scope, constraints, and uncertainty.
Account for each subproblem and open question; identify which unknowns block the intended next step and why.
Mark the slice ready when accepted and no unresolved question would materially change it for the next step; unrelated pending subproblems do not block it.
An explicitly accepted partial handoff identifies usable framing, deferred questions, and the decisions those questions still block.
Keep unaccepted drafts pending. Deferral leaves uncertainty unresolved; it does not establish a default or exclusion.
Link the brief and state its outcome and intended next use, preserving source IDs and evidence links.
An unknown solution concept can feed solution design; a known subject can feed behavioral discovery. Neither requires repeating accepted framing.
This handoff establishes the problem; it does not claim a selected solution, complete behavioral specification, or verified implementation.
