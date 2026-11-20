# Peachy Adventure

A method, plus five Claude Code skills, for a project that has outgrown a single chat: research,
a product plan, an operational change, a legal or financial question, anything where the work is
not code. It charts the project as a map of tickets in a plain folder, then works them one session
at a time until the deliverable is defensible.

This is the shared copy of a personal kit. It was used daily by its author; it is not a product.
Expect rough edges, and let the kit record when something gets in the way (see Feedback below).

This method was written by one person for their own use, so the text says "he" for the person
running the project. Read it as "you".

## When to reach for it

The trigger: **more than one session's work, more than one place the answers live, and enough fog
that the next step is not obvious.**

Do not reach for it when it is one chat's work, a single question with a single answer, a
recurring task that wants a checklist, or anything whose real blocker is one person answering one
email.

## The five skills

| Skill | Session type | What it does |
|---|---|---|
| `peachy-chart` | Charting | Names the destination and the decision it serves, picks the project shape, sweeps the sources, scaffolds the folder, writes the tickets it can state now. Resolves nothing. |
| `peachy-sweep` | Either | Finds where things actually live across your tools and confirms what is reachable from this session. Also step 4 of charting, and useful on its own. |
| `peachy-work` | Working | Exactly one establishing ticket: research, grill, prototype, or task. Writes only files it owns. |
| `peachy-build` | Executing | Batches execute tickets. Gates every write to a live system behind a dry run and your approval, verifies after, may spawn sub-tickets. |
| `peachy-gate` | Closing a round | The only session that merges findings files, writes the canonical outputs, and touches the map. Then refuses to grow it. |

Shared material lives in [`skills/peachy-adventure/`](skills/peachy-adventure/):
[`METHOD.md`](skills/peachy-adventure/METHOD.md) (the spine: shapes, rule packs, invariants, ticket
types, the asking rule, gating, where projects live),
[`evidence-tiers.md`](skills/peachy-adventure/evidence-tiers.md),
[`surfaces.md`](skills/peachy-adventure/surfaces.md),
[`models.md`](skills/peachy-adventure/models.md) (which model and effort a ticket runs at, written
as roles so it survives the lineup changing), and `templates/`.

## The three ideas worth knowing

**Nothing blocks forever.** When a session cannot resolve its item, the item converts to a declared,
bounded, visible form and the work proceeds: a parameter with a range, an assumption plus a reversal
trigger, a marked gap with an owner. This is the most important rule in the kit and it is what kills
the research rabbit hole.

**A filter, not a quota, governs asking.** No cap on questions. One test: would the answer change
what you actually do, or what the deliverable says at the headline level? Yes means ask now, even
mid-ticket. No means decide it, note the pick under `Decided below the bar`, and move.

**A session writes only files it exclusively owns.** Canonical outputs do not exist until a gate
merges them. No locking, no lost update, so several sessions can run at once with no tracker.

## Install

The skills reach Claude Code through symlinks in `~/.claude/skills`, so an edit in this folder is
live in the next session with nothing else to run.

Keep this folder wherever you like (for example `~/code/peachy`), then from inside it:

```bash
./wire.sh                    # idempotent; creates or repairs the symlinks
```

Or, inside Claude Code with this folder open, paste:

> Run `./wire.sh` in this folder, then start a fresh session and confirm the five `peachy-*`
> skills are listed.

Verify: in a new Claude Code session, type `/peachy-` and the five skills should appear.

If your skills folder is somewhere else, point the script at it: `KIT=/path/to/skills ./wire.sh`.
`wire.sh` is a bash script. On Windows, where links are awkward, copying the six `skills/`
folders into `%USERPROFILE%\.claude\skills` works too; copy again after you change them.

The multi-session messaging parts (the relay, `SESSIONS.md`, socket addresses, `SendMessage`) rely
on Claude Code features that let sessions message each other, which may not be in every install.
The method works without them: a person relays between sessions instead.

## First map

1. Make a folder for the project (default `~/Peachy/<Project Name>/`), open Claude Code there.
2. Say what you are trying to get to, and that you want it charted as a Peachy map. The
   `peachy-chart` skill asks what decision the work serves, sweeps where the answers live, and
   writes the first tickets. It builds nothing and answers nothing; that is on purpose.
3. Work one ticket per session with `peachy-work`. When a round of tickets is done, `peachy-gate`
   merges what they found and plans the next round.

Keep the maps out of this repo. The kit lives here; your projects live in their own folders.

## Updating

This copy is a dated snapshot (2026-11-20). Nothing pulls updates into it. Change it as your own.

## Feedback

When the method gets in the way (a gate that fired when it should not have, a rule that cost you
time, a step that was useless), the skills append one line to [`FEEDBACK.md`](FEEDBACK.md). That
file is how the kit gets revised. Method friction only, never project content.

House style for every file in here: no long dashes. Use a comma, a colon, or parentheses.
