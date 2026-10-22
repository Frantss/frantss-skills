---
name: bbd-discover-behavior
description: "Discover expected behavior through a user-agent conversation before formulation. Use when clarifying consumer-visible rules, examples, boundaries, or unresolved behavior decisions. Ordinary implementation, test execution, and Gherkin conversion of settled requirements do not activate it."
---

# Discover behavior

Establish expected behavior from the consumer's perspective through concrete examples and an iterative conversation.
Produce an agreed record for later formulation without requiring another installed skill; Gherkin writing, test integration, and implementation belong to later work.

## Start and maintain the live record

Read supplied context and relevant project evidence before asking questions that those sources can answer.
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
Update the record after each substantive exchange, before asking the next round. Record conclusions and reasoning, not a transcript.
Distinguish agreed behavior, proposals, observations of existing code, assumptions, and unresolved questions; cite sources where available.
User acceptance determines agreement. Apply answers only to the points addressed; silence leaves other points unresolved.
Give substantive points stable IDs: CO context, A areas, R rules, E examples, T terms, Q questions, D decisions; use increasing numbers such as `R-001`, preserving an existing scheme.
Keep one authoritative entry per current ID; update definitions and references in place, preserving identities of continuing points and removing obsolete entries.
Show focused changes and link the record during the conversation rather than repeating the full document.

## Frame and map areas first

Establish the subject, intended outcome, consumer, observable boundary, domain terms, and included or excluded scope.
The consumer may be a person, API client, or calling code; preserve public interface details that affect their expectations.
Use code as evidence of current behavior, not automatic authority for expected behavior.
Before detailed cases, map consumer-visible areas and dependencies; record each area's purpose, boundary, scope, and status: pending, in discussion, agreed, partial, or excluded.
Resolve uncertainty that prevents a useful map through framing questions, then review the map with the user before exploring areas.
Select a small coherent slice across one or more areas, with dependencies explicit; use the whole scope when small or tightly coupled.
Keep other areas mapped and pending; accepted slices can enter formulation before those areas are explored.
Revise the map when evidence changes it; explain and obtain agreement on changed scope instead of silently expanding or dropping behavior.

## Discover one area at a time

Select an area using dependencies and the user's priorities. Keep unrelated areas pending.
Start with known rules or concrete examples. Propose examples to challenge rules and propose rules to explain examples.
Use relevant input classes, boundaries, condition combinations, state changes, failures, retries, and timing to expose missing decisions.
Capture general properties as rules with illustrative examples; examples alone do not establish universal correctness.
For stateful subjects, compare actions across observable states and state-crossing sequences; use a compact state/action table when helpful, with a formal model optional.
For each example, establish starting conditions, action/event, outcomes, meaningful side effects, prohibited effects, and consequential terms or time boundaries.
Recommend behavior when useful, explaining the reason and trade-off; keep it proposed until the user decides.
Identify uncertainties that affect expected behavior. Investigate available facts and ask the user about unresolved choices.
Ask independent questions together using available feedback interfaces, with stable IDs, affected areas, and the behavior each answer determines; defer dependent questions.
After each answer, update agreements and recompute the questions that can now be answered without guessing other decisions.

## Review each area

Review the area's rules, examples, vocabulary, exclusions, gaps, and questions for the current slice before moving to another area.
Incorporate corrections and obtain agreement on resolved behavior; avoid confirmation after every individual answer.
Track accepted behavior by slice; mark an entire area agreed only when its included behavior is accepted and unblocked.
Explicit user deferrals permit a partial area: identify the missing decisions, their effects, and which behavior remains ready.
Deferral leaves a question unresolved; it does not imply agreement, a default outcome, or exclusion from scope.
When agreements change, check linked framing, specifications, and designs; update authorized records or identify required updates, marking affected conclusions pending review.
Questions from formulation or design enter this loop under their source areas; keep unaffected current agreements and IDs without recording the conversation or change itself.

## Cross-area review and handoff

After the slice's area reviews, check interactions, shared terms, contradictions, missing areas, and dependencies on pending behavior against the original goal.
Return newly exposed decisions to their affected areas and repeat review as needed.
Account for every mapped area's status and deferred question; pending work remains in scope, and exclusions require source or user authority.
Present the complete slice for acceptance, with rules, examples, uncertainty, and its place in the overall map visible; reuse prior explicit agreements.
Mark the accepted slice ready for formulation when unblocked; unrelated pending areas do not block it or require a partial-handoff exception.
An explicitly accepted partial handoff names ready behavior and deferred decisions blocking other behavior within the selected slice.
Keep unaccepted records visibly pending; user-requested early handoffs retain unresolved questions and their effects.
Link the record and identify its outcome. Readiness covers the agreed scope and does not claim exhaustive coverage or tested behavior.
