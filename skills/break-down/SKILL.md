---
name: break-down
description: "Break down software or a supplied specification into source-linked areas, rules, states, and cases, then explain them. Use to understand existing software, unpack a full or partial specification, or supply a behavior map requested by discover-behavior. Implementation planning and agreeing expected behavior are separate tasks."
---

# Break down software and specifications

- Collect a supported specification map before explaining it; cover the full in-scope specification, with journeys as one view.

## Establish scope and sources

- Accept existing software, complete or partial specifications, or a scoped request from another skill; implementation and BDD records are not prerequisites.
- Identify the subject, audience, intended use, boundary, vocabulary, and supplied sources; associate observations and code inferences with inspected revisions or versions, noting when these are unknown.
- Inventory in-scope actors, goals, journeys, capabilities, interfaces, data, states, rules, background events, and constraints; retain specification areas outside journeys.
- Use supplied documents and available code, tests, and runtime evidence. For existing software, inspect relevant entry points and dependencies to find behavior the initial journeys omit.
- Keep source requirements, observed results, code inferences, derived cases, assumptions, and open questions distinguishable; preserve whether source requirements are proposed or agreed.
- When sources conflict, report both claims and their consequences. Code describes implementation; tests describe expectations until executed; neither alone establishes agreed requirements.

## Collect the specification map

- Group findings by meaningful capabilities or specification areas; describe responsibilities, interfaces, and dependencies when relevant, rather than mirroring files or functions.
- For broad subjects, inventory the full scope first, then collect and explain one coherent area at a time; keep an overall coverage map and label unfinished analysis.
- Trace each area's rules through input classes, boundaries, condition combinations, permissions, state changes, sequences, failures, retries, and timing where applicable.
- Include system-triggered behavior and cross-area interactions, shared data, and invariants; a journey list alone is insufficient coverage.
- For each case, record relevant starting conditions, action/event, observable outcomes, state changes, side effects, prohibited effects, and source references.
- Preserve stated nonfunctional constraints and their scope, units, thresholds, and conditions; leave missing targets or guarantees explicit.
- Derive cases only from supported rules, label the derivation, and leave unsupported outcomes open. Identify equivalent cases and unreachable combinations with reasons rather than enumerating every input value.
- Map every in-scope source requirement to an area and supported cases or an explicit gap; use stable IDs when needed for references or continued work.
- For reconstructed specifications, record which surfaces and sources were inspected and which remain unexplored; distinguish source coverage from runtime verification.

## Explain and return the map

- Start with an overview of the areas and their relationships, then explain each area's rules and concrete cases in language suited to the audience.
- Use journeys for end-to-end understanding, state diagrams for transitions, and decision tables for condition combinations when they clarify the findings.
- Keep one authoritative definition per finding; reference it across views instead of repeating it. Make supporting sources and uncertainties reachable from the explanation.
- Review coverage, contradictions, cross-area effects, and unexplored scope before delivery; report the supported boundary without claiming exhaustive cases or unexecuted checks.
- Deliver the map, evidence references, and gaps in the conversation or requested document; create persistent records only when requested or continuing an identified record.
- When invoked by another skill, return the requested scope and preserve identities and evidence so the caller can resume; request only consequential missing context and continue independently supported analysis.
- Leave behavior choices open for discover-behavior and preserve supplied agreements; explanation alone does not authorize formulation, ticketing, implementation, or changes to the subject software.
