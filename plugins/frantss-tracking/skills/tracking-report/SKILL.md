---
name: tracking-report
description: "Create, refresh, or retrieve daily and weekly report summaries of frantss's activity and commitments, using task links, saved reports, and temporary source findings."
---

# Tracking report

Choose retrieve for a saved snapshot, create for a new report, or regenerate for a requested refresh. Clarify uncertain intent before collection.
Use `persistence-records` when available and the database in `~/.frantss/persistance.yaml`; reporting never initializes configuration or creates projects.
Create/refresh delegates source-supported task capture/updates to `tracking-tasks` when available, including completed outcomes. Honor explicit no-task-write requests; reporting never acknowledges tasks or applies speculative planning changes.

## Retrieve

Read [snapshot records](references/save.md) for lookup fields/schema; identify the report by supplied ID or key, resolving only missing lookup scope.
Return its saved narrative, scope, generation time, supporting links, and recorded gaps, then stop.
If absent, report that result and offer creation; if inaccessible, report the access gap. Stop without collection, composition, or writes.

## Create or regenerate

1. Resolve project IDs, period, timezone, and report type; read [period rules](references/periods.md) and clarify unresolved scope. Use `~/.frantss/projects.yaml`, with read-only `core-configure` resolution when available; retain historical missing-definition gaps. Explicit selection precedes unique registered remotes, then machine-scoped paths.
2. Retrieve scoped tasks and relevant saved report summaries, including older outstanding commitments; expose access/history gaps.
3. When fresh context is needed/requested, use `tracking-collect` when available with the same scope and `capture: automatic`, unless task writes were explicitly disabled. Honor existing-evidence-only requests using saved summaries, task links, and session findings without source scans; otherwise reuse compatible findings without repeated failed scans or wider scope. Hand their owned outcomes to the task workflow under the same capture policy; unavailable collection or unresolved saves remain explicit gaps.
4. Re-read changed task records after capture; read [content rules](references/content.md) and compose from verified tasks/findings, separating facts, reflection, and uncertainty with links.
5. Read [snapshot records](references/save.md); pass the schema and prepared report to persistence and save without another approval prompt. Save only the summary, links, scope, cutoff, and brief coverage gaps. Finish on a verified write, or return an explicitly partial/unsaved report with recoverable payloads.

Return narrative/reference, exact scope, generation time, supporting links, and gaps. Label incomplete reports partial; planning stays out of scope.
