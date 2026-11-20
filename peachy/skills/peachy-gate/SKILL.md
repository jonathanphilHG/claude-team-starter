---
name: peachy-gate
description: Close a round on a Peachy Adventure map. Merges every ticket findings file into the canonical outputs, resolves contradictions explicitly, updates the map and the frontier, then decides the next round against the materiality bar, writes the human read, and hands over the kickoff prompts. Use when a round of Peachy tickets has finished, when parallel sessions need reconciling, when the canonical files have drifted behind the work that has already landed, or when asked what a Peachy project now knows.
---

# The gate

Findings sit in per-ticket files nobody has reconciled, and some of them contradict each other.
**This is the only session allowed to merge them**, and the only one allowed to write `MAP.md` or any
canonical output file.

Read `../peachy-adventure/METHOD.md` for the shape and its rule pack; the shape decides which
canonical files exist and what the map's index section is called.

**Two things can bring you here, not one.** A round closing is the obvious one. The other is
**drift**: the canonical files have fallen behind work that already landed, so anyone reading them
would be reading something false. Drift is a legitimate reason to fire a gate. Under a readiness
framing "nothing is finished yet" reads as a reason to **defer**, which is backwards when the record
is the broken thing, and that cost one map a round of work. See ADR-0010.

**This permits, it does not instruct.** Gates are not meant to become cheap and frequent by default:
each one is a full stop on the parallelism that is this method's biggest win, and the anti-sprawl
guard below bites hardest at a natural stopping point. Fire on drift when the record needs it, not as
a habit.

**A clause follows, and it is not optional: "clean slate" does not mean everything is closed.** A
gate firing mid-round finds open items by definition. An exception carried forward with an owner and
a next action **is** a clean slate, and forcing closure to make the record look tidy is worse than
leaving the item open and honest.

## A gate runs automatically when the round closes

**Do not wait to be told "gate".** When the last ticket in a round closes, the orchestrator runs this
skill: on the last close relay if it is live, otherwise the next session to open the map and find
every round ticket closed with no gate after them. It used to depend on who was orchestrating, and he
asked why: "Why am I sometimes stopped from running gates, and why do they happen sometimes
automatically? ... I'm leaning towards automatically." A later finance map then ran its last two
gates on his say-so without waiting, with no friction.

**Three things still wait for him, and the gate stops at each rather than picking:**

- **A `MISSION.md` amendment.** Proposed, never written, until he ratifies. See "Amending
  `MISSION.md`" below.
- **A fork that passes the asking rule.** It goes in the human read as a fork with your
  recommendation, and whatever depends on it waits.
- **A ticket with no human input to cite.** It is provisional and goes on the `Blocked:` line, per
  the citation rule below.

Everything else, the merge, the canonical files, the contradictions, the frontier, the human read and
the prompts, was always the gate's own authority. **Launching stays his**: the gate hands over
prompts and he pastes them, so an automatic gate cannot start a round by itself.

**Why this is safe, checked against every reason the kit puts a human at a gate.** Scoping from
evidence he has not seen is stopped by the citation rule, which is self-triggering. MISSION changes
are held for ratification. The judgment calls live in grill tickets and in charting, which stays live.
Waiting bought him the moment before a merge, and the merge was never his to do.

**A map can opt out in one line.** If `MISSION.md` says **Gates wait for his go** under Gates, the
gate asks before it starts. That is for a map where he wants to scope a wide round himself.

This covers a round closing. A gate fired on drift is unchanged: permitted, not scheduled.

Two jobs, and they are in tension: merge faithfully, then **refuse to grow the map**.

---

## Merge

**1. Read everything.** Every `findings/T*.md` from the round, or, if you were fired by drift
rather than by a round closing, everything unmerged since the last gate. Then the whole
`HOTLINE.md`, the current `MAP.md`, and `MISSION.md`. Read the mission last so you finish oriented on what this is for
rather than on what the round happened to turn up.

**2. Create or update the canonical outputs.** They do not exist before the first gate; that is
what makes the file-ownership model work. Which ones exist depends on the shape, per the mission's
required-outputs table. Commonly:

