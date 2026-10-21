# Sources

A source is a configured location from which a workspace can collect evidence of activity and commitments.
The workspace configuration defines its sources; this skill applies no provider catalog or default source selection.
Retain each workspace's `sources` as mappings with stable workspace-local `id`, `provider`, `account`, `identity`, `scope`, and `access`.
`provider` identifies the source system; `account` identifies its host/account or tenant, without credentials.
`identity` is a native user identifier or `{account_ref: <alias>}` resolved through [shared settings](settings.md).
`scope` contains the configured locations and restrictions; preserve its provider-specific fields without imposing a common location schema.

`access` retains descriptors of how to read the source, including references, dependencies, and supplied method preferences.
Preserve descriptors and unknown fields without provider-specific interpretation or executing them during persistence.
Access changes preserve source IDs and existing evidence identity; changing access methods must not create duplicate observations.

Retrieve these mappings for the selected workspace IDs before collection. Use only configured identities and boundaries.
Collection resolves configured access to available capabilities while preserving scope; configuration alone grants no permission for external writes.
Keep workspace/source-ID provenance and configured query scope with coverage; evidence uses native identity as defined in [logical records](records.md).
Unavailable tools or access leave explicit coverage gaps; they do not remove a source or authorize a substitute.
An empty source list enables no collection; missing access or ambiguous scope requires resolution before querying.
Source changes preserve unrelated mappings and human edits. Removing or broadening a mapping requires that requested change.
