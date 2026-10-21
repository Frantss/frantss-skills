# Repository guidance

Before your first reply, read [frantss-communicate](skills/frantss-communicate/SKILL.md).
Apply it to every message to the user throughout the session, on every topic.
If its instructions leave the context, read it again before your next message.

This repository distributes personal skills through standard skill installers
and Codex and Claude Code plugins. Install and authoring commands are in `README.md`;
the writing and packaging conventions are in `CONTRIBUTING.md`.

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

Before finishing changes, run `make validate`. When changing repository tooling,
also run `make test`. For a skill change, exercise a representative task and a
nearby task that should not trigger it; structural validation cannot establish
that its instructions produce useful behavior.
