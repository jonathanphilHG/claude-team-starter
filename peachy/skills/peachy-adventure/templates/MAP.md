# MAP: <project name>

The low-resolution view of the whole project. Every session loads it once, orients, then works its
ticket. It is an **index, not a store**: detail lives in the ticket or its findings file, never
here.

Read `PROCESS.md` before writing anything. **Only a gate session writes this file.**

---

## Destination

<!-- One or two lines, from MISSION.md, including what done means. Every session orients to it
before choosing a ticket. -->

<DESTINATION>

**Shape: <SHAPE>.** Materiality bar: <ONE LINE, from MISSION.md>.

---

## Frontier

<!-- The open, unblocked, unclaimed tickets, in order. Maintained by the gate. A tracker would
render this automatically; files do not, so if this list is stale nobody can see what is takeable.

A session told only "work the map" takes the first one in order, so a parallel launch must name
its tickets explicitly. -->

1.

**Blocked:** <ticket, waiting on which>
**Claimed and in flight:** <ticket, since when>

<!-- A PROVISIONAL ticket belongs on the Blocked line, waiting on the human's read, never in the
frontier above. That is a ticket a gate scoped without being able to cite the human input behind it,
and keeping it off the frontier is what stops it being launched before he has seen it. -->

---

## Notes

**This map plans and executes.** Establishing tickets (`research`, `grill`, `prototype`, `task`)
are worked one per session by `peachy-work`. Execution tickets (`execute`) are batched by
`peachy-build`, may spawn sub-tickets, and gate every live-system write behind a dry run and
approval. Execution can happen in pieces as the map clears or in larger sessions later.

**Nothing blocks the deliverable.** An unresolved item converts to the bounded form this shape
calls for and the work proceeds. No ticket waits on a document.

**The asking rule.** No cap on questions, and no instruction to run silently. Ask when the branches
would change what the human does or what the deliverable says at the headline level; otherwise
decide, note the pick under Decided below the bar, and move. Never ask what the sources can answer.

**Standing rules from `MISSION.md`:**

<!-- The rule pack, written out. Are tiers on. What the bounded form is. Whether the write protocol
is required. Which guard to enforce hardest. -->

-

**Anti-sprawl rules for this map:**

- **12 open tickets is a bar, not a wall.** Past it, one line here saying why this map needs more.
  Do not under-decompose to stay under the number.
- **A ticket must name what it changes in the deliverable.** If it can name nothing, it is not a
  ticket; write it in your findings file.
- **Discovered questions do not become tickets by default.** Only a gate promotes one, against the
  materiality bar. He will pull something forward if it was missed, and that is cheaper than
  carrying speculative tickets.
- **Sub-tickets only from `peachy-build`, and only inside the parent's scope.**
- The test at every decision point: **would knowing this change what <PERSON> does?**

**Session settings:** <!-- tier and effort per session type (for example "research: frontier,
xhigh; execute: workhorse, high; the post-gate harvest: frontier, xhigh"), so whoever starts one sets them before pasting the prompt. Tiers,
never model names: the kit's models.md maps tier to today's model. -->

---

## <Findings so far | Decisions so far | Sections done | Units done | Threads>

<!-- Rename this heading to match the shape, per the rule pack. The index: one line per closed
ticket, enough to judge relevance, then open the link for the detail. Never restate the detail.
Grouped by round.

For a rollout this is the unit tally plus a link to the unit list, not one line per unit. -->

### Round 1

- [T01 <title>](findings/T01.md) <one-line gist>

---

## Not yet specified

<!-- In-scope fog: questions you can tell are coming but cannot yet phrase sharply. Write as
loosely as the view allows; it doubles as a signpost for where the effort is headed.

The test for moving something out of here is whether you can state the question precisely now,
NOT whether you can answer it. Do not pre-slice fog into ticket-sized pieces.

Excludes what is already decided, already a live ticket, or out of scope. -->

-

---

## Out of scope

<!-- Work consciously ruled beyond this destination. Scope, not sharpness, lands it here, and it
never graduates: the frontier stops at the destination. Redrawing the destination is a fresh
project, not a resumption.

One line each: the gist, plus why it is out, linking the closed ticket if there was one. -->

-
