# Shared configuration directory

Create or reuse `~/.frantss` for requested user-wide setup or local configuration writes; preserve sibling configurations and unrelated files.
Resolve the user's actual home directory; reject destinations escaping it through traversal or symlinks.
Store only backend connection options in `persistance.yaml`; credentials stay in their tool's credential store.
Leave repository files and `.gitignore` unchanged; per-repository `.frantss` directories are no longer required or discovered.
For explicit legacy import/export, read only the selected old configuration source; reconcile IDs against the local registry and migrate UUIDs through an explicit recovery mapping.
For former Obsidian connections, update the adapter to `frantss-persistance-obsidian` during requested import; preserve vault/root options rather than moving stored records.
Verify imported registry entries and any requested backend changes before declaring migration complete; retain old records/files and ignore rules until cleanup is separately requested.
