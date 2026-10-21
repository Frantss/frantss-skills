# Frantss skills

My personal agent skills, shared from one source across Codex, Claude Code,
Cursor, GitHub Copilot, Gemini CLI, and other agents that support
[Agent Skills](https://agentskills.io/specification).

Skills live in `skills/<name>/SKILL.md`. Claude Code can install the collection
as a plugin; other agents can install individual skills with GitHub CLI.

## Create a skill

Requires Python 3.10+, GitHub CLI with `gh skill` support, and Claude Code for
manifest validation. This setup is checked with GitHub CLI 2.101.0 and Claude
Code 2.1.291; CI pins those versions.

```bash
python3 scripts/new_skill.py my-skill \
  --description "Use when performing the specific task this skill handles."
```

Edit the generated file, replacing the scaffold comments with real instructions,
then run:

```bash
make validate
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for writing, testing, and packaging skills.

## Communication

[communicate](skills/communicate/SKILL.md) applies to every message. It combines
simple English with rules for direct answers, consistent terms, and natural writing.
It preserves technical meaning and exact code or quotes.

[review-communication](skills/review-communication/SKILL.md) checks selected text
when explicitly invoked. Use it to get specific findings and suggested changes.
In Codex, invoke it as `$review-communication`. Other agents can use their
explicit skill invocation interface.
The review skill includes its own checks and works without `communicate`.

For use across projects, install the skill at user scope after these changes
are committed and pushed:

```bash
gh skill install Frantss/frantss-skills communicate --agent codex --scope user
gh skill install Frantss/frantss-skills review-communication --agent codex --scope user
```

Skill discovery alone does not ensure use on every turn. Add this rule to your
agent's persistent instructions. Replace `<installed-skill-path>` with the actual
path to the installed `communicate/SKILL.md`:

```text
Before your first reply, read <installed-skill-path>.
Apply it to every message to me throughout the session, on every topic.
If its instructions leave the context, read it again before your next message.
```

For Codex, use the global `~/.codex/AGENTS.md`. See the
[persistent instructions guide](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
For other agents, use their supported persistent instructions file or setting.
This repository's `AGENTS.md` already includes the rule for work here.

## Configuration

[setup-frantss-skills](skills/setup-frantss-skills/SKILL.md) manages the shared
`.frantss` configuration directory and its Git exclusion. General setup prepares
this directory without enabling a configuration. Tracking is currently supported;
other configurations can add guides and files without changing shared setup.

Inspection is read-only. Updates preserve unselected configuration files, and
already tracked configuration requires explicit Git index cleanup.

## Tracking

Shared reporting settings and account identities live in the selected backend;
each project record holds its sources. The local config holds only the backend
connection. Agents can discover a unique config in the current directory or
its ancestors. Supply the same config path when working elsewhere, so projects
continue to share one backend. Config files stay outside installed skill folders.
The `.frantss` directory is shared across Frantss skills. Tracking owns only
`tracking.yaml`; other skills can keep separate configuration files alongside it.

[tracking-tasks](skills/tracking-tasks/SKILL.md) captures tasks and commitments,
triages the single inbox into existing projects, and tracks pending work.
It also captures clear user-owned follow-ups during ongoing work.

Tasks start unreviewed. Your explicit acknowledgment adds `reviewed-by-frantss`;
categorization and completion preserve that separate review state.
Project creation requires an explicit command from you.

The skills use short entrypoints and operation-specific references, within a
hard limit of 100 total lines per skill, or 200 for `tracking-persist`.
References load only when needed.
Live writes require a configured persistence interface.

[tracking-collect](skills/tracking-collect/SKILL.md) gathers and persists activity
from each selected project's configured sources. It retains event dates, source
context, and collection coverage for later queries. Source-specific guidance and
the evidence format load only when needed. Collection can hand outstanding
commitments to `tracking-tasks`.

[tracking-report](skills/tracking-report/SKILL.md) creates and saves daily or
weekly reports from collected evidence and task history. It includes untracked
contributions, distinguishes past status from current pending work, and records
coverage gaps. Period, content, and persistence details load only when needed.

[tracking-persist](skills/tracking-persist/SKILL.md) defines what must be saved
and retrieved: tasks, projects, evidence, collection coverage, task events,
report snapshots, and prior revisions. It defines logical records and operation
requirements, then routes requests to the configured storage adapter.

[tracking-persist-obsidian](skills/tracking-persist-obsidian/SKILL.md) implements
that storage in a selected Obsidian vault. It handles note mapping, file reads
and writes, recovery, revision folders, and scoped Bases views. Those references
load only when needed. Install both persistence skills for this backend;
replacing the adapter does not change the tracking, collection, or reporting
workflows. Setup requires a vault path and tracking root. No live vault is
configured by this repository.

For reliable automatic capture across sessions, add a rule to your agent's
persistent instructions to use `tracking-tasks` when clear user-owned follow-ups
or commitments arise. Skill discovery alone does not guarantee that behavior.

## Install

This repository is private. Anyone installing from GitHub needs repository
access. Authenticate GitHub CLI with `gh auth login` first.

### Codex and other agents

Run inside the project that should receive the skills:

```bash
gh skill install Frantss/frantss-skills --all --agent codex
```

Replace `codex` with `cursor`, `github-copilot`, `gemini-cli`, or `claude-code`.
`gh skill install --help` lists supported agents. Several agents share the
project's `.agents/skills/` directory, so one installation can serve them all.
See the [GitHub CLI install reference](https://cli.github.com/manual/gh_skill_install).

To install one skill, replace `--all` with its name. Add `--scope user` for
personal skills available across projects. Use `--pin <commit-sha>` when you
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

`gh skill update --all` updates installed skills across known project and user
locations; `--dir .agents/skills` limits the scan to that directory. Pinned
skills stay pinned unless you pass `--unpin`.

For the Claude plugin:

```bash
claude plugin marketplace update frantss
claude plugin update frantss-skills@frantss
```

For skills installed with Vercel's CLI, use `npx skills update`.

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
