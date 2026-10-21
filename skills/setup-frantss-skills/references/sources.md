# Tracking configuration

For requested tracking settings/accounts, use the `frantss-persistance` schema; preserve existing fields and resolve timezone/week start when needed. Read [persistence setup](persistence.md) for connection checks.
Store workspace `sources` in its backend record; the catalog below defines supported providers for setup.
Each mapping has workspace-unique stable string `id`, `provider`, `account`, user `identity`, and bounded `scope`.
Account identifies the native instance/tenant/mailbox, not a tool profile; identity is the user's native identifier or shared account-identity reference.

| Provider | Scope and account requirements |
| --- | --- |
| `git` | `account`: repository host or stable machine identifier; scope: `repository` path/remote and `branches` |
| `github` | `account`: host; scope: `repositories` as owner/name pairs |
| `slack` | `account`: Slack workspace ID; scope: `channels` or `threads` |
| `jira` | `account`: Jira site URL; scope: `projects` keys or bounded `issue_filter` |
| `loom` | `account`: workspace/organization ID or URL; scope: `spaces` or `recordings` IDs/URLs |
| `gmail` | `account`: mailbox address; scope: `labels` or bounded `thread_filter` |
| `google-calendar` | `account`: Google account; scope: `calendars` IDs |

Prefer stable native IDs or canonical URLs; display names are labels, and ambiguous targets require clarification.
Store locations and actor identities, without `access`, commands, CLI/API/MCP/plugin/skill bindings, credentials, or tool preferences.
Collection chooses available capabilities at runtime; the authenticated agent account never replaces the configured user identity.
Check bounded identity/location metadata when tools allow, without collecting activity; mark unavailable checks unverified rather than invalidating a complete definition.
Patch only requested sources; preserve stable IDs and unrelated fields. Ignore legacy `access` fields at runtime and remove them only on requested source updates.
An empty list enables no collection; missing identity or empty/ambiguous scope is incomplete, never permission to collect everything.
