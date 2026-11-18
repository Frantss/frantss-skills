# Recon signals

Files that reveal a subject's structure, by ecosystem. Read the ones that exist; skip the rest.

## Workspaces and parts

| Ecosystem | Workspace and manifest files | Typical entry points |
|---|---|---|
| JavaScript / TypeScript | `package.json` (`workspaces`, `bin`, `main`, `exports`, `scripts`), `pnpm-workspace.yaml`, `turbo.json`, `nx.json`, `lerna.json`, `tsconfig.json` (`paths`, `references`) | `src/index.*`, `src/main.*`, `app/`, `pages/`, `server.*`, `bin/` |
| Python | `pyproject.toml` (`[project.scripts]`, workspace tools), `setup.cfg`, `requirements*.txt`, `uv.lock`, `poetry.lock` | `__main__.py`, `manage.py`, `app.py`, `main.py`, `wsgi.py`/`asgi.py` |
| Go | `go.mod`, `go.work` | `cmd/*/main.go`, `main.go` |
| Rust | `Cargo.toml` (`[workspace]`, `[[bin]]`) | `src/main.rs`, `src/bin/`, `src/lib.rs` |
| JVM | `settings.gradle*`, `build.gradle*`, `pom.xml` (`<modules>`) | `*Application.*`, `main` methods |
| .NET | `*.sln`, `*.csproj` (`ProjectReference`) | `Program.cs` |
| Ruby | `Gemfile`, `*.gemspec` | `config/routes.rb`, `bin/`, `exe/` |
| PHP | `composer.json` | `public/index.php`, `routes/` |

## Runtime and deployment

`Dockerfile`, `docker-compose*.yml`, `Procfile`, `vercel.json`, `wrangler.*`, `fly.toml`, `railway.*`, `serverless.yml`, Terraform, Helm charts, Kubernetes manifests. A part with its own deploy config is a deployable unit.

## Commands

Take commands from `scripts` blocks, `Makefile`, `justfile`, `Taskfile.yml`, and CI workflows (`.github/workflows/`, `.gitlab-ci.yml`). CI shows the commands that actually run; prefer it when it disagrees with the README.

## Intent docs

`README*`, `CONTRIBUTING*`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `GLOSSARY*`, `docs/`, `docs/adr/`, `docs/decisions/`, PRDs, and specs. They state decided trade-offs and vocabulary. Use their terms in the report.

## Git signal

```bash
git rev-parse --short HEAD
git log --oneline -20
git log --since="6 months ago" --oneline -- <part> | wc -l
git log -1 --format=%cs -- <part>
```

Report activity as these two numbers, not as a label. Name people only when the user asks.
