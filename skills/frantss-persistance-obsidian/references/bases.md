# Bases views

Create requested `.base` files under `<root>/Views`, preserving custom views. Markdown records remain authoritative; reports retain saved snapshots.
Use [Bases YAML](https://obsidian.md/help/bases/syntax). Scope every view to the root and exclude History.
Adapt this Inbox example to the selected root; serialize paths as quoted data rather than interpolating arbitrary expressions:

```yaml
filters: 'file.inFolder("Frantss") && !file.inFolder("Frantss/History")'
views:
  - type: table
    name: Inbox
    filters: 'note.record_type == "task" && note.status == "inbox"'
    order: [note.title, note.project, note.due_date, note.expected_date, note.tags]
```

Other requested [views](https://obsidian.md/help/bases/views) can group tasks by supplied state/project; keep Maybe separate from Next/Later and show blockers/due/expected fields. Task-only unreviewed rows use `!file.hasTag("reviewed-by-frantss")`.
Activity views use report summaries by period/project and show generation time; task links open original sources.
Viewing rows never acknowledges tasks. Canvas is optional presentation; it does not replace records or reports.
Use the CLI write protocol for `.base` files. Read back YAML and run `base:query path=<root>/Views/<name>.base view=<view> format=json` to check scope and filters against sample notes.
