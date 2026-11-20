# MISSION

<!-- The stable document in the folder. When a session feels lost or notices drift, it comes back
here to realign.

STABLE IS NOT FROZEN. On a long project this file will need to change, and that is expected. The
rule is about WHO and WHEN, not never:

- A WORKING SESSION NEVER EDITS THIS FILE. Not a correction, not a typo. Put it in your findings
  file or the Hotline and the gate folds it in.
- A GATE MAY AMEND IT, and only with the human's explicit ratification: the orchestrator proposes
  and says what prompted it, the human ratifies, then the gate writes it.
- EVERY AMENDMENT IS LOGGED, dated, one line, under ## Amendments at the bottom of this file. -->

## What this is

<!-- Who this is for, what the project is, and the plainest possible statement of the question.
Two or three paragraphs. -->

<WHAT>

## The decision this serves

<!-- The single most important section. What will someone DO differently because of this work?
Name the decision, who makes it, and roughly when. A project that serves no decision is a reading
project and it has no end. -->

<DECISION>

## What this is NOT

<!-- Explicit, because scope creeps in through unstated framings more than through new tickets.
Name the adjacent projects this will be mistaken for. -->

<NOT>

## Destination

<!-- What reaching the end looks like, concretely enough to test. "Done means: X exists, it does
Y, and every number in it is either sourced or a bounded parameter." -->

<DESTINATION>

## Shape

<!-- One of the five: investigation, decision, knowledge artifact, operational rollout, program
spine. Name the dominant one and any secondary. The shape decides which disciplines are on, so
getting it wrong misconfigures everything downstream. -->

**Shape: <SHAPE>.** Secondary: <SECONDARY or none>.

<!-- Then write out the rule pack as plain sentences, so a later session can follow it without
reading the skill. Cover: are evidence tiers on, what an unresolved item converts into, is the
write protocol required, what the map's index section is called, and which guard to enforce
hardest. -->

<RULE PACK>

---

## Operating rules

### The asking rule

There is no cap on questions and no instruction to run silently. One test governs every one:

> Would the branches change what the human actually does, or what the deliverable says at the
> headline level?
>
> **Yes:** ask now, immediately, even mid-ticket. **No:** decide it, write the pick and a
> one-line reason in your findings file under Decided below the bar, and move.

Never ask what the sources can answer. Every question ships with your recommended answer so
"yes" is a complete reply. Never ask permission to continue.

### Evidence tiering

<!-- Keep this block if the shape has tiers on; delete it if not. -->

Every factual claim carries a tier A through E and a citation, per the kit's `evidence-tiers.md`.
`UNKNOWN` is an acceptable answer. A confident wrong number is not.

### Confidence downgrade

A prior claim you check and cannot reproduce drops to `UNKNOWN` and goes in Contradictions. Never
agree with earlier work silently.

### Nothing blocks the deliverable

An unresolved item converts to the bounded form this shape calls for, and the work proceeds. No
ticket is ever left open waiting for a document.

### Contradictions are findings

Two sources disagreeing gets recorded with both citations, not smoothed over.

### Writes to live systems

<!-- Keep and sharpen this for a rollout; keep the first line regardless. -->

Read only by default. A write needs a dry run showing exactly what would change, explicit
approval on that specific batch, a mechanical guard where the tool supports one, and verification
by re-reading the target afterwards. Some things a human presses: account and billing settings,
anything that spends money, anything touching a person's access.

<!-- STANDING APPROVAL. Delete this whole block unless the human has actually granted it. It is
granted by him and never assumed, never inferred from a run of approvals, and never granted by a
session to itself. Granted mid-project it is an amendment, written by a gate after he ratifies it.
Record the date and his words. See the standing approval section in `peachy-build`. -->

**Standing approval, with a stop list.** Granted by <who> at <charting | Gate N>, <date>.
Extent: **<this round | tickets T0N and T0M | the whole project>**.

Running on standing approval, no per-batch wait:

- <named system, named operations>

**STOP LIST, needing his explicit yes on that specific action:**

