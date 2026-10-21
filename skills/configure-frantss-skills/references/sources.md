# Sources and shared settings

Sources live in each workspace registry entry; use [registry writes](workspace-identity.md). Shared settings/accounts use `frantss-persistance` when available.
Each mapping has workspace-unique stable `id`, `provider`, native instance `account`, user `identity`, and bounded provider-specific `scope`.
Identity is a native string or `{account_ref: <alias>}` into shared settings; the authenticated agent account never substitutes for the user.

| Provider | Account; scope |
| --- | --- |
| `git` | Host/stable machine ID; `repository` path/remote and `branches` |
| `github` | Host; `repositories` owner/name pairs |
| `slack` | Workspace ID; `channels` or `threads` |
| `jira` | Site URL; `projects` keys or bounded `issue_filter` |
| `loom` | Workspace/organization ID or URL; `spaces` or `recordings` IDs/URLs |
| `gmail` | Mailbox address; `labels` or bounded `thread_filter` |
| `google-calendar` | Google account; `calendars` IDs |

Use native IDs/canonical URLs; ambiguous labels need clarification. Store location/identity data without credentials or tool bindings/preferences.
Collection chooses available tools at runtime. Check bounded location/identity metadata without collecting activity; unavailable checks remain unverified.
An empty source list enables no collection; missing identity or empty/ambiguous scope is incomplete, never permission for an unrestricted scan.
