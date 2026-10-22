# Writes and recovery

1. Resolve fresh notes by type and ID/key; duplicate matches conflict. Before creating, fresh-read the scope to prove both identities absent, repeating on scope changes. Inaccessible/unresolved notes leave absence unproven. Reuse supplied IDs/keys.
2. Before patching, read current identity/content/revision. Reconcile changes; preserve unknown fields and human sections. Increment revision once for changed content; identical retries reuse verified results.
3. Use the batch runner for prepared records. For manual CLI writes, use `eval` with `app.vault.create(path, text)` or `app.vault.process(file, current => { if (current !== expected) throw Error('conflict'); return next; })`. Resolve exact paths, serialize payloads as JSON data literals, await calls, and inspect errors. Existing create destinations must conflict.
4. Read back identity, fields, revision, and links. Update batch mappings only after verified changes/moves/deletions; invalidate uncertain entries before reuse.

After title changes or authorized naming migrations, use [`app.fileManager.renameFile(file, newPath)`](https://github.com/obsidianmd/obsidian-api/blob/master/obsidian.d.ts). Verify source identity/content and target vacancy. Preserve IDs/keys; path-only moves keep logical revisions. Inspect/repair affected links without changing user settings, then verify links/lookup. Create missing parents with `app.vault.createFolder`, checking existing folders and proceeding parent-first.
Save task fields, parent/source links, or report summaries/coverage in one current note. Verify parent/ancestor IDs/types, reject cycles/dangling links, save parents first, and decode parent IDs on readback. Configuration saves are unsupported; keep settings/projects outside notes, without evidence/run/event records or revision archives.
Legacy evidence/history_complete/manifest fields and Pending events sections require migration. Leave affected records unchanged and return unsupported.
For authorized cleanup, back up outside the vault, verify inbound references and exact content, then use `app.vault.trash(file, false)` through CLI `eval`. Remove only empty owned folders; verify absence and retained records.

After uncertain writes, fresh-read by identity and compare expected/next content. Reuse verified results; retry only missing operations with the same identities. Preserve unsaved inputs/conflicts, report persisted parts/missing steps/recovery locations, and stop after a repeated unresolved conflict or access failure.