- Anything sent to a customer, a vendor or any other person. Communications are drafted, never sent.
- Anything that moves money, or that changes someone's access.
- <deleting a record, rows outside <scope>, the irreversible thing this project can reach>

A dry run still gets posted before a batch. It just does not block. The pre-state, the guard, the
sequential order and the verification by re-read all still run on every write: **standing approval
removes the wait, not the record.**

It covers the approval gate only. A worker still does not write `MAP.md`, `MISSION.md` or any
canonical output, and the orchestrator still does not execute.

### Communications are drafted, never sent

Separate from the rule above and the same weight, because it is the only one that cannot be undone.
**No communication templated up on this map is ever sent without explicit approval on that specific
message.** Draft it completely and hand it over. Every comms draft carries **the premise it rests
on**, one line, naming the fact the message would be wrong without, **in the handover or the relay
and not in the draft body**: the body is exactly what he would send. A comms deliverable is drafted
in a ticket and assembled at the gate. A comms draft is never done at a gate, only ready for a human
to read.

### Do not draft outreach

<!-- Keep where the human owns the relationships; drop otherwise. -->

Where something can only be obtained by asking a person, log who has it and move on.

### Scope discipline on tangents

You will find unrelated problems. One line in `outside-scope.md`, then keep moving.

### Access

<!-- State plainly what this project may read and what it must not touch. Be explicit about which
systems are read-only and which are writable. -->

<ACCESS>

---

## Definition of done

**This does not need to be perfect. It needs to be good enough to act on.**

- A well characterized bounded form beats a falsely precise answer.
- Stop when the marginal finding stops moving the answer.
- Do not gold-plate. Correct in structure and honest about uncertainty is the bar.
- **There are no time gates on this project**, on any ticket, in any shape. A session cannot
  measure its own elapsed time, so a wall-clock budget fires at random and only ever truncates work
  that was about to pay. Stop on materiality. See ADR-0007.

**The materiality bar for this project:**

<!-- REQUIRED, and it must come from the human in their own words. State it numerically or
concretely: "would move the headline number more than 10%", "would change whether I sign", "would
change which accounts get done this month". This is the test every later session and every gate
applies, so a vague bar makes every guard vague. -->

<MATERIALITY>

**The test at every decision point: would knowing this change what <PERSON> does?** If not, it is not
worth another hour.

---

## Gates

<!-- How many, and what each is for. Three is the recommendation, not a ceiling: if this project
needs more, say why in one line here. Note that any session may call one early if it finds something
that changes the shape of the problem.

These are the PLANNED gates, and they are not the only ones that may run. A gate may also fire
because the record has DRIFTED, which is unplanned by definition: the canonical files have fallen
behind work that already landed and anyone reading them would be reading something false. That does
not need to be listed here in advance.

Gates run AUTOMATICALLY when a round's last ticket closes, stopping only for a MISSION amendment, a
fork that passes the asking rule, or a ticket with no human input to cite. That is the default and
needs nothing here. Only if he wants this map's gates to wait for him, add one line under GATES:
**Gates wait for his go.** -->

<GATES>

---

## Required outputs

<!-- Shape-dependent. Investigations want facts / parameters / contradictions / open-questions /
dead-ends. Rollouts want the unit list and the exception list. Artifacts want the artifact and a
review log. Always name the deliverable itself and where it finally lands. -->

| File | Purpose |
|---|---|
| | |

**Only a gate session writes these.** They do not exist until the first gate. See `PROCESS.md`.

---

## Known errors in prior work

<!-- If any prior session, document, or person's summary is an input here, list what is known or
suspected to be wrong in it, plainly, so it gets challenged rather than inherited. This has
repeatedly been the most valuable section in the file. Delete the heading if there genuinely is no
prior work. -->

<PRIOR>

---

## Amendments

<!-- One line per amendment, appended, newest last: the date, what changed, and what prompted it.
Only a gate writes here, and only after the human has ratified the change. An empty list is normal
on a short project. -->

- <date>: <what changed, and what prompted it>
