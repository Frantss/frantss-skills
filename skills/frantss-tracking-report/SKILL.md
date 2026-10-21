---
name: frantss-tracking-report
description: "Create, save, or retrieve daily/weekly activity and pending-work reports across selected workspaces, including past dates. Use collected evidence/task history. Source scans, direct capture, code review, and ordinary implementation requests belong elsewhere."
---

# Tracking report

Choose retrieve for a saved snapshot, create for a new report, or regenerate for a requested refresh. Clarify uncertain intent before collection.
Use `frantss-persistance` when available and the backend in `~/.frantss/persistance.yaml`; reporting never initializes configuration or creates workspaces.
Leave task records/events unchanged, including capture, acknowledgment, and triage. Explicit task changes belong to `frantss-tracking-tasks` when available.

## Retrieve

Read [snapshot records](references/save.md) for lookup fields/schema; identify the report by supplied ID or key, resolving only missing lookup scope.
Return its saved narrative, scope, generation time, supporting links, and recorded gaps, then stop.
If absent, report that result and offer creation; if inaccessible, report the access gap. Stop without collection, composition, or writes.

## Create or regenerate

1. Resolve workspace IDs, period, timezone, and report type; read [period rules](references/periods.md) and clarify unresolved scope.
   Use `~/.frantss/workspaces.yaml`, with read-only `frantss-configure-skills` resolution when available; retain historical missing-definition gaps.
   Explicit selection precedes unique registered remotes, then machine-scoped paths.
2. Retrieve scoped evidence, coverage, tasks, and dated history/revisions, including older outstanding commitments; expose access/pagination gaps.
3. When fresh evidence is needed/requested, use `frantss-tracking-collect` when available with the same scope and `capture: none`.
   Honor existing-evidence-only requests; reuse observations/coverage without repeating failed scans or widening scope. Unavailable collection remains a gap.
4. Read [content rules](references/content.md); compose from evidence, separating facts, reflection, and uncertainty, with supporting links.
5. Read [snapshot records](references/save.md); pass the schema and prepared report to persistence and save without another approval prompt.
   Finish when the write verifies, or return an explicitly partial/unsaved report with missing steps and recoverable payloads.

Return narrative/reference, exact scope, generation time, supporting links, and gaps. Label incomplete reports partial; planning stays out of scope.
