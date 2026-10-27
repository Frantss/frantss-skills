# Frantss skills

My personal agent skills for communication, development, task tracking, and activity
reports. Use them with agents that support [Agent Skills](https://agentskills.io/specification),
including Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

These skills are a work in progress.

## Skills

The `frantss-skills` plugin includes all skills below.

- [core-communicate](skills/core-communicate/SKILL.md): Write clear, direct replies throughout the session.
- [refactoring](skills/refactoring/SKILL.md): Refactor existing code through scoped changes and behavior-preservation checks, or assess requested refactoring opportunities.
- [atomic-commits](skills/atomic-commits/SKILL.md): Group all pending changes or a selected subset into small, cohesive Git commits.
- [bdd-frame-problem](skills/bdd-frame-problem/SKILL.md): Establish needs, outcomes, evidence, scope, and constraints in a live problem brief.
- [bdd-design-solution](skills/bdd-design-solution/SKILL.md): Select a solution concept and refine its design against agreed needs and behavior.
- [bdd-discover-behavior](skills/bdd-discover-behavior/SKILL.md): Discover expected behavior through examples and per-area review in a live Markdown record.
- [bdd-formulate-behavior](skills/bdd-formulate-behavior/SKILL.md): Turn agreed behavior into Gherkin specifications for existing test tools.
- [bdd-slice-work](skills/bdd-slice-work/SKILL.md): Group specified behavior into manageable tickets and review the breakdown with the user.
- [bdd-implement-ticket](skills/bdd-implement-ticket/SKILL.md): Implement one accepted ticket with native tests and current behavioral verification evidence.
- [core-configure](skills/core-configure/SKILL.md): Set up and maintain connections, projects, and sources.
- [core-update](skills/core-update/SKILL.md): Update skills by commit hash and migrate configuration and stored records.
- [tracking-tasks](skills/tracking-tasks/SKILL.md): Capture tasks and manage commitments, dates, and blockers.
- [tracking-collect](skills/tracking-collect/SKILL.md): Read project sources for task links and report summaries.
- [tracking-report](skills/tracking-report/SKILL.md): Create daily and weekly activity reports.
- [tracking-team-digest](skills/tracking-team-digest/SKILL.md): Summarize team initiatives from supplied sources and save a digest by default.
- [persistence-records](skills/persistence-records/SKILL.md): Store task links and report summaries through a shared database.
- [persistence-obsidian](skills/persistence-obsidian/SKILL.md): Store records in Obsidian through its official CLI.

## Install

This repository is private. Your installer needs GitHub access. Choose one
installation method per agent to avoid duplicate skills.

Codex, Claude Code, and Copilot install the complete `frantss-skills` plugin from
the shared `frantss` marketplace. Start a new session after installation.

<details>
<summary>Codex CLI</summary>

```bash
codex plugin marketplace add Frantss/frantss-skills
codex plugin add frantss-skills@frantss
```

</details>

<details>
<summary>Claude Code CLI</summary>

```bash
claude plugin marketplace add Frantss/frantss-skills
claude plugin install frantss-skills@frantss
```

</details>

<details>
<summary>GitHub Copilot CLI</summary>

```bash
copilot plugin marketplace add Frantss/frantss-skills
copilot plugin install frantss-skills@frantss
```

Copilot reads the shared Claude-compatible marketplace and plugin manifest.
See the [Copilot plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).

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

<details>
<summary>Replace the old domain plugins</summary>

If you installed `frantss-development`, `frantss-bdd`, or `frantss-tracking`,
refresh the marketplace and install `frantss-skills` with your CLI:

```bash
codex plugin marketplace upgrade frantss
codex plugin add frantss-skills@frantss
```

```bash
claude plugin marketplace update frantss
claude plugin install frantss-skills@frantss
```

```bash
copilot plugin marketplace update frantss
copilot plugin install frantss-skills@frantss
```

Check that all 17 skills load from `frantss-skills`. Then remove each old plugin
you installed, using your CLI below. Replace `frantss-development` with each old
plugin name as needed. For Claude, match the original installation scope with
`--scope user`, `--scope project`, or `--scope local`.

```bash
codex plugin remove frantss-development@frantss
```

```bash
claude plugin uninstall frantss-development@frantss
```

```bash
copilot plugin uninstall frantss-development
```

Restart your agent after removal to load the skills once. Shared configuration
and stored records do not need migration. Direct skill installations do not
need to switch to the plugin; use `core-update` to follow the moved source paths.

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
[database key migration](skills/persistence-records/references/database-migration.md).

## Setup and automatic use

Use [core-configure](skills/core-configure/SKILL.md) to set up the shared
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

Skills live in `skills/<name>/SKILL.md`. Each skill has one source folder, used
directly by the plugin and individual installers.
See [CONTRIBUTING.md](CONTRIBUTING.md)
for authoring and testing instructions, or the [glossary](GLOSSARY.md) for shared terms.

```bash
make validate
```