| File | Holds |
|---|---|
| `facts.md` | Every established claim, tier tagged, cited |
| `parameters.md` | Everything bounded but not established: value, range, tier, basis, what would settle it |
| `contradictions.md` | Every source conflict, both sides cited, and every prior claim that could not be reproduced |
| `open-questions.md` | Unresolved items: what was tried, what would resolve it |
| `SOURCES.md` | Where things live, including the search patterns that worked |
| `dead-ends.md` | Empty wells and confirmed absences |
| `outside-scope.md` | One line each for material problems that are not this project |
| the deliverable | Whatever the destination named |

For a rollout, the unit list with per-unit status is the canonical output that matters, and the
exception list is the second.

**3. Resolve contradictions explicitly, never silently.** Two findings files disagreeing is the
most valuable output of a round, not a defect to smooth over. For each conflict: state both sides
with both citations, then either resolve it with reasoning you write down, or record it as live and
say what would settle it. **Never pick one quietly.** If settling it needs a judgment only the
human can make, it goes in the human read.

**4. Call out every tier movement.** A claim that went from assumption to evidence, or a claim that
could not be reproduced and dropped to `UNKNOWN`, usually moves the answer more than any new fact
does. Those are headlines, not footnotes.

**Any rule you verify mechanically gets a positive control first.** You are the session that checks
rules on behalf of the whole map, so a matcher that lies here writes a false all-clear into the
canonical files and into the human read at the same time. Three separate guards have now reported
CLEAN on corpora that contained exactly what they were hunting. Prove the matcher finds a known
positive, then trust the zero. See `../peachy-adventure/evidence-tiers.md`, "a scan you have not
tested is not a scan."

**A claim that something was sent, filed or done is checked against its confirmation record before
it is merged**, whoever made it, the human included. A report of an action is Tier C until the
record confirms it. See `../peachy-adventure/evidence-tiers.md`, "a person's report of an action is
a claim."

**5. Update `MAP.md`.** One line per closed ticket in the index section: a gist plus a link to its
findings file, never the detail. The map is an index, not a store.

Then three maintenance passes people skip:

- **Rewrite the frontier list**, the open unblocked unclaimed tickets. Files have no tracker UI to
  render this, so if the gate does not maintain it, nobody can see what is takeable. **A provisional
  ticket does not go here.** It is blocked on the human's read, so it goes on the map's `Blocked:`
  line naming that, which is what stops it being launched. See the citation rule below.
- **Graduate fog.** Anything the round made specifiable moves out of **Not yet specified** and into
  a ticket, and gets cleared from the fog section so it lives in exactly one place.
- **Rule things out of scope.** Anything the round revealed to sit past the destination gets closed
  with one line under **Out of scope** and the reason. It stays out of the index, because a scope
  boundary is not a step on the route.

---

## Then refuse to grow the map

**Default to zero new tickets, and say so out loud when it is true.** The best moment in this
method's history was a gate that wrote "no new research tickets: everything left is analysis or
merge."

A question becomes a ticket only if answering it would move the deliverable materially or change
the decision the destination serves. Everything else stays a line in the findings files, where it
is still findable and costs nothing. The human will pull something forward if it was missed; that
is cheaper than carrying twelve speculative tickets.

Before creating any ticket, all four must hold:

- It names what it changes in the deliverable.
- It clears the materiality bar stated in `MISSION.md`.
- The map stays under twelve open tickets, or you say in one line why this one needs more. It is a
  bar that asks for a justification, not a wall.
- **You could not just do it in two minutes.** If you could, do it. A ticket that only restates
  what the next session already knows is pure overhead.
- **You can cite where its human input came from**, in one line. See below.

**Every ticket you scope for the next round cites its human input.** One line on the ticket naming
the row he marked, the sentence he said, or the decision from the last read. A gate **may** scope the
next round, and it may only do so from human input that already exists and still applies.

**A ticket that cannot cite one is provisional.** Write it, mark it provisional, keep it off the
frontier and on the `Blocked:` line waiting on his read. Then give him something to read.

What this bans is narrower than it first sounds, and the narrowness is the entire point: it bans
**scoping from evidence the human has not seen.** Scoping from marks he already gave is the normal
case and stays fine, because review artifacts are cumulative and demanding fresh marks at every gate
is its own failure mode on a long project.

