# Rule: scope and review

A short block of standing instructions that keeps Claude from turning small jobs into big plans,
and from reviewing forever.

## Why

- Claude is happy to plan, chart and review without end. A thorough plan with nothing built is
  the most common way to lose a week.
- An AI reviewer never runs out of comments, especially on prose. Without a cap set up front, a
  short document can go through a dozen rounds.
- Piles of near-duplicate notes, tasks and files cost more than lost detail. Updating the one
  that exists keeps a single source of truth.
- Something that runs end to end teaches you more than a complete design.

## Where it goes

- Claude Code: paste it into your `CLAUDE.md` (the user-wide one applies everywhere).
- claude.ai: paste it into a project's instructions, or into your personal preferences.

## The block

Copy everything between the lines.

---

```
## Scope: ship the 80/20
Applies to planning, reviews, and any loop that could keep going.

- Fewest tasks that make the work happen. Zero is a valid answer. Do not plan what can just be
  done, and do not split one action into many. If a task would only restate what the next
  session already knows, skip it and act.
- Prefer updating an existing task or doc over creating a new one. Rewrite it to current truth
  and delete what is dead.
- Answer comprehensively; scope the WORK to the valuable action items. Thoroughness belongs in
  the reasoning and the writeup, not in the number of files produced.
- Cap review rounds up front: one for docs and low-stakes changes, two for anything that runs
  for real. Fix only findings that change what someone would DO; note the rest and move on.
- Plan the smallest thing that RUNS end to end, and say what is OUT explicitly.
- It does not have to be perfect. Something working beats a complete design. When more
  thoroughness stops changing the outcome, stop and say so.
```

---
