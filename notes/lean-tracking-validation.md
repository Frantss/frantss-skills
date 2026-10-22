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
Original revisions and retired notes remain in verified external backups. Missing evidence blocks
the affected conversion. A retry reuses the migration journal's identities.
After reference/back-up checks, remove retired notes/history from active storage. Never substitute a retrieval date.

## Invocation boundaries

| Skill | Representative request and walkthrough result | Nearby request that does not activate it |
| --- | --- | --- |
| Collect | Collect yesterday's activity: temporary findings and task-link handoffs | Retrieve saved daily report: report lookup only |
| Tasks | Track a stated follow-up: task with links, no event note | Create daily report: no task capture or triage |
| Report | Create daily report: saved summary and links | Collect activity only: no report save |
| Persistence | Save a prepared task/schema: delegate one logical record | Search project sources: collection owns source access |
| Obsidian adapter | Save selected-backend task: One current Tasks note, replaced if changed | Edit an unrelated note: ordinary editing |
| Configure | Remove a configured source: patch configuration and preserve tasks/reports | Quoted suggestion to remove a source: no configuration write |

## Structural checks

`make validate` passed, with existing private-package license/version/icon
warnings. All skills installed into the temporary directory, including the
migration reference. `git diff --check` passed. Runtime adapter behavior and
live-data migration remain untested.

## Human-readable Obsidian names

Additional manual walkthrough against the updated adapter and common record
rules. This checks instruction decisions, without a live rename or link update.

| Fixture | Walkthrough result |
| --- | --- |
| Task titled “Fix invoice export” with a UUID property | `Tasks/Fix invoice export.md`; UUID remains in `id` |
| Gildara daily report for 2026-10-20 | `Reports/2026-10-20 - Gildara daily report.md` |
| Two distinct tasks with the same title/project | Add readable project context and then `(2)` when needed; keep distinct IDs and reuse chosen paths on retries |
| Task title containing `/`, `:`, `[`, `]`, and `#` | Replace unsafe characters before path creation; retain the original meaningful title in properties |
| Existing task renamed after its outcome changes | Find by ID/key, save the changed title in place, rename through FileManager, and verify inbound links and lookup |
| Path-only rename with unchanged content | Preserve ID/key and logical revision; do not manufacture a new task or logical revision |
| Historical task revision | Return unsupported for unavailable prior revisions; use saved reports or dated sources for historical state |
| Interrupted migration from a UUID path | Resolve the journaled ID/revision at old/new paths; reuse a verified move and conflict on another identity at the target |
| Internal-link auto-update disabled | Inspect and repair affected references; preserve the user's setting and report unresolved links as partial |
| Request to edit an unrelated Obsidian note | Do not activate the adapter or apply database naming migrations |

The rename method and its dependence on user link settings were checked against
the official [Obsidian API declarations](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts).
Existing vault notes and agent installations remain unchanged by this exercise.

## Current-record cleanup correction

The previous migration retained retired notes/history in the active vault. The
corrected workflow keeps only current tasks, saved report summaries, settings,
and requested views. Migration backups and journals remain outside the vault.

Manual walkthrough of the corrected instructions:

- Change T1's state: compare current content, replace one note, increment its
  revision, and read back. Create no history/event/evidence record.
- Retry after an uncertain write: compare with the intended result; return the
  verified current record without a second change or archive.
- Regenerate R1: update the same period/scope key in place, preserve human edits,
  and retain its task/source links. Create no prior-report note.
- Request T1's old revision: return unsupported; use saved reports or dated
  sources for historical reporting without inventing a prior state.
- Cleanup legacy notes: verify external backup and retained inbound references,
  trash only unchanged retired records, and retain tasks/settings/custom notes.
- Nearby request to edit an unrelated Obsidian note: use ordinary note editing;
  neither persistence nor its cleanup migration applies.
