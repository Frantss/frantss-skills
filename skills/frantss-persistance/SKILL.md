---
name: frantss-persistance
description: "Store and retrieve prepared Frantss records using caller-supplied schemas. Use for persistence handoffs, record saves and queries, or current-record lookups; configuration changes and source scans belong elsewhere."
---

# Frantss persistance

The caller supplies domain schemas, relationships, content, and requested changes; the adapter owns physical storage and recovery.
Read only `~/.frantss/persistance.yaml`, expanding the current OS account's home independently of the working directory.
Require `schema_version: 1` and `backend: {adapter: <skill-name>, options: <mapping>}`; parse configuration as data.
One backend serves every project; reject per-project overrides. Pass configured options unchanged to the selected adapter.
Use `frantss-persistance-obsidian` when selected and available; missing configuration/capabilities leave requests explicitly unsaved, never in another store.
Project/source definitions remain in `~/.frantss/projects.yaml`; supplied project references are readable strings, never backend project records.
Configuration inspection/changes belong to `frantss-configure` when available; record operations never initialize configuration or create projects.

Before record operations, read [common fields](references/records.md) and [operation requirements](references/operations.md).
For an explicitly requested legacy tracking upgrade, read [migration rules](references/lean-migration.md); ordinary operations never migrate data.
Pass complete domain fields/schema, stable identities, expected revisions, related records, filters, limits, and requested cutoff to the adapter.
If a required domain schema is missing, ask for it rather than inventing fields or workflow decisions.

Check returned records/revisions against requested changes and require a result for every related write.
Return verified references, scope, gaps, and unsaved inputs; preserve identities and payloads for recovery of partial operations.
