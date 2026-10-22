# Bases views

Every Obsidian setup must create `<root>/Views/Tasks.base` and `<root>/Views/Reports.base`; setup authorization includes these files without another request. Markdown records remain authoritative; reports retain saved snapshots.
Tasks.base requires Inbox, Next, Later, Maybe, Completed, Unreviewed, By project, and By parent table views. Filter by `note.record_type == "task"`; match each state exactly (Completed uses `done`), keep Maybe separate, and use `!file.hasTag("reviewed-by-frantss")` for Unreviewed. Group the last two by project/parent; expose title, project, parent, blocker, due/expected dates, tags, and source links.
Reports.base requires Daily and Weekly table views, filtered by `note.record_type == "report"` and the matching `note.report_type`; show title, window_start, window_end, projects, and generated_at.
Preserve custom files, views, formulas, and columns; add missing defaults without replacing existing definitions. Repeated setup creates no duplicates; conflicting default names leave setup partial until reconciled.
Use [Bases YAML](https://obsidian.md/help/bases/syntax). Scope every view to the configured root and exclude History; adapt this Inbox example and serialize paths as quoted data:
```yaml
filters: 'file.inFolder("Frantss") && !file.inFolder("Frantss/History")'
views:
  - type: table
    name: Inbox
    filters: 'note.record_type == "task" && note.status == "inbox"'
    order: [note.title, note.project, note.parent, note.blocker, note.due_date, note.expected_date, note.tags, note.source_urls]
```
Use the CLI write protocol for `.base` files. Read back YAML and run `base:query path=<root>/Views/<name>.base view=<view> format=json` for every required view; verify root/type/state/grouping and preserved customizations against existing or temporary sample notes. Valid empty results need no synthetic records. Missing files, unsupported Bases, or failed queries leave setup incomplete.
On an authorized upgrade of an initialized Obsidian store, back up and add missing default Bases/views using the update journal and expected-content protocol. Task/report schemas, IDs, states, and content stay unchanged; verify each view and retry only missing work with the same paths/names.
Inspection and ordinary record reads/writes only report missing views; they do not initialize or repair them. Editing/installing this skill alone does not create vault files.
Viewing rows never acknowledges tasks. Canvas is optional presentation; it does not replace records or reports.
