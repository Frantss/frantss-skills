# Source access

Each source identifies project-local `id`, `provider`, frantss's `identity`, and required project locations in `scope`. Hosted sources require native `instance`; local Git derives it from repository common directories. Slack/Gmail use their instance without selectors.
Resolve `{account_ref: <alias>}` identities through shared settings; provider/instance must match. Never substitute authenticated-agent identity.
Use native IDs/locations independently of tool profiles; empty source lists enable no collection. Unresolved identity or required locations need clarification. Retired search options have no effect; registrations supply where/who, never search behavior.
Choose tools at runtime; preserve instance, identity, and restrictions across methods. Unavailable access/dependencies leave gaps; continue accessible branches without installing dependencies, broadening scope, or source writes.
Use inclusive-start/exclusive-end local calendar windows converted to source time; supplied timezone/week start precede shared settings, with no guessed defaults.
Retrieve only necessary attribution/meaning/date context around personal matches; distinguish performed actions, assignments, scheduled activity, and quotations. Attribute native actors and dated events; older context and unsupported/inferred dates retain uncertainty.
Keep non-secret capability/query scope and cursors in temporary handoffs; resume only for compatible method, instance, identity, fixed provider policy, project locations, and window. Older handoffs require bounded rescans.

Before any source search, read [fixed personal policies](personal.md); for `provider: git`, also read [Git collection](git.md).
