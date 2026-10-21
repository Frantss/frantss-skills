# Tracking configuration

For requested tracking settings/accounts, use the `frantss-persistance` schema; preserve existing fields and resolve timezone/week start when needed. Read [persistence setup](persistence.md) for connection checks.
Store workspace `sources` in its backend record; the catalog below defines supported providers for setup.
Each mapping has workspace-unique stable string `id`, `provider`, `account`, user `identity`, bounded `scope`, and nonempty `access` list.
Account identifies a host/account or tenant; identity is a user identifier or shared account-identity reference.

| Provider | Scope and account requirements |
| --- | --- |
| `git` | `repository` path or remote; `branches` |
| `github` | `repositories` as owner/name pairs; `account` identifies the host/account |
| `slack` | Slack `workspace` ID; `channels` or `threads` |
| `jira` | `site`; `projects` keys or bounded `issue_filter` |
| `loom` | `spaces` or `recordings` links |
| `gmail` | `labels` or bounded `thread_filter`; `account` identifies the Google account |
| `google-calendar` | `calendars` IDs; `account` identifies the Google account |

Access entries have `kind` and these fields; optional fields are marked optional.
| Kind | Fields |
| --- | --- |
| `cli` | `executable`; optional `profile`, command `guidance` reference |
| `api` | `base_url`, `docs` reference; `auth_ref` when authentication is required |
| `skill` | `name` or `path` |
| `mcp` | `server`, relevant `tools` names |
| `plugin` | `id`; optional relevant `skills` or `tools` names |

Combine methods when referenced guidance requires it; prefer earlier entries when methods are interchangeable.
Resolve exact identifiers and dependencies from supplied configuration, workspace metadata, or available tools; clarify ambiguous scope or identity.
Check availability and bounded identity/location metadata without collecting activity; report unavailable checks as unverified and unsupported entries explicitly.
Install or enable dependencies only when requested. Keep credentials outside configuration; store references without secret values.
Patch only requested sources and retain stable IDs; access changes preserve existing evidence identity. Read back mappings and unknown fields.
An empty list enables no collection. Missing access or empty/ambiguous scope is incomplete, never permission to collect everything.
