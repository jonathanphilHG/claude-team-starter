---
name: peachy-chart
description: Chart a Peachy Adventure map for a large non-code project. Use when a knowledge, operational, financial, legal, or research project has outgrown a single session and needs structure before more work goes into it. Offer it in one line and scaffold only on approval; never chart a project that was not asked about. Not for code repos where the tickets resolve design decisions, which is /wayfinder.
---

# Chart a Peachy Adventure map

One session, and it **resolves nothing**. It produces a map and the tickets to work it.
Hand-working a ticket in the charting session is the most common way this goes wrong.

Read `../peachy-adventure/METHOD.md` before starting. You need the shapes, the rule packs, the
ticket types, and the asking rule, and this skill assumes them.

**Offer, do not hijack.** If the human did not ask for a map, say in one line that this looks
like a Peachy project and why, and wait. The trigger worth naming back to them: more than one
session's work, more than one system involved, and enough fog that the next step is not
obvious.

---

## The eight steps

### 1. Confirm this is a Peachy project

The test is what the tickets resolve, not where the files live. Design decisions about code
someone will then write go to `/wayfinder`. Establishing facts, producing documents, or
changing live operational state is Peachy. A small repo that is not really a codebase is
usually Peachy.

Then check the four "do not use it" cases in `METHOD.md`. If it is one session's work, say so
and do the work instead.

### 2. Name the destination, and the decision it serves

Grill for this, live. Two questions matter more than the rest: what does reaching the end look
like, concretely enough to test, and **what would someone do differently** because of it. A
destination that serves no decision is a reading project, and reading projects have no end.

Get four things **in the human's own words**, not invented:

- The destination, and what done means.
- The decision it serves, and roughly when it gets made.
- The **materiality bar**, stated as concretely as they can. "Would move the headline number
  more than 10%." "Would change whether I sign." This is the test every later session applies,
  so a vague bar makes every later guard vague.
- What this is **not**. Scope creeps in through unstated framings more than through tickets.

Apply the asking rule while you do it. Ask what only they can answer; look up the rest.

### 3. Pick the shape and write its rule pack

One of the five in `METHOD.md`. Pick the dominant shape, name any secondary one, and take the
stricter rule where they conflict. Copy the matching rule pack column into the map's Notes as
plain sentences, not a table reference: a later session must be able to follow the rules
without reading this skill.

Say the shape out loud to the human. It decides whether evidence tiering is on, what an
unresolved item converts into, and what the map's index section is called, so a wrong shape
here misconfigures everything downstream.

### 4. Sweep the sources

Invoke `peachy-sweep`. Do not skip it and do not do it casually inline: a ticket written against
a surface nobody can actually reach burns a whole session discovering that. The sweep is the
step non-code work needs that code work does not, and its output becomes `SOURCES.md`.

**Anything a prior map or the human says was already sent or filed is checked against its
confirmation record before it goes into `MISSION.md`.** A mission once inherited "filed the twelve
defects" when the filing had 503'd, and the whole map was built on it. See "a person's report of an
action is a claim" in `../peachy-adventure/evidence-tiers.md`.

### 5. Grill breadth-first for the frontier

Fan out across the whole space rather than deep on any one thread. Surface the open questions
and the first steps takeable now.

**If this surfaces no fog**, the way is already clear and the whole thing fits in one session.
Say so and stop. Do not build a map for a task.

### 6. Locate the root and scaffold

Resolve the project root per `METHOD.md`. Short version: an existing folder under your
projects root if there is one, the project's repo if it already has one, otherwise a new
`~/Peachy/<Project Name>/`.

Scaffold from `../peachy-adventure/templates/`: `MISSION.md`, `MAP.md`, `PROCESS.md`,
`HOTLINE.md`, `SESSIONS.md`, `SOURCES.md`, and empty `tickets/` and `findings/` directories. Fill
the placeholders; do not leave a template comment in a live file.

**Write the `ORCHESTRATOR` line into `SESSIONS.md` yourself**, using this session's own socket path.
You are the orchestrator, and this is the one line in that file a worker does not append. Derive the
path with the snippet in the template, which walks your process ancestry to the `claude` process and
names its socket in `/tmp/cc-socks/`. There is no tool that will hand it to you: `ListAgents` lists
peers, not self. Without this line, workers have no way to reach you and every relay this round
fails silently, which is exactly what happened on the map that produced this rule.

`git init` if the root is not already a repo, and add no remote. If it is already a repo with
a remote, normal git rules apply, and do not move confidential material into it without
asking.

**Canonical output files are not created here.** No `facts.md`, no `contradictions.md`. They
come into existence at the first gate, by merging. That is deliberate and `PROCESS.md`
explains why.

### 7. Write the tickets you can state now

One file each at `tickets/T<NN>-<slug>.md` from `../peachy-adventure/templates/ticket.md`.

