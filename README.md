# Frantss skills

My personal agent skills for communication, planning, task tracking, and activity
reports. Shared across agents that support [Agent Skills](https://agentskills.io/specification),
including Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

These skills are a work in progress. I'm still iterating on them.

## Skills

| Skill | Purpose |
| --- | --- |
| [frantss-communicate](skills/frantss-communicate/SKILL.md) | Write clear, direct replies throughout the session. |
| [frantss-decompose](skills/frantss-decompose/SKILL.md) | Break down problems through guided planning conversations. |
| [frantss-configure](skills/frantss-configure/SKILL.md) | Set up and maintain connections, projects, and sources. |
| [frantss-update](skills/frantss-update/SKILL.md) | Update skills by commit hash and migrate configuration and stored records. |
| [frantss-tracking-tasks](skills/frantss-tracking-tasks/SKILL.md) | Capture tasks and manage commitments, dates, and blockers. |
| [frantss-tracking-collect](skills/frantss-tracking-collect/SKILL.md) | Read project sources for task links and report summaries. |
| [frantss-tracking-report](skills/frantss-tracking-report/SKILL.md) | Create daily and weekly activity reports. |
| [frantss-persistance](skills/frantss-persistance/SKILL.md) | Store task links and report summaries through a shared backend. |
| [frantss-persistance-obsidian](skills/frantss-persistance-obsidian/SKILL.md) | Store records in Obsidian through its official CLI. |

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
Obsidian CLI with an existing vault.

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
