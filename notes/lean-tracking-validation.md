# Task links, hierarchy, and report validation

Manual instruction walkthrough against a temporary local installation. These
synthetic fixtures check workflow decisions; they do not establish live source
completeness or execute task writes in the personal vault.

## Outcome capture

Scope: `sample/widget`, 2026-10-20, `America/Montevideo`.

| Finding/request | Walkthrough result |
| --- | --- |
| Assigned Jira outcome with a clear completion condition | Capture the owned task, then triage from supported commitment/timing |
| Authored implementation already completed, with supported occurrence date | Capture and triage Done even without a previously recorded promise; retain the completion date and source link |
| Opened PR, routine review, or Slack discussion without an owned outcome | Report activity; create no task |
| Accepted Slack follow-up to fix invoice exports | Match the outcome before creation; attach the discussion link |
| Ticket created for somebody else, or unclear ownership | Do not infer ownership; return an unsaved candidate/question |
| Explicitly capture a tentative idea | Capture Inbox, then Maybe if clear; no inferred commitment |
| Duplicate findings for the same outcome | One task with deduplicated links; identical retry creates no revision |
| Older completion finding for a task subsequently reopened | Preserve the later current state; earlier completion can inform historical reporting |
| Unknown completion date | Keep the date unknown; retrieval time never supplies it |

## Parent and subtask fixture

Jira J1 is the owned outcome “Improve registration.” Three PRs implement owned,
independently trackable outcomes: API, form, and failure coverage. The parent
has an acceptance condition requiring all three plus verified integration.

| Case | Walkthrough result |
| --- | --- |
| First capture | Create/verify one parent task, then three ordinary tasks referencing its ID through `parent` |
| Three distinct children share the same Jira link | Keep distinct suboutcomes; a shared source link cannot merge them |
| Three PRs are successive iterations of one fix | One task with three links, without manufactured subtasks |
| All three child outcomes complete; integration remains unverified | Three Done children; parent remains pending |
| Parent acceptance condition satisfied | One completed top-level outcome and three completed subtasks, never four deliveries |
| Additional nested child | Group under the highest verified ancestor; intermediate parents do not add top-level deliveries |
| Parent missing or inaccessible; self-link; cycle | Reject the invalid/uncertain relationship and expose the gap |
| Parent save fails | Dependent children remain unsaved; retry reuses the parent/child identities |
| Parent completes, reopens, or receives acknowledgment | No automatic child state/date/review changes; surface inconsistent states |
| Existing version-1 task without `parent` | Read as standalone; no migration write or invented grouping |

## Report and source boundaries

- Creating/refreshing a report uses automatic capture unless task writes are
  explicitly disabled. The task workflow persists clear owned outcomes/updates;
  the report re-reads changed tasks before composition.
- Explicit no-task-write requests return candidates without task writes. Source
  workers always stay read-only with `capture: none`; only the coordinator saves.
- Retrieving a saved report performs no source scan, capture, or report rewrite.
- Existing-evidence-only requests use saved summaries/links/session findings
  without opening source links. Inaccessible storage/sources remain gaps.
- Reviews/discussions without tasks remain report summaries and source links.
  No evidence/event/run/history records or source transcripts are persisted.
- Reports use supported occurrence dates and saved summaries for historical
  state; current task state cannot silently replace missing past state.

## Adapter and configuration boundaries

- Save parent IDs as quoted wikilinks to human-readable task notes; decode their
  target task IDs on reads. Derive children instead of storing a second list.
- A parent title rename preserves identity and repairs affected inbound links,
  including child parent links, without changing user link-update settings.
- Unknown/changed content conflicts before replacement; uncertain writes are
  read back by identity and only missing work is retried.
- Backend settings saves remain unsupported; preferences stay in local YAML.
- Editing an unrelated note uses ordinary note editing, without activating
  tracking, storage setup, or migration.
- A general implementation request alone does not create tracking records.

## Source names

| Finding/request | Walkthrough result |
| --- | --- |
| Jira VILL-8614 with original modal-title summary | Title is `VILL-8614 - Add missing question mark to discount code deactivation modal title`; filename has the same stem |
| Jira summary contains `[S1]`, punctuation, or a slash | Preserve the original title; sanitize only unsafe filename characters |
| Distinct regression-test child links the same Jira issue | Keep its own source title or suboutcome qualifier; do not rename it to the entire Jira outcome |
| No named source exists | Use a concise owned-outcome title |
| Explicit rename of an existing source-backed task | Preserve stable identity/state, update its title and readable path, and repair child/report links with exact-content conflict checks |
| Read a saved report or edit an unrelated note | No source scan, task-title change, or naming migration |
| Source title unavailable or outcome-to-source match unclear | Preserve the existing name and report the unresolved match |

## Required Obsidian Bases

Manual instruction walkthrough using the adapter copied to a temporary installation;
these cases do not create views or synthetic records in the personal vault.

| Request/fixture | Walkthrough result |
| --- | --- |
| Set up Obsidian storage; empty existing vault, no Views folder | Create Tasks, Reports, Views, Tasks.base, and Reports.base without a separate view request; query all eight task views and both report views before completion |
| Task/report notes exist but a required Base or view is missing | Setup remains incomplete; ordinary reads report the gap without repairing it |
| Task rows include Inbox, Next, Later, Maybe, Done, and reviewed/unreviewed notes | State views match exactly; Maybe remains separate, Unreviewed includes only tasks without acknowledgment, and project/parent groupings preserve relationships |
| Query returns out-of-root notes, wrong record types/states, or fails | Report partial setup; do not claim verified Bases |
| All required queries succeed with no rows | Empty storage is valid; create no synthetic records |
| Repeat setup with existing defaults and custom views/formulas/columns | Preserve existing definitions, add only missing defaults, and create no duplicates; conflicting default names remain explicit |
| Authorized upgrade of initialized storage with missing views | Back up and journal additive view changes; preserve task/report records and retry only missing paths/view names |
| Retrieve a saved report, update a task, inspect the backend, or edit/install the skill | No implicit view creation, repair, record migration, or acknowledgment |

`make validate`, `git diff --check`, and a temporary `gh skill install` exercise
packaging and resource portability. Live data verification checks existing
standalone task reads without introducing synthetic tasks into the vault.
