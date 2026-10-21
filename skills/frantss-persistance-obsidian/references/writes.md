# File writes and recovery

1. Find current notes by key before creation; reuse the supplied ID/key. Return a conflict for multiple matches.
2. Read content/revision before patching. Reconcile changed content; preserve unknown fields and human sections.
3. Archive the previous revision before replacement. Verify an existing archive instead of overwriting it.
4. Use CLI `eval code=<javascript>` with `app.vault.create(path, text)` for new records and archives; existing paths must conflict.
   For replacement, use `app.vault.process(file, current => { if (current !== expected) throw Error('conflict'); return next; })`. Resolve `file` by exact path; serialize path/expected/next as JSON data literals in trusted code. Await calls and inspect errors.
5. Increment revision for a logical content change, not an identical retry. Read back fields, revision, and links.
After title changes or during a naming migration, use CLI `eval` with [`app.fileManager.renameFile(file, newPath)`](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts); check source identity/content and target vacancy first. Link updates depend on user settings: inspect and repair affected references without changing settings. Preserve IDs/keys; path-only moves keep logical revisions and require link/lookup verification.
Create missing parents through CLI `eval` using [`app.vault.createFolder`](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts), checking existing folders and proceeding parent-first.

## Task and report saves

Save task fields and source links in one note; save report summaries, links, and brief coverage in one note.
Only task/report/settings writes and their revision archives use this protocol; ordinary operations never create evidence/run/event notes or checkpoint journals.
Legacy evidence/history_complete/manifest fields or Pending events sections require migration, not ordinary write recovery. Leave affected records unchanged and return unsupported.

## Partial failures

Archives and current notes are separate writes. After an uncertain write, inspect both; retry only missing steps using the same identities and expected content. Preserve unsaved inputs when no recoverable note was written.
Return persisted parts, missing steps, and recovery locations; stop after a repeated unresolved conflict or access failure.
