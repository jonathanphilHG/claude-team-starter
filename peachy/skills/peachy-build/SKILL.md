---
name: peachy-build
description: Run an execution session on a Peachy Adventure map, working the execute tickets that build the deliverable or change live state. Unlike peachy-work it batches several tickets in one session, gates every write to a live system behind a dry run and explicit approval, verifies after the fact, and may spawn sub-tickets. Use when pointed at execute tickets, a rollout across many units, or asked to build out what a cleared part of a map decided.
---

# Execution session

The map plans **and** executes. This is the executing half: the session that builds pieces of the
deliverable or changes live state, rather than establishing what is true.

Read `../peachy-adventure/METHOD.md` first for the shape and its rule pack. This session's rules
are deliberately the opposite of `peachy-work`'s in three places, so do not carry that skill's
habits across:

| | `peachy-work` | here |
|---|---|---|
| Tickets per session | Exactly one | **Several, batched** |
| Writes | None, read only | **The point of the session**, and gated |
| New tickets | Never, only the gate creates them | **May spawn sub-tickets** of the ticket being worked |

---

## Before you touch anything

**1. Orient and pick the batch.** Read `MAP.md`, `PROCESS.md`, `HOTLINE.md`, `MISSION.md`. Read
`MISSION.md` for **Known errors in prior work**, which lists what is known or suspected to be wrong
in this project's inputs so it gets challenged rather than inherited, and for the Access section,
which says plainly what this project may read and what it must not touch. Both matter more here
than anywhere else, because you are about to write.

Take execute tickets that are unblocked and unclaimed, and say the whole batch out loud before
starting so the human can cut it. Prefer a batch that shares a system or a shape of change, because
the dry run and the verification then amortize.

**Confirm the artifacts your tickets name still exist** before you plan around them: the tab, the
file, the sheet, the record. Work orders are written at a gate and the artifacts move afterwards,
and an execute ticket is where that bites hardest, because you are about to write against them. If
one is gone, **check `git log` for it before rebuilding it**, and Hotline what you found. Two
sessions once lost time to a spreadsheet tab a later annotation round had deleted, and only one of
them thought to look in git.

**2. Check the `Run at:` lines against the model you actually are, then claim the batch.**

Before the first `Claimed:` line, not after. The tickets name a tier; `../peachy-adventure/models.md`
says which model that tier is today, and your system prompt names the model you are running on. **If
they differ, stop: write nothing, claim nothing, register nothing, and
tell the human to relaunch at the stated setting.** A session cannot change its own model, so this is
the only guard there is, and it matters most here, where the session writes to live systems. If the
batch's tickets disagree with each other on `Run at:`, that is a scoping error: raise it rather than
picking one. A newer release of the same family counts as a match: run, and note in the findings
file that the lineup table is behind.

Check the model, not the effort. The model is always visible; the effort usually is not, and a rule
a session cannot evaluate is the defect ADR-0007 removed time gates for. Both get recorded at close
in each findings file's session line. See ADR-0012 for the three mis-launches behind this.

**Then claim every ticket in the batch** with a `Claimed:` line, before any work. Then register
**once** in `SESSIONS.md`, naming the whole batch, so the orchestrator has one address for this
session rather than one per ticket:

```bash
printf '%s\n' "- [T06,T07,T08 . $(date '+%Y-%m-%d %H:%M')] uds:/tmp/cc-socks/71346.sock . claimed" >> SESSIONS.md
```

`SESSIONS.md` carries the snippet that derives your own socket path. You need it, because no tool
reports your own address: `ListAgents` does not list self.

**3. Establish the pre-state.** Read before you write, always. Record what the target looks like
now: the row count, the current values, the file that exists, the setting as it stands. You cannot
verify a change you never measured, and you cannot roll back to a state you never wrote down.

**4. Read what is known about the system.** Write-side gotchas are worse than read-side ones and
they live in memory, many flagged. A select field that PATCHes as a full replacement, a tool that
silently drops address fields, a schedule that double-pays if two systems both hold it. Read the
entry for the system **before** the dry run, not after the write.

---

## The write protocol

Non-negotiable, and it comes straight from the house rules rather than from this kit.

**Read only by default.** If the ticket can be satisfied without a write, satisfy it without a
write.

**Dry run first, and show the diff.** Enumerate exactly what would change: which records, which
fields, from what to what, how many. A count is not a dry run. Where the tool has no dry run
mode, do one unit and stop.

**Then get explicit approval.** Name the blast radius in the ask: how many objects, which system,
whether it is reversible, and how you would reverse it. Approval for one batch is not approval for
the next one, **unless the map is running on standing approval.**

### Standing approval, with a stop list

A named state, and the only legitimate way to stop asking per batch. Three maps invented the same
wording independently before it was written down here, which is what promoted it.

