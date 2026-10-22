---
name: bbd-design-solution
description: "Choose a solution concept or refine its design against agreed needs and behavior. Use when comparing approaches or deciding responsibilities, interfaces, dependencies, and consequential trade-offs. Routine implementation, task scheduling, and behavioral specification alone do not activate it."
---

# Design a solution

Choose an approach to an established problem and explain how its responsibilities cooperate to satisfy agreed needs and behavior.
Support solution-concept selection and later design refinement. Implementation, delivery task breakdown, and behavioral specification are separate work.
Accept a problem brief, clear requirements, or an existing design; no other skill or particular document format is required.

## Establish the design context and record

Read supplied context, agreements, and project evidence; identify the outcome, scope, slice, constraints, known behavior, and intended design decision before proposing a direction.
Default to a small coherent slice with explicit dependencies; use the whole scope when small or tightly coupled, and reuse settled context.
If the problem itself is unclear, return focused framing questions rather than choosing an approach to an assumed need.
Use `.scratch/bdd/<run_id>/` for one feature across sessions and slices.
On creation, fix `feature_name`, lowercase kebab-case `feature_slug`, and `run_id: <feature_slug>-<NNN>` in `run.md` YAML; use the next per-feature ordinal, padded to at least three digits.
Resume the identified run by reading `run.md`; ask if ambiguous. Create another only for a different feature or an explicit new-run request.
Create exactly `run.md`, `problem.md`, `discovery.md`, `behavior.feature`, `design.md`, and `tickets.md`, even standalone; on resume, preserve contents and initialize only missing files/sections.
Use `<feature_name>: <document role>` Markdown titles and `Feature: <feature_name>`. Use `Pending` for unvisited content, `None` for empty lists, and only a pending comment beneath an unvisited Feature.
Keep current content only: replace changed definitions and remove obsolete entries and resolved questions. Keep no transcripts, histories, tombstones, or extra files/subfolders; preserve continuing IDs and repair affected references.
YAML `stage` is `framing`, `concept`, `discovery`, `formulation`, `design`, or `slicing`, identifying active work; `current_slice` names a stable slice ID such as `S-001`.
`run.md` uses exactly `Documents`, `Validation`, `Next action` as level-two sections, in order; keep latest checks/limits under Validation and the next step under Next action. Update affected records before asking the next round.
Under Documents, use `### <slice_id>: <name>` per current slice with `Scope`, `Members`, and `Dependencies` fields, then a `File | Status` table for the other five files.
Members lists explicit file-qualified IDs, such as `discovery.md:R-001`, including in-slice rules/examples; use `Pending` until known. Dependencies lists slice/question references or `None`; preserve other slices when focus changes.
Document statuses: `pending` = unvisited, `draft` = unaccepted work, `blocked` = an unresolved prerequisite prevents readiness, `ready` = accepted and unblocked, `partial` = explicitly accepted usable subset with named blockers.
Keep scope/blockers in slice fields; for partial, Scope names usable member IDs. Keep check results under Validation. Area-map statuses use the same values plus `excluded`, requiring source/user authority; area status covers its whole included scope.
`problem.md` uses exactly these level-two sections, in order: `Problem`, `Context and evidence`, `People`, `Goals and success criteria`, `Scope and constraints`, `Open questions`.
`discovery.md` uses exactly these level-two sections, in order: `Boundary and vocabulary`, `Area map`, `Area details`, `Coverage gaps`, `Open questions`.
Area map is an `ID | Area | Status | Dependencies` table; Area details uses `### <id>: <name>` with `Boundary`, `Rules`, `Examples` fields. Qualify cross-document IDs with their filename.
`design.md` uses exactly these level-two sections, in order: `Context`, `Approach`, `Structure`, `Decisions`, `Open questions`; Structure describes parts' purposes, boundaries, interfaces, and dependencies.
`behavior.feature` contains one named Feature, current scope description, Rule groups, tagged Given/When/Then scenarios, and Examples for outlines. Cross-check slice membership and references before handoff.
`tickets.md` uses exactly `Overview`, `Tickets`, `Coverage gaps` as level-two sections, in order. Each `### <TK-id>: <outcome>` has a one-sentence summary, bold `Dependencies`, then a `Behavior | Cases` table; add bold `Verification` only for essential setup or regressions absent from the cases.
Use stable IDs such as A-001 alternatives, P-001 parts, D-001 decisions, Q-001 questions; keep one authoritative entry per point.
Link current needs, constraints, and behavior by qualified ID or source location rather than copying specifications.

## Choose a solution concept when needed

If a direction is already agreed or fixed by the user, retain it unless relevant evidence challenges its suitability.
Otherwise compare credible approaches against the same goals and constraints, including reuse, nontechnical change, or no change when viable.
Recommend one approach and explain its main trade-offs and the consequences of the alternatives; explain when only one is credible.
Investigate feasibility through available code and documentation; distinguish evidence from assumptions and identify uncertainty that could change the choice.
Ask independent questions together using available feedback interfaces, with stable IDs and the decisions they affect.
Apply answers only to addressed points; keep choices proposed until the user chooses or accepts them.
Complete concept selection when its purpose, boundary, alternatives, rationale, and consequential uncertainty are reviewed and the direction is accepted.
When detailed behavior is unsettled, hand the accepted concept and behavioral questions to discovery; keep dependent design choices provisional.

## Refine the design against agreed behavior

Read the accepted behavioral context and specification where available; refinement can resume after discovery and formulation without repeating concept selection.
Identify which decisions the current behavioral contract supports and which are blocked by missing or conflicting requirements.
Map cooperating responsibilities for the current slice, including shared boundaries with pending areas, purposes, interfaces, and dependencies.
Keep parts at comparable depth and review their boundaries before developing one; retain an already accepted structure when it still fits.
Develop parts in dependency order or the user's priority, examining one part at a time and leaving unrelated parts pending.
Compare material alternatives within each part and record the selected design, rationale, and links to the needs or behavior it serves.
Use only the detail needed to resolve the intended design decisions; files, functions, and implementation tasks are not completion requirements.
Review consequential choices, assumptions, interfaces, and dependencies together where useful; reuse explicit agreement without adding redundant confirmation gates.
Check interactions by walking behavioral examples, constraints, and prohibited effects through the design; these are consistency checks, not proof of passing implementation tests.

## Route feedback to its owner

Changes to the problem, intended outcome, or scope return to framing; use a framing skill if available or ask the focused questions directly.
Missing or changed consumer-visible behavior returns to behavioral discovery; update its specification after the behavioral decision is agreed.
Use discovery/formulation skills when available; their absence does not authorize inventing behavior or changing an agreed contract.
Resolve technical alternatives within design. A cheaper or easier design is not authority to weaken agreed behavior.
When agreements change, check linked framing, discovery, specifications, designs, and tickets; update authorized records or identify required updates, marking affected conclusions draft or blocked.
Explicitly deferred decisions remain unresolved; name the design work they block while continuing independent work.

## Review and handoff

Review the current slice against its intended decision and shared boundaries: approach, rationale, scope, cooperating parts, and remaining uncertainty.
Account for all material source needs and constraints at the chosen design depth; identify behavior/design conflicts rather than hiding them as assumptions.
Mark refinement ready for the accepted slice when its consequential decisions and interactions support the next use; unrelated pending areas do not block it.
Link the design and its next use, including ticket slicing when requested; follow separately authorized work without claiming behavior is tested.