Both halves of that come from real rounds. Ten parallel research tickets once produced several
thousand lines of findings, dozens of escalations and over a dozen structural defects; the gate merged them
faithfully, scoped six execute tickets and handed over six prompts, exactly as prescribed. It could
have cited human input for none of them. He then answered one whole ticket from his own head in a
single sentence and cancelled three more as "great work tickets but ones we can wait on." **After a
wide round the gate scopes from evidence and the human scopes from judgment, and his judgment is
cheaper and better.** But the opposite error is just as real: a stricter version of this rule,
demanding a fresh review beat every time, would have blocked three well-scoped tickets whose content
he had marked on a review sheet hours earlier.

The citation is what makes that distinction auditable instead of a judgment call, and it costs one
line. On a small map it is usually "he said so, in this conversation," and that is a complete
citation.

**Prefer rewriting an existing ticket to current truth over creating a near duplicate beside it.**
Accumulating overlapping tickets is the failure mode, not losing detail. If a ticket is now
invalid, delete or rewrite it and say which.

Also decide, explicitly, whether the next round needs execution rather than more establishing. A
map that keeps producing findings and never builds anything has drifted, and the tell is a round
that closes with no `execute` ticket in sight and no deliverable moving.

---

## The human read

A short document he can read in a few minutes and act on, not a transcript of the merge.

- **What changed.** The two or three findings that moved the answer, with their tiers.
- **What is now the largest unknown.** It is usually not what it was at the start of the round, and
  naming it is the most useful line in the document.
- **What needs a decision from him**, each as a fork with your recommendation. Not a request for
  permission to continue. Batch the sub-material calls that sessions made along the way here, so he
  can overrule cheaply.
- **What is next**, and whether the map is closing.
- **Anything needing a professional**, flagged as such: attorney, CPA, licensed engineer. Do not
  present a conclusion in those areas as settled. **Conditional: state it when something qualifies,
  and omit the bullet entirely when nothing does.** The other bullets in this list always have
  content; this one frequently has none, and a required bullet then makes every gate report the
  absence. "Nothing here needs an attorney or CPA", map after map, is noise in the one document that
  has to survive a few minutes of his attention. He asked for it twice.

Then hand over the kickoff prompts, one per ticket in the next round, written out rather than
described, to paste into separate terminal windows. Each must **name its ticket explicitly**: a
session told only "work the map" takes the first frontier ticket in order, so a parallel launch
without named tickets means two sessions grab the same one.

**What belongs in a prompt**, and it is less than you will be tempted to put there:

> The **project location**, the **ticket**, the **skill** to invoke, and the **goal in a sentence
> or two**. Plus any hard rule the session must not discover late.>
> **Not the model and the effort.** A session cannot set its own model or effort, so a prompt
> carrying them instructs a reader who cannot act on it. They are a precursor said to the human
> alongside the prompt, "run this one on the workhorse tier at high," not a line inside it. The ticket's `Run at:`
> line and the map's **Session settings** line already carry them.
>
> **Everything else is a pointer.** Ticket traps, `MISSION.md` context, where-to-look content: those
> live in the files and get read from the files. Copying them into the prompt is two sources of
> truth, and a gate that revises a ticket has just made every prompt carrying its detail stale. That
> is the second invariant, and a gate is the session most likely to break it, because it has just
> read everything and has it all in hand.

**Each prompt also tells the session to register in `SESSIONS.md` at claim and relay back to you on
close**, two lines, per `PROCESS.md`. Neither happens otherwise, and the relay is what lets you
propagate a finding to a live sibling without waiting for the next gate. You are the orchestrator:
sessions report to you, not to each other.

**When you need to reach a live worker, read `SESSIONS.md`, not `ListAgents`.** The registry lists
this map's sessions and their socket addresses. `ListAgents` lists every Claude session on the
machine, and a gate that broadcasts to it will reach sessions working other projects.

If this map predates `SESSIONS.md`, its live workers have no entry and no way to reach you. Message
each one first and have it reply by copying your message's `from` into its `to`, then have it
register, so the fallback is needed once rather than every round.

Then commit, files staged by name.

---

## After the gate: the structural harvest

A round teaches things that belong outside the map: a flow document that is now wrong, a trap in a
tool, a template line the round disproved, a rule the kit should carry. The canonical files do not
hold those, and a map that closes over them leaves the next project to learn them again. **So each
gate hands over one more ticket: a harvest.**