**It is granted by the human and by nobody else.** Never assumed, never inferred from a run of
approvals, and never granted by a session to itself. Once granted it is **recorded in `MISSION.md`
under Writes to live systems**, with the date, who granted it, and the words if they are quotable.
If it arrives mid-round rather than at charting, it is a `MISSION.md` amendment and only a gate
writes it, with the human's ratification, which is the existing rule and is not relaxed here.

**A grant has three parts and is incomplete without all three:**

1. **What runs without waiting.** Named systems and named operations, not "writes."
2. **The stop list**: what still needs his explicit yes on that specific action. It always includes
   anything sent to a person, anything that moves money, and anything that changes someone's access.
   Deletes and out-of-scope rows usually belong there too.
3. **Its extent**: this round, this batch of tickets, or the project. A round-scoped grant expires
   with the round and is re-granted at the gate, which is the safer default and the one the field
   used most.

**Standing approval removes the wait, not the record.** Every other clause in the write protocol
still runs on every write: the pre-state, the dry run written to the findings file, the mechanical
guard, sequential writes, and verification by re-read. The dry run still gets posted before a batch;
it just does not block.

**It does not extend to the file-ownership rules.** A worker still does not write `MAP.md`,
`MISSION.md` or any canonical output, and the orchestrator still does not execute. Those are not
approval gates, they are the concurrency design (invariant 6) and the record design, and no session
can tell whether a sibling is live. Suspending an approval gate is a judgment about risk appetite
and it is the human's to make; suspending file ownership is a lost update waiting for a second
session.

**If a ticket has already claimed when the grant changes, message it.** A claimed session owns its
ticket file and will never see an edit to it. Update unclaimed tickets directly, relay to the
claimed ones.

**Use a mechanical guard wherever the tool supports one.** A filter, a limit, an allowlist, a
scoped credential, a `WHERE` clause you have already run as a `SELECT`. The guard is what makes a
mistake small.

**Sequential, not parallel, on writes.** Concurrent writes to the same system are how a partial
rollout becomes an unknown state.

**Verify after, by re-reading the target.** Do not trust the write's own success response. Re-read
and confirm the new state matches the intent, and record the confirmation. A write that reported
success and did not take is the failure mode that costs the most to discover late.

**A refusal is a fact about the credential, not the resource.** A 4xx or auth-shaped error on a
write describes the tuple (credential, scope or selection, host, verb) you sent, not the thing you
were writing to. Before you record a block, re-run the same request on every credential the project
holds, and on a different selection where a token is scoped to one (a dashboard token scoped to the
selected account 403s on every other account), then write the block with the credential named. On one map a 403 had hardened into a documented fact, "a
write needs the dashboard browser session", and a later ticket built a HAR-capture protocol
around it; the same request, same host, same body, sent with a second application key, returned
200. The positive controls on that map were sound and could not catch it, because the credential
was the one constant in every run. It recurred four times on one evening across two maps before
it was written here. Recording a refusal is the write-side case of an absence, so the scope rule in
`../peachy-adventure/evidence-tiers.md` applies to it: the credential is part of the surface.

**Some things a human presses.** Account and billing settings, anything that spends money,
anything that touches a person's access. Prepare it completely, then hand it over.

---

## Communications are drafted, never sent

This has the same weight as the write protocol above, and it is stated separately rather than as one
item in that list for one reason: it is the only entry whose failure mode is **irreversible and
public**. Money can be refunded and access can be revoked. A message blast to customers cannot be
unsent.

**Unless you have explicit approval on that specific message, always draft and never send any
communication templated up on a Peachy map.** Not email, not SMS, not a portal notice, not a
voice blast. Prepare it completely, hand it over, and the human presses send.

**Every comms draft carries the premise it rests on**, one line, naming the fact the message would
be wrong without. This is the cheap part and it is the part that works.

**The premise does not go in the draft body.** It goes in the message that hands the draft over, or
in the relay, referencing the draft by id. The guarantee is that he sees what the message assumes
**before** he can send it, and a handover serves that in full. Putting it in the body taxes the
person the rule is protecting: he deletes it from every draft by hand, and the draft body should be
exactly what he would send, untouched. If something genuinely has to sit inside the draft for him to
decide, make it one bracketed sentence rather than a block, and say in the handover that it is there
to be deleted.

**A comms deliverable is drafted in a ticket and assembled at the gate.** The drafting is work that
produces a findings file, so it is a ticket, and the ticket owns the draft file. The gate creates the
canonical copy from it. An orchestrator that drafts the message itself has skipped both the record
and the second pass, which is the failure in "the orchestrator never executes."

