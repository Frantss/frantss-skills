# Sources and shared settings

Sources live in each project registry entry; use [registry writes](project-identity.md). Shared settings/accounts use `frantss-persistance` when available. Each mapping has project-unique stable `id`, `provider`, frantss's `identity`, and bounded provider-specific `scope`. Hosted providers also require native `instance`; local Git derives repository identity from its paths. Identity is a native string or `{account_ref: <alias>}` into shared settings; the authenticated agent account never substitutes for frantss.

| Provider | Instance; scope |
| --- | --- |
| `github` | Host; `repositories` owner/name pairs |
| `git` | No configured instance; `repositories` canonical absolute checkout roots; identity is an exact author email |
| `slack` | Workspace ID; nonempty `channels`/`threads` and/or `messages: authored-or-mentioned` |
| `jira` | Site URL; `projects` keys or bounded `issue_filter` |
| `loom` | Workspace/organization ID or URL; `spaces` or `recordings` IDs/URLs |
| `gmail` | Mailbox address; `labels` or bounded `thread_filter` |
| `google-calendar` | Google account; `calendars` IDs |

Keep repository locations only in sources. For project resolution, combine a `github` instance host with each scoped repository.
Git source paths refer to the machine that holds this configuration. Resolve configured checkout roots and compare canonical Git common directories, so linked worktrees share identity. Distinct clones remain distinct local sources. Use GitHub for hosted repository events and Git for local commit activity. Git sources do not require a remote or GitHub access. Verify configured roots with read-only Git commands. Offer the effective Git author email as an identity candidate; preserve an explicitly supplied email. Multiple author emails use separate source mappings.
Changing an existing source provider preserves its ID but replaces provider-specific instance, identity, and scope together; old collection coverage cannot resume under the new provider. Git is additive under registry schema version 1; upgrades preserve existing sources and records without conversion. Read back explicit provider switches and retry only unsaved changes. Use native IDs/canonical URLs; ambiguous labels need clarification. Store location/identity data without credentials or tool bindings/preferences.
Slack identity must resolve to a native member ID. `messages: authored-or-mentioned` alone spans the workspace and matches that ID as author or direct mention; supplied nonempty `channels`/`threads` restrict those matches.
Collection chooses available tools at runtime. Check bounded location/identity metadata without collecting activity; unavailable checks remain unverified. An empty source list enables no collection; missing identity or empty/ambiguous scope is incomplete, never permission for an unrestricted scan.
