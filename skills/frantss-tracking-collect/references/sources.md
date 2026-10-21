# Source access

Each configured source identifies project-local `id`, `provider`, native `instance`, frantss's `identity`, and bounded provider-specific `scope`.
Resolve `{account_ref: <alias>}` identities through shared settings; provider/instance must match. Never substitute authenticated-agent identity.
Use configured native IDs/locations, independent of tool profiles. Empty source lists enable no collection; missing identity/ambiguous scope needs clarification.
Choose tools at runtime; preserve instance, identity, and restrictions across methods. Source configuration grants no external-write permission.
Unavailable access/dependencies leave coverage gaps; continue accessible sources without installing dependencies or broadening scope.
Use inclusive-start/exclusive-end local calendar windows converted to source time; supplied timezone/week start precede shared settings, with no guessed defaults.
Retrieve context for actors, negation, agreement, and dates; distinguish performed actions, assignments, scheduled activity, and quotations.
Attribute actual actors; inspect dated events inside updated threads, retaining older context only as context. Unsupported/inferred dates retain uncertainty/basis.
Record non-secret capability/query scope with cursors; resume only for compatible method, instance, identity, scope, and window, otherwise bounded rescan/deduplication.
For incremental scans, overlap prior checkpoints to catch late updates; native evidence identity remains unchanged across methods/query filters.

## Slack message scope

`scope.messages: authored-or-mentioned` selects messages across the configured workspace, including accessible public/private channels and direct/group messages; optional nonempty `channels`/`threads` intersect it.
Search authorship and direct mentions of the resolved member ID separately within the collection window and location scope; union results and deduplicate by native message identity.
Verify the native author or direct mention field/token (`<@ID>`); display-name text, thread participation, and surrounding messages alone do not match. Retain surrounding messages only as context.
Attribute mentions to their authors; a request addressed to frantss is not evidence that frantss performed it.
Preserve access restrictions across both searches; report missing authorship/mention branches and conversation types as coverage gaps.
