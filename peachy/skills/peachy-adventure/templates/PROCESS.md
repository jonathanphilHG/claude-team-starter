# PROCESS: how parallel sessions share this folder without colliding

Read this before writing anything. It is short on purpose.

---

## The one rule

**A working session writes only files it exclusively owns. It never edits a shared file.** Merging
into shared files happens in a single sequential gate session.

That is the whole collision-avoidance design. No locking, no claim protocol on shared files, and no
lost-update race, because no two sessions ever write the same file.

---

## Who owns what

| Path | Written by | Notes |
|---|---|---|
| `findings/T<NN>.md` | ticket T\<NN\> only | Everything you find. The pre-merge record. |
| `tickets/T<NN>-*.md` | ticket T\<NN\> only | Your `Claimed:` line, then `## Resolution` and `Status: closed`. |
| `tickets/T<NN><a,b,c>-*.md` | the `peachy-build` session working T\<NN\> | Sub-tickets, and only inside the parent's scope. |
| `source-docs/<new file>` | any session | Adding a file is collision free. Never overwrite an existing one. |
| the unit list | the `peachy-build` batch that owns those units | Rollouts only. Per-unit status. |
| `HOTLINE.md` | any session, **append only** | Cross-ticket flags. `printf ... >>` only, never Write and never Edit. |
| `SESSIONS.md` | any session, **append only** | Who is live and how to reach them. Same `printf ... >>` discipline. Charting writes the `ORCHESTRATOR` line. |
| `MAP.md` | gate sessions only | Index, frontier, fog, scope. |
| canonical outputs: `facts.md`, `parameters.md`, `contradictions.md`, `open-questions.md`, `SOURCES.md`, `dead-ends.md`, `outside-scope.md` | gate sessions only | Produced at a gate by merging every findings file. They do not exist until then. Deliberate. |
| the deliverable | <!-- name the one ticket that owns it; note that ownership transfers when that ticket closes --> | |
| `MISSION.md` | gate sessions only, **and only with the human's explicit ratification** | Stable, not frozen. A working session never edits it: send the correction to the Hotline or your findings file. Every amendment is dated under `## Amendments`. |

**If you want to edit a file you do not own, you want the Hotline or your own findings file
instead.** New questions and new sources go under their headings in your findings file, and the
merge folds them in.

---

## Claiming

Append one line to the ticket file, **before any work**:

```
Claimed: 2026-08-10 14:20
```

**Every time you write on this map comes from `date`, never from an estimate**: the `Claimed:` line,
`SESSIONS.md` and `HOTLINE.md`. The `printf` examples below substitute it. Sessions that copied the
times on neighbouring lines ran over an hour fast, and these are the lines whose ordering is the
concurrency evidence.

There is no tracker assignee here, so that line is the entire concurrency guard. An open ticket with
no claim line is takeable.

**Then register in `SESSIONS.md`, on the next line, still before any work.** The claim line says the
ticket is taken; the registry line says who took it and how to reach them. They are one step, not
two:

```bash
printf '%s\n' "- [T05 . $(date '+%Y-%m-%d %H:%M')] uds:/tmp/cc-socks/71346.sock . claimed" >> SESSIONS.md
```

`SESSIONS.md` carries the snippet that derives your own socket path, because no tool will tell you
your own address.

Two things to know when several sessions run at once:

- **A session told only "work the map" takes the first frontier ticket in order.** A parallel launch
  must name its tickets explicitly, or two sessions grab the same one.
- **The claim line cannot say which session claimed it**, only that it is taken. That is enough.

---

## The Hotline

For the mid-flight case: something another **live** session needs now, not at the gate. Append only,
one line, never Write and never Edit:

```bash
printf '%s\n' "- [T04 . $(date '+%Y-%m-%d %H:%M')] The orders table has 20 records, not 10. T03: the total may cover more orders than assumed." >> HOTLINE.md
```

Format: `- [<ticket> . <date time>] <what you found> <which ticket needs it>`

Read it when you start and again before you close. A reply to another entry is often the most
valuable line in the file. Two or three entries per round is healthy; twenty means the ticket
boundaries were drawn wrong, and that is itself worth flagging.

Findings do not go here. They go in your findings file and reach everyone at the gate.

