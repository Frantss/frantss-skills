---
name: design-solution
description: "Design a solution or technical migration when the user asks to compare approaches or define responsibilities, interfaces, dependencies, and consequential trade-offs. Accept supplied requirements or an existing design. Routine implementation and task scheduling alone do not require solution design."
---

# Design a solution

- Deliver a scoped proposal or refine an existing design against supplied needs and behavior; concept selection may precede detailed discovery.

## Choose the working mode

- Use supplied requirements, a problem brief, or an existing design; earlier skills and particular document formats are not prerequisites.
- Use tracked records only when explicitly requested or when explicitly continuing an identified run.

## Establish the design context

- Read agreements and project evidence to identify the decision, outcome, scope, constraints, known behavior, and dependencies before proposing a direction.
- Preserve fixed choices unless relevant evidence challenges their suitability; identify assumptions and unanswered questions explicitly.
- Check feasibility in code and authoritative documentation; distinguish evidence from assumptions and name uncertainties that could change the recommendation.
- Use stable IDs when continued work or cross-references need them; retain supplied identities and link source needs instead of copying specifications.

## Choose or refine the approach

- Compare credible alternatives against shared goals and constraints, including viable reuse or no change; recommend one with trade-offs and explain when only one is viable.
- Describe cooperating parts at comparable depth: each part's purpose, boundary, interface, dependencies, and contribution to agreed needs or behavior.
- Refine parts by dependencies or user priority; preserve agreed structure and examine consequential alternatives within each part.
- Check examples, constraints, prohibited effects, and interaction conflicts against the design without claiming passing implementation tests.
- Keep technical choices within agreed behavior and scope; resolve consequential needs or behavior questions without starting another full workflow.
- Keep proposals distinct from decisions and block only dependent work; review affected source links and conclusions when decisions change.

## Deliver the proposal

- Review approach, rationale, scope, responsibilities, interactions, alternatives, and consequential uncertainty against the requested design depth.
- Deliver the proposal in the conversation or requested document, distinguishing proposed, decided, and unverified points and including migration sequencing when requested.
- Delivering the proposal completes a draft request; continue only authorized work and ask only about consequential unresolved choices.

## Tracked records

- Use `.scratch/bdd/<feature_slug>-<NNN>/`, with a stable feature name, lowercase kebab-case slug, and next per-feature ordinal padded to at least three digits.
- Keep `run.md` YAML: `feature_name`, `feature_slug`, `run_id`, `stage`, `current_slice`, `current_ticket` (null until selected).
- Set `stage` to concept for approach selection or design for refinement; keep level-two sections Documents, Validation, and Next action.
- Under Documents, keep `### S-001: <name>`, Scope, file-qualified Members, Dependencies (slice/question references or None), and a File | Status table.
- Use pending (unvisited), draft (proposed/incomplete), blocked (unresolved prerequisite), ready (settled and sufficient for intended use), or partial (named usable scope and blockers).
- Keep checks and limits under Validation, the current step under Next action, and scope/blockers outside status cells.
- Create only participating records; preserve source locations, identities, human edits, and unaffected work.
- Reset affected checks to not_run and reopen affected done tickets when source decisions invalidate evidence.
- Use level-two sections in `design.md`: Context; Approach; Structure; Decisions; Open questions.
