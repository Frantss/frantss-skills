# Digest records

This skill owns the `team-digest` report schema; reuse persistence's common version-1 envelope and configured adapter. Daily/weekly schemas remain unchanged.
Envelope: `schema_version: 1`, `record_type: report`, UUID `id`, stable `key`, readable `title`, integer `revision`, offset `created_at`/`updated_at`; start revision at 1.
Domain fields: `report_type: team-digest`, `projects` (sorted unique readable project IDs, or `[]`), `source_scope`, `window_start`, `window_end`, `timezone`, `generated_at`, `source_urls` (unique supporting links/locators), `narrative`, and brief text `coverage`.
Store boundaries as offset timestamps and an IANA timezone; keys use canonical UTC timestamps ending in `Z`, omitting zero fractional seconds. Generation time remains distinct from the activity period.
`source_scope` is a sorted unique list of `[kind, instance, location]` string tuples describing selected discovery boundaries, not credentials, tool profiles, search logs, or retrieved observations.
Use verified native service kind, instance/account/workspace, and canonical container/object ID or URL; preserve meaningful path case and selectors that define the supplied boundary. Local paths need a machine identity and canonical absolute location.
For supplied material without a native locator, assign a request-local UUID reference with a readable label; retain that tuple on retries and explicit refresh. Never store its raw contents in the report.
Sort tuples lexicographically by their three strings. Equivalent tool aliases and reordered/duplicate source selections must produce the same scope; unresolved native equivalence requires clarification, never merging unrelated locations.
Key: compact JSON `["team-digest", window_start_utc, window_end_utc, timezone, source_scope, projects]`, with fixed tuple order and sorted lists above. Context-only links belong in `source_urls`, outside `source_scope`.
Example key: `["team-digest","2026-10-19T00:00:00Z","2026-10-20T00:00:00Z","Etc/UTC",[["github","github.com","example/service"]],[]]`.
Use a readable title such as `<local period> - <source/team label> team digest`; native record IDs never become filenames.
Coverage names checked/missing sources, date/participation uncertainty, truncation, and partial status. Persist the scope as report metadata only; source selections must be supplied again unless refreshing an identified report.
Keep raw messages, transcripts, observations, queries, and scan cursors temporary. No task relationships or task captures are implied by this report.
Lookup/query filters include `record_type: report`, `report_type: team-digest`, ID/key, and supplied scope/window; use bounded results. Comparison baselines have earlier `generated_at`, matching `source_scope`/`projects`/timezone, and explicit windows/coverage limits. Unavailable overwritten revisions remain a history gap.
Find by key before creation; regenerate the same scope/period in place with expected revision, preserving human edits and unknown fields. Scope/period changes select a different key; preserve the original record.
Read back uncertain writes by stable identity before retrying. Return verified references/revisions or partial/unsaved payloads with missing steps; stop after repeated unresolved conflicts/access failures.
Missing configuration, persistence skill, or adapter leaves the digest explicitly unsaved in chat; do not create fallback files. Retrieve never creates a missing record.
This adds a report subtype; existing task/daily/weekly records need no conversion. Installing the skill changes no configuration, records, or database views; preserve their IDs/keys/revisions and human edits.
