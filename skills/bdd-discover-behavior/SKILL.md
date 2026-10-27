---
name: bdd-discover-behavior
description: "Clarify unresolved consumer-visible rules, examples, boundaries, or behavior decisions through conversation. Use when expected behavior needs agreement. Implementation, test execution, and converting already-settled rules to Gherkin do not require discovery."
---

# Discover behavior

Deliver agreed behavior definitions through examples and conversation. Accept supplied requirements and prior agreements without requiring earlier skills.

## Choose the working mode

Default to standalone: use the conversation and supplied sources; deliver rules, examples, and open decisions in the reply or the requested document. Selecting this skill does not enroll the task in a BDD run.
Track a run only when the user requests a tracked BDD workflow or the current task explicitly continues an identified run. A nearby run folder alone is insufficient. For tracked work, read [the run contract](references/run-record.md) and create only the records this stage needs.
Keep Gherkin, test integration, and implementation within separately requested scope. Address a blocking question directly without creating other stages' records.

## Establish the boundary

Read supplied context and project evidence before asking questions those sources answer. Code establishes current behavior, not automatic authority for expected behavior.
Establish the subject, outcome, consumer, observable boundary, vocabulary, and included or excluded scope. A consumer may be a person, API client, or calling code.
Map relevant behavior areas and dependencies before detailed cases. Resolve uncertainty preventing a useful map and review consequential scope choices with the user.
Select a coherent scope using dependencies and user priorities; use the whole subject when small or tightly coupled. Obtain agreement before changing scope.
Preserve stable source IDs when present; assign rule/example/area IDs when continued work needs traceability. Keep one authoritative definition per point.

## Explore rules and examples

Start with known rules or concrete examples. Challenge rules with examples and use proposed rules to explain examples; examples alone do not establish universal correctness.
Explore relevant input classes, boundaries, condition combinations, state changes, failures, retries, and timing. For stateful behavior, compare actions across states and sequences.
For each example, establish starting conditions, action/event, observable outcomes, side effects, prohibited effects, and meaningful terms, units, or time boundaries.
Distinguish agreed behavior, observations, assumptions, proposals, and unresolved questions. Recommend behavior with reasons and trade-offs while leaving it proposed until accepted.
Investigate available facts; ask about unresolved choices that affect expected behavior. Group independent questions and explain their impact; defer dependent questions.
Apply answers only to addressed points, update agreements, and recompute remaining questions. Silence and explicit deferral do not establish agreement, defaults, or exclusions.

## Review and deliver

Review each relevant area's rules, examples, vocabulary, exclusions, and gaps before expanding another area. Reuse explicit agreements rather than confirming every answer.
Check cross-area interactions, shared terms, contradictions, missing areas, and dependencies against the original outcome. Account for all included scope; exclusions require source or user authority.
When agreements change, update affected authorized definitions and existing links; preserve unaffected agreements and mark dependent conclusions unresolved until reviewed.
Deliver the complete supported definitions and consequential questions. A draft request is complete when this draft is delivered; acceptance governs readiness for dependent work.
For tracked work, update discovery and run status. An area's status covers its included scope; an accepted, unblocked slice may be ready while unrelated areas remain pending. Use partial only for explicitly accepted usable scope with named blockers.
State what is agreed and what remains open without claiming exhaustive coverage or tested behavior. Stop before unrequested formulation or implementation.
