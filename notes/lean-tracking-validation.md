# Lean tracking validation

Manual instruction walkthrough against a temporary `gh skill install . --all
--from-local --dir <temporary-directory>` copy. Inputs below are synthetic.
No live connector, Obsidian write, or database migration was exercised.

## Collection and report fixture

Scope: `sample/widget`, 2026-10-20, `America/Montevideo`. Existing task T1 is
Next: “Fix invoice export,” with an issue link and no completion date.

Source inputs:

- Frantss: “I'll finish the invoice export fix today,” linked to T1's issue.
- A second connector result wraps the same native message.
- Frantss reviewed a separate permissions change, with a dated review link.
- A calendar item shows a scheduled discussion, without evidence it occurred.
- One source is inaccessible; another result has no supported occurrence date.

Walkthrough results:

1. Direct collection uses automatic capture. The duplicate message becomes one
   finding. Match T1 by outcome/source; merge the message link and supported
   expected date into T1. Create no evidence, run, or event records.
2. The review remains temporary report input. Create no completed task for it.
   The scheduled discussion establishes no performed work. Undated activity
   establishes no dated completion. Return the inaccessible source as a gap.
3. A separate report request uses `capture: none`. Even a newly discovered
   commitment remains a candidate; reporting changes no task fields or links.
4. The report summarizes the review and T1's pending outcome. Its domain fields
   are type, projects, window, timezone, generation time, task IDs, source links,
   narrative, status cutoff, and brief coverage. The report is partial because
   of source access. It contains no transcript, input manifest, or cursor log.
5. An identical retry reuses task/report keys and payloads, including generation
   time. Existing links remain unique; no new logical revision is needed.
6. A saved-report lookup returns its saved summary and gaps without collection
   or writes. An existing-evidence-only report uses saved summaries/task links
   without opening source links. An unknown historical task state stays unknown.

## Migration fixture

Legacy task T2 has an evidence ID and `history_complete`; legacy report R2 has
evidence IDs and a manifest. One evidence note has a URL; another has only a
repository locator and full commit hash.

Ordinary task/report operations return unsupported for those legacy shapes.
For an explicit update, the documented mapping preserves T2/R2 IDs and keys,
resolves both link forms, merges task links, and maps report cutoff/coverage.
Original revisions and retired notes remain available. Missing evidence blocks
the affected conversion. A retry reuses the migration journal's identities.
No step authorizes deleting the old archive or substituting a retrieval date.

## Invocation boundaries

| Skill | Representative request and walkthrough result | Nearby request that does not activate it |
| --- | --- | --- |
| Collect | Collect yesterday's activity: temporary findings and task-link handoffs | Retrieve saved daily report: report lookup only |
| Tasks | Track a stated follow-up: task with links, no event note | Create daily report: no task capture or triage |
| Report | Create daily report: saved summary and links | Collect activity only: no report save |
| Persistence | Save a prepared task/schema: delegate one logical record | Search project sources: collection owns source access |
| Obsidian adapter | Save selected-backend task: Tasks note and prior revision if changed | Edit an unrelated note: ordinary editing |
| Configure | Remove a configured source: patch configuration and preserve tasks/reports | Quoted suggestion to remove a source: no configuration write |

## Structural checks

`make validate` passed, with existing private-package license/version/icon
warnings. All skills installed into the temporary directory, including the
migration reference. `git diff --check` passed. Runtime adapter behavior and
live-data migration remain untested.
