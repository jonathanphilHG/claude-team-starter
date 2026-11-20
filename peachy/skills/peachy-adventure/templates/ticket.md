# T<NN>: <what this ticket resolves, as a statement>

Type: **<research | grill | prototype | task | execute>** (<AFK | HITL>)
Depends on: **<none | T0N, T0M>**
Parent: **<none | T0N>** <!-- sub-tickets only -->
Run at: **<frontier | workhorse>, <effort>** <!-- A TIER, never a model name: the kit's models.md
holds the one table mapping tier to today's model, so no ticket goes stale on a release. The ticket
TYPE carries the default: research is frontier at xhigh, grill workhorse at xhigh, and bounded work
(task, prototype, a small execute batch) workhorse at high. Deviate freely, and say why on this line. -->
Changes in the deliverable: <!-- REQUIRED. The section it writes, the number it sets, the units it
changes, the decision it unblocks. If you cannot name one, this is not a ticket. -->
Human input: <!-- REQUIRED ON A TICKET A GATE SCOPED. One line naming the row he marked, the sentence
he said, or the decision from the last read. A gate may scope a round only from human input that
already exists and still applies; a ticket that cannot cite one is PROVISIONAL, stays off the
frontier, and waits on the Blocked line for his read. Implicit and omittable on a ticket written at
charting, because charting IS the human conversation. -->
Owns: `findings/T<NN>.md` <!-- plus any deliverable file or unit range this ticket exclusively owns -->

**Check your model before anything else.** This ticket runs at the tier on the `Run at:` line
above; the kit's `models.md` lineup table says which model that tier is today. Your system prompt
names the model you are running on. **If it is not that model, stop: write nothing, claim nothing,
and tell the human to relaunch this ticket at the stated setting.** A newer release of the same
family counts as a match. A session cannot
change its own model, so this check is the only guard there is, and it is worth nothing after the
claim line. Effort is often not visible to a session at all; check the model, which always is, and
record both at close in the findings file.

**Before you start:** read `MAP.md`, `PROCESS.md`, `HOTLINE.md`. Work it with `peachy-work`, or
`peachy-build` if the type is `execute`.

---

## Question

<!-- The one thing this resolves, stated sharply, then the specific list of what would answer it. A
question that needs a paragraph to state is two tickets.

For an execute ticket: what gets built or changed, and the acceptance test that says it worked. -->

<QUESTION>

---

## Why it matters

<!-- What downstream changes depending on the answer. Two or three sentences. This is what a session
reads when deciding whether to keep going or bound it and close. -->

<WHY>

---

## Where to look

<!-- The highest-value section. Name the actual surfaces: system, table, record ID, folder, portal,
person. Carried forward from SOURCES.md.

Name the traps you already know about. "This table has 5 records and is known to be incomplete; the
chart of accounts contradicts it; let the ledger win." That one sentence saves an hour and prevents
a wrong answer.

For an execute ticket: the pre-state to record, the dry run to show, the guard to use, and how to
verify afterwards. -->

<WHERE>

---

## Ticket types

<!-- Delete this block once the type is chosen. Kept so the template is self contained. -->

- **research (AFK):** reading documents, systems or third-party sources to establish a fact. Needs
  no human in the loop, so several run in parallel, each in its own session rather than as a
  subagent.
- **grill (HITL):** the answer is the human's to give. Taste, priority, risk appetite, a relationship
  they own. Never answer your own grill questions.
- **prototype (HITL):** something cheap and concrete to react to. An outline before the article,
  three sample rows before the table, the brief's headline before the analysis.
- **task (either):** manual work that must happen before something else can be established.
  Provisioning access, moving data so its shape is visible. Earns its place by unblocking.
- **execute (either):** builds a piece of the deliverable or changes live state. Batched by
  `peachy-build`. May spawn sub-tickets. Live-system writes need a dry run, approval on that batch, a
  guard, and verification after.

---

<!-- Everything below is written by the session that works this ticket. -->

Claimed:

## Resolution

<!-- If this ticket starts working again after it was closed, set Status back to
`open, reopened <date>, <why>` before touching anything, add the new work under
`## Addendum <date>` in the findings file, then re-close by UPDATING this Resolution rather than
replacing it. A closed ticket with live work in it tells other sessions it is takeable. -->

Status: open
