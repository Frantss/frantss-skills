# Task content and dates

Aim for 5–15 lines; enforce at most 50 authored task-content lines across title, context, blocker, and triage reason, including headings/blanks.
Exclude link-only lines and storage metadata; inline-link prose counts. Store source URLs in `source_urls` and supporting record IDs in `evidence`.
State the intended outcome and brief high-level context; link Jira tickets, threads, documents, or evidence instead of copying their contents.
Keep acceptance criteria and implementation detail at the source; a task without a source still needs a clear outcome.
Summarize updates instead of appending transcripts. Put longer supporting material in separate linked evidence/notes; preserve human edits and prior revisions.
If safe condensation needs clarification, return a draft/conflict rather than silently deleting user content or saving an over-limit task.

Use optional `due_date`/`due_at` for firm deadlines and `expected_date`/`expected_at` for anticipated completion; both kinds can coexist.
Within each kind, retain either a date or a timestamp with offset, preserving precision. Unknown dates stay null; never invent dates for categorization.
Resolve relative dates from the statement's occurrence date/timezone; clarify material ambiguity. A sprint boundary alone supplies neither kind.
Dates guide triage and reports; they do not create commitment, acknowledgment, or a scheduled state change.
