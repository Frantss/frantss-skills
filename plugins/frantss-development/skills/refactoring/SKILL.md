---
name: refactoring
description: "Refactor existing code to address a concrete maintenance problem while preserving behavior, or assess requested refactoring opportunities. Ordinary code reading, feature work, and bug fixes alone do not trigger this workflow."
---

# Refactoring

Improve the requested part of the code without changing its observable behavior.
For an assessment or proposal, inspect the code and deliver findings with
verification suggestions. A review request does not authorize edits.

## Principles

- **YAGNI and KISS**: Prefer the smallest change that solves the maintenance problem.
  Justify complexity through current requirements or project constraints.
- **DIE**: Extract duplication when a shared implementation simplifies maintenance.
  Similar text alone does not establish a shared responsibility.
- **SOLID**: Check responsibilities, extension points, substitutability, interfaces,
  and dependency direction. Add abstractions only when they improve this design.
- Use descriptive, unambiguous names. Delete code only after verifying that it is
  unused or unnecessary for required behavior, including callers outside the module.
- Keep cleanup within scope. Report unrelated opportunities separately.

## Workflow

1. **Define the improvement.** Inspect the relevant documentation, code, callers,
   and tests. Name the concrete maintenance problem and the affected boundary.
   Resolve ambiguity that could change the intended outcome before editing.
2. **Establish the baseline.** Identify behavior to preserve: public contracts,
   outputs, errors, state changes, side effects, and ordering as applicable.
   Run the relevant existing checks and record pre-existing failures.
   Add characterization checks only where an uncovered risk needs evidence.
3. **Choose a small change.** Connect the proposed restructuring to the problem.
   Consider a local simplification before introducing a shared abstraction.
   Explain material trade-offs when several approaches remain viable.
   Keep requested behavior changes explicit and separate from structural work.
4. **Refactor incrementally.** Keep each step reviewable and checkable.
   Separate mechanical moves or renames from logic changes where practical.
   Check callers before changing interfaces or removing code. Preserve meaningful
   behavior assertions; adapt tests coupled to internals only when needed.
5. **Verify preservation.** Run focused checks after risky steps and the relevant
   broader checks at completion. Compare results with the baseline, including
   boundary and failure cases affected by the change. Investigate new failures
   before continuing; use an equivalent check if the original is unavailable.
6. **Close the scope.** Review the diff against the maintenance problem and
   preserved contracts. Finish when the targeted improvement is present and
   relevant checks support behavior preservation. Report the improvement,
   checks run, pre-existing failures, and remaining verification limits.
