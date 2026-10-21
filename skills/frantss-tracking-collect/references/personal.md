# Fixed personal search policies

Use only the policy below for each provider; search modes, custom queries, channel/thread selectors, and other search overrides are not configuration. Native project locations and the requested time window bound eligible results.
Resolve frantss's native identity before searching; display names never suffice. `currentUser()`/`me` is valid only when the authenticated account is verified as frantss.

| Provider | Eligible personal involvement |
| --- | --- |
| Slack | Authored messages or direct mentions, across accessible public/private channels and direct/group messages in the workspace |
| Jira | Current/historical assignment, creation, or authored comments/worklogs/changelog actions within registered native projects |
| GitHub | Authored commits, created/assigned issues or PRs, and authored reviews/comments in registered repositories |
| Git | Authored commits only; follow the Git collection guide |
| Loom | Created recordings or authored comments in registered spaces/recordings |
| Gmail | Messages sent by or directly addressed to frantss through native From/To/Cc/Bcc fields in the registered mailbox |
| Google Calendar | Events identifying frantss as organizer or attendee in registered calendars; scheduled time never proves attendance |

Search minimal identity-matched candidates within instance, native project locations, and window; parenthesize personal OR branches before intersecting boundaries. Union branches and deduplicate native IDs; verify relationships/dates before expanding details.
Slack searches authorship and direct mentions separately. Verify native author or exact direct-mention token/field; channel/group mentions, membership, name text, and thread participation alone never qualify. Read surrounding messages only as necessary context, never as unrelated findings.
Jira uses supported assignment/history, creator, and actor-filtered activity searches. Reporter alone and linked/parent issues never qualify. Use `updatedBy`/worklog search only when supported; day-granular `updatedBy` matches require exact event-time verification, not attribution from `updated` alone.
Keep others' actions attributed to them; personal relationships establish relevance, not authorship/completion. Match results to projects using native locations or explicit source context; a shared workspace/mailbox alone cannot establish project attribution. Leave ambiguous results unassigned or report a gap.
Missing identity, actor-search capabilities, or permissions leaves explicit gaps. Continue supported personal branches without replacing them with broad channel/project scans; provider methods may vary with capabilities, but the eligibility policy cannot.
