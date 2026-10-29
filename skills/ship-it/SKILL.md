---
name: ship-it
description: "Use only when the user issues `ship it` as a command. Plan and execute project-specific testing, atomic commits, integration, and release or PR creation after approval."
disable-model-invocation: true
---

# Ship it

Discover the project's delivery conventions, propose a concrete plan, and execute it once approved. Completion means reaching the approved endpoint with verification evidence.

## Discover the workflow

1. Inspect the repository without changing it. Read applicable agent instructions, Git status, staged and unstaged diffs, untracked contents, branch history, remotes, and existing PR or release state. Include all current changes and undelivered branch commits by default; honor a narrower user scope. Keep ignored files excluded unless requested. Account for every included change before proposing commits.
2. Read contribution, testing, review, release, and deployment guidance. Look for `README.md`, `CONTRIBUTING.md`, `TESTING.md`, `REVIEW.md`, `REVIEWING.md`, `RELEASE.md`, `RELEASING.md`, and `DEPLOYMENT.md`, including relevant files under `.github/` and `docs/`. Match names without case sensitivity and follow relevant documentation links; these names are discovery hints, not required files.
3. Inspect PR templates, CI workflows, package manifests and scripts, lockfiles, release tooling, and deployment configuration. Check remote repository rules and connected service settings when available. Identify required checks, branch and commit conventions, integration method, release mechanism, targets, and automatic effects of pushes or tags. Use recent history to fill gaps, distinguishing observed practice from explicit requirements.
4. Resolve the delivery endpoint from project identity, instructions, and configuration. In the user's personal projects, the usual path is committing all changes, rebasing onto the latest `main`, merging into `main`, pushing it, and publishing an npm version or deploying to Railway. In Guildara, the usual endpoint is committed changes and an open PR, including the necessary branch push. Treat these as defaults for identified projects; adapt to repository conventions and explicit user instructions. Resolve consequential conflicts or missing targets before approval.
5. Verify current remote branch tips and compare them with local history through read-only remote queries or APIs; cached tracking refs alone are insufficient. Determine the exact integration actions before presenting the plan. Record the compared revisions. When required state cannot be verified, report the blocker rather than substituting a conditional step.

## Propose the plan

Present the approval plan as a numbered list. Give each step one short sentence, normally at most 20 words, with one concrete action. Reserve nested bullets for the proposed commits; keep other steps flat and without per-step explanations. Show test commands and approval-relevant scope, versions, destinations, and history changes; keep investigation details and rationale available on request. Keep scope context and approval notes to one short line each; add only material blockers or decisions after the list.

State the exact actions supported by the inspected state. Resolve decisions during discovery instead of writing placeholders such as "rebase if needed" or "publish or deploy". Omit unnecessary actions, including rebasing or merging when the branch state does not require them.

Use the available workflow for atomic commit planning: discover and read its instructions, then split pending changes into commits by purpose. Use one numbered step for creating commits, with a nested bullet list in commit order. Give each commit its exact subject and brief scope. Use this format even for a single commit, which is appropriate when all included changes serve one purpose.

Before writing that compact plan, establish the following details internally. Summarize the resulting actions; do not reproduce this checklist in the response:

- **Scope and commits:** Included changes, ordered atomic commit subjects and purposes, source branch, and target branch. Retain this workflow's approval boundary for commit planning and execution.
- **Testing:** Exact commands or manual checks, why they cover the changes, when they run, and their success criteria. Include required repository checks and relevant lint, types, unit, integration, end-to-end, and build checks. Explain exclusions and unavailable prerequisites.
- **Integration:** Fetch, rebase, merge, and push actions in the order required by project conventions. Identify any branch creation or shared-history rewrite; force-pushing the target branch is outside the routine workflow.
- **Delivery:** PR destination, or exact package version, registry, and dist-tag, or deployment service and environment. Explain version selection. Include version files, lockfiles, changelogs, tags, release commits, and generated artifacts when the release mechanism requires them. Account for hooks and CI automation so publication or deployment happens once.
- **Completion:** Required local and CI results, package-content checks and published-version verification for npm, or deployment status and relevant health or smoke checks for Railway. State which checks require the external action first.

Keep the sequence proportional to the project. Use existing release tooling rather than replacing it with manual commands. If pushing triggers deployment, place all required pre-deployment checks before that push. Surface unresolved choices and risks that could change the plan.

When documentation is missing, suggest the appropriate file and topics to add. When documentation conflicts with observed configuration or behavior, identify the mismatch and suggest a correction without assuming which source is wrong. Keep each optional documentation suggestion to one brief line, separate from required shipping steps; provide supporting evidence on request. Missing documentation alone does not block shipping; unresolved testing or delivery decisions can. Edit documentation only when its changes are explicitly included in the approved scope.

## Obtain approval

Wait for approval of the concrete plan before running tests, preparing files, fetching, staging, committing, rewriting history, pushing, opening a PR, publishing, or deploying. A draft, plan, or dry-run request completes with the proposal; no execution approval question is needed. When an execution request requires approval, keep its explanation to the minimum relevant excerpt.

Approval covers the displayed sequence and routine in-scope fixes needed to complete it, subject to applicable repository rules. Execute that sequence without asking again for each listed action. If scope, history impact, required checks, destination, version, or release mechanism materially changes, present the revised steps and obtain renewed approval before the affected actions.

## Execute and verify

1. Recheck repository and remote state against the approved scope and recorded revisions. Preserve concurrent edits and excluded work. If changed state requires different integration actions, present the revised plan for approval before those actions. Run the approved checks and inspect hook or generated-file changes before including them in commits. Create atomic commits in the approved order, following repository commit conventions.
2. Perform the approved integration. Resolve conflicts within the agreed behavior; seek a decision for consequential ambiguity. Verify the final integrated code before publication or deployment. Rerun affected checks after conflict resolution, fixes, or release preparation changes. Associate passing results with the code that will ship; earlier results cover only unchanged code and inputs.
3. Treat failed or unavailable required checks as blockers to downstream integration or delivery. Report the evidence, fix in-scope failures, and rerun affected checks. Any proposed exception must identify the failed or missing check and receive explicit approval, where repository rules permit it. Preserve completed work and report the stopping point when blocked.
4. Deliver through the approved mechanism. For a PR endpoint, open or update the current branch's PR using project conventions and the template, include actual test evidence, and report CI status; merging or releasing it requires additional scope. For a release endpoint, verify the remote branch, published package/version, or active deployment corresponds to the intended code. A successful push or accepted deployment request alone does not prove release completion.
5. On failure or resume, inspect local and external state before retrying. Continue from the first incomplete action, preserving completed commits, PRs, versions, and deployments. If publication or deployment has an unknown outcome, verify it before retrying. Stop and report the remaining uncertainty when verification is unavailable; rollback or a different release needs its own approved plan.

Report completed steps, commit hashes, checks and results, relevant PR/release/deployment links, remaining changes, and blockers. Distinguish a PR awaiting CI, a requested deployment, and a verified release. Include outstanding documentation suggestions without silently making them release requirements.
