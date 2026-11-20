# Peachy Adventure: the method

Shared spine for `peachy-chart`, `peachy-sweep`, `peachy-work`, `peachy-build` and
`peachy-gate`. Read the parts you need; do not read it end to end unless you are charting.

Wayfinder, for work that is not code. A project has reached critical mass: too big for one
session, spread across systems and people, and enough fog that charging at the destination
produces motion without progress. Peachy Adventure charts it as a map of tickets, then works
them until the deliverable is defensible.

---

## Is this a Peachy Adventure project

**The test is what the tickets resolve, not where the files live.**

- Tickets that resolve **design decisions about code someone will then write**: use
  `/wayfinder`.
- Tickets that **establish facts, produce documents, or change live operational state**: use
  Peachy Adventure.

A small repo that is not really a codebase is usually Peachy, because its tickets are
operational in shape. A local folder full of markdown that is actually a system design is
Wayfinder. The two hand off in both directions: Peachy establishes the facts and the
decision, then Wayfinder charts the build if the build is substantial code. Or Wayfinder
clears a design map and Peachy carries the operational rollout that follows.

**Do not use either when:**

- It is one session's work. Do the work.
- It is a single question with a single answer. Answer it.
- It is recurring operational work. That wants a runbook or a cron. A Peachy project might
  produce the runbook once.
- The real blocker is one person answering one email. Send the email.

---

## The five project shapes

Charting picks one and writes its rule pack into the map's Notes. The shape decides which
disciplines are on, because a discipline that is essential for one shape is pure overhead
for another.

| # | Shape | Unit of unknown | Done is | Main failure mode |
|---|---|---|---|---|
| 1 | Investigation | A fact | Facts established, gaps bounded, brief written | Retrieval rabbit hole |
| 2 | Decision | A judgment under uncertainty | The decision, its reasoning, and what would reverse it | Analysis substituting for deciding |
| 3 | Knowledge artifact | A section, a term, a policy | The artifact exists and someone can follow it | Sprawl into a document nobody reads |
| 4 | Operational rollout | A unit of live state changed | N units done, exceptions documented | Partial rollout with no record of what is done |
| 5 | Program spine | A thread that needs a home | Every thread has an owner and a next action | Becoming a second job to maintain |

Shapes mix. Pick the dominant one, name the secondary in Notes, and take the stricter rule
where they conflict.

### Rule packs

| | 1 Investigation | 2 Decision | 3 Artifact | 4 Rollout | 5 Spine |
|---|---|---|---|---|---|
| Evidence tiers | **On, mandatory** | **On, for inputs** | On for factual claims | Off | Off |
| Confidence downgrade | On | On | On | n/a | n/a |
| An unresolved item becomes | a bounded parameter | a stated assumption plus a reversal trigger | a marked gap with an owner | a documented exception on the unit list | a thread with an owner and a next action |
| Write protocol | n/a, read only | n/a | n/a | **Required** | As needed |
| The map's index section | Findings so far | Decisions so far | Sections done | Units done | Threads |
| Guard to enforce hardest | Stop when the marginal finding stops moving the answer | Force a recommendation at every gate | Outline before prose, cap the sections | Per-unit status record, never a blocked unit | Hard ceiling on threads |

Tier definitions and the bounded-form conversions live in `evidence-tiers.md`.

---

## The invariants

True for all five shapes. Everything else is packaging.

1. **State lives in files, not in context.** The project outlives every session. If it is
   not written down it did not happen.
2. **The map is an index, not a store.** Loaded once per session at low resolution. One
   line per closed ticket plus a link. Detail lives in exactly one place, its ticket or
   findings file.
3. **Fog of war.** Do not chart what you cannot yet state precisely. The test is whether you
   can phrase the question sharply now, **not** whether you can answer it. Coarser than a
   ticket goes in Not yet specified. Past the destination goes in Out of scope, and that
   never graduates.
4. **The destination fixes the scope**, and it is named first.
5. **One ticket per session**, with two exceptions: AFK research tickets parallelize, and
   execution sessions batch (see `peachy-build`).
6. **A session writes only files it exclusively owns.** Merging is a separate sequential
   job. This is the whole collision-avoidance design: no locking, no lost update, because
   no two sessions write the same file.
7. **Nothing blocks forever.** When a session cannot resolve its item, the item converts to
   a **declared, bounded, visible form** and the work proceeds. The form is shape-specific,
   per the rule pack. This is the most important rule in the kit.
