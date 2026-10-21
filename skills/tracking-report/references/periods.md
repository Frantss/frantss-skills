# Periods and history

Use inclusive-start/exclusive-end local calendar intervals, converting boundaries for timestamp queries; state exact boundaries/timezone.
Today/this week end now; a specified past day spans midnight to next midnight. Last week is the previous full configured week.
Resolve unknown timezone/week start from the request/settings or ask; clarify ambiguous custom-range end dates.
Attribute activity by occurrence, not collection time; unsupported occurrence dates stay unknown and cannot establish dated completion.
Reconstruct task state, dates, and blockers at the declared cutoff from dated events/revisions; distinguish historical from current pending work.
If history is insufficient, label historical state unknown and displayed current state with its current cutoff.
A completion followed by reopening remains a dated completion; show later reopening separately.
For due/expected grouping use the full local day/week at the cutoff, just before exclusive period ends, even when activity ends now.
Historical groups use dates/fields known at cutoff; missing snapshots remain gaps, never replacements with current values.
