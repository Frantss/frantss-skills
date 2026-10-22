---
name: frantss-discover-behavior
description: "Discover expected behavior through a user-agent conversation before formulation. Use when clarifying consumer-visible rules, examples, boundaries, or unresolved behavior decisions. Ordinary implementation, test execution, and Gherkin conversion of settled requirements do not activate it."
---

# Discover behavior

Establish expected behavior from the consumer's perspective through concrete examples and an iterative conversation.
Produce an agreed discovery record for later formulation. Gherkin writing, test integration, and implementation belong to later work.
This skill works independently; formulation can use the record without requiring another installed skill.

## Start and maintain the live record

Read supplied context and relevant project evidence before asking questions that those sources can answer.
Use the user's destination or workspace convention; otherwise choose an unused `<subject>-discovery.md` path in the workspace.
Create one evolving Markdown record from the first exchange. On resume, read it and continue from its current state.
Organize it by context, area map, area details, cross-area review, and open questions.
Keep the current stage, active area, scope, and review status visible; future areas remain pending.
Update the record after each substantive exchange, before asking the next round. Record conclusions and reasoning, not a transcript.
Distinguish agreed behavior, proposals, observations of existing code, assumptions, and unresolved questions; cite sources where available.
User acceptance determines agreement. Apply answers only to the points addressed; silence leaves other points unresolved.
Give substantive points stable IDs: CO for context, A for areas, R for rules, E for examples, T for terms, Q for questions, D for decisions.
Use a prefix, hyphen, and increasing three-digit number, such as `R-001`; preserve an existing identity scheme.
Keep one authoritative entry per point and cross-reference its ID. Preserve IDs across clarification, movement, and status changes.
Never renumber or reuse IDs. For changed meaning, merges, or splits, retain superseded entries and link their replacements.
Show focused changes and link the record during the conversation rather than repeating the full document.

## Frame and map areas first

Establish the subject, intended outcome, consumer, observable boundary, domain terms, and included or excluded scope.
The consumer may be a person, API client, or calling code; preserve public interface details that affect their expectations.
Use code as evidence of current behavior, not automatic authority for expected behavior.
Before detailed cases, map consumer-visible responsibilities into behavior areas and identify their dependencies.
For each area, record its purpose, boundary, scope, and status: pending, in discussion, agreed, partial, or excluded.
Resolve uncertainty that prevents a useful map through framing questions, then review the map with the user before exploring areas.
Revise the map when evidence changes it; explain and obtain agreement on changed scope instead of silently expanding or dropping behavior.

## Discover one area at a time

Select an area using dependencies and the user's priorities. Keep unrelated areas pending.
Start with known rules or concrete examples. Propose examples to challenge rules and propose rules to explain examples.
Use relevant input classes, boundaries, condition combinations, state changes, failures, retries, and timing to expose missing decisions.
Capture general properties as rules with illustrative examples; examples alone do not establish universal correctness.
For stateful subjects, compare actions across relevant observable states and include sequences that cross those states.
Use a compact state/action table when it clarifies different outcomes; a formal state model is optional.
For each example, establish relevant starting conditions, the action or event, and observable outcomes.
Include meaningful side effects and effects that must not occur; clarify terms and time boundaries when they change the outcome.
Recommend behavior when useful, explaining the reason and trade-off; keep it proposed until the user decides.
Identify uncertainties that affect expected behavior. Investigate available facts and ask the user about unresolved choices.
Ask independent questions together using available feedback interfaces; defer questions that depend on unanswered decisions.
Give each question its stable ID, affected area, and the behavior its answer will determine.
After each answer, update agreements and recompute the questions that can now be answered without guessing other decisions.

## Review each area

Before moving on, present the area's rules, examples, vocabulary, exclusions, coverage gaps, and open questions for review.
Incorporate corrections and obtain agreement on resolved behavior; avoid confirmation after every individual answer.
An area becomes agreed when its behavior is accepted and no unresolved behavior decisions block its included scope.
Explicit user deferrals permit a partial area: identify the missing decisions, their effects, and which behavior remains ready.
Deferral leaves a question unresolved; it does not imply agreement, a default outcome, or exclusion from scope.
If later evidence changes an accepted area, reopen the affected conclusions while preserving unaffected agreements.
Questions returned by formulation enter this same loop under their source areas; retain existing IDs and prior decisions.

## Cross-area review and handoff

After area reviews, check interactions, shared terms, contradictions, missing areas, and the original goal and boundary.
Return newly exposed decisions to their affected areas and repeat review as needed.
Account for every mapped area and deferred question; use exclusions only when established by the source or user.
Present the complete discovery record for acceptance, with agreed rules, supporting examples, scope, and uncertainty visible.
Mark it ready for formulation when accepted and no unresolved decisions block the agreed scope.
An explicitly accepted partial handoff names ready behavior and deferred decisions that block formulation of the remaining behavior.
Keep unaccepted records visibly pending; user-requested early handoffs retain unresolved questions and their effects.
Link the record and identify its outcome. Readiness covers the agreed scope and does not claim exhaustive coverage or tested behavior.
