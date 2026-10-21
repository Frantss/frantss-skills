# Frantss skills

These skills are a work in progress. I'm still iterating on them.

My personal agent skills, shared from one source across Codex, Claude Code,
Cursor, GitHub Copilot, Gemini CLI, and other agents that support
[Agent Skills](https://agentskills.io/specification).

Skills live in `skills/<name>/SKILL.md`. Codex and Claude Code can install the
collection as a plugin; other agents can install individual skills with GitHub CLI.

## Install

This repository is private. Anyone installing from GitHub needs repository
access. Authenticate GitHub CLI with `gh auth login` first.

### Individual skills

Run inside the workspace that should receive the skills:

```bash
gh skill install Frantss/frantss-skills --all --agent codex
```

Replace `codex` with `cursor`, `github-copilot`, `gemini-cli`, or `claude-code`.
`gh skill install --help` lists supported agents. Several agents share the
workspace's `.agents/skills/` directory, so one installation can serve them all.
See the [GitHub CLI install reference](https://cli.github.com/manual/gh_skill_install).

To install one skill, replace `--all` with its name. Add `--scope user` for
personal skills available across workspaces. Use `--pin <commit-sha>` when you
need a fixed revision. Unpinned installs prefer the latest release tag, falling
back to the default branch when there are no releases.

For another installer, [Vercel's skills CLI](https://github.com/vercel-labs/skills)
reads the same source:

```bash
npx skills add Frantss/frantss-skills
```

### Codex plugin

Use a Codex CLI with `plugin` commands and Git credentials that can read this private repository:

```bash
codex plugin marketplace add Frantss/frantss-skills
codex plugin add frantss-skills@frantss
```

Start a new Codex session after installation. Codex uses its own manifest and
the same marketplace and `skills/` directory as Claude Code.
See the [Codex plugin command reference](https://learn.chatgpt.com/docs/cli/reference#codex-plugin).

### Claude Code plugin

```bash
claude plugin marketplace add Frantss/frantss-skills
claude plugin install frantss-skills@frantss
```

Use either the plugin or direct skill installation for each agent to avoid
duplicate skills. For private Git sources, configure SSH access to GitHub on
the machine running Claude Code. See its
[private marketplace guidance](https://code.claude.com/docs/en/plugins/host-marketplace).

## Update

Use the installer that originally installed the skills:

```bash
gh skill update --dry-run
gh skill update frantss-my-skill
```

`gh skill update --all` updates installed skills across known workspace and user
locations; `--dir .agents/skills` limits the scan to that directory. Pinned
skills stay pinned unless you pass `--unpin`.

For the Codex plugin, refresh the marketplace and reinstall the updated package:

```bash
codex plugin marketplace upgrade frantss
codex plugin add frantss-skills@frantss
```

For the Claude Code plugin:

```bash
claude plugin marketplace update frantss
claude plugin update frantss-skills@frantss
```

For skills installed with Vercel's CLI, use `npx skills update`.

## Skills

| Skill | Description |
| --- | --- |
| [frantss-communicate](skills/frantss-communicate/SKILL.md) | Write clear, direct replies throughout the session while preserving technical meaning. |
| [frantss-decompose](skills/frantss-decompose/SKILL.md) | Break down problems through context gathering, alternatives, and questionnaire rounds per part, with a live Markdown document and stable IDs. |
| [frantss-configure](skills/frantss-configure/SKILL.md) | Set up, inspect, and maintain Frantss configuration, including lasting project/source changes stated during conversation. |
| [frantss-tracking-tasks](skills/frantss-tracking-tasks/SKILL.md) | Capture brief tasks, triage them across Inbox, Next, Later, Maybe, and Done, and manage projects, dates, blockers, and acknowledgment. |
| [frantss-tracking-collect](skills/frantss-tracking-collect/SKILL.md) | Gather dated activity and evidence from configured sources, preserving provenance and collection coverage. |
| [frantss-tracking-report](skills/frantss-tracking-report/SKILL.md) | Create, save, and retrieve daily or weekly reports covering contributions, pending work, and evidence gaps. |
| [frantss-persistance](skills/frantss-persistance/SKILL.md) | Persist complete workflow payloads through one backend, preserving common record identities, revisions, and recoverable operations. |
| [frantss-persistance-obsidian](skills/frantss-persistance-obsidian/SKILL.md) | Use the Obsidian CLI to store Frantss records and revisions as notes and create requested Bases views. |

A [project](GLOSSARY.md) groups related tasks, activity, and sources for frantss. It may be ongoing or bounded and span multiple repositories.

Tasks start in Inbox. Clear evidence supports automatic triage: assigned current-sprint work goes to Next,
nonurgent commitments to Later, and tentative possibilities to Maybe. Uncertain decisions stay in Inbox for clarification.
Project assignment and your `reviewed-by-frantss` acknowledgment are independent of state; blockers remain notes on Next/Later tasks.
Firm due dates and expected completion dates are optional and distinct. Weekly reports include undated Later commitments;
daily reports emphasize Next, dates, and blockers. Reports suggest reassessment without changing tasks.
Task content aims for 5–15 lines, with a hard limit of 50 excluding link-only lines and storage metadata.
Linked tickets/documents retain their details; tasks hold an outcome, brief context, and references.

## Configuration

Use `frantss-configure` to set up, inspect, and maintain your user-wide connection, project registry, and sources.
Its [persistence guide](skills/frantss-configure/references/persistence.md)
checks the shared backend; its [tracking guide](skills/frantss-configure/references/sources.md)
configures tracking settings, source instances, target locations, and the user's identity in each source.
Source records contain `id`, `provider`, `instance`, `identity`, and bounded `scope`; collection chooses available tools in the active harness.

Setup initializes only explicitly selected configuration. Inspection reads without changing it.
Maintenance applies clear, lasting changes stated by you during conversation and asks when the target or scope is uncertain.
Incidental mentions, quoted discussions, inactivity, and access failures do not establish additions or removals.
Project creation and backend changes still need explicit commands. Source changes retain stable IDs when they represent the same logical source,
apply to subsequent collection runs, and preserve stored evidence/history.

Frantss workflows share one connection in `~/.frantss/persistance.yaml`, regardless of the current directory.
The file holds `schema_version: 1` and `backend: {adapter, options}`. Other Frantss configurations can use sibling files.
Project definitions live in `~/.frantss/projects.yaml`, independently of backend availability:

```yaml
schema_version: 1
projects:
  frantss/frantssuy:
    title: Frantss website
    area: side-projects
    local_paths: []
    sources:
      - id: code
        provider: github
        instance: github.com
        identity: frantss
        scope: {repositories: [frantss/frantssuy]}
```

The backend stores tasks, evidence, collection runs, reports, revisions, and shared
[settings/accounts](skills/frantss-persistance/references/settings.md). Records reference project IDs as strings; they do not store project or source definitions.
Repository-backed IDs use kebab-case `org/repo`, such as `frantss/frantssuy`; other projects use a chosen slug, such as `personal-admin`.
IDs remain fixed after repository renames or moves; backend workflow records use UUIDs.

Sources define repository associations as well as collection scope. An explicit project selection takes precedence.
GitHub supplies repository events; local Git identifies the checkout through its root and remotes.
For the current project, match repository locations from sources, then machine-specific canonical paths;
ask when a match is absent or ambiguous. Worktrees can share a project identity.
Creating projects requires an explicit command; established association changes use configuration maintenance. General setup creates no projects or associations.
Inbox capture and cross-project reports need no local project association.

Configuration is user-wide; repository-local folders and Git-ignore changes are unnecessary.
Only the documented current formats are supported. Incompatible data is reported without conversion; record history and partial-write recovery remain supported.
Install both persistence skills to use Obsidian; setup requires an existing vault path and a storage root, defaulting to `Frantss` for new setups.
Enable and register the official Obsidian CLI; it connects to the desktop app.

## Automatic use

For consistent communication, task capture, and configuration maintenance across sessions, reference
`frantss-communicate`, `frantss-tracking-tasks`, and `frantss-configure` in your agent's persistent instructions.
Skill discovery alone does not ensure automatic use.

For `frantss-communicate`, replace `<installed-skill-path>` with its installed location:

```text
Before your first reply, read <installed-skill-path>.
Apply it to every message to me throughout the session, on every topic.
If its instructions leave the context, read it again before your next message.
```

For Codex, use `~/.codex/AGENTS.md`; see the [persistent instructions guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
For other agents, use their supported persistent instructions file or setting.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for writing, testing, and packaging skills.
Create a skill with `python3 scripts/new_skill.py frantss-my-skill --description "Use when ..."`,
then run `make validate`. Validation requires Python 3.10+, GitHub CLI with `gh skill`,
and Claude Code.

## Layout

```text
skills/<name>/SKILL.md         Shared, installable skills
templates/SKILL.md.tmpl        Starter; excluded from skill discovery
scripts/new_skill.py           Create a skill without overwriting an existing one
scripts/validate.py            Packaging checks and official CLI validators
.claude-plugin/                Claude plugin and shared marketplace manifests
.codex-plugin/                 Codex plugin manifest pointing to the shared skills
AGENTS.md                     Guidance for agents editing this repository
```

Each skill can carry its own `references/`, `scripts/`, and `assets/` when
needed. Agent-specific UI metadata belongs alongside the skill, such as
`agents/openai.yaml`; shared instructions remain portable. See the
[Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).
