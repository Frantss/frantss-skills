---
name: bbd-slice-work
description: "Slice accepted behavioral specifications into implementation tickets, or review an existing breakdown for granularity and dependencies. Behavior discovery, implementation, and publishing approved tickets alone do not activate it."
---

# Slice work into tickets

Deliver local implementation tickets that define their observable outcomes, specification cases, and verification. Publishing and implementation require separate authorization.

## Establish the supported scope

Read the selected slice, accepted specifications, relevant design decisions, and existing tickets; use supplied context without requiring other installed skills.
Inspect available code and tests to distinguish required work from already-satisfied behavior; cite evidence and qualify unverified claims.
Resolve unsettled behavior through discovery/formulation and consequential technical choices through design; continue independent work with agreed cases and name blocked behavior.
Before writing, apply the Run record contract below. Proceed with an explicit selected scope, its source cases, and identified blockers.

## Draft vertical slices

Use `S-*` for specification slices and stable `TK-001` ticket IDs. One specification slice can produce several delivery tickets.
Group scenarios that deliver one coherent outcome; one ticket can cover the entire selected scope.
Each vertical slice includes the relevant implementation layers and native tests, with an outcome verifiable after its prerequisites.
Size tickets by change scope, uncertainty, and verification effort; explain proposed splits using those factors.
List blocking ticket IDs under Dependencies, or `None`; add a brief reason only when the prerequisite is unclear. Keep ordering preferences separate.
Create preparatory/refactoring tickets only for concrete prerequisites: name the dependent tickets in the behavior row, use `None` for Cases, and require verifiable preservation checks under Verification.
For a wide mechanical change, use compatible expansion, bounded migration, and contraction steps.
Keep Overview to one sentence naming selected slices and source documents; record ticket-to-slice membership in run.md Members. Add already-satisfied case references/evidence only when needed.

## Define behavior and check coverage

Each Behavior row briefly names the implemented behavior and its `behavior.feature` case tags; the title states the outcome. Reuse source context instead of adding outcome, scope, slice, or design-reference fields.
Treat each linked case as its complete acceptance contract, including outputs, state changes, and prohibited effects; use short behavior summaries instead of repeating assertions.
Assign all Examples rows unless allocation identifies stable groups by case tag and Examples name/tag; each allocation must be verifiable after ticket prerequisites.
Default verification is all assigned cases and Examples through existing project tests. Add at most one sentence under Verification for non-obvious setup or extra regressions; omit the field otherwise.
Give each required case/group one accountable delivery ticket; optional Verification can reference regression cases or prerequisite tickets without transferring ownership.
When a case spans several changes, its owner completes the behavior and names earlier tickets as dependencies; those prerequisites still need their own completion checks.
Account for every selected case as assigned, already satisfied with evidence, or an explicit gap. Coverage gaps lists only in-scope gaps/exclusions and source references, or `None`; exclusions require source/user authority and other questions stay with their owners.
Before each user review, verify bounded outcomes, source references, unique ownership, coverage, verifiable acceptance criteria, and an acyclic dependency graph; repair defects or identify blockers.

## Obtain agreement on the breakdown

Save the draft, then present ticket IDs, outcomes, implemented behaviors/cases, and dependencies as a compact numbered breakdown.
Ask through an available feedback interface: "Does this breakdown fit how you want to work? Which tickets should we split further or group together?"
Recommend useful merges or splits with their trade-offs; apply answers only to addressed points and update affected allocations/dependencies before presenting the result again.
Keep the breakdown draft until the user explicitly accepts its actual ticket boundaries, behavior allocation, and dependencies; silence or agreement to the general approach leaves it draft.
An explicitly accepted usable subset may be partial with named blockers; unrelated pending slices do not block a complete selected slice.
Reuse explicit acceptance. Material changes to ticket boundaries, allocated behavior, or dependencies reopen affected portions and their readiness.
When source behavior or design changes, review affected tickets and downstream dependencies; return decisions to their owning stage and mark affected conclusions draft or blocked.

## Handoff

