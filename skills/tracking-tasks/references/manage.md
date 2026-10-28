# Management

Acknowledgment needs clear task/batch scope; general workflow agreement is insufficient. Remove the review tag only on an explicit request to mark unreviewed.
Resolve the exact task before updates; preserve unrelated fields, source links, and human edits. Older findings never overwrite a later known state; uncertain ordering leaves state unchanged and remains an explicit gap. Apply [record/content rules](content.md).
Completion requires the whole outcome; merged PRs or completed children alone never complete a parent. State, dates, and acknowledgment never cascade between relatives; flag inconsistent states. Reopening uses [triage](triage.md).
Save changed task fields and links together; unchanged retries/repeated triage create no revision. Recover uncertain task writes before further changes.
Inbox queries select `status: inbox` regardless of project. Pending queries include Next/Later and unresolved Inbox; Maybe appears separately when requested. Return parent context and derived children without flattening them into independent deliveries.
Respect project/area scope; without scope include Inbox and all projects. Return references, dates, blockers, acknowledgment, and explicit access/pagination gaps.
