# Fixed personal collection

Manual instruction walkthrough with synthetic Slack/Jira results and configured
native identities. No live source scan, configuration write, or task/report save
was exercised. Collection has one eligibility policy per provider, fixed call/item
budgets, and source registrations containing only native identities/locations.

## Scope and query decisions

- Slack always searches authored messages and direct mentions across the native
  workspace. There are no channel/thread selectors or message-search modes.
- Jira always searches current/past assignment, creator, and authored
  interactions in registered native projects. Raw issue filters are retired.
- Slack/Gmail need no scope mapping. Jira and other providers requiring native
  project locations remain incomplete when those locations are missing.
- Two registered Jira project keys produce a location predicate intersected
  with parenthesized personal branches and the time window. No source-supplied
  query can replace or widen these predicates.
- Authenticated identity differing from the configured identity prevents using
  `me`/`currentUser()`. Use the configured native ID or stop that source.
- Unsupported actor/history search leaves branch-specific gaps. Continue known
  personal branches without scanning all issues to find personal matches later.
- A pre-policy handoff is incompatible; start a bounded rescan with the fixed
  policy without writing configuration or altering native project locations.
- A retired `collection_limits` setting does not change the 20-call/50-item
  project/source budget. Ordinary reads ignore it without changing storage.

## Slack fixture

Registered workspace W, identity U1, and a one-day window. Channel selectors and
`messages` settings have no effect. Project context is explicit where needed.

| Candidate | Decision |
| --- | --- |
| Message by U1 in C1 during the window | Include |
| Message by U2 with native direct mention `<@U1>` in C1 | Include; U2 remains the actor |
| Same message returned by authored and mention searches | Include once by native message ID |
| Message by U2 containing only U1's display-name text | Skip |
| Message by U2 with a channel/group mention | Skip |
| Message by U2 in a thread where U1 replied earlier | Context only when needed for a matched message |
| Incoming DM by U2 with no direct mention of U1 | Skip under authored-or-mentioned selection |
| Message by U1 in another accessible channel C2 of W | Include when dated and project-attributable; there is no channel selector |
| Message by U1 in another workspace | Skip |
| Personal match without enough context to resolve its project | Leave unassigned or report a gap; workspace membership alone does not assign it to a project |
| Message by U1 outside the requested window | Skip as activity; read only if necessary context |
| Mention branch inaccessible | Authored findings remain usable; mention coverage is partial, with no channel-wide fallback |

## Jira fixture

Registered site S, identity A1, native project key WIDGET, and a one-day window. Search
results supply native relationship fields or actor-filtered activity matches.

| Candidate | Decision |
| --- | --- |
| WIDGET-1 currently assigned to A1 with an in-window update by A2 | Relevant task context; never claim A1 performed A2's update |
| WIDGET-2 created by A1, now assigned to A2 | Include supported in-window activity/context |
| WIDGET-3 assigned/created by A2, with an in-window comment by A1 | Include A1's dated comment |
| WIDGET-4 has an in-window worklog or changelog action by A1 | Include the supported action, independently of assignee |
| WIDGET-5 has verified historical assignment to A1 | Relevant; establish activity dates separately from relationship history |
| WIDGET-6 is recent and in the same project, without A1 involvement | Skip before expanding details |
| WIDGET-7 is mentioned or linked by a qualifying issue, without A1 involvement | Do not expand it into another finding |
| WIDGET-8 has reporter A1 but creator/assignee A2 and no A1 action | Skip; reporter is not evidence of creation by A1 |
| OTHER-1 has an A1 comment but belongs to another native project | Skip for this project/source |
| An actor search returns an event outside the exact window because of day-level matching | Skip that event after timestamp verification |
| Only assignment/creator search is supported | Return those matches with interaction/history coverage gaps; no broad issue crawl |

## Other provider policies

| Provider fixture | Qualifying result | Nonmatch/context |
| --- | --- | --- |
| GitHub repository | Frantss-authored commit, created/assigned issue/PR, or authored review/comment | Unrelated repository updates or membership alone |
| Local Git repository | Commit with exact configured raw author email | Matching committer alone or author display-name text |
| Loom space/recording | Recording created or comment authored by frantss | Unrelated recordings in the same space |
| Gmail mailbox | Native From/To/Cc/Bcc identifies frantss | Name text or mailbox access alone; received messages remain attributed to their senders |
| Google Calendar | Frantss is a native organizer/attendee | Unrelated shared-calendar events; scheduled events do not establish attendance |

## Retired search settings

Ordinary reads ignore old Slack message/channel/thread selectors, Jira raw
filters, Gmail label/thread filters, and collection-limit settings. They do not
edit stored configuration. An explicit update removes owned retired fields with
verified backups and preserves native source/account identities and project
locations. A Jira source with only an old filter must recover unambiguous native
project keys or remain unresolved. Retried updates patch only missing work after
checking expected content; custom/unknown fields and human edits survive.

## Workflow boundaries and limits

“Collect yesterday's activity” activates collection with these defaults.
“Show the saved daily report” remains a report lookup with no collection.
“Set up a Slack/Jira source” registers native identity/location without a choice
of search mode or an activity scan. Quoted suggestions do not write configuration. A report
handoff retains `capture: none`; personal matches do not authorize task writes.

The native-author search and direct-mention distinction were checked against
[Slack search documentation](https://docs.slack.dev/reference/methods/search.messages/)
and [mention documentation](https://slack.com/help/articles/205240127-Use-mentions-in-Slack).
Jira's `updatedBy` coverage and day-level precision were checked against
[Atlassian's JQL function reference](https://support.atlassian.com/jira-software-cloud/docs/jql-functions/).
These walkthroughs check instruction decisions; live connector completeness and
provider permission behavior remain untested.

`make validate` passed with the existing package warnings. All skills installed
into a temporary directory; the copied collection/configuration references
matched the source files. `git diff --check` passed.
