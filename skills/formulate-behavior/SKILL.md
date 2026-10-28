---
name: formulate-behavior
description: "Write or review Gherkin scenarios from agreed behavioral requirements, supplied examples, or discovery records. Use when the requested output is a behavioral specification. Unsettled behavior discovery, native test implementation, and test execution are separate tasks."
---

# Formulate behavior

- Deliver source-linked Gherkin for existing test tools, using settled requirements without another discovery conversation.

## Choose the working mode

- Use supplied sources.
- Use tracked records only when explicitly requested or when explicitly continuing an identified run.

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
- Account for every in-scope rule/example with concrete, source-faithful outcomes; check interactions, duplicate cases, blocked work, and authorized exclusions.
- Count coverage only when an assertion distinguishes success from a violation; source tags establish provenance rather than coverage or passing tests.
- Use an available Gherkin parser or report manual syntax review; distinguish parsing, behavioral review, user acceptance, and executed system tests.

## Deliver the specification

- Deliver the specification with source mappings, usable scope, and remaining questions in the conversation or requested document.
- Continue into ticketing, integration, or implementation only when authorized; faithful formulation of settled behavior needs no separate approval.

## Tracked records

- Use `.scratch/bdd/<feature_slug>-<NNN>/`, with a stable feature name, lowercase kebab-case slug, and next per-feature ordinal padded to at least three digits.
- Keep `run.md` YAML: `feature_name`, `feature_slug`, `run_id`, `stage`, `current_slice`, `current_ticket` (null until selected).
- Set `stage` to formulation; keep level-two sections Documents, Validation, and Next action.
- Under Documents, keep `### S-001: <name>`, Scope, file-qualified Members, Dependencies (slice/question references or None), and a File | Status table.
- Use pending (unvisited), draft (proposed/incomplete), blocked (unresolved prerequisite), ready (settled and sufficient for intended use), or partial (named usable scope and blockers).
- Keep checks and limits under Validation, the current step under Next action, and scope/blockers outside status cells.
- Create only participating records; preserve source locations, identities, human edits, and unaffected work.
- Reset affected checks to not_run and reopen affected done tickets when source decisions invalidate evidence.
- Write one named Feature in `behavior.feature`, with Rule groups and the scenario/source-mapping rules above.
- Add a source-definition record only when existing sources cannot resolve the mappings.
