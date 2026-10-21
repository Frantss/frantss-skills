# Report snapshot records

Supply the common persistence envelope with UUID `id`; retain `report_type: daily|weekly`, `projects`, `window_start`, `window_end`, and `timezone`.
Also retain `generated_at`, `tasks` (referenced task IDs), `source_urls` (unique supporting links/locators), `narrative`, `status_cutoff`, and brief text `coverage`.
Key: compact canonical JSON `[report_type, window_start, window_end, timezone, sorted_project_ids]`.
Normalize key timestamps to UTC, sort unique readable project strings lexicographically, and use inclusive-start/exclusive-end windows.
The narrative summarizes outcomes and commitments, including activity without a task; links point directly to sources or referenced tasks.
Coverage states checked sources/window, material access/truncation/history gaps, and partial status. Keep raw observations, transcripts, run/cursor details, and input manifests temporary.
Generation time is distinct from the activity period. Identify whether pending work is historical or current at `status_cutoff`; unavailable history remains a gap.
Find by key before creation; identical scope identifies one report with successive revisions, and retries cannot duplicate it.
Retain prior report revisions and preserve human narrative edits during regeneration; links permit source lookup without promising exact input reconstruction.
If storage cannot retain a prior revision, resolve replacement before overwriting. Live views supplement saved summaries.
Read back uncertain writes by key; return a verified reference or partial/unsaved payload with missing steps, without repeating saved effects.
Legacy `evidence` or `manifest` fields require `frantss-update`; ordinary report operations leave affected records unchanged and return unsupported.
