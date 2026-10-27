# Tracked BDD run contract

This bundled reference is generated from the repository's `templates/bdd-run-record.md`; edit that source and regenerate bundled copies.

Use `.scratch/bdd/<run_id>/` for one explicitly tracked feature across conversations and slices. Preserve an identified run; ask only when the intended run is ambiguous.
For a new run set stable `feature_name`, lowercase kebab-case `feature_slug`, and `run_id: <feature_slug>-<NNN>` using the next per-feature ordinal padded to at least three digits.
Create `run.md` and only artifacts this stage produces or needs for traceability. Leave future-stage files absent; existing legacy placeholders may remain without expansion.
Known artifacts are `problem.md`, `discovery.md`, `behavior.feature`, `design.md`, and `tickets.md`. Honor supplied source locations rather than copying them merely to fill this layout.
Keep current definitions, stable IDs, acceptance, and human edits. Replace obsolete content and resolved questions in authorized records; keep no transcripts, histories, tombstones, or extra per-slice folders.

`run.md` YAML has `feature_name`, `feature_slug`, `run_id`, `stage`, `current_slice`, and `current_ticket` (null until selected). Stage is framing, concept, discovery, formulation, design, slicing, or implementation; it does not establish readiness.
Use exactly `Documents`, `Validation`, `Next action` as level-two sections. Under Documents give each current slice a `### S-001: <name>` entry with Scope, Members, Dependencies, and a File | Status table for participating artifacts/sources, not future placeholders.
Members uses file-qualified IDs such as `discovery.md:R-001`; preserve all current slices when focus changes. Dependencies lists slice/question references or None.
Document statuses: pending = unvisited; draft = unaccepted; blocked = an unresolved prerequisite; ready = accepted and unblocked for intended use; partial = an explicitly accepted usable subset with named blockers.
Keep scope/blockers outside status cells; partial Scope identifies usable members. Area maps use these statuses plus excluded, which needs source/user authority; an area's status covers its included scope.
Validation contains current checks and limits; Next action names the current step. Delivering a draft completes a draft request; acceptance governs dependent work and does not imply passed tests or authorize later stages.
When execution is tracked, add Implementation under Validation: Ticket | State | Evidence, with pending, in_progress, blocked, or done. Evidence identifies checked code, commands, limits, and justified test-first exceptions.
Add Behavior checks: Ticket | Cases | Check | Result, with passed, failed, blocked, or not_run. Cases identifies source cases/Examples groups, or None for non-scenario checks; split rows with different results.
Mark done only after all assigned behavior and required checks pass on current code. Changed code/agreements/design/prerequisites invalidate affected evidence, set affected results to not_run, and reopen affected done work.

Created Markdown artifacts use `<feature_name>: <document role>` titles and the following level-two sections; use Pending for unvisited sections inside an existing artifact and None for empty lists.
`problem.md`: Problem; Context and evidence; People; Goals and success criteria; Scope and constraints; Open questions.
`discovery.md`: Boundary and vocabulary; Area map; Area details; Coverage gaps; Open questions. Map columns: ID | Area | Status | Dependencies; each area detail has Boundary, Rules, Examples.
`design.md`: Context; Approach; Structure; Decisions; Open questions. Structure describes purposes, boundaries, interfaces, and dependencies; decisions retain current rationale, not a chronology.
`tickets.md`: Overview; Tickets; Coverage gaps. Use stable TK-* headings with an outcome, one-sentence context, Dependencies, Behavior | Cases, and optional essential Verification. Definitions stay separate from execution evidence.
`behavior.feature`: one named Feature, relevant scope, Rule groups, stable tagged scenarios, Given/When/Then outcomes, and Examples for outlines. Source tags resolve to actual current definitions; source mappings need no separate discovery file when supplied sources suffice.
Preserve existing run/slice/case identities and accepted scope on resume. Update only records affected by authorized work; installing these skills does not migrate, delete, or rewrite prior runs.
