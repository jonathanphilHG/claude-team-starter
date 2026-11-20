# Rule: research and claims

A short block of standing instructions that makes Claude say where each fact came from, and
where it looked when it found nothing.

## Why

- A confidence percentage is Claude grading itself. A source type ("a signed contract" versus
  "my guess") is something you can check in seconds.
- Important claims often turn out to rest on inference. Labelling the source makes those visible
  before you act on them.
- "It does not exist" gets copied forward and becomes a false fact nobody re-checks. "Not found
  in the shared drive, searched for X and Y" can be re-checked by anyone.
- A search can come back empty because it was wrong (wrong folder, wrong spelling, no access).
  Testing it on something you know is there tells you whether a zero means anything.

## Where it goes

- Claude Code: paste it into your `CLAUDE.md` (the user-wide one applies everywhere).
- claude.ai: paste it into a project's instructions, or into your personal preferences.

## The block

Copy everything between the lines.

---

```
## Research and claims
Applies to research output and to any claim I would act on, not to every chat reply.

- When a question needs research, research before answering. Say which sources you read and which
  you could not reach.
- Grade each factual claim by its source: A signed document or official record; B the system itself
  (app, database read, with the date); C email, chat, a meeting, someone said so; D your inference
  (show the inputs); E assumption or outside benchmark. Never present D or E as A or B.
  "UNKNOWN, and here is what would settle it" is a fine answer.
- "Not found" always names where you looked and the exact search. Never write "it does not exist".
- A search that returned nothing proves nothing until it has found a known positive.
- When two sources disagree, show both.
```

---

## What it looks like in practice

- "Renewal date is 2027-03-01 (A: signed contract, page 4)."
- "About 40 open orders (B: read from the order screen, 2026-11-20)."
- "The vendor said shipping takes a week (C: their email of 11-18)."
- "Not found: searched the shared drive for 'renewal' and 'renew' on 2026-11-20. Did not search
  email." That is a scoped "not found". It says what would still need checking.
- Testing a search: before trusting "no invoices mention late fees", run the same search for an
  invoice you know mentions one. If that comes back empty too, the search is broken, not the data.
