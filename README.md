# Frantss skills

My personal agent skills, shared from one source across Codex, Claude Code,
Cursor, GitHub Copilot, Gemini CLI, and other agents that support
[Agent Skills](https://agentskills.io/specification).

Skills live in `skills/<name>/SKILL.md`. Claude Code can install the collection
as a plugin; other agents can install individual skills with GitHub CLI.

## Install

This repository is private. Anyone installing from GitHub needs repository
access. Authenticate GitHub CLI with `gh auth login` first.

### Codex and other agents

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

### Claude Code plugin

```bash
claude plugin marketplace add Frantss/frantss-skills
claude plugin install frantss-skills@frantss
```

Use either the plugin or direct skill installation for Claude Code to avoid
duplicate skills. For private Git sources, configure SSH access to GitHub on
the machine running Claude Code. See its
[private marketplace guidance](https://code.claude.com/docs/en/plugins/host-marketplace).

## Update

Use the installer that originally installed the skills:

```bash
gh skill update --dry-run
gh skill update my-skill
```

`gh skill update --all` updates installed skills across known workspace and user
locations; `--dir .agents/skills` limits the scan to that directory. Pinned
skills stay pinned unless you pass `--unpin`.

For the Claude plugin:

```bash
claude plugin marketplace update frantss
claude plugin update frantss-skills@frantss
```

For skills installed with Vercel's CLI, use `npx skills update`.

## Skills

| Skill | Description |
| --- | --- |
| [communicate](skills/communicate/SKILL.md) | Write clear, direct replies throughout the session while preserving technical meaning. |
| [setup-frantss-skills](skills/setup-frantss-skills/SKILL.md) | Set up `.frantss`, workspace identity, and tracking's shared backend and source access. |
| [tracking-tasks](skills/tracking-tasks/SKILL.md) | Capture commitments into one inbox, triage them into workspaces, and manage pending tasks and acknowledgment. |
| [tracking-collect](skills/tracking-collect/SKILL.md) | Gather dated activity and evidence from configured sources, preserving provenance and collection coverage. |
| [tracking-report](skills/tracking-report/SKILL.md) | Create, save, and retrieve daily or weekly reports covering contributions, pending work, and evidence gaps. |
| [tracking-persist](skills/tracking-persist/SKILL.md) | Define shared settings, logical records, and storage requirements for tasks, evidence, and reports across backends. |
| [tracking-persist-obsidian](skills/tracking-persist-obsidian/SKILL.md) | Store tracking records and revisions as Obsidian notes, with Bases views for tasks and activity. |

## Configuration

Use `setup-frantss-skills` to configure a workspace. Its [tracking guide](skills/setup-frantss-skills/references/tracking.md)
handles the shared backend; its [source guide](skills/setup-frantss-skills/references/sources.md)
defines source scope and CLI, API, skill, MCP, or plugin access methods.

Each workspace has a stable identity in `.frantss/workspace.yaml`. Tracking uses
one shared backend selected by `.frantss/tracking.yaml`. Shared [settings](skills/tracking-persist/references/settings.md)
and workspace source mappings live in that backend. Setup excludes `.frantss` from Git.
Install both persistence skills to use Obsidian; setup requires an existing vault path and a tracking root.

## Automatic use

For consistent communication and task capture across sessions, reference
`communicate` and `tracking-tasks` in your agent's persistent instructions.
Skill discovery alone does not ensure automatic use.

For `communicate`, replace `<installed-skill-path>` with its installed location:

```text
Before your first reply, read <installed-skill-path>.
Apply it to every message to me throughout the session, on every topic.
If its instructions leave the context, read it again before your next message.
```

For Codex, use `~/.codex/AGENTS.md`; see the [persistent instructions guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
For other agents, use their supported persistent instructions file or setting.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for writing, testing, and packaging skills.
Create a skill with `python3 scripts/new_skill.py my-skill --description "Use when ..."`,
then run `make validate`. Validation requires Python 3.10+, GitHub CLI with `gh skill`,
and Claude Code. CI pins GitHub CLI 2.101.0 and Claude Code 2.1.291.

## Layout

```text
skills/<name>/SKILL.md         Shared, installable skills
templates/SKILL.md.tmpl        Starter; excluded from skill discovery
scripts/new_skill.py           Create a skill without overwriting an existing one
scripts/validate.py            Packaging checks and official CLI validators
.claude-plugin/                Claude plugin and marketplace manifests
.github/workflows/validate.yml Validation on pushes and pull requests
AGENTS.md                     Guidance for agents editing this repository
```

Each skill can carry its own `references/`, `scripts/`, and `assets/` when
needed. Agent-specific UI metadata belongs alongside the skill, such as
`agents/openai.yaml`; shared instructions remain portable. See the
[Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).
