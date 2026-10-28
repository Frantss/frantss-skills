---
name: frame-problem
description: "Clarify an unclear problem's needs, evidence, intended outcomes, scope, and constraints. Use when those decisions are unresolved or the user asks to reframe them. A settled implementation request or a chosen solution alone does not require framing."
---

# Frame a problem

- Deliver a problem brief that distinguishes needs from symptoms and proposed solutions.

## Choose the working mode

- Use supplied context and prior decisions; deliver in the conversation or requested document.
- Use tracked records only when explicitly requested or when explicitly continuing an identified run.

## Establish the problem

- Read relevant evidence to identify the current situation, trigger, previous attempts, affected people, and consequences.
- Separate facts, claims, assumptions, proposals, and agreements; existing arrangements alone do not establish requirements.
- Define the intended outcome, its value, and success criteria; leave unknown baselines and targets explicit.
- Distinguish suggested solutions from authorized choices; preserve authorized choices unless relevant evidence challenges their fit.
- Define scope, dependencies, constraints, and intended use; challenge unsupported causal claims and mismatches between the solution and need.
- For distinct needs, propose comparable outcome-focused subproblems and relationships; select coherent scope by user priorities and keep remaining work visible.
- Use stable point IDs when cross-references or continued work need them; retain supplied IDs and one authoritative definition per point.

## Clarify consequential uncertainty

- Ask about missing facts or choices that materially change the brief and remain unresolved after reading the evidence.
- Recommend consequential choices with reasons and credible alternatives; apply answers only to addressed points and leave other choices unresolved.
- Preserve emerging behavior requirements and technical ideas as sourced inputs, distinct from agreed directions.
- Review affected conclusions and links when decisions change; keep deferred questions open and block only dependent work.

## Deliver the brief

- Review coherence, evidence, affected people, outcomes, scope, constraints, subproblem coverage, and blockers to intended use.
- Deliver the supported brief and consequential uncertainties; delivery completes a draft request.
- Continue into solution comparison, behavior discovery, or delivery planning only when authorized; resolve blockers without starting unrelated workflows.

## Tracked records

- Use `.scratch/bdd/<feature_slug>-<NNN>/`, with a stable feature name, lowercase kebab-case slug, and next per-feature ordinal padded to at least three digits.
- Keep `run.md` YAML: `feature_name`, `feature_slug`, `run_id`, `stage`, `current_slice`, `current_ticket` (null until selected).
- Set `stage` to framing; keep level-two sections Documents, Validation, and Next action.
- Under Documents, keep `### S-001: <name>`, Scope, file-qualified Members, Dependencies (slice/question references or None), and a File | Status table.
- Use pending (unvisited), draft (proposed/incomplete), blocked (unresolved prerequisite), ready (settled and sufficient for intended use), or partial (named usable scope and blockers).
- Keep checks and limits under Validation, the current step under Next action, and scope/blockers outside status cells.
- Create only participating records; preserve source locations, identities, human edits, and unaffected work.
- Reset affected checks to not_run and reopen affected done tickets when source decisions invalidate evidence.
- Use level-two sections in `problem.md`: Problem; Context and evidence; People; Goals and success criteria; Scope and constraints; Open questions.
