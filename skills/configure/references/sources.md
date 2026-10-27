# Sources and shared settings

Sources live in project registry entries; use [registry writes](project-identity.md). Each has project-unique stable `id`, `provider`, the user's native `identity` or `{account_ref: <alias>}`, and hosted `instance` when applicable. Resolve account aliases through local `settings.accounts` below. `scope` holds only required native project locations below; Slack/Gmail need no scope. Authenticated-agent identity never substitutes for the user.

| Provider | Instance; project locations |
| --- | --- |
| `github` | Host; `repositories` owner/name pairs |
| `git` | No configured instance; `repositories` canonical absolute checkout roots; identity is an exact author email |
| `slack` | Workspace ID; identity is a native member ID; no selectors |
| `jira` | Site URL; `projects` keys; identity is a native account ID |
| `loom` | Workspace/organization ID or URL; `spaces` or `recordings` IDs/URLs |
| `gmail` | Mailbox address; no selectors |
| `google-calendar` | Google account; `calendars` IDs |

Keep repository locations only in sources; GitHub host plus repository identifies remotes for project resolution. Local Git paths belong to this machine: verify checkout roots read-only and compare canonical Git common directories to deduplicate worktrees; distinct clones stay distinct. Offer effective author email, preserve explicit identity, and use separate mappings for multiple emails. Git needs no remote or hosted access.
Provider switches retain source ID but replace native instance/identity/locations together; old handoffs become incompatible. Use native IDs/canonical URLs; ambiguous labels need clarification. Store no credentials, tool preferences, search modes, queries, or optional search restrictions.
Check only bounded location/identity metadata during setup; unavailable checks remain unverified. Empty source lists enable no collection; unresolved identity or missing required project locations remains incomplete. Collection owns one fixed policy per provider, with no source-level overrides.
Registry version 1 remains: retired Slack `messages`/`channels`/`threads`, Jira `issue_filter`, and Gmail `labels`/`thread_filter` have no search effect; ordinary reads leave them untouched. Legacy-only Jira filters leave source locations unresolved; never use site-wide fallback. Route requested legacy conversion to `migrate-tracking` when available.
Shared preferences use optional top-level `settings` in `~/.frantss/projects.yaml` version 1: `timezone` (IANA string or null), `week_start` (ISO weekday 1–7 or null), and `accounts` (alias to `{provider, instance, identity}` native strings). No database records or credentials.
Missing preferences stay unconfigured; request values precede stored values, missing accounts means `{}`, and provider/instance must match each alias. Save only requested changes through registry writes; search policies/budgets remain fixed.
Legacy database Settings notes require an explicitly requested `migrate-tracking` when available; ordinary setup and maintenance leave them untouched.