8. **Something must actively stop the sprawl.** The materiality bar and a default of zero new
   tickets at a gate are the mechanism. Twelve open tickets is a bar that asks charting to
   justify the count in the map's Notes, not a wall: under-decomposing to stay under a number
   is worse than the number.
9. **The seam between sessions is where work is lost**, so the seam gets an artifact: the
   findings file plus the ticket resolution, and a short handoff note for the conversational half.
   Where sessions run concurrently the seam also gets a **relay**: a live message to the
   orchestrating session, which notifies rather than stores. It covers what the Hotline
   cannot, a closed session reaching a live one. The relay needs an address book, so the
   folder carries a **session registry**, `SESSIONS.md`: every session registers when it
   claims, and the orchestrator's address sits at the top for workers to read. Addresses are
   socket paths, because no tool reports a session its own name and none can say which of
   its listed peers belong to this map. See `templates/PROCESS.md` and ADR-0008.

---

## The five ticket types

| Type | Mode | What it is |
|---|---|---|
| `research` | AFK | Reading documents, systems or third-party sources to establish a fact. Needs no human in the loop, so several run in parallel. Give each its own session, not a subagent: a subagent dies with its parent and cannot take part in the relay. |
| `grill` | HITL | The answer is the human's to give: taste, priority, risk appetite, a relationship they own. Only a live exchange gets it. Never answer your own grill questions. |
| `prototype` | HITL | Raise the fidelity of the discussion with something cheap and concrete to react to. An outline before the article. Three sample rows before the table. The brief's headline before the analysis. |
| `task` | Either | Manual work that must happen before something else can be established. Provisioning access, moving data so its shape is visible, signing up so a service can be judged. Earns its place by unblocking. |
| `execute` | Either | Builds a piece of the deliverable or changes live state. Batches several per session. May spawn sub-tickets. Worked by `peachy-build`. |

**`grill` is the default type**, but see the asking rule below: defaulting to the type does
not mean defaulting to a long interview.

**The type also carries the default model and effort**, because the thing that decides both is
whether a human is in the loop to redirect. `models.md` holds the tiers, the effort defaults
and the per-type table. Tickets and maps name a tier, never a model: `models.md` carries the one table
mapping tier to today's model, so a release changes one line rather than every map.

## The asking rule

Wayfinder walks every branch of the decision tree by design, and that is too much. It
over-asks, gets nitty-gritty on questions that resolve themselves later, and makes a project
take longer than the work in it. The research kit swung the other way and forbade asking at
all, which parked a material fork for a whole round and inverted an answer.

The happy medium is a filter, not a quota. **There is no cap on questions. There is one test
every question has to pass.**

> **Would the branches change what the human actually does or what the deliverable says at
> the headline level?**
>
> **Yes:** ask now. Immediately, mid-ticket if that is when you found it. Do not park it for
> the gate and do not pick for them.
>
> **No:** decide it yourself, write the pick and the one-line reason in your findings file,
> and move. They can overrule at the gate, where it costs nothing.

Three corollaries:

- **Never ask what the sources can answer.** Look it up. The decisions are the human's; the
  facts are yours to go get.
- **Every question ships with your recommended answer**, so "yes" is a complete reply. A
  question with no recommendation attached is unfinished work.
- **Never ask permission to continue.** "Should I keep going" is not a question, it is a
  hesitation. Name the fork or proceed.
- **An escalation is not re-litigated.** If you decided a fork goes to the human, it goes. An
  orchestrator standing between you and them routes it, and may batch it, but does not absorb it and
  does not restate it: your wording, your tier and the surface you measured it on travel with it.
  The rule and its three clauses live in `peachy-gate`, under "the orchestrator routes, it does not
  restate."

## The gating model

Six places a human gate sits. Charting sets the shape of gates 1, 4, 5 and 6; the asking rule
governs 2 and 3.

1. **Charting.** Non-negotiable and live. Charting must get the destination, the decision it
   serves, the definition of done and the materiality bar **from the human in their own
   words**, not invent them.
2. **Ticket type.** `grill` and `prototype` are HITL by construction. AFK is the type you
   justify: this is reading, there is nothing here to decide.
3. **Mid-ticket escalation.** A fork that passes the asking rule stops and asks immediately,
   rather than picking or parking it for the gate.
