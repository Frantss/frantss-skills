---
name: refactoring
description: "Use when writing, editing, or reading code."
---

# Refactoring

Apply these rules whenever writing, editing, or reading code.

1. **YAGNI**: Do not build it until it is needed.
2. **DIE**: Extract patterns after the second duplication.
3. **KISS**: Build the obvious solution first. Optimize when needed.
4. **SOLID**: Check your solutions against the 5 SOLID principles.
   4.1. **S**ingle responsibility
   4.2. **O**pen/closed
   4.3. **L**iskov substitution
   4.4. **I**nterface segregation
   4.5. **D**ependency inversion
5. **Delete aggressively**: The less code, the better. Aim for simplicity.
6. **The Boy Scout Rule**: Refactor as needed, if out of scope report the opportunity.
7. **Semantic naming**: Use self documenting names. Avoid brevity. Avoid ambiguity.
8. When rules collide the simplest approach prevails until the complexity can be justified.

When reading code, use the rules to explain or assess it. Report relevant
refactoring opportunities without treating a reading request as permission to edit.

When changing code, preserve required behavior and keep refactors within the
requested scope. Before finishing, verify behavior with checks appropriate to
the change and explain any complexity that the current requirements justify.