**If the map publishes under a redaction rule, positive-control the scan before you trust it.** A
mandated pre-publish grep for a multi-word phrase once returned nothing on a file that plainly
contained it, because markdown had wrapped the phrase across two lines. It failed
close-to-looking-clean rather than loudly, which is the whole danger. Prove the matcher finds a
seeded positive first, then run it. The rule and a matcher that survives wrapping, blockquote
markers and multibyte characters are in `../peachy-adventure/evidence-tiers.md`, under "a scan you
have not tested is not a scan."

**A comms draft is never "done" at a gate, only "ready for a human to read."** Do not close it out
as complete and do not let a merged findings file imply it went anywhere.

The near-miss this comes from is worth carrying, because nothing else in the method would have
caught it. A research ticket drafted a customer announcement, correctly, on the premise its own
evidence supported. The draft was well sourced and the ticket followed every rule. Then the human
answered from his own knowledge that the premise was wrong, which made the message wrong in a way
that would have told several hundred customers to do something they did not need to. **Correct by evidence and wrong by fact** is exactly the case a send-gate exists
for, and the error lived in a premise only the human held. It was findable in seconds solely because
the premise had been written down next to the draft. That is the guarantee to preserve, and it is
indifferent to whether the line sits in the body or in the handover, which is why moving it costs
nothing.

---

## The per-unit record

For a rollout across many units, this is the deliverable as much as the change is, because the
failure mode of shape 4 is a partial rollout nobody can audit.

Maintain a unit list with a status per unit, owned by the batch, in the project root. Every unit is
in exactly one state:

- **done**, with the date and what was verified
- **exception**, with the reason and what would clear it
- **not started**

**Never leave a unit "blocked."** A blocked unit is an exception with a reason: that is the shape's
bounded form, per the rule pack, and it is what lets the rollout finish rather than stall. Write
the reason and move to the next unit.

The map's index section for a rollout is the unit tally, so the gate can read progress in one line.

---

## Sub-tickets

An execute ticket may turn out to contain several units of work that need separate claiming,
separate approval, or separate verification. Split it: `tickets/T04a-<slug>.md`,
`T04b-<slug>.md`, each carrying a `Parent: T04` line, and note the split in the parent.

This is the one place a non-gate session creates tickets, and it is narrow. **A sub-ticket is a
piece of work already inside its parent's scope.** A new question, a new fact to chase, an
adjacent thing you noticed: those go in your findings file, and only the gate promotes them. If
you are about to write a sub-ticket that the parent does not already imply, you are growing the
map, and that is not yours to do here.

---

## Closing

Same as `peachy-work`, once per ticket in the batch: a findings file at `findings/T<NN>.md` from
`../peachy-adventure/templates/findings.md`, then `## Resolution` and `Status: closed` on the
ticket.

**Re-read what the gate owns before you write any of it**: `MAP.md`, `MISSION.md` and any canonical
output file the batch touches. A gate may have amended one while you were writing, and your beliefs
about those files date from when you started. This is the mirror of the artifact check you ran
before touching anything, and it matters here in particular, because a batch runs long enough for
the record to move under it.

For execution work the findings file's Facts section records **what changed**: the objects
touched, the before and after, the verification, and the exceptions. That record is the only thing
standing between a completed rollout and an unauditable one.

Commit per ticket, files staged by name, ticket-prefixed message.

When the batch is done, append your `. closed` line to `SESSIONS.md`. Then **relay the result** per
`PROCESS.md`: `SendMessage` the orchestrating session two lines, what changed and what it unblocks,
sent to the socket on the `ORCHESTRATOR` line. A rollout that half the map is waiting on is exactly
the case the gate is too slow for. If no orchestrator is reachable, the close is still complete.

**A closed ticket that starts working again is open.** This happens here more than anywhere else,
because approval to extend a sweep arrives after the ticket has been written up: set `Status: open,
reopened <date>, <why>` *before* the next write, put the new work under `## Addendum <date>` in the
same findings file, and re-close by updating the Resolution rather than replacing it. `Status` is
what tells another session whether a ticket is takeable, so a closed ticket with live work in it is
a concurrency bug, not only an untidy record. The test: **if a unit row says in flight, the ticket
cannot say closed.** This is not the sub-ticket case; splitting new scope into `T04a` is still
right, and unlike reopening it grows the batch rather than reviving a ticket.

**Do not write `MAP.md` or any canonical output file.** Even here. The gate reconciles. **That
includes `MISSION.md`**, which is amendable only at a gate and only with the human's ratification:
send the correction, do not make it.

## Do not

- Do not write to a live system without a dry run and an approval on that specific batch.
- Do not batch across systems just to make the session look productive.
- Do not treat a tool's success response as verification.
- Do not proceed past a unit that failed in a way you do not understand. That is a material fork:
  stop and ask.
- Do not grow the map. Sub-tickets only, and only inside the parent's scope.
