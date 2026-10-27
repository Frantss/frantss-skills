# Frantss skills

My personal agent skills for communication, development, task tracking, and activity
reports. Use them with agents that support [Agent Skills](https://agentskills.io/specification),
including Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

These skills are a work in progress.

## Skills

### Core

Manage communication, shared configuration, and skill updates.

| Skill | Purpose |
| --- | --- |
| [core-communicate](plugins/frantss-development/skills/core-communicate/SKILL.md) | Write clear, direct replies throughout the session. |
| [core-configure](plugins/frantss-tracking/skills/core-configure/SKILL.md) | Set up and maintain connections, projects, and sources. |
| [core-update](plugins/frantss-tracking/skills/core-update/SKILL.md) | Update skills by commit hash and migrate configuration and stored records. |

### Planning and BDD

Plan and implement work through behavior-driven development (BDD).

| Skill | Purpose |
| --- | --- |
| [bdd-frame-problem](plugins/frantss-bdd/skills/bdd-frame-problem/SKILL.md) | Establish needs, outcomes, evidence, scope, and constraints in a live problem brief. |
| [bdd-design-solution](plugins/frantss-bdd/skills/bdd-design-solution/SKILL.md) | Select a solution concept and refine its design against agreed needs and behavior. |
| [bdd-discover-behavior](plugins/frantss-bdd/skills/bdd-discover-behavior/SKILL.md) | Discover expected behavior through examples and per-area review in a live Markdown record. |
| [bdd-formulate-behavior](plugins/frantss-bdd/skills/bdd-formulate-behavior/SKILL.md) | Turn agreed behavior into Gherkin specifications for existing test tools. |
| [bdd-slice-work](plugins/frantss-bdd/skills/bdd-slice-work/SKILL.md) | Group specified behavior into manageable tickets and review the breakdown with the user. |
| [bdd-implement-ticket](plugins/frantss-bdd/skills/bdd-implement-ticket/SKILL.md) | Implement one accepted ticket with native tests and current behavioral verification evidence. |

### Code quality

| Skill | Purpose |
| --- | --- |
| [refactoring](plugins/frantss-development/skills/refactoring/SKILL.md) | Refactor existing code through scoped changes and behavior-preservation checks, or assess requested refactoring opportunities. |

### Git

Organize code changes into focused commits.

| Skill | Purpose |
| --- | --- |
| [atomic-commits](plugins/frantss-development/skills/atomic-commits/SKILL.md) | Group all pending changes or a selected subset into small, cohesive Git commits. |

### Tracking

Track commitments, report personal activity, and follow team initiatives from
supplied sources.

| Skill | Purpose |
| --- | --- |
| [tracking-tasks](plugins/frantss-tracking/skills/tracking-tasks/SKILL.md) | Capture tasks and manage commitments, dates, and blockers. |
| [tracking-collect](plugins/frantss-tracking/skills/tracking-collect/SKILL.md) | Read project sources for task links and report summaries. |
| [tracking-report](plugins/frantss-tracking/skills/tracking-report/SKILL.md) | Create daily and weekly activity reports. |
| [tracking-team-digest](plugins/frantss-tracking/skills/tracking-team-digest/SKILL.md) | Summarize team initiatives from supplied sources and save a digest by default. |

### Persistence

Store and retrieve task records and reports.

| Skill | Purpose |
| --- | --- |
| [persistence-records](plugins/frantss-tracking/skills/persistence-records/SKILL.md) | Store task links and report summaries through a shared database. |
| [persistence-obsidian](plugins/frantss-tracking/skills/persistence-obsidian/SKILL.md) | Store records in Obsidian through its official CLI. |

## Install

This repository is private. You need GitHub access and credentials for your
installer. Choose either a plugin or direct skill installation for each agent
to avoid duplicates.

Codex and Claude share the `frantss` marketplace. Choose domain plugins:

| Plugin | Included skills |
| --- | --- |
| `frantss-tracking` | All `tracking-*` and `persistence-*` skills, `core-configure`, and `core-update` |
| `frantss-bdd` | All six `bdd-*` skills |
| `frantss-development` | `core-communicate`, `refactoring`, and `atomic-commits` |

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
<summary>npx skills (Vercel)</summary>

Use Node.js 22.20 or later, then run inside your workspace:

```bash
npx skills add Frantss/frantss-skills
```

Choose the skills and agents interactively. Add `--agent codex` to select Codex,
`--skill core-communicate` to select one skill, or `--global` to install across
workspaces.

List available skills before installing:

```bash
npx skills add Frantss/frantss-skills --list
```

Update installed skills:

```bash
npx skills update
```

See the [skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

</details>

<details>
<summary>Codex plugin</summary>

Use a Codex CLI with `plugin` commands and Git credentials for this repository:

```bash
codex plugin marketplace add Frantss/frantss-skills
codex plugin add frantss-tracking@frantss
```

Replace `frantss-tracking` with another plugin from the table, or repeat the
command for each domain you want.
Start a new Codex session after installation. To update a selected plugin:

```bash
codex plugin marketplace upgrade frantss
codex plugin add frantss-tracking@frantss
```

</details>

<details>
<summary>Claude Code plugin</summary>

Configure SSH access to GitHub, then install:

```bash
claude plugin marketplace add Frantss/frantss-skills
claude plugin install frantss-tracking@frantss
```

Replace `frantss-tracking` with another plugin from the table, or repeat the
command for each domain you want.
To update a selected plugin:

```bash
claude plugin marketplace update frantss
claude plugin update frantss-tracking@frantss
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

For older installations, see the
[database key migration](plugins/frantss-tracking/skills/persistence-records/references/database-migration.md).

## Setup and automatic use

Use [core-configure](plugins/frantss-tracking/skills/core-configure/SKILL.md) to set up the shared
database, projects, and sources. Configuration applies across workspaces.
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

Skills live in `plugins/<plugin>/skills/<name>/SKILL.md`. Each skill has one source
folder, used directly by its plugin.
See [CONTRIBUTING.md](CONTRIBUTING.md)
for authoring and testing instructions, or the [glossary](GLOSSARY.md) for shared terms.

```bash
make validate
```
