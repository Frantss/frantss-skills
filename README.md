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

For use across workspaces, install the skill at user scope after these changes
are committed and pushed:

```bash
gh skill install Frantss/frantss-skills communicate --agent codex --scope user
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
`.frantss` configuration directory and its Git exclusion. General setup prepares this directory
without enabling a configuration. Named configurations load their own guides;
workspace identity and tracking are currently supported. Other configurations can
add separate guides and files without changing the shared setup procedure.

Inspection is read-only. Updates preserve unselected configuration files, and
already tracked configuration requires explicit Git index cleanup.

Each workspace has its own `.frantss/workspace.yaml`, containing one
stable UUID and display name. This identity is shared by that workspace's Frantss
skills and requires no tracking backend. Explicit workspace setup allocates the
identity once; renaming the workspace, moving its files, or changing backends
preserves it. Tracking can query other workspaces through their persisted records.
Inbox capture and operations scoped by stored workspace IDs require no local identity file.

## Tracking

Shared reporting settings and account identities live in the selected backend;
each tracking workspace record holds its sources and uses its workspace ID.
Tracking setup configures each source's stable ID, provider, account, user identity,
collection scope, and access methods. The [source configuration guide](skills/setup-frantss-skills/references/sources.md)
defines supported providers and fields, including `gmail` and `google-calendar`.
Collection and persistence consume configuration without their own provider catalogs.
Source changes preserve other mappings; unavailable access checks remain explicit.
The tracking connection file holds only the backend
connection. Agents can discover a unique config in the current directory or
its ancestors. Supply the same config path when working elsewhere, so workspaces
continue to share one backend. Config files stay outside installed skill folders.
The `.frantss` directory is shared across Frantss skills. Tracking owns only
`tracking.yaml`; other skills can keep separate configuration files alongside it.

A source can use a CLI, API, skill, MCP server, plugin, or a combination.
Referenced guidance can connect methods; interchangeable methods follow list order.
Setup resolves exact references and checks availability. Credentials remain in credential stores.

This example is a `sources` payload for a workspace record in the backend.
Replace placeholders with actual account, scope, and installed capability references:

```yaml
sources:
  - id: personal-mail
    provider: gmail
    account: <google-account>
    identity: <user-identity>
    scope:
      labels: [<label-id>]
    access:
      - kind: skill
        name: <installed-mail-skill>
      - kind: mcp
        server: <configured-mail-server>
        tools: [<read-tool>]
      - kind: plugin
        id: <installed-mail-plugin>
        tools: [<read-tool>]
  - id: personal-calendar
    provider: google-calendar
    account: <google-account>
    identity: <user-identity>
    scope:
      calendars: [<calendar-id>]
    access:
      - kind: cli
        executable: <calendar-cli>
        profile: personal
        guidance: <command-documentation-reference>
      - kind: api
        base_url: <calendar-api-base-url>
        docs: <api-documentation-reference>
        auth_ref: <credential-store-reference>
```

Access changes retain source IDs and existing evidence identities. Missing access
or ambiguous scope leaves collection incomplete; it never expands collection to all locations.

[tracking-tasks](skills/tracking-tasks/SKILL.md) captures tasks and commitments,
triages the single inbox into existing workspaces, and tracks pending work.
It also captures clear user-owned follow-ups during ongoing work.

Tasks start unreviewed. Your explicit acknowledgment adds `reviewed-by-frantss`;
categorization and completion preserve that separate review state.
Workspace creation requires an explicit command from you.

The skills use short entrypoints and operation-specific references, within a
hard limit of 100 total lines per skill, or 200 for `tracking-persist`.
References load only when needed.
Live writes require a configured persistence interface.

[tracking-collect](skills/tracking-collect/SKILL.md) gathers and persists activity
from each selected workspace's configured sources. It retains event dates, source
context, and collection coverage for later queries. Access guidance and
the evidence format load only when needed. Collection can hand outstanding
commitments to `tracking-tasks`.

[tracking-report](skills/tracking-report/SKILL.md) creates and saves daily or
weekly reports from collected evidence and task history. It includes untracked
contributions, distinguishes past status from current pending work, and records
coverage gaps. Period, content, and persistence details load only when needed.

[tracking-persist](skills/tracking-persist/SKILL.md) defines what must be saved
and retrieved: tasks, workspaces, evidence, collection coverage, task events,
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