Each ticket needs a type from the five in `METHOD.md`, a `Depends on:` line, and, mandatory,
a line naming **what it changes in the deliverable**. A ticket that can name nothing it
changes is not a ticket.

It also needs a `Run at:` line naming a **tier and an effort, never a model**. Read
`../peachy-adventure/models.md` for the two tiers, the per-type table and the one lineup table that
maps tier to today's model. The short version: the type decides it, because what decides the tier is
whether a human is in the loop to redirect. AFK research goes to the frontier tier at `xhigh`, a grill
to the workhorse tier at `xhigh`, and bounded work (a task, a prototype, a small execute batch) to the
workhorse tier at `high`.

Create them, then wire the `Depends on:` edges in a second pass. Then write the frontier, the
open unblocked unclaimed tickets, as a short list at the top of the map's index section so a
later session sees what is takeable without reading every ticket. This is the part files do
worst compared to a tracker, so it has to be maintained deliberately.

Everything you cannot yet state sharply stays in **Not yet specified**. The test is whether you
can phrase the question precisely now, **not** whether you can answer it. Do not pre-slice fog
into ticket-sized pieces.

**Twelve open tickets is where you stop and justify, not a wall.** If the map needs more, write one
line in its Notes saying why, and write it. A broad domain genuinely needs more tickets than a
narrow one, and the failure this replaces is real: a map hit exactly twelve and compressed "how the
business works" into a single ticket to stay under the number. **Under-decomposing to respect a
count is worse than the count.**

What actually stops sprawl is the materiality bar and a default of zero new tickets at a gate. A
number is a backstop, not the mechanism. If twelve keeps being exceeded on maps that turn out fine,
that is information about the destination, not about the tickets.

### 8. Propose the gates, hand over the kickoff prompts, stop

Propose how many gates and what each is for, and write them into the map. **Gates run automatically
when a round closes**; only if he wants this map's gates to wait for his go, add the one-line
opt-out to `MISSION.md` under Gates. **Three is the recommendation, not a ceiling.** If this map needs more, write one line in its Notes saying why. Big
projects, several shapes in play, and live state being changed all legitimately run longer, and a
hard number would only pressure a later gate not to fire when it should.

Then hand the human **one kickoff prompt per ticket in the round**, written out in full rather than
described, to paste into separate terminal windows.

**Not subagents.** A subagent dies with its parent, shares its budget and its context window, and
cannot register in `SESSIONS.md` or take part in the relay, so a round fired as subagents evaporates
when the charting session ends. A Peachy ticket wants its own session: its own context window, its
own address, and survival past this conversation. Hand over prompts and let the human launch them.

**What belongs in a kickoff prompt.** The kit's second invariant is that detail lives in exactly one
place, and a prompt is not that place:

> A prompt carries the **project location**, the **ticket**, the **skill** to invoke, and the
> **goal in a sentence or two**. Plus any hard rule the session must not discover late.>
> **Not the model and the effort.** A session cannot set its own model or effort, so a prompt
> carrying them instructs a reader who cannot act on it. They are a precursor said to the human
> alongside the prompt, "run this one on the workhorse tier at high," not a line inside it. The ticket's `Run at:`
> line and the map's **Session settings** line already carry them.
>
> **Everything else is a pointer.** Ticket traps, `MISSION.md` context, where-to-look content: those
> live in the files and get read from the files. Copying them into the prompt is two sources of
> truth, and it goes stale the moment a gate revises the ticket.

Each prompt must **name its ticket explicitly**. A session told only "work the map" takes the first
frontier ticket in order, so a parallel launch without named tickets means two sessions grab the
same one.

Each prompt also tells the session to **register in `SESSIONS.md` at claim and relay its result back
on close**, two lines, per `PROCESS.md`. It will not do either otherwise.

---

## The asking rule, inline because it matters most

There is **no cap** on questions. There is one test each has to pass:

> Would the branches change what the human actually does, or what the deliverable says at the
> headline level?
>
> **Yes:** ask now. **No:** decide it, write the pick and a one-line reason, move on.

Never ask what the sources can answer. Every question ships with your recommended answer, so
"yes" is a complete reply. Never ask permission to continue.

Charting is the most grilling-heavy session in the kit, and it is still not an exhaustive
interview. Wayfinder walks every branch of the decision tree and that is too much: it gets
nitty-gritty on questions that resolve themselves two tickets later, and it makes a project
take longer than the work in it. Stay on the 80/20. The fog is supposed to still be foggy when
you finish.

## Do not

- Do not resolve a ticket in this session. **This is the orchestrator rule, and it holds past
  charting:** if the work would produce a findings file were someone else doing it, it is a ticket,
  at any round size. Run an orchestrator when two or more tickets are live at once or when output
  leaves the company; below that, run the ticket and skip the orchestrator rather than letting it
  quietly do the work itself.
- Do not invent the materiality bar or the definition of done. Get them in his words.
- Do not create the canonical output files.
- Do not chart past the destination. Work beyond it goes in Out of scope, and it never
  graduates.
