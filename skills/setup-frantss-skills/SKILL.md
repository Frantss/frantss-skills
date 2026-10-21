---
name: setup-frantss-skills
description: "Set up, inspect, or change personal tracking configuration: the shared backend in .frantss/tracking.yaml, reporting settings, account identities, and explicitly requested project/source mappings. Ensure .frantss is ignored by Git. Ordinary task capture, collection, and report requests do not initiate setup."
---

# Setup Frantss skills

Configure one backend shared by all tracked projects. Use real filesystem tools and an available persistence adapter.
Own only `.frantss/tracking.yaml`; preserve configuration files for other skills in the shared `.frantss` directory.
Read [configuration](references/configuration.md) for discovery, schema, and ownership before selecting or changing settings.
For inspection or checks, report resolved configuration and read-only access checks; do not run initialization or repairs.

## Configure

1. Resolve the selected configuration workspace, independently of the projects being tracked.
   Reuse an existing config; when creating one, use an explicitly selected workspace or the current Git root, otherwise ask.
2. Resolve the adapter and required connection options with the user. Never save example paths as actual destinations.
   Keep missing values as unresolved draft fields; setup remains partial until the adapter verifies its required options.
3. Before writing config, follow [Git exclusion](references/configuration.md#git-exclusion).
   Preserve existing config fields and human edits. Parse YAML as data; reject unsupported schema versions or conflicting backend selections.
4. Write `.frantss/tracking.yaml` with one backend. Create or patch it safely, then parse and read back the saved selection.
   All projects use that backend; per-project backend overrides are unsupported.
5. If its skill is available, pass the selected options to the adapter for explicit storage initialization.
   Otherwise retain the connection draft and report the unavailable adapter; do not claim backend setup succeeded.
6. Save supplied timezone, week start, account identities, and collection limits through the adapter's settings operation.
   Preserve existing settings; ask for missing timezone/week start when required, rather than guessing them.
7. For explicitly requested project creation, resolve its name and work/personal area; use `tracking-tasks` when available.
   Without it, persist only an explicitly authorized project payload. Setup alone creates no project records.
   Apply supplied source mappings to exact existing projects; resolve ambiguous targets and identities before changing their scope.

Changing a backend selection does not migrate records. Preserve the previous selection and explain any separate migration requirement.
Do not scan sources, capture tasks, generate reports, or change agent-wide instructions as part of setup.

## Finish

Return the config path, selected backend, Git exclusion result, verified settings/project changes, and unresolved requirements.
Verify project/source records through persistence and confirm every project still shares the same backend.
Report partial config/backend writes with their saved locations and missing steps. An ignored draft is not a configured backend.
