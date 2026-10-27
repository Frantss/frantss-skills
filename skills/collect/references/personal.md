# Fixed personal search policies

Use only the policy below for each provider; search modes, custom queries, channel/thread selectors, and other search overrides are not configuration. Native project locations and the requested time window bound eligible results.
Resolve the user's native identity before searching; display names never suffice. `currentUser()`/`me` is valid only when the authenticated account is verified as belonging to the user.

| Provider | Eligible personal involvement |
| --- | --- |
| Slack | Authored messages or direct mentions, across accessible public/private channels and direct/group messages in the workspace |
| Jira | Current/historical assignment, creation, or authored comments/worklogs/changelog actions within registered native projects |
| GitHub | Authored commits, created/assigned issues or PRs, and authored reviews/comments in registered repositories |
| Git | Authored commits only; follow the Git collection guide |
| Loom | Created recordings or authored comments in registered spaces/recordings |
| Gmail | Messages sent by or directly addressed to the user through native From/To/Cc/Bcc fields in the registered mailbox |
| Google Calendar | Events identifying the user as organizer or attendee in registered calendars; scheduled time never proves attendance |

Slack searches authorship and direct mentions separately. Verify native author or exact direct-mention token/field; channel/group mentions, membership, name text, and thread participation alone never qualify. Read surrounding messages only as necessary context, never as unrelated findings.
Jira uses supported assignment/history, creator, and actor-filtered activity searches; parenthesize personal OR branches before intersecting instance/project/window boundaries. Reporter alone and linked/parent issues never qualify. Use `updatedBy`/worklog search only when supported; day-granular matches require exact event times, not attribution from `updated` alone.
Return in-window updates to personally assigned/created Jira issues as relevant task context, even when others made the update; attribute those actions to their authors, not the user. Match projects using native locations or explicit source context; shared workspace/mailbox alone never establishes project attribution. Leave ambiguous results unassigned or report a gap.
