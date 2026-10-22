# Authoring skills

Start with one concrete task you repeat across workspaces. Give the skill a name
that describes that task and a description that helps an agent recognize when
to use it. The folder and frontmatter name must match.

```bash
python3 scripts/new_skill.py frantss-my-skill --description "Use when ..."
```

Prefix skill names with `frantss-`. Use lowercase letters, digits, and single
hyphens, up to 64 characters.
The generator refuses existing destinations and invalid names.

## Write the shared instructions

Each skill has a hard limit of 75 total lines across its authored UTF-8 text
files. `frantss-communicate` and `frantss-update` each have a 50-line limit;
`frantss-persistance` and `frantss-persistance-obsidian` each have a 100-line limit.
`frantss-decompose` has a 200-line limit.
Count frontmatter, blank lines, references, helper code, and metadata.
Binary assets are excluded. `make validate` enforces the total per skill;
progressive disclosure does not increase the budget.

Workflows own their domain schemas; persistence owns the common record envelope
and storage operations. Ordinary workflows support only current formats. Keep
current records and interrupted-write recovery; keep migration backups outside
active storage. `frantss-update` owns upgrades:
compare source commits and migrate configuration/data before recording success.
When changing a stored format, document the old/new mapping, applicability,
verification, and retry behavior in the same commit. Preserve those instructions
in source history so updates can cross several revisions.

Replace every scaffold comment with the workflow's actual decisions and a
checkable completion condition. Keep only guidance that changes how an agent
performs the task. The description is read before activation; put detailed
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

## Check a skill

```bash
make validate
```

This runs repository packaging checks, `gh skill publish --dry-run` for actual
skills, and `claude plugin validate`. Packaging checks include the Codex manifest
and its shared marketplace identity. It publishes nothing. A missing-version
or missing-license warning can be expected for these private manifests; review
other warnings. An empty collection is allowed while setting up the repository.

The packaging checker catches symlinks, broken inline relative Markdown
links, unfinished scaffold comments, and manifest drift. It does not parse all
Markdown syntax, validate remote URLs, or establish workflow correctness.

Try installation into a temporary directory before sharing a new skill:

```bash
preview_dir=$(mktemp -d)
gh skill install . frantss-my-skill --from-local --dir "$preview_dir"
```

Inspect that copied folder and exercise it with the intended agents. Check one
request that should activate the skill, one nearby request that should not,
and any scripts or resource links used during the task. Testing only the
authoring folder can hide dependencies that disappear during installation.

For Claude, `claude --plugin-dir .` loads the local plugin for a test session.
Avoid installing drafts into your everyday skills directories.

With the Codex CLI installed, `make test` also exercises plugin installation and
reinstallation through the shared marketplace, using a temporary Codex configuration
and cache. It verifies that new and edited skills reach the installed package.

## Share changes

Commit and push completed skills to this private repository. Every new skill
under `skills/` is discovered automatically; manifests need no per-skill list.
Use `gh skill install` to choose individual skills, or a Codex or Claude plugin for the
collection. Keep skill names stable so installations and explicit invocations
continue to resolve.

When changing a trigger, explain which requests should now activate it. When
changing a workflow, record the representative task you exercised. Tooling
changes also need `make test`.
