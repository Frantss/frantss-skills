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
gh skill update my-skill
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
| [communicate](skills/communicate/SKILL.md) | Write clear, direct replies throughout the session while preserving technical meaning. |
| [setup-frantss-skills](skills/setup-frantss-skills/SKILL.md) | Set up `~/.frantss`, the shared backend connection, workspace registrations, and source locations and identities. |
| [tracking-tasks](skills/tracking-tasks/SKILL.md) | Capture commitments into one inbox, triage them into workspaces, and manage pending tasks and acknowledgment. |
| [tracking-collect](skills/tracking-collect/SKILL.md) | Gather dated activity and evidence from configured sources, preserving provenance and collection coverage. |
| [tracking-report](skills/tracking-report/SKILL.md) | Create, save, and retrieve daily or weekly reports covering contributions, pending work, and evidence gaps. |
| [frantss-persistance](skills/frantss-persistance/SKILL.md) | Persist shared workspace configuration and prepared workflow records through one backend, with conditional tracking schemas. |
| [frantss-persistance-obsidian](skills/frantss-persistance-obsidian/SKILL.md) | Use the Obsidian CLI to store Frantss records and revisions as notes and create requested Bases views. |

## Configuration

Use `setup-frantss-skills` to configure your user-wide connection and register workspaces.
Its [persistence guide](skills/setup-frantss-skills/references/persistence.md)
checks the shared backend; its [tracking guide](skills/setup-frantss-skills/references/sources.md)
configures tracking settings, source instances, target locations, and the user's identity in each source.
Source records contain `id`, `provider`, `account`, `identity`, and bounded `scope`; collection chooses available tools in the active harness.

Frantss workflows share one connection in `~/.frantss/persistance.yaml`, regardless of the current directory.
The file holds `schema_version: 1` and `backend: {adapter, options}`. Other Frantss configurations can use sibling files.
The backend stores shared [settings](skills/frantss-persistance/references/settings.md) and each workspace's
stable readable ID, display name, work/personal area, repository associations, machine-specific local paths, and sources.
Repository-backed IDs use kebab-case `org/repo`, such as `frantss/frantssuy`; other workspaces use a chosen slug, such as `personal-admin`.
IDs remain fixed after repository renames or moves; other record types continue to use UUIDs.

An explicit workspace selection takes precedence. For the current workspace, match registered repository remotes,
then machine-specific canonical paths; ask when a match is absent or ambiguous. Worktrees can share a workspace identity.
Creating workspaces and changing their associations require explicit instructions; general setup creates neither.
Inbox capture and cross-workspace reports need no local workspace association.

Repository-local `.frantss` folders and Git-ignore changes are no longer required.
Existing connections using the former tracking config or adapter name require explicit import; vault/root options stay unchanged.
Legacy UUIDs need an old-to-new ID mapping and reference/history migration. Local files are not discovered automatically.
Install both persistence skills to use Obsidian; setup requires an existing vault path and a storage root, defaulting to `Frantss` for new setups.
Enable and register the official Obsidian CLI; it connects to the desktop app.

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
.claude-plugin/                Claude plugin and shared marketplace manifests
.codex-plugin/                 Codex plugin manifest pointing to the shared skills
.github/workflows/validate.yml Validation on pushes and pull requests
AGENTS.md                     Guidance for agents editing this repository
```

Each skill can carry its own `references/`, `scripts/`, and `assets/` when
needed. Agent-specific UI metadata belongs alongside the skill, such as
`agents/openai.yaml`; shared instructions remain portable. See the
[Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).
