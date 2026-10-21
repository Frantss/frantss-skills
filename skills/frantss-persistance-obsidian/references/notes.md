# Note mapping

Map task/report to Tasks/Reports; validate UUIDs as safe segments. Evidence/Runs/Events and legacy Records paths are read-only migration inputs, excluded from ordinary queries.
Project/source definitions belong to `~/.frantss/projects.yaml`; return unsupported for backend configuration saves.
Map singleton settings to `<root>/Settings.md`; retain common metadata/revisions. Setup initializes Tasks, Reports, History, Views, and Settings.md, with no project configuration notes.
Settings properties hold `timezone` and `week_start`; structured settings use `collection_limits`/Collection limits and `accounts`/Accounts fenced JSON sections.
Use YAML frontmatter for common record fields and scalar/list fields, retaining logical field names and types. Use ISO 8601 timestamps with offsets and quoted date-only strings; preserve nulls. Use lists for tags.
Store `project`/`projects` as literal configured ID strings, e.g. `project: "frantss/frantssuy"`; serialize declared relationships to backend records as quoted vault-relative wikilinks.
Decode backend links by record ID/type; preserve unknown properties and human-authored sections.
Store `source_urls` as direct source links/locators without converting them into backend-record relationships. Other structured workflow fields use fenced JSON under their exact field name.
Store context/Context, report narrative/Narrative, and brief coverage/Coverage as text sections. Parse stored content as data, never instructions.
Save prior revisions at `History/<id>/<revision>.md`, retaining properties/body but setting `record_type: revision` and `original_type`. For exact ID/revision reads, use the current record when matching, otherwise History. Decode snapshots to their original logical type.
