---
name: bbd-formulate-behavior
description: "Formulate or review Gherkin specifications from agreed behavioral context, including discovery records. Use when turning requirements into consumer-visible scenarios. Ordinary test implementation, test execution, and open-ended behavior discovery do not activate it."
---

# Formulate behavior

Turn agreed behavior into Gherkin for the project's existing test tools; accept discovery records or clear requirements without requiring other skills.
Deliver a source-linked specification and track readiness in `run.md`; test integration and production changes belong to later work.

## Establish the source

Read the supplied context and relevant existing specifications before drafting or revising.
Identify the subject, consumer, boundary, terms, sources, and dependencies; select a small coherent agreed slice, or the whole scope when small or tightly coupled.
Distinguish agreed requirements from proposals, observations of current code, and deferred decisions.
If sources conflict, identify the affected behavior and obtain a decision rather than choose silently.

## Draft the supported specification

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
Use independently understandable scenarios with relevant starting conditions, an action or event, and observable outcomes.
Preserve meaningful interface details, units, time boundaries, side effects, and effects that must not occur.
Use consistent domain terms; keep test setup mechanics and internal implementation choices in later test code.
Use `Scenario Outline` and `Examples` for the same behavior with different data; distinguish different behaviors explicitly.
Give current scenarios stable, unique tags such as `@case-001`; update cases in place and remove obsolete scenarios without retaining retired entries.
Put `@source-<id>` tags such as `@source-R-001 @source-E-001` on scenarios, resolving to current discovery definitions; preserve source IDs/citations or record supplied agreed definitions there without another discovery conversation.

Add cases when agreed context clearly determines their expected outcomes. Confidence must come from that context.
Explore relevant input classes, boundaries, condition combinations, state changes, failures, retries, and timing.
If integers 1 through 5 succeed and other integers are rejected without changes, derive 0, 1, 5, and 6; decimal handling remains undecided.
Outline rows inherit scenario sources; split differing row sources into tagged `Examples` blocks. Mark derived cases or example groups `@derived`; deduplicate while retaining their source tags.

## Return uncertainty to discovery

For each uncertain case, record its source area, the exact missing decision, and the scenarios it blocks.
Use a stable question ID and preserve whether the user has explicitly deferred it.
Reopen the affected discovery area with these questions; use the discovery skill if available, otherwise ask directly.
Keep unaffected agreements and continue independent formulation work.
When a question is resolved, incorporate the answer into current discovery definitions and scenarios, then remove the resolved question; source tags must point to current definitions.
When source agreements change, check linked scenarios, design decisions, and tickets; update authorized records or identify required updates, marking affected conclusions draft or blocked.
A deferred decision remains unresolved; it does not imply a default outcome or exclusion from scope.

## Review the complete draft

Present the complete supported draft for the selected slice, rather than requiring approval area by area; reuse prior explicit agreements.
Check fidelity to agreed behavior, concrete outcomes, consistent terms, duplicates, and interactions across areas.
For each scenario, check assertions for relevant outputs, observable state changes, and prohibited effects promised by its sources.
Count a promise as covered only when a scenario distinguishes correct behavior from a violation; source links alone establish provenance.
Account for every in-slice rule/example as represented, blocked, or excluded by source/user authority; check cross-slice interactions and report gaps without claiming exhaustive coverage.
Use an available Gherkin parser or report manual syntax review only; parsing checks syntax, fidelity requires review, and passing system tests requires execution.
Apply editorial corrections directly. Return changes to expected behavior to the affected discovery area.
Retain the full draft while resolving feedback; obtain acceptance of the complete supported slice before marking it ready.

## Handoff

Link `behavior.feature` and its current `discovery.md` definitions; set the current specification review state and validation results in `run.md`.
Mark an accepted slice ready when unblocked; unrelated pending work does not make it partial. An explicitly accepted partial handoff names ready and blocked behavior within its slice.
The handoff guides the project's existing testing approach; no particular runner or framework is required.
