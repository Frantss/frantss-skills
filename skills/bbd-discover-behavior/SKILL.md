---
name: bbd-discover-behavior
description: "Discover expected behavior through a user-agent conversation before formulation. Use when clarifying consumer-visible rules, examples, boundaries, or unresolved behavior decisions. Ordinary implementation, test execution, and Gherkin conversion of settled requirements do not activate it."
---

# Discover behavior

Discover consumer-visible behavior through examples and conversation; deliver agreed definitions for formulation without requiring other skills. Gherkin, test integration, and implementation belong to later work.

## Start and maintain the live record

Read supplied context and relevant project evidence before asking questions that those sources can answer.
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
Distinguish agreed behavior, proposals, observations of existing code, assumptions, and unresolved questions; cite sources where available.
User acceptance determines agreement. Apply answers only to the points addressed; silence leaves other points unresolved.
Give substantive points stable IDs: CO context, A areas, R rules, E examples, T terms, Q questions, D decisions; use increasing numbers such as `R-001`, preserving existing schemes and one authoritative entry per point.
Show focused changes and link the record during the conversation rather than repeating the full document.

## Frame and map areas first

Establish the subject, intended outcome, consumer, observable boundary, domain terms, and included or excluded scope.
The consumer may be a person, API client, or calling code; preserve public interface details that affect their expectations.
Use code as evidence of current behavior, not automatic authority for expected behavior.
Before detailed cases, map consumer-visible areas and dependencies; record each area's purpose, boundary, scope, and status using the area-map vocabulary.
Resolve uncertainty that prevents a useful map through framing questions, then review the map with the user before exploring areas.
Select a small coherent slice using dependencies and the user's priorities; use the whole scope when small or tightly coupled.
Revise the map when evidence changes it; explain and obtain agreement on changed scope instead of silently expanding or dropping behavior.

## Discover one area at a time

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
Track accepted behavior by slice; mark an entire area ready only when its included behavior is accepted and unblocked.
Explicit user deferrals permit a partial area: identify the missing decisions, their effects, and which behavior remains ready.
Deferral leaves a question unresolved; it does not imply agreement, a default outcome, or exclusion from scope.
When agreements change, check linked framing, specifications, and designs; update authorized records or identify required updates, marking affected conclusions draft or blocked.
Questions from formulation or design enter this loop under their source areas; keep unaffected current agreements and IDs without recording the conversation or change itself.

## Cross-area review and handoff

After the slice's area reviews, check interactions, shared terms, contradictions, missing areas, and dependencies on pending behavior against the original goal.
Return newly exposed decisions to their affected areas and repeat review as needed.
Account for every mapped area's status and deferred question; pending work remains in scope, and exclusions require source or user authority.
Present the complete slice for acceptance, with rules, examples, uncertainty, and its place in the overall map visible; reuse prior explicit agreements.
Mark the accepted slice ready for formulation when unblocked; unrelated pending areas do not block it or require a partial-handoff exception.
User-requested early handoffs retain unresolved questions and their effects.
Link the record and identify its outcome. Readiness covers the agreed scope and does not claim exhaustive coverage or tested behavior.
