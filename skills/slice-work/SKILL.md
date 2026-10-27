---
name: slice-work
description: "Draft or review implementation tickets from agreed behavioral specifications, checking scope, granularity, coverage, and dependencies. Accept supplied specifications without an existing BDD run. Behavior discovery, implementation, and publishing tickets alone are separate tasks."
---

# Slice work into tickets

Deliver compact implementation tickets with observable outcomes, source behavior, and verification. Publishing and implementation need their own authorization.

## Choose the working mode

Default to standalone: use supplied sources and deliver the breakdown in the reply or the requested document. Selecting this skill does not enroll the task in a BDD run.
Track a run only when the user requests a tracked BDD workflow or the current task explicitly continues an identified run. A nearby run folder alone is insufficient. For tracked work, read [the run contract](references/run-record.md) and create only the records this stage needs.
Accept agreed behavioral specifications and relevant design directly, including source cases outside Gherkin. Clarify blocking behavior/design choices without creating earlier stages' records.

## Establish supported scope

Read the selected scope, specifications, design decisions, existing tickets, code, and tests. Distinguish required work from already-satisfied behavior with evidence and qualified verification claims.
Identify agreed behavior, source cases/examples, dependencies, and consequential blockers. Keep independently supported work moving and preserve existing source identities.

## Draft verifiable outcomes

Give tickets stable IDs such as TK-001. Group behavior into coherent outcomes across the necessary implementation layers and native tests; one ticket may cover the selected scope.
Size tickets by change scope, uncertainty, and verification effort. Explain meaningful splits and separate genuine prerequisites from ordering preferences.
For wide mechanical changes, consider compatible expansion, bounded migration, and contraction. Preparatory/refactoring tickets must justify concrete dependent work and independently verifiable preservation checks.
Each ticket has an outcome title, one-sentence context, blocking Dependencies or None, and concise behavior/source-case mappings. Add extra Verification only for non-obvious setup or regressions.
Reference complete acceptance cases, including outputs, state changes, and prohibited effects, instead of copying their assertions into tickets.
Assign all relevant Examples rows, or identify stable groups. A ticket must be verifiable after its prerequisites; give each required case/group one accountable delivery owner.
When behavior spans changes, its completing ticket owns the cases and names prerequisites; prerequisite tickets still need their own checks. Regression references do not transfer ownership.
Account for every selected case as assigned, already satisfied with evidence, or an explicit gap. Preserve authorized exclusions and keep other unresolved choices with their source definitions.
Verify bounded outcomes, source resolution, unique ownership, meaningful completion checks, and an acyclic dependency graph before presenting the draft.

## Deliver and review the breakdown

Deliver a compact breakdown of IDs, outcomes, source behaviors/cases, and dependencies. A draft request is complete when the supported proposal and gaps are delivered.
When acceptance or dependent work is requested, ask whether boundaries should be split or grouped. Recommend changes with trade-offs and apply answers only to addressed portions.
Keep definitions draft until the user accepts the actual boundaries, behavior allocation, and dependencies; general agreement or silence does not establish that acceptance.
Reuse explicit acceptance. Material allocation/boundary/dependency changes reopen affected portions while preserving unaffected agreements; revisit downstream dependencies when sources change.
For tracked work, update tickets and run status. Mark accepted, unblocked definitions ready; delivery prerequisites separately govern when implementation may start.
An explicitly accepted usable subset may be partial with named blockers; unrelated pending scope does not block the selected scope. Report review checks without claiming executed implementation tests.
Link supplied or requested artifacts when present. Stop before unrequested publication or implementation, or continue when that work is already authorized.
