# Report snapshot records

Supply the common persistence envelope with UUID `id`; retain `report_type: daily|weekly`, `workspaces`, `window_start`, `window_end`, and `timezone`.
Also retain `generated_at`, `evidence`, `narrative`, and `manifest`; generation time is distinct from the reported activity period.
Key: compact canonical JSON `[report_type, window_start, window_end, timezone, sorted_workspace_ids]`.
Normalize key timestamps to UTC, sort unique readable workspace strings lexicographically, and use inclusive-start/exclusive-end windows.
The manifest retains collection IDs, exact input IDs/revisions, status cutoffs, coverage, and completeness at generation time.
Identify whether pending work is at period end or current status, with timestamp; preserve unavailable snapshots/history as gaps.
Find by key before creation; identical scope identifies one report with successive revisions, and retries cannot duplicate it.
Retain prior report/input revisions so exact inputs remain retrievable after edits. Preserve human narrative edits during regeneration.
If storage cannot retain a prior revision, resolve replacement before overwriting. Live views supplement, never replace saved narratives/manifests.
Read back uncertain writes by key; return a verified reference or partial/unsaved payload with missing steps, without repeating saved effects.
