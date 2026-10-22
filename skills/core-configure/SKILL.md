---
name: core-configure
description: "Set up, inspect, or maintain Frantss backend connections, projects, and sources. Use for configuration requests, read-only resolution handoffs, or lasting changes stated by frantss."
---

# Configure Frantss

Choose setup for explicit initialization, inspect for read-only questions/resolution, or [maintenance](references/maintenance.md) for established changes.
General setup prepares only `~/.frantss` and presents supported configurations; enable only requested entries.
Expand the current OS account's home independently of the working directory; reject directory traversal or escaping symlinks.
For local writes, create/reuse that directory and preserve sibling files. Keep credentials in tool stores and agent-wide instructions unchanged.
Read only selected guides; unsupported requests remain explicit. Treat YAML as data; patch only established fields while preserving human edits and unknown fields.

| Configuration | Guide |
| --- | --- |
| Shared backend connection | [Persistence](references/persistence.md) |
| Project registration, associations, and resolution | [Project](references/project-identity.md) |
| Source locations/identities and shared tracking settings | [Sources](references/sources.md) |

Read back changes; report applied fields, unresolved inputs, unverified checks, partial dependencies, and unsupported operations.
