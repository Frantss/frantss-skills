# Sources

A source is a configured location from which a workspace can collect evidence of activity and commitments.
Read sources from the selected `~/.frantss/workspaces.yaml` entry; this skill applies no provider catalog or default source selection.
Each source mapping has stable workspace-local `id`, `provider`, `account`, `identity`, and `scope`; configuration edits belong to `configure-frantss-skills`, not the adapter.
`provider` identifies the source system; `account` identifies its native instance/tenant/mailbox, independent of tool profiles and credentials.
`identity` is a native user identifier or `{account_ref: <alias>}` resolved through [shared settings](settings.md).
`scope` contains the configured locations and restrictions; preserve its provider-specific fields without imposing a common location schema.

Store enough native IDs or canonical URLs to identify the target; human labels alone do not resolve ambiguous locations.
Source configuration contains no tool bindings or method preferences; ignore legacy `access` fields and remove them only on requested updates.
Preserve unrelated unknown fields as data. Runtime tool changes preserve source IDs and existing evidence identity.

Retrieve these mappings for the selected workspace IDs before collection. Use only configured identities and boundaries.
Collection discovers capabilities in the active harness while preserving configured identity and scope; configuration grants no permission for external writes.
Keep workspace/source-ID provenance and configured query scope with coverage; evidence uses native identity as defined in [tracking records](tracking.md).
Unavailable tools or access leave explicit coverage gaps; they do not remove a source or authorize a substitute.
An empty source list enables no collection; missing identity or ambiguous scope requires resolution before querying.
Source changes preserve unrelated mappings and human edits; removal or broader scope requires an explicit request or lasting change stated by the user, never tool inference.
