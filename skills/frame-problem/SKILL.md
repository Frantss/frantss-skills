---
name: frame-problem
description: "Clarify an unclear problem's needs, evidence, intended outcomes, scope, and constraints. Use when those decisions are unresolved or the user asks to reframe them. A settled implementation request or a chosen solution alone does not require framing."
---

# Frame a problem

Deliver a problem brief that distinguishes needs from symptoms and proposed solutions. Reuse supplied context and prior agreements.

## Choose the working mode

Default to standalone: use the conversation and supplied sources; deliver the brief in the reply or the requested document. Selecting this skill does not enroll the task in a BDD run.
Track a run only when the user requests a tracked BDD workflow or the current task explicitly continues an identified run. A nearby run folder alone is insufficient. For tracked work, read [the run contract](references/run-record.md) and create only the records this stage needs.
Keep solution comparison, behavior discovery, and delivery planning within separately requested scope. Resolve a blocking question directly without starting another stage's records.

## Establish the problem

Read relevant evidence before asking questions it can answer. Identify the current situation, trigger, previous attempts, affected people, and consequences.
Separate observed facts, reported claims, assumptions, proposals, and agreements. Existing arrangements are context, not automatic requirements.
Establish the intended outcome, why it matters, and how success can be recognized; keep unknown baselines and targets visibly unknown.
When a request names a solution, distinguish a suggestion from an authorized choice. Preserve authorized choices unless relevant evidence challenges their fit.
Define scope, dependencies, constraints, and intended next use. Challenge unsupported causal claims or mismatches between the proposed solution and need.
For distinct needs, propose comparable outcome-focused subproblems and their relationships. Select a coherent scope using the user's priorities; keep remaining work visible.
Use stable point IDs when cross-references or continued work need them; retain supplied IDs and one authoritative definition per point.

## Clarify consequential uncertainty

Ask about missing facts and choices that materially change the brief. Group independent questions and explain what each answer determines.
For a consequential choice, recommend a direction with reasons and credible alternatives when available. Leave dependent questions until their prerequisites are known.
Apply answers only to addressed points; user agreement establishes acceptance and silence leaves other points unresolved.
Preserve emerging behavior requirements and technical ideas as sourced inputs for later work; they do not become accepted directions automatically.
When agreements change, check affected existing references and conclusions. Update authorized records, preserve unaffected agreements, and name remaining blockers.
Deferral leaves uncertainty unresolved; it does not establish a default or remove scope.

## Deliver the brief

Review coherence, evidence, affected people, outcomes, scope, constraints, subproblem coverage, and questions that block its intended use.
Delivering the requested brief completes a draft request. Acceptance determines readiness for dependent work; reuse existing acceptance and request a new decision only when that work needs one.
For tracked work, update the current framing record and run status. Mark accepted, unblocked scope ready; name usable scope and blockers for an explicitly accepted partial handoff.
Summarize the brief or link the requested document, state consequential uncertainties, and identify the next use without executing unrequested stages.
