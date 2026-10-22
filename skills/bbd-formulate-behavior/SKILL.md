---
name: bbd-formulate-behavior
description: "Formulate or review Gherkin specifications from agreed behavioral context, including discovery records. Use when turning requirements into consumer-visible scenarios. Ordinary test implementation, test execution, and open-ended behavior discovery do not activate it."
---

# Formulate behavior

Turn agreed behavior into Gherkin for the project's existing test tools; accept discovery records or clear requirements without requiring other skills.
Deliver a source-linked specification and track readiness in `run.md`; test integration and production changes belong to later work.

## Establish the source

Read the supplied context and relevant existing specifications before drafting or revising.
Identify the subject, consumer, observable boundary, scope, domain terms, and authoritative sources.
Select a small coherent slice of agreed behavior and its dependencies; use the whole scope when small or tightly coupled.
Keep other behavior visibly pending; formulate an accepted slice without waiting for discovery of unrelated areas.
Distinguish agreed requirements from proposals, observations of current code, and deferred decisions.
If sources conflict, identify the affected behavior and obtain a decision rather than choose silently.
Proceed when supported behavior and behavior blocked by unresolved decisions are distinguishable.

## Draft the supported specification

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
Use independently understandable scenarios with relevant starting conditions, an action or event, and observable outcomes.
Preserve meaningful interface details, units, time boundaries, side effects, and effects that must not occur.
Use consistent domain terms; keep test setup mechanics and internal implementation choices in later test code.
Use `Scenario Outline` and `Examples` for the same behavior with different data; distinguish different behaviors explicitly.
Use `Background` only for shared context that remains easy to understand without relying on another scenario.
Give current scenarios stable, unique tags such as `@case-001`; update cases in place and remove obsolete scenarios without retaining retired entries.
Put `@source-<id>` tags such as `@source-R-001 @source-E-001` on scenarios, resolving to current discovery definitions; preserve source IDs/citations or record supplied agreed definitions there without another discovery conversation.

Add cases when agreed context clearly determines their expected outcomes. Confidence must come from that context.
Explore relevant input classes, boundaries, condition combinations, state changes, failures, retries, and timing.
If integers 1 through 5 succeed and other integers are rejected without changes, derive 0, 1, 5, and 6; decimal handling remains undecided.
Outline rows inherit scenario sources; split differing row sources into tagged `Examples` blocks. Mark derived cases or example groups `@derived`; deduplicate while retaining their source tags.
Finish when every in-scope rule/example is represented, blocked, or excluded by source/user authority; report other missing coverage as current gaps.

## Return uncertainty to discovery

For each uncertain case, record its source area, the exact missing decision, and the scenarios it blocks.
Use a stable question ID and preserve whether the user has explicitly deferred it.
Reopen the affected discovery area with these questions; use the discovery skill if available, otherwise ask directly.
Keep unaffected agreements and continue independent formulation work.
When a question is resolved, incorporate the answer into current discovery definitions and scenarios, then remove the resolved question; source tags must point to current definitions.
When source agreements change, check linked scenarios and design decisions; update authorized records or identify required updates, marking affected conclusions pending review.
A deferred decision remains unresolved; it does not imply a default outcome or exclusion from scope.

## Review the complete draft

Present the complete supported draft for the selected slice, rather than requiring approval area by area; reuse prior explicit agreements.
Check fidelity to agreed behavior, concrete outcomes, consistent terms, duplicates, and interactions across areas.
For each scenario, check assertions for relevant outputs, observable state changes, and prohibited effects promised by its sources.
Count a promise as covered only when a scenario distinguishes correct behavior from a violation; source links alone establish provenance.
Account for every source rule and example in the slice; check cross-slice interactions and report gaps without claiming exhaustive coverage.
Use an available Gherkin parser or report manual syntax review only; parsing checks syntax, fidelity requires review, and passing system tests requires execution.
Apply editorial corrections directly. Return changes to expected behavior to the affected discovery area.
Retain the full draft while resolving feedback; obtain acceptance of the complete supported slice before marking it ready.

## Handoff

Link `behavior.feature` and its current `discovery.md` definitions; set the current specification review state and validation results in `run.md`.
Keep source mappings and derivation tags beside cases; keep gaps, exclusions, and unresolved/deferred questions with their discovery areas. Add no separate mapping document.
Mark an accepted slice ready when unblocked; unrelated pending work does not make it partial. An explicitly accepted partial handoff names ready and blocked behavior within its slice.
Keep review-pending drafts visibly pending. Distinguish syntax review, parser results, and behavior not yet tested.
The handoff guides the project's existing testing approach; no particular runner or framework is required.
