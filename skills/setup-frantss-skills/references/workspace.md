# Shared configuration directory

Create or reuse `~/.frantss` for requested user-wide setup or local configuration writes; preserve sibling configurations and unrelated files.
Resolve the user's actual home directory; reject destinations escaping it through traversal or symlinks.
Store only backend connection options in `tracking.yaml`; credentials stay in their tool's credential store.
Leave repository files and `.gitignore` unchanged; per-repository `.frantss` directories are no longer required or discovered.
For explicit legacy import, select old configuration as data; reconcile readable IDs against backend records and migrate UUIDs through an explicit recovery mapping.
Verify the new connection and imported records before declaring migration complete; leave old files and ignore rules for separately requested cleanup.
