# Tracking configuration migration

Use only through an explicitly requested `migrate-tracking`, with its verified backups, fixed mappings, journal, and content checks. Preserve IDs, native identities/locations, human edits, unknown fields, and unrelated entries.
Applies to legacy source selectors in `~/.frantss/projects.yaml` version 1 or database Settings notes; current configuration needs no rewriting.

1. Back up originals outside active storage. Retired Slack `messages`/`channels`/`threads`, Jira `issue_filter`, and Gmail `labels`/`thread_filter` no longer restrict searches. Remove only these owned fields; omit empty Slack/Gmail scopes. If Jira has only a legacy filter, recover native project keys only from an unambiguous project constraint or verified registration; unresolved locations block that source, never permit site-wide fallback.
2. Merge non-null legacy Settings `timezone`, `week_start`, and `accounts` into local registry `settings` without overwriting conflicts. Use IANA timezone strings, ISO weekday 1–7, and account aliases mapped to native `{provider, instance, identity}` strings; empty values need no YAML section. Resolve unsupported legacy fields; discard retired `collection_limits` and record-envelope metadata only after backup.
3. Verify normalized source locations and fixed-policy selection, settings read-back, and inbound references. Pre-policy source handoffs require bounded rescans; never treat broader current searches as verified legacy coverage.
4. Trash an unchanged legacy Settings note through the adapter only after the merged configuration, inbound references, and external backup verify. Journal expected content; on retry, reuse verified patches and finish only missing steps. Source-selector cleanup alone requires no record conversion.
