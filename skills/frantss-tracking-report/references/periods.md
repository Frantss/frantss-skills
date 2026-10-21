# Periods and history

Use inclusive-start/exclusive-end local calendar intervals, converting boundaries for timestamp queries; state exact boundaries/timezone.
Today/this week end now; a specified past day spans midnight to next midnight. Last week is the previous full configured week.
Resolve unknown timezone/week start from the request/settings or ask; clarify ambiguous custom-range end dates.
Attribute activity by occurrence, not collection time; unsupported occurrence dates stay unknown and cannot establish dated completion.
Use retained task revisions for fields recorded at the declared cutoff; source-supported dates and saved reports establish occurrence separately.
If history is insufficient, label historical state unknown and displayed current state with its current cutoff.
A saved report or dated source can support an earlier completion followed by reopening; missing transition history stays unknown.
For due/expected grouping use the full local day/week at the cutoff, just before exclusive period ends, even when activity ends now.
Historical groups use dates/fields known at cutoff; missing snapshots remain gaps, never replacements with current values.
