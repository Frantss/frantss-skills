# Frantss skills

My personal agent skills for communication, planning, task tracking, and activity
reports. Shared across agents that support [Agent Skills](https://agentskills.io/specification),
including Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

These skills are a work in progress. I'm still iterating on them.

## Skills

| Skill | Purpose |
| --- | --- |
| [frantss-communicate](skills/frantss-communicate/SKILL.md) | Write clear, direct replies throughout the session. |
| [bdd-frame-problem](skills/bdd-frame-problem/SKILL.md) | Establish needs, outcomes, evidence, scope, and constraints in a live problem brief. |
| [bdd-design-solution](skills/bdd-design-solution/SKILL.md) | Select a solution concept and refine its design against agreed needs and behavior. |
| [bdd-discover-behavior](skills/bdd-discover-behavior/SKILL.md) | Discover expected behavior through examples and per-area review in a live Markdown record. |
| [bdd-formulate-behavior](skills/bdd-formulate-behavior/SKILL.md) | Turn agreed behavior into Gherkin specifications for existing test tools. |
| [bdd-slice-work](skills/bdd-slice-work/SKILL.md) | Group specified behavior into manageable tickets and review the breakdown with the user. |
| [bdd-implement-ticket](skills/bdd-implement-ticket/SKILL.md) | Implement one accepted ticket with native tests and current behavioral verification evidence. |
| [frantss-configure](skills/frantss-configure/SKILL.md) | Set up and maintain connections, projects, and sources. |
| [frantss-update](skills/frantss-update/SKILL.md) | Update skills by commit hash and migrate configuration and stored records. |
| [frantss-tracking-tasks](skills/frantss-tracking-tasks/SKILL.md) | Capture tasks and manage commitments, dates, and blockers. |
| [frantss-tracking-collect](skills/frantss-tracking-collect/SKILL.md) | Read project sources for task links and report summaries. |
| [frantss-tracking-report](skills/frantss-tracking-report/SKILL.md) | Create daily and weekly activity reports. |
| [frantss-persistance](skills/frantss-persistance/SKILL.md) | Store task links and report summaries through a shared backend. |
| [frantss-persistance-obsidian](skills/frantss-persistance-obsidian/SKILL.md) | Store records in Obsidian through its official CLI. |

For the framing, design, and BDD flow, map the overall scope, then advance a small
coherent slice through discovery, formulation, design refinement, and ticket
slicing. Select a solution concept first when needed. Reuse existing agreements and keep other
areas pending; use the whole scope when it is small or tightly coupled. Changed
agreements require checking affected linked records before reusing their conclusions.
The [run layout](#planning-and-bdd-runs) fixes where these skills keep their outputs.
Ticket slicing can use accepted specifications directly when no consequential
design decisions remain open. Each ticket lists the behaviors it implements and
their specification cases. The user explicitly accepts the actual breakdown,
including grouping and dependencies, before its ticket definitions become ready.
That acceptance does not authorize tracker publication or implementation.
When implementation is requested, advance one accepted ticket whose delivery
prerequisites are implemented. Work test-first by default, reuse agreed observable
boundaries, and verify the complete linked cases through native project tests.
Already-correct behavior needs adequate passing evidence, not an artificial red
test. A justified change in test-first ordering does not reduce final verification.
Behavior/design questions return to their owning stages; routine implementation
choices stay with the implementing agent.

Tracking stores tasks with direct evidence links and saved report summaries,
including daily reports. Tasks represent owned outcomes, including work discovered
after completion. Optional parent links group distinct subtasks; PRs and discussions
supply evidence without automatically becoming tasks. Creating or refreshing a
report captures clear owned outcomes unless task writes are explicitly disabled.
Collection findings and scan cursors stay temporary;
activity without a task survives in a requested report's summary and source links.
Each task/report has one current record; revision numbers detect conflicting writes.
Shared settings live in the local project registry, outside the backend. Migration backups stay outside the active store.
Task titles and Obsidian filenames follow their source names. Jira tasks use
`<issue key> - <original summary>`; distinct subtasks retain their own scope.
Reports use names such as `2026-10-20 - Gildara daily report.md`;
stable IDs remain note properties.
Existing evidence, run, and event records need an explicit
[migration](skills/frantss-persistance/references/lean-migration.md); editing or
installing these skills does not migrate or delete stored data.

Each provider has one fixed personal-search policy. Slack searches your messages
and direct mentions; Jira searches issues you were assigned, created, or acted on.
Source registrations contain identities and native project locations. Search
modes, custom filters, and collection budgets are not configurable. Unsupported
personal searches remain explicit coverage gaps.
Source searches attempt delegation to small, fast sub-agents. The main agent
merges results and handles writes; workers share the existing collection budget.
Unavailable delegation falls back to direct collection with an explicit reason.

## Planning and BDD runs

Each run covers one feature across conversations and slices. Its six files describe
only the current state. Update changed requirements, behavior, and design in place;
remove obsolete entries and resolved questions. Keep no conversation transcript,
revision history, superseded definitions, change log, migration narrative, or audit file.

```text
.scratch/bdd/
└── slot-booking-001/
    ├── run.md
    ├── problem.md
    ├── discovery.md
    ├── behavior.feature
    ├── design.md
    └── tickets.md
```

`run.md` starts with YAML frontmatter:

```yaml
feature_name: Slot booking
feature_slug: slot-booking
run_id: slot-booking-001
stage: design
current_slice: S-001
current_ticket: null
```

Use a lowercase kebab-case slug and the next per-feature ordinal, padded to at
least three digits. The folder name equals `run_id`. Keep identity stable when the
solution changes. Resume the identified run; create another only for a different
feature or an explicit new-run request. Ask when the intended run is ambiguous.

Every Markdown file has the title `<feature_name>: <document role>` and exactly the
level-two sections below, in this order. Mark unvisited sections `Pending` and an
empty current list `None`. Keep current facts, assumptions, proposals, and agreements
distinguishable without recording when or how they changed.

| File | Required structure |
| --- | --- |
| `run.md` | Identity, stage, current slice/ticket in YAML; `Documents`, `Validation`, `Next action` |
| `problem.md` | `Problem`, `Context and evidence`, `People`, `Goals and success criteria`, `Scope and constraints`, `Open questions` |
| `discovery.md` | `Boundary and vocabulary`, `Area map`, `Area details`, `Coverage gaps`, `Open questions` |
| `design.md` | `Context`, `Approach`, `Structure`, `Decisions`, `Open questions` |
| `tickets.md` | `Overview`, `Tickets`, `Coverage gaps` |
| `behavior.feature` | One named `Feature`, current scope description, `Rule` groups, tagged scenarios, Given/When/Then outcomes, and `Examples` for outlines |

`stage` identifies active work: `framing`, `concept`, `discovery`, `formulation`,
`design`, `slicing`, or `implementation`. It does not establish readiness.
`current_slice` identifies a stable slice such as `S-001`; `current_ticket` identifies
the selected ticket, such as `TK-001`, or is `null` before ticket selection.

Under `run.md`'s `Documents`, give each current slice a `### <slice_id>: <name>`
entry with `Scope`, `Members`, and `Dependencies` fields, followed by a
`File | Status` table containing the other five files. `Members` lists explicit
file-qualified IDs, including in-slice rules and examples; use `Pending`
until known. `Dependencies` lists slice/question references or `None`.
Qualify cross-document IDs, for example `discovery.md:R-001`, to avoid ambiguity.
Keep every slice's current definition when focus changes; these entries describe
current scope and readiness, without recording its history.

Use these exact document statuses:

| Status | Meaning |
| --- | --- |
| `pending` | Unvisited |
| `draft` | Unaccepted work |
| `blocked` | An unresolved prerequisite prevents readiness |
| `ready` | Accepted and unblocked for the intended next use |
| `partial` | An explicitly accepted usable subset with named blockers |

Keep scope and blockers in the slice fields, outside status cells. For `partial`,
`Scope` names usable member IDs. Put the latest check results and limits under
`Validation`, with no history of findings or repairs; `Next action` states the
current next step. Acceptance and readiness do not imply implementation tests pass.
For `tickets.md`, readiness means the user explicitly accepted the actual ticket
breakdown and its definitions are unblocked. Delivery dependencies still govern
when implementation can start; neither approval nor readiness means tickets are done.

Once execution is tracked, add these level-three sections under `Validation`:

| Section | Columns | Values |
| --- | --- | --- |
| `Implementation` | `Ticket`, `State`, `Evidence` | `pending`, `in_progress`, `blocked`, `done` |
| `Behavior checks` | `Ticket`, `Cases`, `Check`, `Result` | `passed`, `failed`, `blocked`, `not_run` |

Execution state belongs to each ticket; document review statuses remain unchanged.
`Cases` identifies the case or Examples group; use `None` for checks without
specification cases, including repository or preparatory completion checks. `Check` names native test selectors or executable commands. Split rows
when case groups have different results. `Evidence` identifies the checked code,
commands, blockers, limitations, and any justified exception to test-first ordering.
These are current records, without a work journal or test-run history.

A ticket is `done` only when every assigned behavior and required repository check
passes against current code. For preparatory tickets, verify their explicit
completion and preservation checks. Reuse adequate existing tests and check all
promised outputs, state changes, and prohibited effects. Parsing Gherkin, reviewing
assertions, or finding a source tag does not establish that behavior passes.
Failed, blocked, or unexecuted required checks keep the ticket unfinished.
After code, source behavior, design, or prerequisite changes, invalidate affected
evidence, set affected results to `not_run`, and reopen affected `done` tickets
until reverified. Keep execution evidence here rather than expanding `tickets.md`.

In `problem.md`, put current evidence and assumptions under `Context and evidence`,
current requirements and success measures under `Goals and success criteria`, and
included/excluded scope, dependencies, and constraints under `Scope and constraints`.

`discovery.md` uses an `ID | Area | Status | Dependencies` table. Area statuses
use the same vocabulary plus `excluded`, which requires source or user authority.
An area's status covers its whole included scope; slice statuses remain separate.
Within `Area details`, use `### <id>: <name>` for each area, with `Boundary`, `Rules`,
and `Examples` fields. Keep one authoritative definition per stable ID and put only
unresolved questions under `Open questions`. State/action tables may clarify the
current boundary or rules without adding another level-two section.
`design.md` records the selected approach and its current rationale/trade-offs under
`Approach`; describe each part's purpose, boundary, interfaces, and dependencies
under `Structure`. `Decisions` contains applicable choices and rationale, not a
chronology of choices. Resolved questions become current definitions and disappear
from question lists.

`tickets.md` is a compact delivery map. Keep `Overview` to one sentence naming
selected `S-*` slices and source documents. Add evidence for already-satisfied
cases only when needed; keep ticket-to-slice membership in `run.md`'s `Members`.
Under `Tickets`, use `### TK-001: <outcome>`, a one-sentence summary, a bold
`Dependencies` field with blocking IDs or `None`, and a `Behavior | Cases` table. Give a dependency reason
only when unclear. The title states the outcome; the summary adds brief purpose
or context. Scope and design details remain in their source documents.

Each behavior row briefly names what the ticket implements and links its case
tags. Every linked case is the full acceptance contract, including state changes
and prohibited effects. Default verification exercises all assigned cases and
Examples using existing project tests. Add an optional bold `Verification` field
of at most one sentence only for non-obvious setup or extra regressions; omit it
otherwise. Keep review state, validation results, and execution limits in `run.md`.

Every required case or explicitly identified Examples group has one accountable
delivery ticket; regression references do not transfer ownership. A ticket that
completes behavior spanning several changes owns its cases and names prerequisites.
Preparatory tickets must justify a concrete prerequisite in the behavior row,
name dependent tickets, use `None` for Cases, and include independently verifiable
preservation checks under `Verification`. Every selected case is assigned, already
satisfied with evidence, or a current gap. `Coverage gaps` lists only in-scope gaps
and source references, or `None`; exclusions require source/user authority and
other unresolved questions stay with their owners.

Save the proposed breakdown before asking whether the user wants finer tickets
or some tickets grouped together. Review outcomes, behavior allocation, and real
dependencies; iterate until the user explicitly accepts the resulting breakdown.
Silence or agreement to the general approach leaves the actual tickets unaccepted.
Material changes reopen affected portions; preserve unaffected acceptance.

Initialize all six files even when using one skill alone. On resume, preserve
current contents and initialize only missing files/sections. Pending formulation
uses `Feature: <feature_name>` and a pending comment, with no invented scenarios.
Update current run status after substantive exchanges. Keep areas and slices inside
the fixed files; add no per-area/per-slice directories or extra documents.

Keep traceability beside scenarios using `@source-<id>` tags. For example,
`@case-006 @source-R-005 @source-E-006` identifies a case and its current definitions
in `discovery.md`. If supplied requirements lack IDs, record their agreed definitions
there without requiring another discovery conversation. Verify every source tag
resolves. Keep identities of continuing points stable; update their definitions
and references in place, and remove obsolete entries without retaining tombstones.
Source tags establish provenance; assertion review establishes behavioral coverage.

```gherkin
Feature: Slot booking
  @case-006 @source-R-005 @source-E-006
  Scenario: Recover a confirmation after a lost response
    Given Alice confirmed slot A using key K1 with reservation ID R
    And the confirmation response did not reach Alice
    When Alice repeats the slot A request using key K1
    Then the result is confirmed with the same reservation ID R
    And no additional reservation is created
```

Outline rows inherit scenario tags. Use separate tagged `Examples` blocks when
row groups have different sources; mark derived scenarios/groups with `@derived`.
These use [standard Gherkin tags](https://cucumber.io/docs/cucumber/api/#tags) and
require no Cucumber runner. Current gaps and unresolved behavior stay in discovery;
current specification review and parser outcomes stay in the run record.

When converting earlier outputs, normalize their current content into these fixed
sections. Keep existing run/slice IDs and map stages to the active-work vocabulary.
For runs without execution metadata, add `current_ticket: null`; keep the stage
and document acceptance states. Initialize execution tables only when execution
is tracked. Existing planning readiness never becomes `done` or `passed` by
conversion; unknown execution results remain `not_run`, with unresolved
prerequisites or environmental limits recorded as blockers. Preserve only current
execution evidence tied to checked code. Verify ticket IDs, case references,
state/result values, and the separation between review and execution states;
retries update the same rows and never infer implementation from accepted plans.
For a five-file run, initialize missing `tickets.md` with its canonical title and
three required sections marked `Pending`; add a `pending` tickets.md row to each
slice's document table. Preserve existing ticket content if present and normalize
it to the compact structure without inferring approval. For earlier verbose ticket
entries, retain IDs, behavior/case allocations, dependencies, and acceptance.
Keep the distinct outcome in the title and brief context in its one-sentence
summary; preserve only essential extra verification in its optional sentence. Put slice membership in `run.md`, scope/design facts in
their owning records, and latest validation/limits in `run.md`. Remove duplicated
fields and prose after checking that every case and prerequisite is retained.
Turn prose slice descriptions into current `Scope`, `Members`, and `Dependencies`
fields and per-slice document tables. Map unvisited work to `pending`, unaccepted
work to `draft`, and unresolved prerequisites to `blocked`. Map accepted, unblocked
work to `ready`; use `partial` only for an explicitly accepted usable subset with
named blockers. Preserve unresolved status meanings for clarification rather than
inferring acceptance. Apply the same mapping to area statuses, retaining authorized
exclusions as `excluded`. Do not interpret a syntax check as acceptance.
Move source mappings onto scenarios, applicable gaps/questions into
discovery, and the latest validation outcomes into the run record. Incorporate
answered questions into definitions, then discard resolved-question records,
superseded content, session logs, snapshots, and conversion narratives. Preserve
current IDs and acceptance states, and verify the six-file set, section order,
canonical names, status values, slice membership, source references, and cases.
A retry uses the same run rather than allocating another ordinal; initialize only
missing content and verify ticket references and dependency edges resolve.
Editing/installing skills does not itself rewrite existing records; conversions
must remain within the user's authorized scope.

## Install

This repository is private. You need GitHub access and credentials for your
installer. Choose either a plugin or direct skill installation for each agent
to avoid duplicates.

<details>
<summary>GitHub CLI</summary>

Authenticate with `gh auth login`, then run inside your workspace:

```bash
gh skill install Frantss/frantss-skills --all --agent codex
```

Replace `codex` with your agent, such as `cursor`, `github-copilot`, `gemini-cli`,
or `claude-code`. Replace `--all` with a skill name to install one skill.
Add `--scope user` to make skills available across workspaces.

Update installed skills:

```bash
gh skill update --all
```

See the [GitHub CLI install reference](https://cli.github.com/manual/gh_skill_install)
for supported agents and revision pinning.

</details>

<details>
<summary>Vercel skills CLI</summary>

```bash
npx skills add Frantss/frantss-skills
```

Update installed skills:

```bash
npx skills update
```

See the [skills CLI reference](https://github.com/vercel-labs/skills).

</details>

<details>
<summary>Codex plugin</summary>

Use a Codex CLI with `plugin` commands and Git credentials for this repository:

```bash
codex plugin marketplace add Frantss/frantss-skills
codex plugin add frantss-skills@frantss
```

Start a new Codex session after installation. To update:

```bash
codex plugin marketplace upgrade frantss
codex plugin add frantss-skills@frantss
```

</details>

<details>
<summary>Claude Code plugin</summary>

Configure SSH access to GitHub, then install:

```bash
claude plugin marketplace add Frantss/frantss-skills
claude plugin install frantss-skills@frantss
```

To update:

```bash
claude plugin marketplace update frantss
claude plugin update frantss-skills@frantss
```

See the [private marketplace guidance](https://code.claude.com/docs/en/plugins/host-marketplace).

</details>

## Update

Ask `frantss-update` to update your Frantss skill set or check for updates.
It reviews changes through a fixed default-branch commit, applies required
configuration/database migrations, and updates through the original installer.
Checks are read-only; explicit pins and selected skills remain in effect.

Full installation and shared data commit hashes are tracked separately in
`~/.frantss/skills-state.yaml`. First use verifies existing provenance and data
formats. Backups and a pending-step journal support interrupted updates.
The installer commands above update skill files only; use this workflow for
configuration and stored-record migrations.

## Setup and automatic use

Use [frantss-configure](skills/frantss-configure/SKILL.md) to set up the shared
backend, projects, and sources. Configuration applies across workspaces.
For Obsidian storage, install both persistence skills and enable the official
Obsidian CLI with an existing vault. Setup requires Tasks and Reports Bases with
verified default views; missing or failing views leave setup incomplete.

For automatic use across sessions, reference `frantss-communicate`,
`frantss-tracking-tasks`, and `frantss-configure` in your agent's persistent
instructions. Skill discovery alone does not ensure automatic use.

For communication, add this text with the installed skill's path:

```text
Before your first reply, read <installed-skill-path>.
Apply it to every message to me throughout the session, on every topic.
If its instructions leave the context, read it again before your next message.
```

For Codex, use `~/.codex/AGENTS.md`. For other agents, use their supported
persistent instructions file or setting.

## Contributing

Skills live in `skills/<name>/SKILL.md`. See [CONTRIBUTING.md](CONTRIBUTING.md)
for authoring and testing instructions, or the [glossary](GLOSSARY.md) for shared terms.

```bash
python3 scripts/new_skill.py frantss-my-skill --description "Use when ..."
make validate
```
