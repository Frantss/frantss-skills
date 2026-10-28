---
name: implement-ticket
description: "Implement or resume one authorized ticket with clear behavioral requirements and verification. Accept an external ticket without a BDD run. Unsettled behavior, ticket drafting, standalone review, and whole-scope orchestration are separate tasks."
---

# Implement one ticket

- Deliver the selected authorized ticket in code and native tests, with current evidence for its complete behavioral requirements.

## Choose the working mode

- Use the supplied ticket and its source cases; Gherkin, earlier skills, and new planning documents are not prerequisites.
- For an explicitly requested tracked workflow or explicit continuation of an identified run, read [the run contract](references/run-record.md).

## Verify the ticket and baseline

- Read the full ticket, linked requirements/cases/Examples, design, repository instructions, and tests; ask only about unresolved ticket identity or consequential requirements.
- Reuse supplied requirements and existing authorization without new ticket acceptance; verify delivery prerequisites through current code and test evidence.
- Identify required checks from test/build configuration.
- Map every promised case/example to native assertions for outputs, state changes, and prohibited effects; test count need not match case count.
- Run relevant existing tests and inspect assertions; use adequate passing evidence for correct behavior and preservation/completion checks for preparatory work.
- Reuse agreed boundaries and project conventions; use case IDs when practical, expected results independent of implementation, and substitutes only at genuine external boundaries.

## Implement incrementally

- Default to test-first: strengthen one behavior test, observe its intended failure, implement enough to pass, and rerun focused checks before advancing.
- Fix setup/import/tool failures before counting behavioral failures; record a concrete reason for impractical test-first ordering without reducing final coverage.
- Improve code within agreed outcome/design while keeping checks passing; preserve required behavior and avoid tests coupled to private construction.
- Resolve routine choices directly; ask consequential unresolved behavior/design questions without starting another full workflow and continue independently supported work.
- Review affected code, tests, and references when source decisions or prerequisites change; preserve unaffected decisions.

## Verify and deliver

- Run all assigned behavior/examples, ticket-specific verification, relevant prerequisite regressions, and required repository checks against final code.
- Review scope, design consistency, and assertions that distinguish violations from success; fix in-scope defects before reporting completion.
- Record commands/test selectors, actual outcomes, checked code, blockers, and limitations; distinguish failed, blocked, and unexecuted checks.
- Mark done only when every promised behavior and required check passes on current code, with no missing coverage or unresolved blockers.
- Report results and evidence in the conversation or requested record; continue beyond the ticket or publish only when already authorized.
