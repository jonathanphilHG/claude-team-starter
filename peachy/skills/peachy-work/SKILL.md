---
name: peachy-work
description: Work exactly one ticket on a Peachy Adventure map, the kind that establishes something (research, grill, prototype, or task). Use when pointed at a ticket in a project folder that has a MAP.md, or when asked to take the next thing off a Peachy map. For execute tickets, which batch and write to live systems, use peachy-build instead.
---

# Work one ticket

One ticket, one session. The ticket establishes something: a fact, a judgment, a concrete
artifact to react to, or a piece of unblocking work. Execution tickets are a different job with
opposite rules, and they belong to `peachy-build`.

Read `../peachy-adventure/METHOD.md` for the ticket types, the asking rule and the stop
conditions. If the map's shape has evidence tiers on, read `../peachy-adventure/evidence-tiers.md`
too.

---

## If you are the orchestrator, you are not the one who works this ticket

**Launch it, do not run it.** The rule and its reasoning live in `peachy-gate` under "the
orchestrator never executes", and this pointer is here because an orchestrator invoking this skill
has no reason to open that heading. One did, on a re-entry grill ticket, and went from scanning
surfaces to changing a live record in a production system as a test.

The shape recurs rather than being exotic: a re-entry ticket on a parked map is almost always a
grill, a grill is HITL, so the orchestrator is exactly the session holding the human's attention
when one comes up. The test is unchanged: **if the work would produce a findings file were someone
else doing it, it is a ticket.** If the round is only one ticket's worth of work, run the ticket and
have no orchestrator at all.

## The procedure

**1. Orient, narrowly.** Read `MAP.md`, `PROCESS.md`, `HOTLINE.md`, `MISSION.md`, then the ticket.
Nothing else. The map is low resolution on purpose; zoom into another ticket only when you need it.
Note the map's shape and its rule pack, because they decide how you record what you find.

**`MISSION.md` is on that list for one section in particular: Known errors in prior work.** It lists
what is known or suspected to be wrong in the documents, systems and summaries feeding this project,
and it exists precisely so those claims get challenged rather than inherited. A session that skips
it inherits the errors the section was written to kill. It also holds what this project is NOT,
which is where scope creeps in.

**Then confirm the artifacts your ticket names still exist**: the tab, the file, the sheet, the
record, the folder. Work orders are written at a gate and the artifacts move afterwards. If one is
gone, **check `git log` for it before rebuilding it**, and Hotline what you found so the next
session does not repeat the search. Two sessions once lost time to a spreadsheet tab a later round
had deleted, and only one of them thought to look in git.

**2. Check the `Run at:` line against the model you actually are, then claim and register.**

The check comes before the claim line, because after it the session is committed and the record says
a ticket ran that did not run as scoped. The ticket names a tier; `../peachy-adventure/models.md`
says which model that tier is today, and your system prompt names the model you are running on. **If
they differ, stop: write nothing, claim nothing, register nothing, and tell
the human to relaunch the ticket at the stated setting.** A session cannot change its own model, so
this is the only guard there is. A newer release of the same family counts as a match: run, and note
in the findings file that the lineup table is behind.

Check the model, not the effort. The model is always visible; the effort usually is not, and a rule
a session cannot evaluate is the defect ADR-0007 removed time gates for. Both get recorded at close
in the findings file's session line, which is where a mismatch used to be caught, one whole ticket
too late.

Three launches went out on the wrong tier before this moved to claim time: two execute tickets
halted mid-flight, a second map the same day that lost a round to it twice, and one the next day
that nobody halted and that ran to close a tier down. See ADR-0012.

Then claim it: append `Claimed: <date> <time>` to the ticket file and save, with the time read from
`date` rather than estimated. There is no tracker
assignee here, so that line is the entire concurrency guard. An open ticket with no claim line is
takeable by anyone.

Then register in `SESSIONS.md`, append only, so the orchestrator can reach you and so it knows which
live sessions on the machine are this map's:

```bash
printf '%s\n' "- [T04 . $(date '+%Y-%m-%d %H:%M')] uds:/tmp/cc-socks/71346.sock . claimed" >> SESSIONS.md
```

`SESSIONS.md` carries the snippet that derives your own socket path. You need it, because no tool
reports your own address: `ListAgents` does not list self.

If you were told only "work the map" rather than given a ticket, take the first frontier ticket
in order. Say which one you took before you start, because a parallel session may be about to
take the same one.

**3. Work it.** Front-load the reading before your first question if the ticket is HITL, so the
human is not waiting on you between turns.

Where the shape has tiers on, every claim you write carries a tier and a citation specific
enough to re-find. `UNKNOWN` is an acceptable answer. A confident wrong number is not.

**4. Escalate a material fork immediately.** This is the one rule that most needs following.

