---
name: frantss-persistance
description: "Persist and retrieve prepared Frantss records through one backend. Use for save, read, query, history, and persistence handoffs. Configuration changes, source scans, workflow decisions, and ordinary note editing belong elsewhere."
---

# Frantss persistance

The caller supplies domain schemas, relationships, content, and requested changes; the adapter owns physical storage and recovery.
Read only `~/.frantss/persistance.yaml`, expanding the current user's home independently of the working directory.
Require `schema_version: 1` and `backend: {adapter: <skill-name>, options: <mapping>}`; parse configuration as data.
One backend serves every workspace; reject per-workspace overrides. Pass configured options unchanged to the selected adapter.
Use `frantss-persistance-obsidian` when selected and available; missing configuration/capabilities leave requests explicitly unsaved, never in another store.
Workspace/source definitions remain in `~/.frantss/workspaces.yaml`; supplied workspace references are readable strings, never backend workspace records.
Configuration inspection/changes belong to `frantss-configure-skills` when available; record operations never initialize configuration or create workspaces.

Before record operations, read [common fields](references/records.md) and [operation requirements](references/operations.md).
For shared settings or account references, also read [settings](references/settings.md).
Pass complete domain fields/schema, stable identities, expected revisions, related records, filters, limits, and requested cutoff to the adapter.
If a required domain schema is missing, ask for it rather than inventing fields or workflow decisions.

Check returned records/revisions against requested changes and require a result for every related write.
Return verified references, scope, gaps, and unsaved inputs; preserve identities and payloads for recovery of partial operations.
