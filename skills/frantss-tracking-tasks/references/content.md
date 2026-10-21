# Task records, content, and dates

Supply the common persistence envelope; tasks/events use UUIDs and default `<record_type>:<id>` keys.
Tasks retain `status: inbox|next|later|maybe|done`, nullable `workspace`, `tags`, `evidence` IDs, `history_complete`, and brief `context`.
Optional `source_urls`, `triage_reason`, and `blocker` retain original links, supported categorization, and dependency/next actor.
Optional `due_date`/`due_at` is a firm deadline; `expected_date`/`expected_at` anticipated completion. Both kinds can coexist, each as date or offset timestamp.
Retain supported precision; unknown dates stay null. Resolve relative wording from occurrence date/timezone; clarify ambiguity and infer no dates from sprint boundaries.
Aim for 5–15 content lines; title/context/blocker/reason plus headings/blanks must total at most 50, excluding link-only lines and storage metadata.
Inline-link prose counts. Keep outcomes/high-level context and source links; acceptance criteria, implementation details, and transcripts stay in linked sources/evidence.
Summarize updates rather than append; preserve human edits/revisions. Unsafe condensation leaves a draft/conflict, never silent deletion or over-limit saves.

Events retain `task`, `kind`, `occurred_at`, `occurred_date`, `recorded_at`, `evidence`, and `change` with before/after field values.
Allocate event identity before writing; one logical change may update several fields. Creation and changes to state/workspace/acknowledgment/dates/blockers/reason/context require events.
Separate occurrence and recording times; unknown dates remain unknown. Current state and events must agree; keep `history_complete: false` for missing events/history or unjournaled edits.
