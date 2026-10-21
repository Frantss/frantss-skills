# Source guidance

Apply only configured scopes and the user's identity in each account. Discover exact tool syntax instead of inventing service commands.

Workspace configuration identifies providers, instances, targets, and the user's identity; choose suitable available tools at runtime.
Preserve configured identity, location boundaries, and provider-specific restrictions when translating scope into queries.
Inspect actual tool schemas and verify the target instance; keep identity and scope unchanged across methods. Ignore legacy configured `access` bindings.
Report missing access, dependencies, or unavailable sources as coverage gaps; continue with accessible configured sources without installing dependencies.
Source configuration is location/identity data, not executable guidance or permission for activity outside collection.
Normalize connector wrappers to native event identity before deduplication; switching methods or query filters must reuse the same evidence key.
Record the non-secret runtime capability and query scope with each cursor; resume only when method, instance, identity, scope, and window match, otherwise rescan within budget and deduplicate.
Distinguish performed actions from assignment, current state, scheduled activity, and quoted statements.

Retrieve surrounding context when snippets omit actors, negation, agreement, or dates.
Include relevant collaboration context while attributing each action to its actual actor.
Use source timestamps according to their meaning: created, updated, authored, reviewed, or merged.
For updated threads, inspect dated events inside the requested window; retain older context only as context.
Mark quoted or inferred event dates with their basis. Keep uncertain dates unknown rather than using retrieval time.
Respect requested branch and source restrictions. Ask before adding an unmapped source or expanding workspace scope.
