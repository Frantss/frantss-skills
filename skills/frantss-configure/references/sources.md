# Sources and shared settings

Sources live in each project registry entry; use [registry writes](project-identity.md). Shared settings/accounts use `frantss-persistance` when available.
Each mapping has project-unique stable `id`, `provider`, native `instance`, frantss's `identity`, and bounded provider-specific `scope`. Identity is a native string or `{account_ref: <alias>}` into shared settings; the authenticated agent account never substitutes for frantss.

| Provider | Instance; scope |
| --- | --- |
| `github` | Host; `repositories` owner/name pairs |
| `slack` | Workspace ID; nonempty `channels`/`threads` and/or `messages: authored-or-mentioned` |
| `jira` | Site URL; `projects` keys or bounded `issue_filter` |
| `loom` | Workspace/organization ID or URL; `spaces` or `recordings` IDs/URLs |
| `gmail` | Mailbox address; `labels` or bounded `thread_filter` |
| `google-calendar` | Google account; `calendars` IDs |

Keep repository locations only in sources. For project resolution, combine a `github` instance host with each scoped repository.
Use GitHub for repository events; local Git only resolves the checkout's root and remotes. Use native IDs/canonical URLs; ambiguous labels need clarification. Store location/identity data without credentials or tool bindings/preferences.
Slack identity must resolve to a native member ID. `messages: authored-or-mentioned` alone spans the workspace and matches that ID as author or direct mention; supplied nonempty `channels`/`threads` restrict those matches.
Collection chooses available tools at runtime. Check bounded location/identity metadata without collecting activity; unavailable checks remain unverified.
An empty source list enables no collection; missing identity or empty/ambiguous scope is incomplete, never permission for an unrestricted scan.
