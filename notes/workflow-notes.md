# Workflow notes

## Planning and BDD runs

Use the BDD skills independently or advance a small slice through discovery,
specification, design, and ticket slicing. Reuse agreed work and check affected
records when agreements change. Standalone requests end with the requested output.

Accept the ticket breakdown before dependent work. Acceptance does not authorize
publication or implementation. When implementation is requested, deliver one
accepted ticket whose prerequisites are implemented. Work test-first by default
and verify all linked cases through native tests; existing correct behavior needs
passing evidence. Return unresolved behavior or design decisions to their stages.

Track runs only on explicit request or continuation. Follow the
[tracked-run contract](../templates/bdd-run-record.md), create
`.scratch/bdd/<run_id>/run.md`, and add artifacts as needed by the current stage.
Existing sources can stay in place. Preserve existing run identities, acceptance,
references, and human edits; retries update the same run. Installation does not
migrate runs, infer acceptance, or establish passing checks.

## Tracking and storage

Track owned outcomes with direct evidence links, including completed work.
Use parent links for distinct subtasks; PRs and discussions provide evidence.
Reports capture clear owned outcomes unless task writes are disabled.
Keep collection findings and cursors temporary; retain other activity in requested
report summaries and source links.

Keep one current record per task or report, with revisions for conflicting writes.
Store shared settings in the local registry and migration backups outside active
storage. Preserve source titles and filenames; keep stable IDs in note properties.
Existing evidence, run, and event records require an explicit
[migration](../skills/persistence-records/references/lean-migration.md).
Installing skills does not migrate or delete stored data.

Slack searches your messages and direct mentions. Jira searches issues you were
assigned, created, or acted on. Register identities and native project locations;
search modes, filters, and collection budgets are fixed. Report unsupported searches
as coverage gaps. Delegate source searches when available within the shared budget;
the main agent merges results and writes records. Explain direct-collection fallbacks.