4. **The gate.** Three per map is the recommendation, and it is a bar that asks for one line of
   justification rather than a wall: no upper number is named, and a bigger project or one
   changing live state legitimately runs longer. Any session may call one early if it finds
   something that changes the shape of the problem, and a ceiling would only discourage exactly
   that. **A round closing is not the only thing that may fire a gate.** Drift qualifies too:
   when the canonical files have fallen behind work that already landed, the record itself is
   what needs reconciling, and "nothing is finished yet" is not a reason to wait. That permits a
   gate, it does not schedule one. **A round closing does schedule one: the gate runs
   automatically on the last close**, and stops only for a `MISSION.md` amendment, a fork that
   passes the asking rule, and a ticket with no human input to cite. A map opts out with one line
   in `MISSION.md`. See `peachy-gate`.
5. **Writes to live systems.** Read only by default. Writes need explicit approval and a
   mechanical guard. Dry run, then confirm. See `peachy-build`. **The human may convert this gate
   into standing approval with a stop list**, a named state recorded in `MISSION.md`: it is his to
   grant, never assumed and never self-granted, it names what runs freely and what still stops, and
   it removes the wait rather than the record. It suspends this gate only. It does not touch
   invariant 6 or the orchestrator role, which are the concurrency and record design rather than
   approval gates.
6. **Sending a communication.** Its own gate, separate from the write protocol, because it is the
   one write that cannot be undone: money can be refunded and access revoked, a message blast to
   customers cannot be unsent. **Draft and never send without explicit approval on that specific message**,
   and have every comms draft carry the premise it rests on. A draft that was correct by
   evidence and wrong by fact nearly went to several hundred customers; the human caught it, and the
   premise line is what made it findable in seconds. **The premise travels in the handover or the
   relay, not in the draft body**, which is exactly what he would send. Same guarantee, and it stops
   the rule taxing the person it protects. A comms deliverable is drafted in a ticket and assembled
   at the gate. See `peachy-build`.

## Stop conditions

**The primary stop condition is the materiality bar, not a clock.** Is this answered to the
resolution the deliverable actually needs? Would more precision change what the human does?
If not, it is done.

**There are no time gates in this method, on any ticket type, in any shape.** A session
cannot measure its own elapsed time, so a wall-clock budget fires at random and its only
effect is truncating good work partway. This was tested and it failed: a ticket carrying a
45-minute checkpoint reported it had spent "almost 20 minutes" when far less real time had
passed, and the full retrieval it was about to cut short cost 90 seconds and held the two
largest findings on the map. Do not reintroduce one, and do not soften this into an
advisory budget. See ADR-0007.

And three hard stop conditions that apply everywhere:

- **A well characterized range beats a false point estimate**, and it beats another two
  hours of hunting.
- **If resolving something would change the answer by a rounding error**, write
  `UNKNOWN, immaterial` and move.
- **Tangents get one line** in the outside-scope file, then you move. Do not chase, and do
  not draft outreach about it unless outreach was asked for.

---

## Where a project lives

**Default root: `~/Peachy/<Project Name>/`.** Any folder your Claude Code can open works; a
Google Drive for desktop folder is a good choice if you want the map readable from claude.ai too.

Resolution order:

1. **A folder for this project already exists under your projects root.** Use it, including
   when it sits under another subfolder.
2. **The project is already a repo.** The map can live in the repo instead. Say which, in the
   map's Notes, and never split the map across both.
3. **Neither.** Create `~/Peachy/<Project Name>/`.

Git: if the root is not already a repo, `git init` it and **add no remote**, because these
folders routinely hold confidential operational, financial and legal material. If the root is
already a repo with a remote, normal git rules apply and pushing is fine. Never move
confidential material into a folder that has a remote without asking first.

Commits are ticket-prefixed conventional commits with files staged by name. Never
`git add -A`.

---

## Feedback on the method itself

When the human pushes back on **how the method worked** (not on project content), append one
line, and only then:

```bash
printf '%s\n' "- [2026-08-10 . peachy-work] <what did not work, in their words or close to them>" >> <this kit folder>/FEEDBACK.md
```

Narrow on purpose. Method friction only: a gate that fired when it should not have, a rule
that got in the way, a step that was skipped because it was useless. **Not** project
findings, not corrections to content, not preferences already in `CLAUDE.md` or memory. If
you are unsure whether it qualifies, it does not.

**No long dashes in the line you append.** Use a comma, a colon or parentheses. This file exists
to be read months from now when the kit gets revised, so a handful of real entries is worth more
than a log.
