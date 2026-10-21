# Stop-slop review

Keep `communicate` small. Before this change, it had 45 lines and already covered direct answers,
plain words, active voice, clear actors, filler, vague claims, forced contrasts,
rhetorical questions, dramatic fragments, and decorative dashes.
Source: [communicate](/Users/frantssbongiovanni/development/frantss-skills/skills/communicate/SKILL.md:14).

## Useful additions

Three changes would add useful detail without importing the reference files:

- Cut empty intensifiers such as “really” and “genuinely”. Preserve words that
  carry meaning, such as “only”, “usually”, and “approximately”. `stop-slop`
  identifies filler but bans all adverbs, which is too broad for technical work.
  Source: [adverbs](/Users/frantssbongiovanni/.codex/skills/stop-slop/references/phrases.md:53).
- Use absolute claims only when the evidence supports them. This makes the
  existing accuracy rule more concrete.
  Sources: [extremes](/Users/frantssbongiovanni/.codex/skills/stop-slop/references/structures.md:129),
  [accuracy](/Users/frantssbongiovanni/development/frantss-skills/skills/communicate/SKILL.md:37).
- Remove announcements of the point and repeated conclusions. Preserve useful
  progress updates and explanations of the next action.
  Sources: [meta-commentary](/Users/frantssbongiovanni/.codex/skills/stop-slop/references/phrases.md:85),
  [current opening rule](/Users/frantssbongiovanni/development/frantss-skills/skills/communicate/SKILL.md:14).

## Compact wording to consider

Replace the existing filler and vague-claims bullets with:

> - Remove stock praise, filler, empty intensifiers, and repeated conclusions.
> - State the point directly. Skip announcements such as “Here's what matters”.
> - Replace vague claims and inflated words with specific facts. Use absolutes only when supported.

Add one sentence to the closing check:

> Cut repetition; keep qualifications that change the meaning.

Applied these refinements to `communicate`, preserving its rules about promotional
claims and idioms. It now has 47 lines. The accuracy and preservation rules remain.

## Leave out

- **Absolute grammar bans.** “Restart only the failed worker”, “the key was
  deleted”, and “the server rejects the request” all convey useful meaning.
  Banning adverbs, passive voice, or nonhuman subjects can force inaccurate actors.
  Source: [core rules](/Users/frantssbongiovanni/.codex/skills/stop-slop/SKILL.md:15).
- **Mechanical rhythm rules.** Two items are not inherently better than three.
  Direct questions and conditions often need “what”, “when”, or “how”.
  Source: [sentence and rhythm rules](/Users/frantssbongiovanni/.codex/skills/stop-slop/references/structures.md:108).
- **Removing uncertainty or explanation.** One example changes “most teams” to
  “teams” and “nobody wants to admit” to “nobody admits”. This changes the claim.
  Another replaces handling uncertainty with “Move faster”, a new message.
  Sources: [example 2](/Users/frantssbongiovanni/.codex/skills/stop-slop/references/examples.md:15),
  [example 3](/Users/frantssbongiovanni/.codex/skills/stop-slop/references/examples.md:27).
- **Scoring and long phrase lists.** The five scores and 35/50 threshold add
  review work without a defined measurement method. The current silent check
  fits an automatic communication skill.
  Sources: [scoring](/Users/frantssbongiovanni/.codex/skills/stop-slop/SKILL.md:48),
  [silent check](/Users/frantssbongiovanni/development/frantss-skills/skills/communicate/SKILL.md:44).

If source wording is adapted, preserve its MIT license and attribution as
required by [CONTRIBUTING.md](/Users/frantssbongiovanni/development/frantss-skills/CONTRIBUTING.md:50).
