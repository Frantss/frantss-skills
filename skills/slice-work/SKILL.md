---
name: slice-work
description: "Draft or review implementation tickets from agreed behavioral specifications, checking scope, granularity, coverage, and dependencies. Accept supplied specifications without an existing BDD run. Behavior discovery, implementation, and publishing tickets alone are separate tasks."
---

# Slice work into tickets

- Deliver compact implementation tickets with observable outcomes, source behavior, and verification.

## Choose the working mode

- Use supplied behavioral specifications and relevant design, including cases outside Gherkin; earlier skills are not prerequisites.
- Use tracked records only when explicitly requested or when explicitly continuing an identified run.

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

- Deliver the breakdown and remaining gaps in the conversation or requested document.
- Choose routine boundaries and ordering within agreed scope; seek consequential scope, ownership, delivery, or dependency decisions and review grouping when requested.
- Review affected allocations and dependencies when sources or decisions change; preserve unaffected decisions and block only tickets dependent on unresolved choices.
- Continue authorized publication or implementation without separate approval of routine allocation; verify delivery prerequisites in current code before implementation.
- Report planning checks without claiming executed implementation tests.

## Tracked records

- Use `.scratch/bdd/<feature_slug>-<NNN>/`, with a stable feature name, lowercase kebab-case slug, and next per-feature ordinal padded to at least three digits.
- Keep `run.md` YAML: `feature_name`, `feature_slug`, `run_id`, `stage`, `current_slice`, `current_ticket` (null until selected).
- Set `stage` to slicing; keep level-two sections Documents, Validation, and Next action.
- Under Documents, keep `### S-001: <name>`, Scope, file-qualified Members, Dependencies (slice/question references or None), and a File | Status table.
- Use pending (unvisited), draft (proposed/incomplete), blocked (unresolved prerequisite), ready (settled and sufficient for intended use), or partial (named usable scope and blockers).
- Keep checks and limits under Validation, the current step under Next action, and scope/blockers outside status cells.
- Create only participating records; preserve source locations, identities, human edits, and unaffected work.
- Reset affected checks to not_run and reopen affected done tickets when source decisions invalidate evidence.
- Use level-two sections in `tickets.md`: Overview; Tickets; Coverage gaps; apply the ticket structure above.
