# File writes and recovery

1. Find current notes by key before creation; reuse the supplied ID/key. Return a conflict for multiple matches.
2. Read content/revision before patching. Reconcile changed content; preserve unknown fields and human sections.
3. Use CLI `eval code=<javascript>` with `app.vault.create(path, text)` for new records; existing paths must conflict.
   For replacement, use `app.vault.process(file, current => { if (current !== expected) throw Error('conflict'); return next; })`. Resolve `file` by exact path; serialize path/expected/next as JSON data literals in trusted code. Await calls and inspect errors.
4. Increment revision for a logical content change, not an identical retry. Read back fields, revision, and links.
After title changes or during a naming migration, use CLI `eval` with [`app.fileManager.renameFile(file, newPath)`](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts); check source identity/content and target vacancy first. Link updates depend on user settings: inspect and repair affected references without changing settings. Preserve IDs/keys; path-only moves keep logical revisions and require link/lookup verification.
Create missing parents through CLI `eval` using [`app.vault.createFolder`](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts), checking existing folders and proceeding parent-first.
## Task and report saves

Save task fields, optional parent link, and source links in one note. Verify parent/ancestors by task ID/type, reject cycles/dangling references, and save parents before children; read back/decode parent IDs. Save report summaries, links, and brief coverage in one note.
Task/report records and Base views use this protocol; return unsupported for backend settings/configuration saves. Keep one current record each, without evidence/run/event notes, revision archives, or checkpoint journals.
Legacy evidence/history_complete/manifest fields or Pending events sections require migration, not ordinary write recovery. Leave affected records unchanged and return unsupported.

For authorized cleanup, back up outside the vault, verify inbound references and exact content, then use CLI `eval` with `app.vault.trash(file, false)` for recoverable removal. Remove only empty owned folders; verify absence and retained records.
## Partial failures

After an uncertain write, read the current note by identity and compare expected/next content. Reuse a verified result; retry only missing writes. Preserve unsaved inputs and conflicts.
Return persisted parts, missing steps, and recovery locations; stop after a repeated unresolved conflict or access failure.
