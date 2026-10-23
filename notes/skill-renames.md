# Skill renames

Skills use `core-`, `bdd-`, `tracking-`, and `persistence-` prefixes.
BDD names are unchanged. Use [core-update](../skills/core-update/SKILL.md)
to upgrade older installations with its backup and recovery checks.

| Earlier name | Current name |
| --- | --- |
| `frantss-communicate` | `core-communicate` |
| `frantss-configure` | `core-configure` |
| `frantss-update` | `core-update` |
| `frantss-tracking-tasks` | `tracking-tasks` |
| `frantss-tracking-collect` | `tracking-collect` |
| `frantss-tracking-report` | `tracking-report` |
| `frantss-persistance` | `persistence-records` |
| `frantss-persistance-obsidian` | `persistence-obsidian` |

Map selected skills and agent instruction references; `all` stays `all`.
Verify replacements before removing old owned folders. Preserve local edits
and unrelated installations.

In `~/.frantss/persistance.yaml`, replace only
`backend.adapter: frantss-persistance-obsidian` with `backend.adapter: persistence-obsidian`.
Preserve other settings, configuration paths, stored records, and BDD runs.
This rename needs no data migration or storage initialization.
Verify installed selections and adapter reads before completing the upgrade.
