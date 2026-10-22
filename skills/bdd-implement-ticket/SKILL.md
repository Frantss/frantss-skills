---
name: bdd-implement-ticket
description: "Implement or resume one accepted ticket against its linked behavioral specification. Behavior discovery, ticket drafting, standalone review, and whole-slice orchestration are separate work."
---

# Implement one ticket

Deliver the selected accepted ticket in code and native tests, with current evidence for every promised behavior. Keep ticket definitions compact.

## Bind the ticket and verify prerequisites

Read the ticket, its run slice, complete linked scenarios/Examples, source definitions, and relevant design decisions; ask only if the intended ticket is ambiguous.
Confirm the actual breakdown and applicable behavior/design are accepted; pending unrelated slices do not block an accepted ticket.
Verify delivery prerequisites in current code and test evidence, not just ready planning documents; mark the ticket blocked if a required prerequisite is incomplete or unverifiable.
Apply the Run record contract below before writing. Set stage to implementation, current_ticket to the selected ID, and its execution state to in_progress when prerequisites hold.
Return missing expected behavior to discovery/formulation and consequential design conflicts to design; handle routine implementation choices without reopening settled agreements.

## Establish native coverage and the baseline

Read repository instructions and existing test/build configuration; identify the implementation and test commands for this scope.
Reuse the agreed observable boundaries and project conventions; clarify only a consequential unresolved boundary, rather than requesting confirmation of accepted choices.
Map every assigned case and Examples row/group to meaningful native assertions, including outputs, state changes, and prohibited effects; test count need not match scenario count.
Use case IDs in native test names or metadata where practical.
Run existing relevant tests and inspect assertions to distinguish implemented behavior, missing coverage, and failures; a passing test only covers what it actually asserts.
For behavior already implemented correctly, retain adequate tests and passing evidence instead of manufacturing a failure. Preparatory tickets use their specified preservation/completion checks.
Keep expected results independent of the implementation, using agreed examples; exercise public interfaces and reserve substitutes for genuine external boundaries.

## Implement incrementally, test-first by default

Before edits, invalidate affected prior evidence, set its check results to `not_run`, and reopen affected `done` tickets; also apply this when changed agreements, design, or prerequisites are discovered.
Choose a behavior, add or strengthen its native test, and run it to observe failure for the intended behavioral reason before changing production code.
Resolve setup/import/tool errors before treating a failure as behavioral.
Implement enough to satisfy that behavior, rerun the focused checks, and repeat for the ticket's remaining cases; keep changes within its outcome and accepted design.
When test-first ordering is impractical, record a brief concrete reason in execution Evidence and use an exploratory/code-first step; the final coverage and verification bar remains unchanged.
Improve the code while keeping established checks passing; avoid coupling tests to private construction or broadening the behavioral contract to suit the implementation.
If tools or decisions block a check, record its actual result and continue independent permitted work.

## Verify and hand off

Run all assigned cases/Examples through native tests, ticket-specific verification, relevant prerequisite regressions, and required repository checks against the final code.
Review the diff for scope, design consistency, and assertions that distinguish a violation from success; fix defects before reporting completion.
Record each case/group's test selector or command and actual result in Behavior checks; use Cases None for non-scenario checks and distinguish failed, blocked, and unexecuted work.
Tie execution Evidence to the checked code, commands, and current limitations.
Mark done only when every assigned behavior and required check passes on current code; missing coverage, failed checks, and unresolved blockers keep the ticket unfinished.
Report the outcome, verification, and remaining blockers; stop at this ticket unless more work was authorized. Follow existing Git/publication authorization rather than treating completion as consent.

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
