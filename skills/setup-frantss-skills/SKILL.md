---
name: setup-frantss-skills
description: "Set up, inspect, or update user-wide Frantss skills configuration under ~/.frantss and workspace records in the backend. Load guides for requested connections, workspace registration, or tracking sources. Ordinary use of configured skills does not initiate setup."
---

# Setup Frantss skills

Manage configuration files and records; distinguish initialization, requested updates, and read-only inspection.
General setup prepares only `~/.frantss` and presents available configurations; it enables none by default.
Load only selected guides; a request for all configurations selects every supported entry below. Report unsupported requests without inventing schemas or defaults.

| Configuration | Stored in | Guide |
| --- | --- | --- |
| Persistence connection | `~/.frantss/tracking.yaml` | [Persistence](references/tracking.md) |
| Workspace registration and associations | Backend workspace record | [Workspace](references/workspace-identity.md) |
| Tracking settings and sources | Backend settings/workspace records | [Tracking](references/sources.md) |

Expand `~` using the current user's home, independently of the repository or working directory; never search ancestors for configuration.
Backend setup requires no workspace; workspace/source operations resolve existing backend identities before updates.
Before writes, read [directory setup](references/workspace.md), then follow selected guides; backend-only updates need no local directory writes.
Inspection creates or repairs nothing, including dependencies.
Patch only requested fields; preserve unknown fields, human edits, sibling configurations, and unrelated files.
Keep credentials in tool credential stores. Never change agent-wide instructions during setup.

Verify guide completion and read back changes; return connection/access status, per-configuration results, unsupported operations, and unresolved requirements.
Distinguish prepared directories from partial configuration/dependency setup; retain drafts and recovery steps.
