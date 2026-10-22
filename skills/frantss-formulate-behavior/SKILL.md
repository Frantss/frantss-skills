---
name: frantss-formulate-behavior
description: "Formulate or review Gherkin specifications from agreed behavioral context, including discovery records. Use when turning requirements into consumer-visible scenarios. Ordinary test implementation, test execution, and open-ended behavior discovery do not activate it."
---

# Formulate behavior

Turn agreed behavior into a Gherkin specification for implementation with the project's existing test tools.
Accept a discovery record or another clear requirements source; this skill works independently of other skills.
Deliver the specification and its handoff record. Test integration and production changes belong to later work.

## Establish the source

Read the supplied context and relevant existing specifications before drafting or revising.
Identify the subject, consumer, observable boundary, scope, domain terms, and authoritative sources.
Distinguish agreed requirements from proposals, observations of current code, and deferred decisions.
If sources conflict, identify the affected behavior and obtain a decision rather than choose silently.
Proceed when supported behavior and behavior blocked by unresolved decisions are distinguishable.

## Draft the supported specification

Use the requested destination or project convention; otherwise use an unused `specs/<subject>/` directory.
Keep Gherkin in `.feature` files and traceability, questions, and coverage in `formulation.md` beside them.
Update existing artifacts in place when revising; preserve unrelated specifications and stable identities.
Group coherent capabilities into features and their behavioral rules into `Rule` sections.
Use independently understandable scenarios with relevant starting conditions, an action or event, and observable outcomes.
Preserve meaningful interface details, units, time boundaries, side effects, and effects that must not occur.
Use consistent domain terms; keep test setup mechanics and internal implementation choices in later test code.
Use `Scenario Outline` and `Examples` for the same behavior with different data; distinguish different behaviors explicitly.
Use `Background` only for shared context that remains easy to understand without relying on another scenario.
Give scenarios stable tags such as `@case-001`, unique within this specification; retain tags and never reuse retired identities.
Map each scenario, including outline examples, to its source rules or examples in the handoff record.
Outline rows inherit shared mappings; record row-specific sources or source-example links only where they differ.
Preserve source IDs when available; otherwise use source locations or excerpts without rewriting the source.

Add cases when agreed context clearly determines their expected outcomes. Confidence must come from that context.
Explore relevant input classes, boundaries, condition combinations, state changes, failures, retries, and timing.
For example, if integers 1 through 5 succeed and other integers are rejected without changes, derive 0, 1, 5, and 6.
That rule leaves decimal handling undecided; record the missing decision instead of specifying a guessed outcome.
Deduplicate equivalent cases while retaining links to every source example they represent.
Finish drafting when every in-scope agreed rule and example is represented, blocked, or explicitly excluded with a reason.
Use exclusions established by the source or user; report other missing coverage as gaps.

## Return uncertainty to discovery

For each uncertain case, record its source area, the exact missing decision, and the scenarios it blocks.
Use a stable question ID and preserve whether the user has explicitly deferred it.
Reopen the affected discovery area with these questions; use the discovery skill if available, otherwise ask directly.
Keep unaffected agreements and continue independent formulation work.
When a question is resolved, cite the decision in the handoff, update affected scenarios, and update an authorized discovery record.
A deferred decision remains unresolved; it does not imply a default outcome or exclusion from scope.

## Review the complete draft

Present the complete supported draft for review, rather than requiring approval area by area.
Check fidelity to agreed behavior, concrete outcomes, consistent terms, duplicates, and interactions across areas.
For each scenario, check assertions for relevant outputs, observable state changes, and prohibited effects promised by its sources.
Count a promise as covered only when a scenario distinguishes correct behavior from a violation; source links alone establish provenance.
Account for every in-scope source rule and example in the coverage record; identify gaps without claiming exhaustive coverage.
Use a Gherkin parser if already available; otherwise review syntax and report that parsing was not performed.
Gherkin parsing checks syntax. Behavioral fidelity requires review; passing system tests requires later execution.
Apply editorial corrections directly. Return changes to expected behavior to the affected discovery area.
Retain the full draft while resolving feedback; the user accepts the complete supported specification before marking it ready.

## Handoff

Link the feature files and handoff record, identifying the source revision when available.
Record scenario-to-source mappings, derived cases, coverage gaps, explicit exclusions, and unresolved or deferred questions.
Mark the handoff ready when the user accepts the specification and no unresolved decisions block its agreed scope.
Mark an explicitly accepted partial handoff partial, naming ready behavior and the behavior still blocked.
Keep review-pending drafts visibly pending. Distinguish syntax review, parser results, and behavior not yet tested.
The handoff guides the project's existing testing approach; no particular runner or framework is required.
