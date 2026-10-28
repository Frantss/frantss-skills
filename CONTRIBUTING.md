# Authoring skills

Start with one concrete task you repeat across workspaces. Give the skill a name
that describes that task and a description that helps an agent recognize when
to use it. The folder and frontmatter name must match.

Create `skills/<name>/SKILL.md` with `name` and `description` frontmatter.

Use the `tracking-` prefix for tracking skills and descriptive names without
category prefixes for other skills. Use lowercase letters, digits, and single
hyphens, up to 64 characters.

Use "the user" in instructions and "you" in replies addressed to the user.
Preserve repository attribution, storage paths, and technical identifiers.

## Write the shared instructions

Each skill has a hard limit of 75 total lines across its authored UTF-8 text
files. `atomic-commits` and `communicate` each have a 50-line limit;
`tracking-records` has a 100-line limit; `tracking-obsidian` has a 350-line
limit to include its executable batch runner.
Count frontmatter, blank lines, references, helper code, and metadata.
Binary assets are excluded. Review the total during skill edits;
progressive disclosure does not increase the budget.

Workflows own their domain schemas; persistence owns the common record envelope
and storage operations. Ordinary workflows support only current formats. Keep
current records and interrupted-write recovery; keep migration backups outside
active storage. `tracking-migrate` owns explicit configuration/data migrations;
installers own skill and plugin updates. Ordinary workflows report incompatible
formats without converting them. Keep known migration mappings inside
`tracking-migrate` so individual installations include their procedures.
When changing a stored format, document the old/new mapping, applicability,
verification, and retry behavior in the same commit. Preserve those instructions
in source history so updates can cross several revisions.

Write the workflow's actual decisions and a checkable completion condition.
Keep only guidance that changes how an agent performs the task. The description
is read before activation; put detailed
procedures in the body.

Add supporting files when needed:

| Path | Purpose |
| --- | --- |
| `references/` | Detail read only for a particular branch of the workflow |
| `scripts/` | Repeated operations that benefit from deterministic execution |
| `assets/` | Templates or files copied into the output |
| `agents/` | Optional agent-specific UI metadata |

Link references from the point where an agent needs them. Use links relative
to the containing Markdown file, and bundle every required resource within the
skill as real files and directories. GitHub CLI's local installer skips symlinks,
including internal ones. Keep examples generic enough to travel between workspaces;
record actual system, network, or tool requirements in `compatibility` when
relevant.

Use the [standard frontmatter fields](https://agentskills.io/specification).
Automatic invocation is the default. If you need explicit-only invocation,
configure and test it for each intended agent: Claude's
`disable-model-invocation` and Codex's `agents/openai.yaml` policy are different
interfaces. A tool allowlist also depends on the host; it does not authorize
external actions on the user's behalf.

Keep credentials and machine-specific paths in the user's environment. When
adapting an existing skill, preserve its license and attribution.

## BDD records

Each BDD skill owns its tracked-record guidance in `SKILL.md`, including its
artifact structure. The small repeated `run.md` convention keeps each skill
independently installable; there is no shared base or generation step.
Preserve the existing run fields, section names, slice tables, and status
meanings when changing stage guidance. Keep execution-table details in
`implement-ticket`; other stages only invalidate affected existing evidence.

Behavioral regression requests live in `tests/fixtures/bdd-requests.json`.
Exercise them in isolated workspaces and check actual outputs, artifacts,
questions, and stopping behavior. The matrix records expected outcomes; it is
not an automated claim of model behavior. Include nearby requests that should
use ordinary work and requests that explicitly continue existing tracked runs.

## Check a skill

```bash
make validate
```

This requires GitHub CLI with `gh skill` support and Claude Code CLI.
It runs `gh skill publish --dry-run` for skill format checks, then
`claude plugin validate` for the shared marketplace and root plugin.
Each command's failure stops validation; warnings permit success.
These commands validate local files without publishing. Missing-version,
missing-license, and icon warnings can be expected for these private packages;
review other warnings.

Review line budgets, self-contained resources, and local Markdown links during
authoring. Use the installation and behavioral checks below to verify the result.

Try installation into a temporary directory before sharing a new skill:

```bash
preview_dir=$(mktemp -d)
gh skill install . my-skill --from-local --dir "$preview_dir"
```

Inspect that copied folder and exercise it with the intended agents. Check one
request that should activate the skill, one nearby request that should not,
and any scripts or resource links used during the task. Testing only the
authoring folder can hide dependencies that disappear during installation.

For Claude, `claude --plugin-dir .` loads the complete local plugin for a test session.
Avoid installing drafts into your everyday skills directories.

With the Codex CLI installed, `make test` also exercises plugin installation and
reinstallation through the shared marketplace, using a temporary Codex configuration
and cache. It verifies that all resources survive installation, and added,
edited, and removed skills reach refreshed installations. The suite also tests
Claude Code and Copilot installation through the shared marketplace when those
CLIs are installed. Unavailable CLI integration checks are skipped.

## Plugin packaging

Author each skill directly in `skills/<name>/`. The repository root is the
`frantss-skills` plugin. Codex reads `.codex-plugin/plugin.json`, which references
`./skills/`. Claude Code and Copilot share `.claude-plugin/plugin.json` and
discover `skills/` automatically. There are no generated plugin copies.

The `frantss` marketplace in `.claude-plugin/marketplace.json` points its single
`frantss-skills` entry to `./`. Keep both plugin manifests consistent. New skills
need no manifest changes. Keep resources inside each skill as real files so
direct installation remains portable.

## Share changes

Commit completed skills to this private repository; push only when requested.
Every new skill under `skills/` is discovered by direct installers.
Use `gh skill install` to choose individual skills, or install `frantss-skills`
through Codex, Claude Code, or Copilot. Keep skill names stable so installations
and explicit invocations continue to resolve.

When changing a trigger, explain which requests should now activate it. When
changing a workflow, record the representative task you exercised. Tooling
changes also need `make test`.
