# Frantss skills

My personal agent skills for communication, development, task tracking, and activity
reports. Use them with agents that support [Agent Skills](https://agentskills.io/specification),
including Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

These skills are a work in progress.

## Skills

### frantss-development

Write clear replies, refactor code, and organize Git commits.

- [core-communicate](plugins/frantss-development/skills/core-communicate/SKILL.md): Write clear, direct replies throughout the session.
- [refactoring](plugins/frantss-development/skills/refactoring/SKILL.md): Refactor existing code through scoped changes and behavior-preservation checks, or assess requested refactoring opportunities.
- [atomic-commits](plugins/frantss-development/skills/atomic-commits/SKILL.md): Group all pending changes or a selected subset into small, cohesive Git commits.

### frantss-bdd

Plan and implement work through behavior-driven development (BDD).

- [bdd-frame-problem](plugins/frantss-bdd/skills/bdd-frame-problem/SKILL.md): Establish needs, outcomes, evidence, scope, and constraints in a live problem brief.
- [bdd-design-solution](plugins/frantss-bdd/skills/bdd-design-solution/SKILL.md): Select a solution concept and refine its design against agreed needs and behavior.
- [bdd-discover-behavior](plugins/frantss-bdd/skills/bdd-discover-behavior/SKILL.md): Discover expected behavior through examples and per-area review in a live Markdown record.
- [bdd-formulate-behavior](plugins/frantss-bdd/skills/bdd-formulate-behavior/SKILL.md): Turn agreed behavior into Gherkin specifications for existing test tools.
- [bdd-slice-work](plugins/frantss-bdd/skills/bdd-slice-work/SKILL.md): Group specified behavior into manageable tickets and review the breakdown with the user.
- [bdd-implement-ticket](plugins/frantss-bdd/skills/bdd-implement-ticket/SKILL.md): Implement one accepted ticket with native tests and current behavioral verification evidence.

### frantss-tracking

Configure sources and storage, track commitments, and report personal and team
activity.

- [core-configure](plugins/frantss-tracking/skills/core-configure/SKILL.md): Set up and maintain connections, projects, and sources.
- [core-update](plugins/frantss-tracking/skills/core-update/SKILL.md): Update skills by commit hash and migrate configuration and stored records.
- [tracking-tasks](plugins/frantss-tracking/skills/tracking-tasks/SKILL.md): Capture tasks and manage commitments, dates, and blockers.
- [tracking-collect](plugins/frantss-tracking/skills/tracking-collect/SKILL.md): Read project sources for task links and report summaries.
- [tracking-report](plugins/frantss-tracking/skills/tracking-report/SKILL.md): Create daily and weekly activity reports.
- [tracking-team-digest](plugins/frantss-tracking/skills/tracking-team-digest/SKILL.md): Summarize team initiatives from supplied sources and save a digest by default.
- [persistence-records](plugins/frantss-tracking/skills/persistence-records/SKILL.md): Store task links and report summaries through a shared database.
- [persistence-obsidian](plugins/frantss-tracking/skills/persistence-obsidian/SKILL.md): Store records in Obsidian through its official CLI.

## Install

This repository is private. Your installer needs GitHub access. Choose one
installation method per agent to avoid duplicate skills.

For Codex and Claude, replace `frantss-development` with `frantss-bdd` or
`frantss-tracking` to choose another domain. Repeat the install command for each
plugin you want. Each plugin includes all skills listed under its name above.
Start a new session after installation.

<details>
<summary>Codex CLI</summary>

Install a [domain plugin](#skills):

```bash
codex plugin marketplace add Frantss/frantss-skills
codex plugin add frantss-development@frantss
```

</details>

<details>
<summary>Claude Code CLI</summary>

Configure Git access to this repository, then install a [domain plugin](#skills):

```bash
claude plugin marketplace add Frantss/frantss-skills
claude plugin install frantss-development@frantss
```

</details>

<details>
<summary>GitHub CLI</summary>

Authenticate with `gh auth login`, then install one skill for your agent:

```bash
gh skill install Frantss/frantss-skills core-communicate --agent codex
```

Replace `core-communicate` with any skill name, or use `--all` for every skill.
Replace `codex` with your agent, such as `claude-code`, `github-copilot`, or
`cursor`. Installation defaults to the current project; add `--scope user`
for all projects.

See the [GitHub CLI reference](https://cli.github.com/manual/gh_skill_install).

</details>

<details>
<summary>skills CLI</summary>

Use Node.js 22.20 or later and Git credentials for this repository:

```bash
npx skills@latest add Frantss/frantss-skills --skill core-communicate --agent codex
```

Replace `core-communicate` with any skill name and `codex` with your agent, such
as `claude-code`, `github-copilot`, or `cursor`. Installation defaults to the
current project; add `--global` for all projects. Omit `--skill` and `--agent`
to choose interactively.

See the [skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

</details>

## Update

Ask `core-update` to update your Frantss skill set or check for updates.
It reviews changes through a fixed default-branch commit, applies required
configuration/database migrations, and updates through the original installer.
Checks are read-only; explicit pins and selected skills remain in effect.

Full installation and shared data commit hashes are tracked separately in
`~/.frantss/skills-state.yaml`. First use verifies existing provenance and data
formats. Backups and a pending-step journal support interrupted updates.
Installer updates change skill files only; use this workflow for configuration
and stored-record migrations.

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
