# Configuration

## Locate and read

Use an explicitly supplied config file or `<selected-workspace>/.frantss/tracking.yaml` first.
Otherwise search the current directory and its ancestors for that file; use it only when exactly one exists.
Other `.frantss` files do not participate in tracking discovery; preserve them during setup and reconfiguration.
Ask which file to use when several exist. Ordinary project work must not create another configuration workspace.
Agents working outside that directory tree need the shared config path supplied in their context or persistent instructions.
Keep the directory and config as real local paths; stop on symlinks that redirect setup outside the selected workspace.

## Schema and ownership

```yaml
schema_version: 1
backend:
  adapter: personal-persist-obsidian
  options:
    vault: /path/to/your/vault
    root: Tracking
```

The adapter interprets `options`; Obsidian requires an existing absolute vault path and a vault-relative tracking root.
The example shows the shape, not a configured destination. Null or missing required options mean setup is incomplete.
The single `backend` applies to every project; retain project IDs and source mappings as records in that backend.
Shared timezone, week_start, account aliases/identities, and collection limits live in backend settings, not duplicated in this file.
Project records own sources with provider, account alias, actor identity, and explicit locations/branches/query constraints.
An empty source list enables no collection. Account aliases identify authenticated tools; credentials stay in their credential stores.
Project creation still requires an explicit command for that project. Naming it during inspection or source discovery does not create it.

## Git exclusion

Work in the configuration workspace. Preserve its existing `.gitignore` rules and unrelated files.
Before writing, run `git ls-files -- .frantss` there when inside a Git worktree.
If entries are tracked, stop config writes and explain that ignoring does not untrack them; request explicit index cleanup separately.
Ensure the workspace's `.gitignore` has an effective `/.frantss/` rule; append it only when needed.
Preserve existing content and insert a separator newline if the file has no final newline.
In Git, verify with `git check-ignore --no-index --quiet -- .frantss/tracking.yaml`; reruns must not keep appending effective rules.
Verify the local ignore rule even if a global ignore already applies, so this workspace carries its own exclusion.
Outside Git, create or update the workspace's `.gitignore`; report that Git verification is unavailable there.
Keep the config under the selected `.frantss` directory; reject escaping paths and unsafe symlink destinations before editing.
