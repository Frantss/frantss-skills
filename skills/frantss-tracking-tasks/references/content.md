# Task records, content, and dates

Supply the common persistence envelope; tasks use UUIDs and default `task:<id>` keys.
A task is a specific owned outcome; subtasks use the same record type and fields. Tasks retain `status: inbox|next|later|maybe|done`, nullable `project`, `tags`, brief `context`, and `source_urls` (unique source links or locators).
Keep titles close to their primary source: Jira tasks use `<issue key> - <original summary>`, preserving source spelling, case, and punctuation. Distinct subtasks use their own source titles or a brief suboutcome qualifier; a shared parent-ticket link never substitutes its summary for the child's outcome. Without a source title, use a concise outcome name.
Optional `parent` is a task ID or null; missing means standalone. Derive children by querying this field; store no separate child list or outcome records.
Use a child only for a distinct owned suboutcome with its own completion condition; PR count alone never establishes subtasks. Resolve parent/ancestors as tasks and reject self-links, cycles, dangling references, or ambiguous grouping. Save/verify parents before dependent children; failed dependencies leave children explicitly unsaved.
Prefer verified source URLs; without one, retain a native locator with enough provider/container/object identity to retrieve the source, e.g. repository path plus full commit hash.
Keep evidence directly in `source_urls`, with optional short link labels. Save no separate evidence/event records, excerpts, transcripts, or copied source metadata.
Optional `triage_reason` and `blocker` retain brief categorization and dependency/next actor; supported `completed_date`/`completed_at` records the latest completion, cleared on reopening.
Optional `due_date`/`due_at` is a firm deadline; `expected_date`/`expected_at` anticipated completion. Both kinds can coexist, each as date or offset timestamp.
Retain supported precision; unknown dates stay null. Resolve relative wording from occurrence date/timezone; clarify ambiguity and infer no dates from sprint boundaries.
Aim for 5–15 content lines; title/context/blocker/reason plus headings/blanks must total at most 50, excluding link-only lines and storage metadata.
Keep outcomes/high-level context and source links; acceptance criteria and implementation details stay at the source. Inline-link prose counts toward the limit.
Summarize updates rather than append; preserve human edits. Unsafe condensation leaves a draft/conflict, never silent deletion or over-limit saves.
Keep one current task; dated sources or saved reports support past state. Recording/modification times never establish when an action occurred.
Legacy `evidence`, `history_complete`, or Pending events payloads require migration through `frantss-update`; ordinary task operations leave them unchanged and report the affected record unsupported.
Version 1 remains compatible: existing tasks without `parent` stay standalone with unchanged IDs/keys/state. Upgrades never infer hierarchy from shared projects/links; apply only source-supported parent links through expected-content writes, verify ancestors, and retry missing operations with the original identities.
