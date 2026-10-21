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
| [frantss-tracking-tasks](skills/frantss-tracking-tasks/SKILL.md) | Capture tasks and manage commitments, dates, and blockers. |
| [frantss-tracking-collect](skills/frantss-tracking-collect/SKILL.md) | Gather dated activity and evidence from project sources. |
| [frantss-tracking-report](skills/frantss-tracking-report/SKILL.md) | Create daily and weekly activity reports. |
| [frantss-persistance](skills/frantss-persistance/SKILL.md) | Store workflow records and their history through a shared backend. |
| [frantss-persistance-obsidian](skills/frantss-persistance-obsidian/SKILL.md) | Store records in Obsidian through its official CLI. |

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
