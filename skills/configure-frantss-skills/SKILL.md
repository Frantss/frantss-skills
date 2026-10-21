---
name: configure-frantss-skills
description: "Configure Frantss skills under ~/.frantss. Use for initialization, configuration questions, requested updates, or lasting workspace/source changes stated by the user during conversation. Incidental source activity and ordinary implementation requests alone do not activate it."
---

# Configure Frantss skills

Select setup for explicit initialization/creation commands, inspect for read-only questions, or maintain for changes to existing configuration.
For requested updates or lasting configuration changes stated by the user during conversation, read [maintenance](references/maintenance.md).
General setup prepares only `~/.frantss` and presents available configurations; it enables none by default.
Load only selected guides; a request for all configurations selects every supported entry below. Report unsupported requests without inventing schemas or defaults.

| Configuration | Stored in | Guide |
| --- | --- | --- |
| Persistence connection | `~/.frantss/persistance.yaml` | [Persistence](references/persistence.md) |
| Workspace registration and associations | `~/.frantss/workspaces.yaml` | [Workspace](references/workspace-identity.md) |
| Sources and tracking settings | Workspace config sources; backend shared settings | [Tracking](references/sources.md) |

Expand `~` using the current user's home, independently of the repository or working directory; never search ancestors for configuration.
Backend setup requires no workspace; workspace/source updates resolve local registry IDs and require no backend connection.
Before writes, read [directory setup](references/workspace.md), then follow selected guides; backend-only updates need no local directory writes.
Patch only established changes; preserve unknown fields, human edits, sibling configurations, and unrelated files.
Keep credentials in tool credential stores. Never change agent-wide instructions during configuration.

Verify guide completion and read back changes; report applied changes, connection/access status, partial setup/dependencies, unsupported operations, and recovery needs.
