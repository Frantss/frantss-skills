---
name: bbd-frame-problem
description: "Frame an unclear problem through a guided conversation about needs, evidence, intended outcomes, scope, and constraints. Use before choosing a solution or when the problem itself needs reframing. Routine implementation, detailed behavior discovery, and Gherkin conversion do not activate it."
---

# Frame a problem

Establish needs, affected people, outcomes, and scope in a problem brief; leave solution comparison, detailed behavior, and delivery planning to later work.
Accept existing context and agreements without requiring another skill or repeating settled discussions.

## Maintain the live problem brief

Read supplied material and relevant evidence before asking questions those sources can answer.
Use `.scratch/bdd/<run_id>/` for one feature across sessions and slices.
On creation, fix `feature_name`, lowercase kebab-case `feature_slug`, and `run_id: <feature_slug>-<NNN>` in `run.md` YAML; use the next per-feature ordinal, padded to at least three digits.
Resume the identified run by reading `run.md`; ask if ambiguous. Create another only for a different feature or an explicit new-run request.
Create exactly `run.md`, `problem.md`, `discovery.md`, `behavior.feature`, and `design.md`, even standalone; on resume, preserve contents and initialize only missing files/sections.
Use `<feature_name>: <document role>` Markdown titles and `Feature: <feature_name>`. Use `Pending` for unvisited content, `None` for empty lists, and only a pending comment beneath an unvisited Feature.
Keep current content only: replace changed definitions and remove obsolete entries and resolved questions. Keep no transcripts, histories, tombstones, or extra files/subfolders; preserve continuing IDs and repair affected references.
YAML `stage` is `framing`, `concept`, `discovery`, `formulation`, or `design`, identifying active work; `current_slice` names a stable slice ID such as `S-001`.
`run.md` uses exactly `Documents`, `Validation`, `Next action` as level-two sections, in order; keep latest checks/limits under Validation and the next step under Next action. Update affected records before asking the next round.
Under Documents, use `### <slice_id>: <name>` per current slice with `Scope`, `Members`, and `Dependencies` fields, then a `File | Status` table for the other four files.
Members lists explicit file-qualified IDs, such as `discovery.md:R-001`, including in-slice rules/examples; use `Pending` until known. Dependencies lists slice/question references or `None`; preserve other slices when focus changes.
Document statuses: `pending` = unvisited, `draft` = unaccepted work, `blocked` = an unresolved prerequisite prevents readiness, `ready` = accepted and unblocked, `partial` = explicitly accepted usable subset with named blockers.
Keep scope/blockers in slice fields; for partial, Scope names usable member IDs. Keep check results under Validation. Area-map statuses use the same values plus `excluded`, requiring source/user authority; area status covers its whole included scope.
`problem.md` uses exactly these level-two sections, in order: `Problem`, `Context and evidence`, `People`, `Goals and success criteria`, `Scope and constraints`, `Open questions`.
`discovery.md` uses exactly these level-two sections, in order: `Boundary and vocabulary`, `Area map`, `Area details`, `Coverage gaps`, `Open questions`.
Area map is an `ID | Area | Status | Dependencies` table; Area details uses `### <id>: <name>` with `Boundary`, `Rules`, `Examples` fields. Qualify cross-document IDs with their filename.
`design.md` uses exactly these level-two sections, in order: `Context`, `Approach`, `Structure`, `Decisions`, `Open questions`; Structure describes parts' purposes, boundaries, interfaces, and dependencies.
`behavior.feature` contains one named Feature, current scope description, Rule groups, tagged Given/When/Then scenarios, and Examples for outlines. Cross-check slice membership and references before handoff.
Keep the current focus and review status visible. Distinguish observed facts, reported claims, assumptions, proposals, and agreements.
Give substantive points stable IDs: CO-001 context, G-001 goals, CN-001 constraints, P-001 subproblems, Q-001 questions, D-001 decisions; keep one authoritative entry per point.
After answers, recompute unanswered questions; record conclusions, reasoning, and sources.
Show focused changes and link the brief instead of repeatedly presenting the full document.

## Establish the problem

Identify the current situation, what prompted the request, previous attempts, and evidence of the difficulty.
Establish who is affected and the consequences for them. Separate the problem from symptoms and suspected causes.
If the request names a solution, establish the need it serves and distinguish a suggestion from an explicitly fixed choice.
Preserve choices the user has already authorized; reopen them only when relevant evidence challenges their fit.
Existing arrangements are context, not automatic requirements. Identify which constraints are actual obligations and which are assumptions.
State the intended outcome and why it matters; distinguish goals from proposed features or technical construction.
Define how progress or success could be recognized, keeping unknown baselines or targets visibly unknown rather than inventing them.
Establish scope, dependencies, constraints, and next use; default to a small coherent slice unless the whole scope is small or tightly coupled.
Challenge unclear goals, unsupported causal claims, or a mismatch between the proposed solution and the stated need.
Proceed when the problem, affected people, outcome, scope, and consequential uncertainty can be stated without choosing a new solution.

## Clarify through a focused conversation

Summarize the current interpretation and identify uncertainties that could change the problem or its boundaries.
Investigate available facts through permitted sources; ask the user for missing facts and choices evidence cannot resolve.
Ask independent questions together using available feedback interfaces; leave dependent questions until their prerequisite answers are known.
Give each question its stable ID and explain what its answer will determine.
For a decision, recommend an answer with its reason and main trade-off; present credible alternatives when they exist.
Apply answers only to the points addressed. User agreement establishes acceptance; silence leaves other points open.

## Bound a broad problem when needed

If one problem contains distinct needs, propose outcome-focused subproblems and their relationships before expanding one.
Keep subproblems at comparable depth and review the map with the user; select a useful slice while other subproblems remain pending.
Use only the depth needed to clarify the problem. Behavior cases, technical modules, and implementation tasks belong to their respective later work.
Preserve behavior requirements that emerge, with their sources and agreement status, as inputs to behavioral discovery.
Keep early solution ideas and technical details as linked notes for solution design, rather than treating them as accepted directions.
When evidence changes agreements, check affected points and linked discovery, specifications, and designs; update authorized records or identify required updates, marking affected conclusions draft or blocked.

## Review and handoff

Review the current slice within the overall brief for a coherent problem statement, evidence, people, outcomes, scope, constraints, and uncertainty.
Account for each subproblem and open question; identify which unknowns block the intended next step and why.
Mark the slice ready when accepted and no unresolved question would materially change it for the next step; unrelated pending subproblems do not block it.
An explicitly accepted partial handoff identifies usable framing, deferred questions, and the decisions those questions still block.
Deferral leaves uncertainty unresolved; it does not establish a default or exclusion.
Link the brief and state its outcome and intended next use, preserving source IDs and evidence links.
An unknown solution concept can feed solution design; a known subject can feed behavioral discovery. Neither requires repeating accepted framing.
