# Source guidance

Apply only configured scopes and the user's identity in each account. Discover exact tool syntax instead of inventing service commands.

| Source | Gather within workspace scope | Preserve the distinction |
| --- | --- | --- |
| GitHub | User-authored PRs, reviews, comments, commits, and relevant issue changes in selected repositories | Authorship, review, merge, and assignment are different events |
| Git | Commits reachable on the configured branch, such as `main` | Author and committer identities/times can differ; collection time is neither |
| Slack | Relevant user messages and discussion context in selected workspace/channels/threads | Quoted text, requests, and team suggestions do not establish the user's agreement |
| Jira | Relevant issue changes, worklogs, and user comments in configured Jira projects | Current assignment or status alone does not establish a dated contribution |
| Loom | User recordings and relevant transcript/comment passages in selected spaces or links | Video creation time and the time of an action mentioned in a recording can differ |
| Email | Relevant user-authored sent replies and received thread context in selected accounts/mail scopes | A received request or forwarded promise is not the user's commitment |
| Calendar | Events and available notes from selected calendars | Scheduled duration and event end do not prove attendance or work performed |

Retrieve surrounding context when snippets omit actors, negation, agreement, or dates.
Include relevant collaboration context while attributing each action to its actual actor.
Use source timestamps according to their meaning: created, updated, authored, reviewed, or merged.
For updated threads, inspect dated events inside the requested window; retain older context only as context.
Mark quoted or inferred event dates with their basis. Keep uncertain dates unknown rather than using retrieval time.
Respect requested branch and source restrictions. Ask before adding an unmapped source or expanding workspace scope.
