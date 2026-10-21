---
name: setup-frantss-skills
description: "Set up, inspect, or update Frantss skills configuration under .frantss, including tracking sources. Prepare the shared configuration directory and Git exclusion, then load guides for requested configurations. Ordinary use of configured skills does not initiate setup."
---

# Setup Frantss skills

Manage configuration files and records; distinguish initialization, requested updates, and read-only inspection.
General setup prepares only `.frantss` and presents available configurations; it enables none by default.
Load only selected guides; a request for all configurations selects every supported entry below. Report unsupported requests without inventing schemas or defaults.

| Configuration | Owned file | Guide |
| --- | --- | --- |
| Workspace identity | `workspace.yaml` | [Workspace](references/workspace-identity.md) |
| Tracking | `tracking.yaml` | [Tracking](references/tracking.md) |

Use an explicitly selected workspace, otherwise the current Git root.
Outside Git, use an explicit workspace or unique ancestor `.frantss`; ask when unresolved or ambiguous.
An external tracking connection never changes the selected workspace.
Before writes, read [directory setup](references/workspace.md), prepare `.frantss`, then follow selected guides.
Inspection creates or repairs nothing, including dependencies and Git exclusion.
Patch only requested fields; preserve unknown fields, human edits, sibling configurations, and unrelated files.
Keep credentials in tool credential stores. Never change agent-wide instructions during setup.

Verify guide completion and read back changes; return directory/exclusion status, per-configuration results, unsupported operations, and unresolved requirements.
Distinguish prepared directories from partial configuration/dependency setup; retain drafts and recovery steps.
