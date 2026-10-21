# Task records, content, and dates

Supply the common persistence envelope; tasks use UUIDs and default `task:<id>` keys.
Tasks retain `status: inbox|next|later|maybe|done`, nullable `project`, `tags`, brief `context`, and `source_urls` (unique source links or locators).
Prefer verified source URLs; without one, retain a native locator with enough provider/container/object identity to retrieve the source, e.g. repository path plus full commit hash.
Keep evidence directly in `source_urls`, with optional short link labels. Save no separate evidence/event records, excerpts, transcripts, or copied source metadata.
Optional `triage_reason` and `blocker` retain brief categorization and dependency/next actor; supported `completed_date`/`completed_at` records the latest completion, cleared on reopening.
Optional `due_date`/`due_at` is a firm deadline; `expected_date`/`expected_at` anticipated completion. Both kinds can coexist, each as date or offset timestamp.
Retain supported precision; unknown dates stay null. Resolve relative wording from occurrence date/timezone; clarify ambiguity and infer no dates from sprint boundaries.
Aim for 5–15 content lines; title/context/blocker/reason plus headings/blanks must total at most 50, excluding link-only lines and storage metadata.
Keep outcomes/high-level context and source links; acceptance criteria and implementation details stay at the source. Inline-link prose counts toward the limit.
Summarize updates rather than append; preserve human edits/revisions. Unsafe condensation leaves a draft/conflict, never silent deletion or over-limit saves.
Use retained task revisions for saved-state history; recording/modification times do not establish when a source action or state change occurred.
Legacy `evidence`, `history_complete`, or Pending events payloads require migration through `frantss-update`; ordinary task operations leave them unchanged and report the affected record unsupported.
