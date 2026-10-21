# Acknowledge

The absence of `reviewed-by-frantss` means unreviewed.
Accept acknowledgment in natural language; require a clear task or batch scope.
A general agreement about this workflow does not acknowledge stored tasks.
Preserve existing acknowledgment during other changes. Remove the tag only
when the user explicitly asks to mark the task unreviewed again.

## Update

Resolve the exact task before changing it. Apply the requested change while
preserving unrelated fields, source evidence, and human edits. Clarify an
ambiguous target rather than guessing from a similar title.

Record completion only from an explicit user report or evidence that satisfies
the task's outcome. A merged subtask PR does not complete a broader release.
Persist dated state changes, including completion and reopening, for historical reports.
Separate occurrence and recording times; unknown dates stay unknown.

## Retrieve

Return uncategorized pending tasks for inbox queries. Respect requested project or area scope.
With no scope specified, include the inbox and all projects. Include references, deadlines, and acknowledgment state where useful.
Identify inaccessible or incomplete results instead of presenting them as empty.