Set stage to slicing and tickets.md's per-slice review status in run.md. Readiness covers accepted ticket definitions; unfinished delivery prerequisites still block implementation.
Record completed review checks and their limits under run.md Validation, distinguishing specification review from executed implementation tests.
Link tickets.md and its specification/design sources; state ready work and blockers. Separately authorized implementation can start once its delivery prerequisites are complete.

## Run record contract

Use `.scratch/bdd/<run_id>/` for one feature across sessions/slices; on creation set stable YAML `feature_name`, lowercase kebab-case `feature_slug`, and `run_id: <feature_slug>-<NNN>`, choosing the next per-feature ordinal padded to at least three digits.
Resume the identified run by reading `run.md`; ask if ambiguous. Create another only for a different feature or an explicit new-run request.
Create exactly `run.md`, `problem.md`, `discovery.md`, `behavior.feature`, `design.md`, and `tickets.md`, even standalone; on resume, preserve contents and initialize only missing files/sections.
Use `<feature_name>: <document role>` Markdown titles and `Feature: <feature_name>`. Use `Pending` for unvisited content, `None` for empty lists, and only a pending comment beneath an unvisited Feature.
Keep current content only: replace changed definitions and remove obsolete entries and resolved questions. Keep no transcripts, histories, tombstones, or extra files/subfolders; preserve continuing IDs and repair affected references.
YAML `stage` is `framing`, `concept`, `discovery`, `formulation`, `design`, `slicing`, or `implementation`, identifying active work; `current_slice` names a stable `S-*` slice and `current_ticket` a selected `TK-*` ticket or `null`.
`run.md` uses exactly `Documents`, `Validation`, `Next action` as level-two sections, in order; keep latest checks/limits under Validation and the next step under Next action. Update affected records before asking the next round.
Under Documents, use `### <slice_id>: <name>` per current slice with `Scope`, `Members`, and `Dependencies` fields, then a `File | Status` table for the other five files.
Members lists explicit file-qualified IDs, such as `discovery.md:R-001`, including in-slice rules/examples; use `Pending` until known. Dependencies lists slice/question references or `None`; preserve other slices when focus changes.
Document statuses: `pending` = unvisited, `draft` = unaccepted work, `blocked` = an unresolved prerequisite prevents readiness, `ready` = accepted and unblocked, `partial` = explicitly accepted usable subset with named blockers.
Once execution is tracked, run.md Validation adds `### Implementation` with `Ticket | State | Evidence`: states are `pending`, `in_progress`, `blocked`, `done`; document readiness stays separate.
`### Behavior checks` uses `Ticket | Cases | Check | Result`: case/group IDs or `None` for non-scenario checks, test selectors/commands, and `passed`, `failed`, `blocked`, `not_run`; keep current evidence and invalidate affected results when inputs change.
Keep scope/blockers in slice fields; for partial, Scope names usable member IDs. Keep check results under Validation. Area-map statuses use the same values plus `excluded`, requiring source/user authority; area status covers its whole included scope.
`problem.md` uses exactly these level-two sections, in order: `Problem`, `Context and evidence`, `People`, `Goals and success criteria`, `Scope and constraints`, `Open questions`.
`discovery.md` uses exactly these ordered level-two sections `Boundary and vocabulary`, `Area map`, `Area details`, `Coverage gaps`, `Open questions`; map columns are `ID | Area | Status | Dependencies`, with `### <id>: <name>` details containing `Boundary`, `Rules`, `Examples` fields.
`design.md` uses exactly these level-two sections, in order: `Context`, `Approach`, `Structure`, `Decisions`, `Open questions`; Structure describes parts' purposes, boundaries, interfaces, and dependencies.
`behavior.feature` contains one named Feature, current scope description, Rule groups, tagged Given/When/Then scenarios, and Examples for outlines. Cross-check slice membership and references before handoff.
`tickets.md` uses exactly `Overview`, `Tickets`, `Coverage gaps` as level-two sections, in order. Each `### <TK-id>: <outcome>` has a one-sentence summary, bold `Dependencies`, then a `Behavior | Cases` table; add bold `Verification` only for essential setup or regressions absent from the cases.
