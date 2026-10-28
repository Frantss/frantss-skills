---
name: slice-work
description: "Draft or review implementation tickets from agreed behavioral specifications, checking scope, granularity, coverage, and dependencies. Accept supplied specifications without an existing BDD run. Behavior discovery, implementation, and publishing tickets alone are separate tasks."
---

# Slice work into tickets

- Deliver compact implementation tickets with observable outcomes, source behavior, and verification.

## Choose the working mode

- Use supplied behavioral specifications and relevant design, including cases outside Gherkin; earlier skills are not prerequisites.
- For an explicitly requested tracked workflow or explicit continuation of an identified run, read [the run contract](references/run-record.md).

## Establish supported scope

- Read scope, specifications, design, tickets, code, and tests; distinguish required work from already-satisfied behavior using evidence and qualified verification claims.
- Identify agreed behavior, source cases/examples, dependencies, and consequential blockers; preserve source identities and continue independently supported work.

## Draft verifiable outcomes

- Give tickets stable IDs such as TK-001 and group behavior into coherent outcomes across implementation layers and native tests; one ticket may cover all selected scope.
- Size tickets by change scope, uncertainty, and verification effort; explain meaningful splits and separate prerequisites from ordering preferences.
- For wide mechanical changes, consider compatible expansion, bounded migration, and contraction; justify preparatory/refactoring tickets with concrete dependent work and independently verifiable preservation checks.
- Give each ticket an outcome title, context sentence, blocking Dependencies or None, and behavior/case mappings; add Verification only for non-obvious setup or regressions.
- Reference complete acceptance cases, including outputs, state changes, and prohibited effects, instead of copying their assertions into tickets.
- Assign all relevant Examples rows or stable groups; make each ticket verifiable after prerequisites and give each required case/group one accountable delivery owner.
- Assign spanning behavior to its completing ticket with named prerequisites; give prerequisites their own checks and keep regression references separate from ownership.
- Account for every selected case as assigned, already satisfied with evidence, or a gap; retain authorized exclusions and unresolved choices with their source definitions.
- Verify bounded outcomes, source resolution, unique ownership, meaningful completion checks, and an acyclic dependency graph before presenting the draft.

## Deliver the breakdown

- Deliver IDs, outcomes, source cases, dependencies, and gaps in the conversation or requested document to complete a draft request.
- Choose routine boundaries and ordering within agreed scope; seek consequential scope, ownership, delivery, or dependency decisions and review grouping when requested.
- Review affected allocations and dependencies when sources or decisions change; preserve unaffected decisions and block only tickets dependent on unresolved choices.
- Continue authorized publication or implementation without separate approval of routine allocation; verify delivery prerequisites in current code before implementation.
- Report planning checks without claiming executed implementation tests.