> Would the branches change what the human actually does, or what the deliverable says at the
> headline level?
>
> **Yes:** stop and ask, now, mid-ticket. Do not pick for them and do not park it for the gate.
>
> **No:** decide it, write the pick and a one-line reason in your findings file, and move.

The failure this prevents is real: in the precedent project a ticket hit a fork it could not
settle from documents, closed with a note saying so, and a later ticket settled it with one
lookup and **inverted the project's headline answer**. A round was lost to parking it.

Never ask what the sources can answer. Every question carries your recommended answer so "yes"
is a complete reply. Never ask permission to continue.

**5. Hotline anything another live session needs now.** Append only, one line, `printf` and never
Write or Edit:

```bash
printf '%s\n' "- [T04 . $(date '+%Y-%m-%d %H:%M')] <what you found> <which ticket needs it>" >> HOTLINE.md
```

Read it when you start and again before you close. A reply to another ticket's entry is often the
most valuable line in the file: two sessions each holding half of an answer is exactly what it is
for. Two or three entries per round is healthy; twenty means the ticket boundaries were drawn
wrong, and that is itself worth flagging.

**If what you found invalidates another ticket's premise, relay it too**, immediately: write the
Hotline line first, then `SendMessage` the orchestrating session pointing at it, using the socket on
the `ORCHESTRATOR` line in `SESSIONS.md` as your `to`. The Hotline only reaches sessions that read
it after you write it. Do not reach for `ListAgents`: it cannot tell you which of its entries are
this map's. See the relay section in `PROCESS.md`.

**6. Stop on materiality, not a clock.** Is this answered to the resolution the deliverable
actually needs? Would more precision change what the human does? If not, you are done.

**There is no time gate on this ticket or any other.** You cannot measure your own elapsed time,
so do not act on a sense of how long you have been working, and do not impose a budget on
yourself. Record what actually bounded you in the findings file's `Bounded by` field.

Whatever you could not resolve **converts to the bounded form the shape calls for** and the work
proceeds. A parameter with a range. A stated assumption plus a reversal trigger. A marked gap
with an owner. Never leave a ticket open waiting for a document.

**7. Re-read what the gate owns, then write your findings file.**

**Before you write it, re-read `MAP.md`, `MISSION.md` and any canonical output file your ticket
touches.** Your beliefs about those files were formed when you started, and a gate may have amended
one since; nothing refreshes them on their own. This is the mirror of the artifact check in step 1.
That one stops you working from a stale premise, this one stops you writing one into the record, and
the record is the half that outlives you. On one map a worker reported an item as still needing
confirmation across three separate closes after the gate had already confirmed and committed it, and
relayed a premise flag about a decision the gate had ratified a minute earlier. It matters more on a
Drive-hosted map, where sync lag widens the window.

Then write the findings file at `findings/T<NN>.md` from
`../peachy-adventure/templates/findings.md`. Every heading present even when empty; write "None."
rather than deleting one. The gate parses them.

**8. Close the ticket.** Append `## Resolution` with three to six lines and `Status: closed`, then
commit with files staged by name:

```bash
git add findings/T04.md tickets/T04-*.md
git commit -m "T04: <what it established>"
```

Then append your `. closed` line to `SESSIONS.md` and **relay the result**: `SendMessage` the
orchestrating session two lines, what you established and what it changes for another ticket, sent
to the socket on the `ORCHESTRATOR` line. If no orchestrator is reachable, or the map was charted
before `SESSIONS.md` existed and has no line to read, the close is still complete. Never hold a
close open waiting to deliver a message.

**If a closed ticket starts working again, it is open.** Set `Status: open, reopened <date>, <why>`
on the ticket *before* you touch anything, put the new work under `## Addendum <date>` in the same
findings file, and re-close by updating the Resolution rather than replacing it. `Status` is what
tells another session whether a ticket is takeable, so a closed ticket with live work in it is a
concurrency bug, not only an untidy record. The test: **if a unit row or a deliverable says in
flight, the ticket cannot say closed.** No fresh `Claimed:` line is needed when it is the same
session continuing.

---

## What you must not touch

**Do not write `MAP.md`, and do not write any canonical output file.** Not `facts.md`, not
`contradictions.md`, none of them. Those belong to the gate.

**Do not edit `MISSION.md` either.** It is amendable now, but only at a gate and only with the
human's ratification, so a correction you find mid-ticket goes to the Hotline or your findings file
and the gate folds it in. Read it, never write it.

This is not tidiness. It is the entire reason several sessions can run at once without a lost
update: no two sessions ever write the same file. If you want to edit a file you do not own, you
want the Hotline or your own findings file instead. New questions and new sources go under their
headings in your findings file, and the merge folds them in.

## Do not

- Do not work a second ticket. Close and hand off.
- Do not create tickets for the questions you turned up. They go in your findings file under New
  questions, and only the gate promotes one.
- Do not chase a tangent. One line under Outside scope, then move.
- Do not draft outreach unless outreach was asked for.
