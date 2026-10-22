# Working in this repo

This file defines agent behavior and repository working rules. Read `README.md`
for installation and authoring commands. Before changing skills or packaging,
read `CONTRIBUTING.md` for writing and distribution conventions.

## Communication

Before your first reply, read [core-communicate](skills/core-communicate/SKILL.md).
Apply it to every message to the user throughout the session, on every topic.
If its instructions leave the context, read it again before your next message.

- Keep replies terse and technical. Skip preambles, praise, and restating the request.
- Explain reasoning when it helps the user assess a decision or result.
- Evaluate proposals critically. State relevant strengths, weaknesses, and uncertainty.
- Use the chat's available feedback interfaces when user input is needed.

## Proposing solutions

- When proposing a solution, give at least two viable options if they exist.
  Recommend one and state each option's trade-off. If only one is viable, explain why.
- Briefly explain discarded options when they affect the decision.
- Cite the files, documentation, or other evidence that supports the proposal.
- Use high-level code examples, charts, or reports when they clarify the solution.

## Before acting

- Read the relevant skills, documentation, and code before choosing an approach.
- Check whether existing skills or tooling already address the request.
- Ask about missing information or unresolved ambiguity that affects the task.

## Acting and asking

- Proceed when explicitly asked to act. Make small, reversible local changes
  within the requested scope without requesting approval for each edit.
- If your understanding changes the task's scope or intended outcome, ask for direction
  before executing the changed task.
- Before external or destructive side effects, ask unless the user already
  authorized the action. Local edits and validation are part of implementation.

## Scope

- Keep changes within the request. Report unrelated findings without fixing them.
- If blocked, complete independent work within scope. Report the blocker and
  what remains unfinished.

## Skills and packaging

Keep `skills/<name>/` as the single source for every agent. Each skill must work
when that folder alone is copied elsewhere. Keep required resources inside it
as real files and directories, and use relative links. Installers can skip
symlinks even when their targets are internal. Put agent-specific integrations
in optional metadata or conditional references, with prerequisites stated
explicitly.

Create skills with `scripts/new_skill.py`. The template stays outside discovery
as a `.tmpl` file. Add only resources the workflow actually needs.

Keep plugin and marketplace identities stable. The manifests intentionally
omit `version`, so Git-backed installs follow commit revisions. Both plugins use
the shared `.claude-plugin/marketplace.json`; the Codex manifest points to `./skills/`,
while Claude discovers that directory automatically. Introduce
versioned releases only with a deliberate update policy: `gh skill install`
prefers the latest release over the default branch.

## Validation

Before finishing changes, run `make validate`. When changing repository tooling,
also run `make test`. For a skill change, exercise a representative task and a
nearby task that should not trigger it; structural validation cannot establish
that its instructions produce useful behavior.

## Git

- Use a conventional-commit prefix and lowercase subject, such as `feat:`,
  `chore:`, or `docs:`. Keep the subject on one line. Add a body only when needed.
- Prefer new commits over amending existing commits.
- Prefer `<type>-<slug>` branch names, such as `docs-update-agent-guidance`.
- Push, open, or update a pull request only when explicitly instructed.
  When asked to open one, prefer the `create-pr` skill if available.
