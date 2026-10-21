# Periods and historical status

Use local calendar intervals with an inclusive start and exclusive end; convert boundaries when querying timestamps.
Today and this week end at the current instant. A specified past day spans that local date's midnight to the next midnight.
Last week means the previous full configured calendar week. Resolve an unknown week start before a weekly query.
State exact boundaries and timezone. For custom ranges, clarify whether an ambiguous ending date is included.

Attribute activity by occurrence time, not collection time. An observation collected later can belong to an earlier day's report.
Keep unsupported occurrence dates unknown; exclude them from dated completion claims and explain the uncertainty.
Reconstruct pending work at period end from dated task history. Distinguish that result from what remains pending now.
If history cannot establish prior status, label historical status unknown and any displayed current status with its current cutoff.
A task completed during the period and reopened later retains its completion event; show its later reopening separately.
