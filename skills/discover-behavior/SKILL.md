---
name: discover-behavior
description: "Clarify unresolved consumer-visible rules, examples, boundaries, or behavior decisions through conversation. Use when expected behavior needs agreement. Implementation, test execution, and converting already-settled rules to Gherkin do not require discovery."
---

# Discover behavior

- Resolve expected behavior through rules, examples, and conversation.

## Choose the working mode

- Use supplied requirements and prior decisions; earlier skills are not prerequisites.
- Use tracked records only when explicitly requested or when explicitly continuing an identified run.

## Establish the boundary

- Read supplied context and project evidence; treat code as evidence of current behavior rather than authority for expected behavior.
- Define subject, outcome, consumer, observable boundary, vocabulary, and included/excluded scope; consumers include people, API clients, and calling code.
- Group behavior into areas when useful; keep small or tightly coupled subjects whole and resolve consequential scope changes with the user.
- Preserve source IDs and one authoritative definition per point; assign rule/example/area IDs when continued work needs traceability.

## Explore rules and examples

- Start with known rules or concrete examples; use examples to challenge rules and proposed rules to explain examples.
- Treat examples as evidence for rules rather than proof of universal correctness.
- Explore input classes, boundaries, condition combinations, state changes, failures, retries, and timing; compare stateful actions across states and sequences.
- For each example, establish starting conditions, action/event, observable outcomes, side effects, prohibited effects, and meaningful terms, units, or time boundaries.
- Distinguish agreed behavior, observations, assumptions, proposals, and open questions; recommend behavior with reasons and trade-offs.
- Ask about unresolved behavior choices and apply answers only to addressed points; silence and deferral leave other choices open and block only dependent work.

## Review and deliver

- Review rules, examples, vocabulary, exclusions, and gaps across the included scope.
- Check interactions, contradictions, missing areas, and dependencies against the original outcome; exclusions need source or user authority.
- Review affected definitions, links, and conclusions when decisions change; preserve unaffected decisions.
- Deliver supported definitions and consequential questions in the conversation or requested document, distinguishing agreed/open behavior without claiming exhaustive coverage or tested behavior.
- Delivering the draft completes a draft request; continue authorized formulation or implementation using settled behavior without reconfirmation.

## Tracked records

- Use `.scratch/bdd/<feature_slug>-<NNN>/`, with a stable feature name, lowercase kebab-case slug, and next per-feature ordinal padded to at least three digits.
- Keep `run.md` YAML: `feature_name`, `feature_slug`, `run_id`, `stage`, `current_slice`, `current_ticket` (null until selected).
- Set `stage` to discovery; keep level-two sections Documents, Validation, and Next action.
- Under Documents, keep `### S-001: <name>`, Scope, file-qualified Members, Dependencies (slice/question references or None), and a File | Status table.
- Use pending (unvisited), draft (proposed/incomplete), blocked (unresolved prerequisite), ready (settled and sufficient for intended use), or partial (named usable scope and blockers).
- Keep checks and limits under Validation, the current step under Next action, and scope/blockers outside status cells.
- Create only participating records; preserve source locations, identities, human edits, and unaffected work.
- Reset affected checks to not_run and reopen affected done tickets when source decisions invalidate evidence.
- Use level-two sections in `discovery.md`: Boundary and vocabulary; Area map; Area details; Coverage gaps; Open questions.
- Area map uses ID | Area | Status | Dependencies; each area's included scope has Boundary, Rules, Examples, and a document status.
- Use excluded for areas excluded by supplied sources or the user.
