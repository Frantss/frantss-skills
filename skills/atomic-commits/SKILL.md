---
name: atomic-commits
description: "Atomic commits for `commit-a` or requests to split pending changes into commits, including planning-only requests. Implementation and history rewrites are outside this skill."
---

# Atomic commits

Give each commit one narrowly scoped, reviewable step, including its implementation, tests, documentation, and required generated artifacts. A feature can need several ordered commits. Judge cohesion, without line or file quotas.

## Establish scope

1. Read repository instructions and commit conventions. Inspect status, staged and unstaged diffs, untracked contents, and recent subjects. Record HEAD and index state.
2. Default to all staged, unstaged, and untracked changes. Honor specified paths, hunks, or outcomes; outcome-based scope includes only relevant hunks within a file. Exclude ignored files unless requested. Clarify ambiguous scope; report empty scope without commits.
3. Inspect every selected change and dependency, including renames, deletions, binaries, and generated files. Assign each change to a commit or explicit blocker. Ask before expanding scope when selected changes depend on excluded work.

## Group by purpose

4. Decompose selected work into reviewable steps within each feature. Separate prerequisite configuration or mechanical refactors from product behavior when the intermediate trees remain valid. Split distinct behaviors, including hunks within one file. Dependencies determine commit order; a shared feature, directory, file, or manifest does not establish atomicity.
5. Challenge each proposed group: can an earlier part form a valid, useful change, with the rest added in later commits? If so, split it. Keep inseparable changes together across files, such as an API change and required caller updates or a fix and its regression test. Include matching manifest and lockfile hunks in each step. Retain a broad group only with a concrete coupling reason.
6. Present ordered subjects, purposes, paths or hunks, dependencies, and validation; explain retained broad groups. Planning requests stop here without staging or committing. For execution requests, proceed under existing authorization; clarify unresolved scope or correctness decisions.

## Create and verify

7. Stage one group using explicit paths or selective hunks. Preserve working contents and excluded staging; use an isolated index when needed, then reconcile the real index against the new HEAD without staging excluded edits. Never blindly clear staging or use blanket staging for partial scope.
8. Inspect the complete staged diff against the plan. Check the exact proposed tree in isolation when remaining edits could mask failures. Record unavailable checks and pre-existing failures; new failures block the group.
9. Follow repository commit conventions; otherwise use a conventional-commit prefix and concise lowercase subject. Verify each resulting hash and diff. After hook edits or failures, inspect HEAD, index, and working tree before retrying; reclassify hook edits. Preserve completed commits and report blockers; never bypass hooks automatically.
10. Recheck remaining changes before each group; preserve concurrent edits and revise affected groups. History rewrites, pushes, and pull requests need separate authorization.

Compare commits and remaining diffs with the initial inventory. Report hashes, subjects, checks, limits, and blockers.
Completion requires every selected change committed once, with excluded content and staging preserved.
