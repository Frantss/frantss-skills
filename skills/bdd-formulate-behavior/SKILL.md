---
name: bdd-formulate-behavior
description: "Write or review Gherkin scenarios from agreed behavioral requirements, supplied examples, or discovery records. Use when the requested output is a behavioral specification. Unsettled behavior discovery, native test implementation, and test execution are separate tasks."
---

# Formulate behavior

Deliver a source-linked Gherkin specification for the project's existing test tools. Accept settled requirements directly without another discovery conversation.

## Choose the working mode

Default to standalone: use supplied sources and deliver the specification in the reply or the requested document. Selecting this skill does not enroll the task in a BDD run.
Track a run only when the user requests a tracked BDD workflow or the current task explicitly continues an identified run. A nearby run folder alone is insufficient. For tracked work, read [the run contract](references/run-record.md) and create only the records this stage needs.
Keep test integration and production changes within separately requested scope. Resolve a blocking behavior question directly without starting a full discovery stage or its records.

## Establish the source

Read requirements and relevant existing specifications. Identify the subject, consumer, boundary, terms, sources, dependencies, and a coherent agreed scope.
Distinguish agreed behavior from proposals, observed code, and deferred choices. Obtain decisions on conflicts rather than selecting an expected outcome silently.
Preserve supplied source identities and citations. If IDs are absent, cite source sections or assign local rule/example IDs alongside the output; a separate discovery file is not required.

## Draft supported scenarios

Write independently understandable scenarios with relevant starting conditions, an action/event, and observable outcomes, including promised side effects and prohibited effects.
Preserve domain vocabulary, meaningful interfaces, units, and time boundaries. Keep setup mechanics and private implementation choices out of consumer-visible scenarios.
Use Scenario Outline and Examples for the same behavior with different data; separate distinct behavior. Give continuing cases stable unique tags such as @case-001.
Link scenarios to their actual source definitions. In tracked runs, use @source-<id> tags with mappings to current definitions; resolve every source reference without inventing discovery work.
Derive cases only when agreed rules determine their outcomes. Check relevant boundaries, combinations, states, failures, retries, and timing without guessing missing rules.
For example, integers 1 through 5 accepted and other integers rejected determine 0, 1, 5, and 6; decimal handling remains undecided.
Outline rows inherit sources; separate tagged Examples groups when sources differ. Mark derived scenarios/groups @derived and deduplicate without losing provenance.

## Resolve uncertainty and review

Identify each missing decision, its source area, and affected scenarios. Preserve explicit deferrals and continue independently supported formulation.
Ask the consequential question directly; use discovery guidance when useful. Changed expected behavior requires agreement, while editorial corrections can proceed directly.
When agreements change, review affected scenarios and existing downstream links. Update authorized definitions and preserve unaffected acceptance.
Check fidelity, concrete outcomes, consistent terms, duplicates, cross-area interactions, and coverage of every in-scope rule/example; identify blocked work and authorized exclusions.
Count a promise as covered only when an assertion distinguishes correct behavior from a violation. Source tags establish provenance, not coverage or passing tests.
Use an available Gherkin parser, or report manual syntax review only. Distinguish parsing, behavioral review, user acceptance, and executed system tests.

## Deliver the specification

Deliver the complete supported draft with source mappings and remaining questions. This completes a draft request; acceptance governs readiness for dependent work.
For tracked work, update the specification and run status; create a source-definition record only when source mappings need it. Reuse prior acceptance and mark accepted, unblocked scope ready.
Identify usable scope and blockers for an explicitly accepted partial handoff. Stop before unrequested ticketing, integration, or implementation.
