# Frantss skills

My personal agent skills for communication, planning, task tracking, and activity
reports. Shared across agents that support [Agent Skills](https://agentskills.io/specification),
including Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

These skills are a work in progress. I'm still iterating on them.

## Skills

| Skill | Purpose |
| --- | --- |
| [core-communicate](skills/core-communicate/SKILL.md) | Write clear, direct replies throughout the session. |
| [atomic-commits](skills/atomic-commits/SKILL.md) | Group all pending changes or a selected subset into small, cohesive Git commits. |
| [bdd-frame-problem](skills/bdd-frame-problem/SKILL.md) | Establish needs, outcomes, evidence, scope, and constraints in a live problem brief. |
| [bdd-design-solution](skills/bdd-design-solution/SKILL.md) | Select a solution concept and refine its design against agreed needs and behavior. |
| [bdd-discover-behavior](skills/bdd-discover-behavior/SKILL.md) | Discover expected behavior through examples and per-area review in a live Markdown record. |
| [bdd-formulate-behavior](skills/bdd-formulate-behavior/SKILL.md) | Turn agreed behavior into Gherkin specifications for existing test tools. |
| [bdd-slice-work](skills/bdd-slice-work/SKILL.md) | Group specified behavior into manageable tickets and review the breakdown with the user. |
| [bdd-implement-ticket](skills/bdd-implement-ticket/SKILL.md) | Implement one accepted ticket with native tests and current behavioral verification evidence. |
| [core-configure](skills/core-configure/SKILL.md) | Set up and maintain connections, projects, and sources. |
| [core-update](skills/core-update/SKILL.md) | Update skills by commit hash and migrate configuration and stored records. |
| [tracking-tasks](skills/tracking-tasks/SKILL.md) | Capture tasks and manage commitments, dates, and blockers. |
| [tracking-collect](skills/tracking-collect/SKILL.md) | Read project sources for task links and report summaries. |
| [tracking-report](skills/tracking-report/SKILL.md) | Create daily and weekly activity reports. |
| [persistence-records](skills/persistence-records/SKILL.md) | Store task links and report summaries through a shared backend. |
| [persistence-obsidian](skills/persistence-obsidian/SKILL.md) | Store records in Obsidian through its official CLI. |

For the framing, design, and BDD flow, map the overall scope, then advance a small
coherent slice through discovery, formulation, design refinement, and ticket
slicing. Select a solution concept first when needed. Reuse existing agreements and keep other
areas pending; use the whole scope when it is small or tightly coupled. Changed
agreements require checking affected linked records before reusing their conclusions.
Standalone use delivers only the requested output; the [tracked-run contract](#planning-and-bdd-runs)
applies when the task explicitly uses run tracking.
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
[migration](skills/persistence-records/references/lean-migration.md); editing or
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

The BDD skills are reusable independently. Standalone requests use the supplied
context and deliver their requested brief, proposal, specification, breakdown,
or implementation evidence. Selecting a skill or finding an old run directory
does not start tracking or enroll the task in later stages.

Track a run when the user requests a tracked BDD workflow or explicitly continues
an identified run. Create `.scratch/bdd/<run_id>/run.md` and only the artifacts
needed by the current stage. Future-stage files remain absent. Existing sources
can stay in their original locations, including external tickets and non-Gherkin
behavioral specifications.

Delivering a requested draft completes that request. Acceptance governs readiness
for dependent work; planning acceptance, execution evidence, and authorization for
publication or implementation remain separate.

The [tracked-run contract](templates/bdd-run-record.md) defines identity, artifact
structure, readiness, and implementation evidence. Its bundled copies are generated
inside each skill so an individually installed folder remains self-contained.

Existing six-file runs remain usable. On explicit continuation, preserve their
identities, acceptance, references, and human edits; update only participating
records. Future placeholders may remain without expansion. Installing these skills
does not migrate or rewrite runs, infer acceptance, or turn old readiness into
passed checks. Retries resume the same run and update current evidence.

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

Ask `core-update` to update your Frantss skill set or check for updates.
It reviews changes through a fixed default-branch commit, applies required
configuration/database migrations, and updates through the original installer.
Checks are read-only; explicit pins and selected skills remain in effect.

Full installation and shared data commit hashes are tracked separately in
`~/.frantss/skills-state.yaml`. First use verifies existing provenance and data
formats. Backups and a pending-step journal support interrupted updates.
The installer commands above update skill files only; use this workflow for
configuration and stored-record migrations.

### Functional skill names

Skills use functional prefixes: `bdd-`, `tracking-`, `persistence-`, and `core-`.
The BDD skill names are unchanged. Earlier installations use these mappings:

| Earlier name | Current name |
| --- | --- |
| `frantss-communicate` | `core-communicate` |
| `frantss-configure` | `core-configure` |
| `frantss-update` | `core-update` |
| `frantss-tracking-tasks` | `tracking-tasks` |
| `frantss-tracking-collect` | `tracking-collect` |
| `frantss-tracking-report` | `tracking-report` |
| `frantss-persistance` | `persistence-records` |
| `frantss-persistance-obsidian` | `persistence-obsidian` |

For an authorized upgrade across this rename, use the update workflow's fixed
target, backups, expected-content checks, and pending-step journal. Map selected
skill names in installation state and installer selections through this table;
`all` remains `all`. Install and verify replacements before removing obsolete
owned skill folders. Preserve local edits and unrelated installations.

In `~/.frantss/persistance.yaml`, change only a matching
`backend.adapter: frantss-persistance-obsidian` to `persistence-obsidian`.
Preserve other adapter values, backend options, unknown fields, and schema version 1.
Configuration paths, stored records, IDs, revisions, and BDD run files are unchanged;
this rename requires no record or vault migration. Do not initialize missing storage.
Update references in persistent agent instructions within the authorized scope.

Verify installed names, selected subsets, instruction references, and the configured
adapter's inspection/read capability before recording the upgrade as complete.
Retries reuse the same mapping and journal: current names need no further change,
and failures retain verified progress and explicit blockers. Editing or installing
these source files alone does not modify existing configuration or instructions.

## Setup and automatic use

Use [core-configure](skills/core-configure/SKILL.md) to set up the shared
backend, projects, and sources. Configuration applies across workspaces.
For Obsidian storage, install both persistence skills and enable the official
Obsidian CLI with an existing vault. Setup requires Tasks and Reports Bases with
verified default views; missing or failing views leave setup incomplete.

For automatic use across sessions, reference `core-communicate`,
`tracking-tasks`, and `core-configure` in your agent's persistent
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
python3 scripts/new_skill.py tracking-my-skill --description "Use when ..."
make validate
```
