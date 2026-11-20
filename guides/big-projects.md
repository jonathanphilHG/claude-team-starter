# When one chat is not enough

Some work outgrows a single conversation: a research question with many sources, a decision
with several moving parts, a rollout across many sites. The chat fills up, the early detail gets
lost, and the next session starts from zero.

The `peachy/` folder in this kit holds a method for that, called Peachy Adventure, plus five
Claude Code skills that run it. Start with `peachy/README.md`.

## The idea in four lines

- **A map.** One folder per project, with a `MAP.md` that says where you are going, what
  decision it serves, and what is still unknown.
- **Tickets.** Each unknown becomes a small ticket that one session can finish.
- **One findings file per session.** A session writes only its own file, so several can run at
  once without stepping on each other.
- **A gate that merges.** When a round is done, one session reads every findings file, settles
  contradictions out loud, updates the map, and decides whether another round is worth it.

One more rule does most of the work: **nothing blocks forever.** If a session cannot settle
something, it records a bounded stand-in (a range, an assumption with what would reverse it, a
gap with an owner) and the work moves on.

## When to use it

Reach for it when the work is more than one session, the answers live in more than one place,
and the next step is not obvious.

Do not reach for it for one chat's work, a single question, a recurring checklist, or anything
that is really waiting on one person's reply.

## What it needs

Claude Code, because the method lives in files and folders. The skills are installed by linking
or copying the folders in `peachy/skills/` into your skills folder; `peachy/README.md` has the
steps.
