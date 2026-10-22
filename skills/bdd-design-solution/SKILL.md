---
name: bdd-design-solution
description: "Design a solution or technical migration when the user asks to compare approaches or define responsibilities, interfaces, dependencies, and consequential trade-offs. Accept supplied requirements or an existing design. Routine implementation and task scheduling alone do not require solution design."
---

# Design a solution

Deliver a scoped solution proposal or refine an existing design against supplied needs and behavior. Concept selection may precede detailed behavioral discovery.

## Choose the working mode

Default to standalone: use the conversation and supplied sources; deliver the proposal in the reply or the requested document. Selecting this skill does not enroll the task in a BDD run.
Track a run only when the user requests a tracked BDD workflow or the current task explicitly continues an identified run. A nearby run folder alone is insufficient. For tracked work, read [the run contract](references/run-record.md) and create only the records this stage needs.
Accept clear requirements, a problem brief, or an existing design without requiring earlier skills or a particular document format. Address consequential missing context directly; keep independent design work moving.

## Establish the design context

Read agreements and project evidence. Identify the intended decision, outcome, scope, constraints, known behavior, and dependencies before proposing a direction.
Use a coherent scope and comparable parts. Preserve fixed choices unless relevant evidence challenges their suitability; identify assumptions and unanswered questions explicitly.
Investigate checkable feasibility in the code and authoritative documentation. Distinguish evidence from assumptions and name uncertainty that could change the recommendation.
Use stable IDs when continued work or cross-references need them; retain supplied identities and link source needs instead of copying specifications.

## Choose or refine the approach

Compare credible alternatives against the same goals and constraints, including reuse or no change when viable. Recommend one and explain its consequential trade-offs; explain when only one is viable.
Describe cooperating parts at comparable depth: each part's purpose, boundary, interface, dependencies, and how they satisfy the agreed needs or behavior.
Refine parts in dependency order or the user's priority. Preserve accepted structure and examine only consequential alternatives within each part.
Walk relevant examples, constraints, and prohibited effects through the design. Identify interaction conflicts; these checks do not establish passing implementation tests.
Keep technical choices within design. A cheaper approach is not authority to weaken agreed behavior, reopen fixed choices, or change scope.
Resolve blocking needs or behavior questions directly, using framing/discovery guidance when useful. Create another stage's artifacts or start its full workflow only when that work is requested.
For unresolved choices, group independent questions, explain their effect, and keep proposals distinct from decisions. Deferrals remain unresolved and block only dependent work.
When agreements change, check affected existing source links and downstream conclusions. Update authorized records and preserve unaffected agreements.

## Deliver the proposal

Review approach, rationale, scope, responsibilities, interactions, alternatives, and consequential uncertainty against the requested design depth.
Delivering the requested proposal completes a draft request. Acceptance determines readiness for dependent work; reuse existing acceptance and request a new decision only when that work needs one.
For tracked work, update the design record and run status. Mark accepted, unblocked scope ready; identify usable scope and blockers for an explicitly accepted partial handoff.
State what is proposed, decided, and unverified. Include migration sequencing when requested, without manufacturing tickets or behavioral specifications.
Summarize the design or link the requested document. Identify the next use and stop unless further work is authorized.
