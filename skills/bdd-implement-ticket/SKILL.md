---
name: bdd-implement-ticket
description: "Implement or resume one accepted ticket against its linked behavioral requirements and verification. Accept an external ticket without a BDD run. Unsettled behavior, ticket drafting, standalone review, and whole-scope orchestration are separate tasks."
---

# Implement one ticket

Deliver the selected accepted ticket in code and native tests, with current evidence for its complete acceptance contract.

## Choose the working mode

Default to standalone: use the supplied ticket/specification and report implementation evidence in the reply or requested record. Selecting this skill does not enroll the task in a BDD run.
Track a run only when the user requests a tracked BDD workflow or the current task explicitly continues an identified run. A nearby run folder alone is insufficient. For tracked work, read [the run contract](references/run-record.md) and create only the records this stage needs.
Accept ticket requirements and cases from their existing source format. Gherkin, prior skills, and new planning documents are not implementation prerequisites.

## Verify the ticket and baseline

Read the full ticket, linked requirements/cases/Examples, relevant design, repository instructions, and tests. Ask only when the intended ticket or a consequential requirement is unresolved.
Reuse actual acceptance and authorization; do not reapprove settled choices. Verify delivery prerequisites in current code/test evidence, not merely accepted planning records.
For tracked work, set the selected ticket and active stage, and mark execution in_progress when prerequisites hold. Report blockers while completing independent permitted work.
Read test/build configuration and identify required checks. Map every promised case/example to native assertions for outputs, state changes, and prohibited effects; test count need not equal case count.
Run relevant existing tests and inspect their assertions. Already-correct behavior needs adequate passing evidence, not manufactured failures; preparatory work uses its preservation/completion checks.
Reuse agreed observable boundaries and project conventions. Use case IDs in native tests when practical, keep expected results independent of implementation, and substitute only genuine external boundaries.

## Implement incrementally

Before changes, invalidate affected prior evidence and reopen affected completed work; in tracked runs set affected check results to not_run.
Work test-first by default: strengthen one behavior's test, observe its intended failure, implement enough to satisfy it, and rerun focused checks before advancing.
Fix setup/import/tool failures before counting a failure as behavioral. When test-first ordering is impractical, record a concrete reason; final coverage requirements remain unchanged.
Improve code while keeping checks passing and changes within the ticket's accepted outcome/design. Do not weaken behavior or couple tests to private construction.
Resolve routine implementation choices directly. Ask consequential missing behavior/design questions without starting another stage's records; preserve fixed decisions and continue independent work.
If source agreements or prerequisites change, review affected code, tests, and existing references. Preserve unaffected acceptance and invalidate only affected evidence.

## Verify and deliver

Run all assigned behavior/examples, ticket-specific verification, relevant prerequisite regressions, and required repository checks against final code.
Review scope, design consistency, and assertions that distinguish violations from success; fix in-scope defects before reporting completion.
Record commands/test selectors, actual outcomes, checked code, blockers, and limitations. Distinguish failed, blocked, and unexecuted checks.
For tracked work, update execution Evidence and Behavior checks without enlarging ticket definitions. Planning acceptance and implementation completion remain separate.
Mark done only when every promised behavior and required check passes against current code. Missing coverage, failures, and unresolved blockers keep the ticket unfinished.
Report the result and evidence; stop at this ticket unless further work is authorized. Follow existing Git/publication authorization rather than inferring it from completion.
