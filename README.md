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
- [break-down](skills/break-down/SKILL.md): Map and explain software or full specifications through areas, rules, states, cases, and evidence; callable by behavior discovery.
- [refactoring](skills/refactoring/SKILL.md): Refactor existing code through scoped changes and behavior-preservation checks, or assess requested refactoring opportunities.
- [atomic-commits](skills/atomic-commits/SKILL.md): Group all pending changes or a selected subset into small, cohesive Git commits.
- [ship-it](skills/ship-it/SKILL.md): Propose and execute an approved delivery plan using project conventions, including testing, commits, and release or PR creation.

### BDD

- [frame-problem](skills/frame-problem/SKILL.md): Establish needs, outcomes, evidence, scope, and constraints in a live problem brief.
- [design-solution](skills/design-solution/SKILL.md): Select a solution concept and refine its design against agreed needs and behavior.
- [discover-behavior](skills/discover-behavior/SKILL.md): Resolve expected behavior through rules, examples, and conversation, using break-down when specification context needs analysis.
- [formulate-behavior](skills/formulate-behavior/SKILL.md): Turn agreed behavior into Gherkin specifications for existing test tools.
- [slice-work](skills/slice-work/SKILL.md): Group specified behavior into bounded, verifiable tickets.
- [implement-ticket](skills/implement-ticket/SKILL.md): Implement one authorized ticket or bounded scope from clear acceptance cases, with native tests and current verification evidence.

Start with the smallest workflow that supplies the missing result:

| Starting point | Workflow |
| --- | --- |
| Existing software or a specification needs explanation | `break-down` |
| The need or intended outcome is unclear | `frame-problem` |
| A consequential solution choice is unresolved | `design-solution` |
| Expected behavior needs agreement | `discover-behavior`, using `break-down` for missing specification context |
| Clear acceptance cases and implementation authorization | `implement-ticket`, with no ticket document required |
| Agreed behavior needs implementation boundaries | `slice-work`, then authorized implementation |
| Gherkin is requested or useful to existing tooling | Insert `formulate-behavior` before planning or implementation |
| Existing software needs checking without changes | Ordinary verification: map the supplied cases to checks and report evidence and gaps |

Reuse current inputs and prior agreements. Check revisions before reusing implementation
observations; refresh affected findings without treating code changes as behavior decisions.
Standalone work creates only requested artifacts. Tracked work preserves the existing
`run.md` format and uses one slice for a small subject; additional area maps remain optional.

### Tracking

- [tracking-configure](skills/tracking-configure/SKILL.md): Set up and maintain connections, projects, and sources.
- [tracking-migrate](skills/tracking-migrate/SKILL.md): Check or migrate tracking configuration and stored records, with backups and recovery.
- [tracking-tasks](skills/tracking-tasks/SKILL.md): Capture tasks and manage commitments, dates, and blockers.
- [tracking-collect](skills/tracking-collect/SKILL.md): Read project sources for task links and report summaries.
- [tracking-report](skills/tracking-report/SKILL.md): Create daily and weekly activity reports.
- [tracking-team-digest](skills/tracking-team-digest/SKILL.md): Summarize team initiatives from supplied sources and save a digest by default.
- [tracking-records](skills/tracking-records/SKILL.md): Store task links and report summaries through a shared database.
- [tracking-obsidian](skills/tracking-obsidian/SKILL.md): Store records in Obsidian through its official CLI.

## Install

This repository is private. Your installer needs GitHub access. Choose one
installation method per agent to avoid duplicate skills.

Codex, Claude Code, and Copilot install the complete `frantss-skills` plugin from
the shared `frantss` marketplace. Start a new session after installation.
Use your plugin manager or original installer to update skills.

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

## Tracking

Use [tracking-configure](skills/tracking-configure/SKILL.md) to set up shared storage, projects,
and sources across workspaces. Obsidian storage requires `tracking-records`, `tracking-obsidian`,
and the official Obsidian CLI with an existing vault.

For automatic tracking, reference `tracking-tasks` and `tracking-configure` in your agent's
persistent instructions.

Use [tracking-migrate](skills/tracking-migrate/SKILL.md) to check or migrate
legacy configuration and records with backups and recovery. Package updates
do not migrate stored data.