His request, in short: at or after each gate, a frontier-model session goes in and appends, adds,
changes and updates the structural items across the board, on whatever surfaces the work touches
(knowledge bases, a shared data room, notes and templates in a tracker, anything else).

**The gate's part is small.**

- **Seed the queue.** Create or extend `KB-HARVEST-QUEUE.md` in the project root from
  `../peachy-adventure/templates/KB-HARVEST-QUEUE.md`: one row per learning, with its source, its
  target surface and a status. Take the rows from the round's findings files (New sources,
  Contradictions, Outside scope), the relays, the premise corrections, and his rulings that change
  how the work is done. Between gates the orchestrator appends to it as relays arrive. It is the
  orchestrator's file; only the harvest ticket changes a status.
- **Write one harvest ticket**, type `execute`, at the frontier tier and `xhigh`, and hand its
  prompt over with the round's prompts. Its `Human input:` line cites the standing rule above, so
  it is never provisional. Its `Owns:` line lists the surfaces it may write.
- **Skip it out loud when the queue is empty.** Zero rows is a valid result, and a harvest ticket
  with nothing to carry is the overhead this skill exists to refuse.

**What the ticket carries, so every map's harvest runs the same way.**

- **The queue is the starting list, not the scope.** The session scans on its own: every findings
  file, the Hotline, the log, the sweeps and the project files since the last harvest, read against
  what the targets say today. His words: "it should do its own scanning."
- **It lands directly what only touches our own working files**: flow documents, trap and API
  notes, reference repos on their working branch, this kit. It reads each target before writing it,
  keeps a copy of the before, and records before and after in its findings file.
- **It holds for one table, on his yes:** template text in a system other people work from, any
  document the team reads, and every ADR. A team copy carries facts and rules, never the process
  that found them.
- **It never writes a file a live ticket owns.** It leaves a Hotline line for that ticket.
- **It closes with a table**: surface, item, and landed, held or dropped with the reason, and the
  queue's statuses updated to match.

**Why frontier, when execute tickets default to workhorse.** Nobody can list the steps in advance:
the session decides what is structural, finds where it belongs, and notices what the queue missed.
That is the frontier side of the axis in `../peachy-adventure/models.md`.

**Why this is not growing the map.** It resolves nothing in the deliverable and opens no question;
it moves what the round already established to where the next project will read it. It still
counts against the open-ticket bar.

**Two maps that share surfaces share the collision.** When a sister map queues the same learning,
the first harvest to run lands it and leaves one line on the other map's Hotline naming what
landed and where, so the second extends the text and does not write it twice.

First run: a small rollout map whose gate seeded about a dozen rows; the harvest's own scan added
rows the queue did not hold.

---

## The orchestrator never executes

You merge, you scope, you talk to the human, and you write the canonical files. **You do not do the
work.**

The test: **if the work would produce a findings file were someone else doing it, it is a ticket.**
Drafting outbound comms produces one. So does any read of a live surface to establish a fact.
Legitimately in-orchestrator: reading the map's own files, talking to the human, scoping, merging,
and writing the canonical outputs.

This holds **at any round size.** If there is only one ticket's worth of work, run the ticket and
skip the orchestrator entirely; if you are already orchestrating, open the ticket. "It is only a
small job" is how the rule gets broken, and the orchestrator role genuinely is overhead on a
one-ticket round, which is an argument for not having one rather than for letting it work.

**The cost is not context, it is the record and the second pass.** A round-3 orchestrator was asked
to work an open-items pass with the human, surfaced eight outbound comms and drafted seven itself:
roughly fifteen Gmail searches, an attachment inventory, seven drafts. Two things broke:

- **No record.** No `SESSIONS.md` registration and no findings file, so what was drafted, what was
  verified, and six corrections to canonical files lived only in a chat transcript. The kit tells
  workers that state lives in files; it never said it to the orchestrator, who is the one session
  whose conclusions reach the canonical files with no merge step in between.
- **No second pass.** A worker verifies before relaying and a gate merges only what survives. Here
  the finder and the merger were the same context. It failed the same day: a search that could not
  have matched its target produced a false absence, and that absence went straight into two
  canonical files **and** the human-facing read, because there was no ticket boundary to cross.

---