---

## The relay

The Hotline is a file, so it only reaches a session that is still running and still reading it. Two
cases it cannot cover: **a session that has already closed** telling a live sibling something, and a
finding a sibling needs **before** its next read of the file.

For those, message the orchestrating session directly. **Read the `ORCHESTRATOR` line in
`SESSIONS.md` and use that socket path as your `SendMessage` `to`.**

**Do not use `ListAgents` for this.** It lists every Claude session on the machine, including
sessions working other projects, and it does not list self, so it can tell you neither your own
address nor which of its entries belong to this map. Both failures are real: a whole round of
relays was lost to the second, and a broadcast built on the first reached three sessions on an
unrelated project. `SESSIONS.md` exists because the tool cannot answer either question.

- **Write the file first, then message.** The Hotline line or your findings file is the durable
  record; the message only points at it. State lives in files, and a finding that exists solely in a
  chat never reaches the gate.
- **Message the orchestrator, never a sibling.** You do not know which siblings are live or what
  they are holding. The orchestrator does, and fans out. Session-to-session messaging is a mesh that
  produces cross-talk.
- **Two triggers, and only these two.** On close, a two-line result. Mid-ticket, immediately, when
  you find something that invalidates another ticket's premise. Not "I have started," not progress.
- **Never block a close on delivering a message.** If no orchestrator is reachable, which happens
  whenever the launching session has exited or the work is running headless, the Hotline plus your
  findings file is the whole channel and that is a complete close, not a degraded one.
- **Your words travel, not a summary of them.** The orchestrator routes what you relay and quotes
  it; it does not restate it. So write the relay the way you want it read downstream: the claim, its
  tier, and the surface you measured it on. **If it is single-source and unverified, say so in the
  line.** That is what decides whether it reaches the human now or waits for the gate, and an
  unverified claim that arrives sounding settled is how a false alarm gets acted on.

---

## Closing a ticket

1. **Re-read what the gate owns first**: `MAP.md`, `MISSION.md`, and any canonical output file your
   ticket touches. A gate may have amended one since you started, and nothing refreshes your beliefs
   about those files on their own. This is the mirror of the artifact check you ran at the start:
   that one stops you working from a stale premise, this one stops you writing one into the record.
   Then the findings file, every heading present even if empty. Write "None." rather than deleting.
2. Append to the ticket file:
   ```
   ## Resolution

   <three to six lines: what you established or changed, what you bounded, what you could not get
   and why. Link your findings file.>

   Status: closed
   ```
3. Commit, ticket-prefixed, staging files **by name**:
   ```bash
   git add findings/T04.md tickets/T04-*.md
   git commit -m "T04: <what it established>"
   ```
   Never `git add -A`.
4. Append your `. closed` line to `SESSIONS.md`, then relay the result to the orchestrating session,
   two lines. See the relay section above.

**If a closed ticket starts working again, it is open.** Set `Status: open, reopened <date>, <why>`
before you touch anything, put the new work under `## Addendum <date>` in the same findings file,
and re-close by updating the Resolution rather than replacing it. `Status` is what tells another
session whether a ticket is takeable, so a closed ticket with live work in it is a concurrency bug,
not only an untidy record. The test: **if a unit row or a deliverable says in flight, the ticket
cannot say closed.**

You do **not** touch `MAP.md`. The gate does that.

---

## Git

<!-- Charting fills this in. Two cases: -->

**If this folder was created for the project:** it is a **local-only** repository. It exists so a
bad concurrent write is recoverable and so findings carry attribution. **No remote**, because
folders like this routinely hold confidential operational, financial and legal material.

**If the project already lives in a repo with a remote:** normal git rules apply, including pushing.
Do not move confidential material into it without asking first.

---

## Stop conditions, which are not optional

- **Stop on materiality, not a clock.** Answered to the resolution the deliverable needs is done.
  There are no time gates on any ticket in this method. A session cannot measure its own elapsed
  time, so a wall-clock budget only ever truncates good work at random.
- **If resolving something would change the answer by a rounding error**, write
  `UNKNOWN, immaterial` and move.
- **Do not rabbit-hole on interesting-but-irrelevant findings.** One line under Outside scope, then
  move.
