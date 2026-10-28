---
name: formulate-behavior
description: "Write or review Gherkin scenarios from agreed behavioral requirements, supplied examples, or discovery records. Use when the requested output is a behavioral specification. Unsettled behavior discovery, native test implementation, and test execution are separate tasks."
---

# Formulate behavior

- Deliver source-linked Gherkin for existing test tools, using settled requirements without another discovery conversation.

## Choose the working mode

- Use supplied sources; deliver the specification in the conversation or requested document.
- For an explicitly requested tracked workflow or explicit continuation of an identified run, read [the run contract](references/run-record.md).

## Establish the source

- Read requirements and existing specifications to identify the subject, consumer, boundary, terms, sources, dependencies, and coherent agreed scope.
- Distinguish agreed behavior from proposals, observed code, and deferred choices; resolve conflicts with the user rather than silently choosing outcomes.
- Preserve source identities and citations; use section references or local rule/example IDs when absent, without requiring a discovery file.

## Draft supported scenarios

- Write independently understandable scenarios with relevant starting conditions, an action/event, and observable outcomes, including promised side effects and prohibited effects.
- Preserve domain vocabulary, interfaces, units, and time boundaries; exclude setup mechanics and private implementation choices from consumer-visible scenarios.
- Use Scenario Outline and Examples for shared behavior with varying data; separate distinct behavior and give continuing cases stable unique tags such as @case-001.
- Link scenarios to current source definitions; tracked runs use resolvable @source-<id> mappings without invented discovery work.
- Derive outcomes only from agreed rules; check boundaries, combinations, states, failures, retries, and timing without guessing missing rules.
- For integers 1 through 5 accepted and all other integers rejected, derive 0, 1, 5, and 6; leave decimal handling undecided.
- Let outline rows inherit sources; separate tagged Examples groups when sources differ and tag derived scenarios/groups @derived without losing provenance during deduplication.

## Resolve uncertainty and review

- Identify missing decisions and affected scenarios; ask consequential questions and continue supported formulation without starting a full discovery workflow.
- Resolve behavior changes with the user; editorial corrections and cases derived from settled rules need no new decision.
- Review affected scenarios and links when sources change.
- Check fidelity, concrete outcomes, consistent terms, duplicates, cross-area interactions, and coverage of every in-scope rule/example; identify blocked work and authorized exclusions.
- Count coverage only when an assertion distinguishes success from a violation; source tags establish provenance rather than coverage or passing tests.
- Use an available Gherkin parser or report manual syntax review; distinguish parsing, behavioral review, user acceptance, and executed system tests.

## Deliver the specification

- Deliver the supported specification with source mappings, usable scope, and remaining questions to complete a draft request.
- Continue into ticketing, integration, or implementation only when authorized; faithful formulation of settled behavior needs no separate approval.
