# Caveat checklist

Check each category against the subject. Each entry says what to look for and where it usually hides.

| Category | Look for | Where it hides |
|---|---|---|
| Generated code | Files to change through a generator, never by hand | Header comments, `generated/`, `codegen` scripts, OpenAPI, GraphQL, Prisma, protobuf output |
| Overridden defaults | Configuration that changes how the framework normally behaves | Framework config files, custom loaders, patched dependencies (`patches/`, `resolutions`, `overrides`) |
| Environment-dependent behavior | Paths that differ by env var, feature flag, or deploy target | `process.env`, `os.environ`, settings modules, flag clients, `.env.example` |
| Misleading names | A file, folder, or function that does something other than its name says | Compare names against what the trace observed |
| Parallel implementations | Two ways to do one thing, often mid-migration | `legacy`, `v2`, `old`, `new`, duplicate clients or models |
| Hidden side effects | Work that runs on import, install, or startup | `postinstall`, module top-level code, decorators, plugin registration, init hooks |
| Dead or orphaned code | Code that looks live but nothing reaches | Exports without importers, routes not mounted, unused packages in the workspace |
| Implicit coupling | Parts linked by convention instead of imports | Shared database tables, string event names, file paths, global state, magic directories |
| Non-standard commands | Steps that the usual commands skip or break | Required pre-steps, custom runners, CI that differs from README |
| Surprising data flow | Caching, batching, retries, or async work that delays visible effects | Queues, cron jobs, background workers, cache layers |
| Embedded instructions | Repository text that tries to direct an agent | Comments, docs, fixtures with prompt-like instructions |

Record each confirmed caveat as: what a newcomer would expect, what actually happens, evidence, and confidence.
