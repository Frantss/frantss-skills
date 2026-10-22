---
name: frantss-design-solution
description: "Choose a solution concept or refine its design against agreed needs and behavior. Use when comparing approaches or deciding responsibilities, interfaces, dependencies, and consequential trade-offs. Routine implementation, task scheduling, and behavioral specification alone do not activate it."
---

# Design a solution

Choose an approach to an established problem and explain how its responsibilities cooperate to satisfy agreed needs and behavior.
Support solution-concept selection and later design refinement. Implementation, delivery task breakdown, and behavioral specification are separate work.
Accept a problem brief, clear requirements, or an existing design; no other skill or particular document format is required.

## Establish the design context and record

Read supplied context, existing agreements, and relevant project evidence before proposing a direction.
Identify the intended outcome, overall scope, current slice, constraints, known behavior, and the decision this design must support.
Default to a small coherent slice with explicit dependencies; use the whole scope when small or tightly coupled, and reuse settled context.
If the problem itself is unclear, return focused framing questions rather than choosing an approach to an assumed need.
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
Keep the active focus and whether this is concept selection or refinement visible; distinguish proposed and agreed current decisions.
Use stable IDs such as A-001 alternatives, P-001 parts, D-001 decisions, Q-001 questions; keep one current entry per point, updating definitions and references in place and removing obsolete entries.
Link current needs, constraints, and behavior by ID or source location rather than copying specifications; update relevant sections before the next questions and link the file.

## Choose a solution concept when needed

If a direction is already agreed or fixed by the user, retain it unless relevant evidence challenges its suitability.
Otherwise compare credible approaches against the same goals and constraints, including reuse, nontechnical change, or no change when viable.
Recommend one approach and explain its main trade-offs and the consequences of the alternatives; explain when only one is credible.
Distinguish evidence from assumptions and identify unknowns that could change the choice. Avoid forcing a fixed number of alternatives.
Use available code and documentation to investigate feasibility; keep unsupported feasibility claims visibly uncertain.
Ask independent questions together using available feedback interfaces, with stable IDs and the decisions they affect.
Apply answers only to addressed points; keep proposals pending until the user chooses or accepts them.
Complete concept selection when its purpose, boundary, alternatives, rationale, and consequential uncertainty are reviewed and the direction is accepted.
When detailed behavior is unsettled, hand the accepted concept and behavioral questions to discovery; keep dependent design choices provisional.

## Refine the design against agreed behavior

Read the accepted behavioral context and specification where available; refinement can resume after discovery and formulation without repeating concept selection.
Identify which decisions the current behavioral contract supports and which are blocked by missing or conflicting requirements.
Map cooperating responsibilities for the current slice, including shared boundaries with pending areas, purposes, interfaces, and dependencies.
Use technical modules, data/state models, or interaction flows only where they clarify consequential design decisions.
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
When agreements change, check linked framing, discovery, specifications, and designs; update authorized records or identify required updates, marking affected conclusions pending review.
Explicitly deferred decisions remain unresolved; name the design work they block while continuing independent work.

## Review and handoff

Review the current slice against its intended decision and shared boundaries: approach, rationale, scope, cooperating parts, and remaining uncertainty.
Account for all material source needs and constraints at the chosen design depth; identify behavior/design conflicts rather than hiding them as assumptions.
Mark a concept ready for discovery when the user accepts its direction and no unresolved choice blocks specifying that concept's behavior.
Mark refinement ready for the accepted slice when its consequential decisions and interactions support the next use; unrelated pending areas do not block it.
An explicitly accepted partial handoff separates supported decisions from deferred questions and names their effects.
Keep unaccepted drafts pending. Link the design and its source context, decisions, alternatives, and follow-ups.
State what the record supports next without starting implementation or claiming behavior is tested; follow any separately authorized next-stage work.
