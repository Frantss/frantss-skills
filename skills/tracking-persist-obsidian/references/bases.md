# Bases views

Create requested `.base` files under `<root>/Views`, preserving custom views. Markdown records remain authoritative; reports retain saved snapshots.
Use [Bases YAML](https://obsidian.md/help/bases/syntax). Scope every view to the root and exclude History.
Adapt this Inbox example to the selected root; serialize paths as quoted data rather than interpolating arbitrary expressions:

```yaml
filters: 'file.inFolder("Tracking") && !file.inFolder("Tracking/History")'
views:
  - type: table
    name: Inbox
    filters: 'note.record_type == "task" && note.status == "pending" && !note.workspace'
    order: [note.title, note.due_date, note.tags]
```

Other requested [views](https://obsidian.md/help/bases/views) can show pending tasks grouped by workspace, or task-only unreviewed rows using `!file.hasTag("reviewed-by-frantss")`.
Activity views filter evidence/events by occurred_date; report views filter saved reports by period/workspace and show generation time.
Viewing rows never acknowledges tasks. Canvas is optional presentation; it does not replace records or reports.
Read back and parse YAML; check scope and filters against sample notes before claiming readiness.
