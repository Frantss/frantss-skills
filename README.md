# Frantss skills

My personal agent skills for communication, development, task tracking, and activity
reports. Use them with agents that support [Agent Skills](https://agentskills.io/specification),
including Codex, Claude Code, Cursor, GitHub Copilot, and Gemini CLI.

> [!NOTE]
> These skills are still a work in progress. Their behavior and configuration may change.

## Skills

The `frantss-skills` plugin includes all skills below.

### Development

- [communicate](skills/communicate/SKILL.md): Write clear, direct replies throughout the session.
- [refactoring](skills/refactoring/SKILL.md): Refactor existing code through scoped changes and behavior-preservation checks, or assess requested refactoring opportunities.
- [atomic-commits](skills/atomic-commits/SKILL.md): Group all pending changes or a selected subset into small, cohesive Git commits.

### BDD

- [frame-problem](skills/frame-problem/SKILL.md): Establish needs, outcomes, evidence, scope, and constraints in a live problem brief.
- [design-solution](skills/design-solution/SKILL.md): Select a solution concept and refine its design against agreed needs and behavior.
- [discover-behavior](skills/discover-behavior/SKILL.md): Discover expected behavior through examples and per-area review in a live Markdown record.
- [formulate-behavior](skills/formulate-behavior/SKILL.md): Turn agreed behavior into Gherkin specifications for existing test tools.
- [slice-work](skills/slice-work/SKILL.md): Group specified behavior into manageable tickets and review the breakdown with the user.
- [implement-ticket](skills/implement-ticket/SKILL.md): Implement one accepted ticket with native tests and current behavioral verification evidence.

### Tracking

- [configure](skills/configure/SKILL.md): Set up and maintain connections, projects, and sources.
- [migrate-tracking](skills/migrate-tracking/SKILL.md): Check or migrate tracking configuration and stored records, with backups and recovery.
- [tasks](skills/tasks/SKILL.md): Capture tasks and manage commitments, dates, and blockers.
- [collect](skills/collect/SKILL.md): Read project sources for task links and report summaries.
- [report](skills/report/SKILL.md): Create daily and weekly activity reports.
- [team-digest](skills/team-digest/SKILL.md): Summarize team initiatives from supplied sources and save a digest by default.
- [records](skills/records/SKILL.md): Store task links and report summaries through a shared database.
- [obsidian](skills/obsidian/SKILL.md): Store records in Obsidian through its official CLI.

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
gh skill install Frantss/frantss-skills communicate --agent codex
```

Replace `communicate` with any skill name, or use `--all` for every skill.
Replace `codex` with your agent, such as `claude-code`, `github-copilot`, or
`cursor`. Installation defaults to the current project; add `--scope user`
for all projects.

See the [GitHub CLI reference](https://cli.github.com/manual/gh_skill_install).

</details>

<details>
<summary>skills CLI</summary>

Use Node.js 22.20 or later and Git credentials for this repository:

```bash
npx skills@latest add Frantss/frantss-skills --skill communicate --agent codex
```

Replace `communicate` with any skill name and `codex` with your agent, such
as `claude-code`, `github-copilot`, or `cursor`. Installation defaults to the
current project; add `--global` for all projects. Omit `--skill` and `--agent`
to choose interactively.

See the [skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

</details>

## Updates and tracking migrations

Use your plugin manager or original installer to update skills. Package updates
do not migrate tracking configuration or stored records.

Ask `migrate-tracking` to check compatibility, migrate legacy tracking formats,
or resume an interrupted migration. Checks are read-only. Migrations preserve
identities and human edits, with verified backups and a recovery journal in
`~/.frantss/skills-state.yaml`. Existing installation entries remain unchanged;
the skill manages only migration state.

For older connection configurations, see the
[database key migration](skills/migrate-tracking/references/database-migration.md).

## Tracking setup and automatic use

The tracking skills use a shared database, projects, and sources. Use
[configure](skills/configure/SKILL.md) to set them up across workspaces.
For Obsidian storage, install `records` and `obsidian` and enable the official
Obsidian CLI with an existing vault. Setup requires Tasks and Reports Bases with
verified default views; missing or failing views leave setup incomplete.

For automatic tracking across sessions, reference `tasks` and `configure` in
your agent's persistent instructions. Skill discovery alone does not ensure
automatic use.

## Communication across sessions

To apply `communicate` automatically, add this text to your agent's persistent
instructions with the installed skill's path:

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