## The orchestrator routes, it does not restate

You decide **whether** a finding travels, **to whom**, and **when**. You do not decide **how
strongly it is stated.**

That split is the answer to a question this kit carried open for a while, whether the orchestrator
is a filter or a relay. It is both, and the axis was wrong: volume was never the problem. Every
failure on record here is a **provenance** failure. A relay that keeps provenance is safe at any
volume; a filter that strips it is dangerous at any volume. See ADR-0011 for why neither side of
that question was adopted.

**1. A claim travels in the worker's own words, carrying its tier and the surface it was measured
on.** Quote the ticket for any bounded claim rather than paraphrasing it. You restate several
sessions' findings at speed, without their calls in front of you, and every restatement is a chance
to drop a qualifier. The dropped qualifier then travels **further** than the original, because it
arrives carrying your authority and siblings read it as merged truth rather than as one ticket's
Tier B observation. Two instances in two consecutive messages on one map: a single unreproduced
observation about a page-size cap relayed as settled fact, and "there is no bulk-export route **in
this MCP**" restated as "unknowable from the API," which was false and had two untried routes behind
it. When you paraphrase a limit, the surface it was measured on is part of the claim, not context
around it. See `../peachy-adventure/evidence-tiers.md`.

**2. A worker's escalation is not re-litigated.** If a session applied the asking rule and decided
its fork goes to the human, route it to the human. Batch it if you like. **Do not absorb it.** The
asking rule was already run by the session that actually held the evidence, and re-running it from a
summary is strictly worse. On one round five sessions relayed constantly, between them three
retractions, two premise changes and a live-data alarm, and the human heard from the orchestrator
maybe four times.

**3. A single-source claim that would make him act gets verified before it travels, or it travels
labelled.** This is the clause that costs anything, and it guards the one hop with no second pass
behind it: a worker verifies before relaying, and a gate merges only what survives, but nothing sits
between you and him. A ticket relayed that payments were still going into an account being closed,
with one payment missing, and it reached him as money at risk within the minute. Another ticket
then checked the system directly and **both halves were wrong**: the account had been closed long
before, and the payment had arrived from a different payer.

Verifying is cheap and it cuts both ways. On another map a gate that checked five workers' claims
against the artifact, rather than accepting the reports, found one real defect **and** one false
positive. Check what will travel. Accept the rest.

---

## Amending `MISSION.md`

`MISSION.md` is frozen against workers and against you acting alone. It is **not** frozen against the
project. On a long map it will need to change, and in practice it does: one map amended it five
times in two days, always by the human and always correctly, while the template still said the file
was fixed forever.

**A gate is the only session that may amend it, and only with the human's explicit ratification.**
You propose the change and say what prompted it, he ratifies, then you write it and log one line
under `## Amendments` with the date, what changed, and why. Never unilaterally, in either direction.
That keeps the file-ownership invariant intact, since a gate is the only sequential writer, and it
keeps the mission worth re-reading when a session feels lost.

Ratification rather than gate authority is deliberate. **An orchestrator that has just been wrong
writes rules stricter than the evidence supports**, which is the exact failure that produced this
rule: a gate over-corrected from one real incident into a blanket rule that would have blocked three
well-scoped tickets, and the human was the one who caught it.

---

## Closing the map

The map closes when **the deliverable is defensible**, not when the tickets run out and not when
everything is known. Say it plainly in `MAP.md` with the date.

A closed map can still take a **correction round**: a short fresh list against a map that stays
closed. Reopening properly should feel like a decision, because it is one.

**Justify the gate count, do not cap it.** Three gates is the recommendation for most projects. It
is a bar that asks you to write one line in the map's Notes saying why this one needs more, **not a
wall, and no upper number is named.** How big the project is, how many shapes are in play, and
whether live state is being changed all legitimately push it longer.

A hard number backfires in the exact case gates exist for. Gate 2 on one map fired early and out of
order because a call answered the blocking question and inverted the mechanism from delete to
transfer; running the old tickets would have executed the wrong operation on live records. That is
a gate doing its job, and under a ceiling of three it read as spending one of them. **A ceiling
pressures a gate not to fire when new information arrives mid-round, which is backwards.**

Sprawl control rests where it always did: the materiality bar, and a default of zero new tickets at
a gate.
