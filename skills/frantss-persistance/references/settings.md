# Shared settings

Settings are one backend-wide singleton, independent of project identity; use the common fields from [logical records](records.md).
Use `record_type: settings` and `key: settings`; allocate one UUID on explicit initialization and reuse it for updates/retries.
Read and patch settings through the same logical save/read operations; preserve revisions, unknown fields, and existing values.

| Field | Logical value |
| --- | --- |
| `timezone` | IANA timezone string, or null while unresolved |
| `week_start` | ISO weekday integer 1 (Monday) through 7 (Sunday), or null while unresolved |
| `accounts` | Mapping of stable aliases to `{provider, instance, identity}`; all three values are nonempty native identifier strings |

Missing `accounts` defaults to an empty mapping. Collection uses fixed limits of 20 calls/50 items per project/source; settings cannot override search behavior or budgets.
Timezone and week start have no implicit defaults; resolve them when required, using explicit request values before stored settings.
Reading defaults does not initialize or save settings. Store only requested changes; credentials remain outside this payload.
A source's `identity` is a native string or `{account_ref: <alias>}` into `accounts`.
Resolve references before collection; provider/instance must match the source. Missing aliases or conflicting identities require clarification.
Retain supplied aliases in configuration and resolved native identity in evidence attribution; never substitute the agent's authenticated identity silently.
Retired `collection_limits` has no effect. On explicit update, back up then remove that owned field/Collection limits section; preserve singleton identity, revisions, accounts, other settings, and human edits. Verify read-back and fixed-policy selection; journal expected content and retry only missing changes.
