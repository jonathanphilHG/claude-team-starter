---
name: peachy-sweep
description: Find where things actually live across systems before committing to a plan, and confirm which surfaces are reachable from this session. Use when asked what we have on a topic, where something lives, or whether a system is reachable; before writing tickets against systems; and as step 4 of peachy-chart. Records the searches that worked and the wells that came back empty so nobody re-searches them.
---

# Source sweep

Code work does not need this. The repo is right there and `grep` reaches all of it. Non-code
work is the opposite: the answers are scattered across a dozen systems, half need credentials,
one is silently broken this week, and the fastest way to burn a session is to plan against a
surface nobody can actually reach.

Two modes, same discipline:

- **Inside a map**, as `peachy-chart` step 4. Output is `SOURCES.md` in the project root.
- **Standalone**, when the question is just "what do we have on this and where is it." Output
  is a report in the conversation, plus an offer to save it.

---

## The six steps

**1. Name the surfaces before searching any of them.** For the question at hand, list where the
answers could live, and be specific. Not "Drive" but the actual folder. Not "the database" but
"the production database, the `sessions` table." Work from the checklist in
`../peachy-adventure/surfaces.md`; the value is usually in the one surface you would not have
thought of.

**2. Read what is already known about a surface before you sweep it.** Most of these have a
gotcha that is not discoverable from the tool itself: a filter that hides rows, a field that
lies, a permission that needs a human tap, an ID that looks canonical and is not. Those live in
memory, many flagged. Read the entry for a surface **before** you trust its output, not after
you have built on it.

**3. Confirm reachability cheaply, now.** One trivial call per surface. Does the tool answer, is
it the right account, does the query language behave as expected. Five minutes here saves a
session later. Record what answered and what did not, and treat a broken surface as a finding
rather than a problem to fix mid-sweep.

**4. Record every search pattern that worked, verbatim.** The query, and where you ran it. This
is the highest-value line in the output and the one people skip. A later session re-deriving a
working search wastes as much time as re-reading the document.

**5. Record every empty well, with the query verbatim and the surface you actually reached.**
Where a thorough search establishes an absence, write it as a finding: **confirmed absent is a real
answer**, often worth as much as finding the thing. But an empty-well entry tells later sessions not
to look again, so it has to name the surface it actually queried, and **never assert absence from a
surface you did not reach.** A query that cannot match the thing looks identical to a real absence.
See `../peachy-adventure/evidence-tiers.md`, which carries the rules and the incidents behind
them.

**6. Say what is out of reach and who holds it.** Some things can only be obtained by asking a
person. Name the person and the artifact, then stop. Do not draft the outreach unless outreach
was asked for: the relationship is the human's.

Same discipline as step 5 applies to a surface you could not reach at all. "Out of reach" and
"queried and empty" are different findings and plans get written against both, so never let the
first read as the second.

---

## Two habits to enforce

**Re-derive, do not inherit.** Where prior work summarized a source, go back to the source. A
summary is a map of where to look, not a finding. The precedent case for this kit found that an
earlier session's text pipeline had mangled the single most important clause in a contract, and
every conclusion downstream of it was wrong.

**Look at the rendered page when a number matters.** PDFs with an annotation layer routinely
lose content through text extraction. In that same precedent, a document everyone believed was
blank turned out to carry a filled annotation layer that a page render showed plainly, and it
overturned the project's central premise. If a figure is load-bearing, render the page.

---

## Output

Inside a map, write `SOURCES.md` from `../peachy-adventure/templates/SOURCES.md`: the
reachability table, then documents, systems, people, working search patterns, and out of reach.

Standalone, give the same sections in the conversation, lead with the answer rather than the
method, and offer to save it. Do not scaffold a project folder from a sweep.

Either way, **do not start answering the underlying question.** A sweep establishes where the
answers live and whether you can get at them. Pulling the thread is the next session's job, and
a sweep that turns into an investigation stops being reusable.
