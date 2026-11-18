---
name: weird-shit
description: "Stop, diagnose, and correct an approach the user calls weird. Use when the user says \"stop doing weird shit\" or objects that the current approach is strange, hacky, convoluted, or not what a competent engineer would do."
---

# Weird shit

The user saw you take the least expected path. Treat that as evidence of a wrong turn, not as a taste disagreement. Your goal is to find the **obvious approach**: the one a competent engineer who knows this codebase and stack would reach first.

## 1. Stop

- Make no more edits, commands with side effects, or retries of the current approach.
- Leave existing changes in place until the user approves a revert.

## 2. Reconstruct the path

Write down, for yourself:

- The user's actual goal and constraints, quoted from the conversation where possible.
- Each decision you made, in order, and the evidence behind it.
- The point where you left the obvious approach.

Done when you can name the first decision that a reviewer would question.

## 3. Get independent review

Dispatch reviewer subagents with fresh context. Give them the goal, constraints, and file paths. Keep your justification out of their brief so they do not anchor on it.

- **Solver**: gets the goal and code only. Asks: "What is the conventional way to do this here?"
- **Critic**: also gets your changes or commands. Asks: "What is wrong with this approach, and what should it be instead?"

Use only the critic for a small change. Without a subagent tool, re-read the goal and the relevant code, and answer both questions yourself before you look at your own changes.

Done when you have at least one answer that was not produced from your own reasoning chain.

## 4. Diagnose

Compare the reviews with your path. Name the wrong turn concretely. Common causes:

- A workaround for a symptom instead of a fix for the cause.
- Fighting the framework, or rebuilding something the codebase or a dependency already provides.
- A misread requirement, or an invented constraint.
- Persisting on a failed path instead of stepping back.
- Added abstraction or scope nobody asked for.

Done when the cause explains every weird change, not only the latest one.

## 5. Report and propose

Tell the user, briefly and without excessive apology:

1. What you did, in plain terms.
2. Why it was the wrong approach, and the cause from step 4.
3. What the reviewers found, including any disagreement with your diagnosis.
4. The proposed approach, how to verify it, and its risks.
5. What to do with the existing changes: keep, revert, or partly revert.

Wait for approval before you change anything. When the reviewers and you disagree on the obvious approach, present both and recommend one.
