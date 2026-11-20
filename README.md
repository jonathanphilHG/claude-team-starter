# Claude team starter

A small kit of rules, templates, skills and short guides for working with Claude, put together
after a cross-company AI lunch and learn on 2026-11-20. Take one piece or all of it: each piece
works on its own. Everything is plain text you can open, read and change.

**A dated snapshot (2026-11-20), not maintained.** Nothing here updates itself and nobody is
keeping it current. Fork it or copy it, then change anything you like.

Two kinds of Claude come up below:

- **claude.ai**: the Claude chat you use on the web, the desktop app or your phone.
- **Claude Code**: Claude that works directly with files and folders on your computer.

Each piece says which one it works in.

**Only use claude.ai? Start with these:** the three rules files
([writing for people](rules/writing-for-people.md), [research and claims](rules/research-and-claims.md),
[scope and review](rules/scope-and-review.md)), the [house rules template](rules/house-rules-template.md),
the [voice file](templates/VOICE.md), and two templates: the [shared doc](templates/shared-doc-two-tabs.md)
and the [relationship file](templates/relationship-file/README.md).

---

## Make Claude's writing shorter and more like me

- **[Writing for people](rules/writing-for-people.md)** (claude.ai and Claude Code)
  A short set of standing rules for anything another person will read.
  Why: messages come out answer-first and short, and drafts are ready to send as written.
  **A good place to start.**

- **[Your voice file](templates/VOICE.md)** (claude.ai and Claude Code)
  A template that teaches Claude how you write, one real correction at a time, per audience.
  Why: after a dozen corrections, drafts sound like you instead of like Claude.

- **[Shared doc with two tabs](templates/shared-doc-two-tabs.md)** (claude.ai and Claude Code)
  A layout for a shared document: a short "Now" tab for people, a "Reference" tab for Claude.
  Why: your colleague gets four lines; their Claude still gets all the evidence.

## Trust research more

- **[Research and claims](rules/research-and-claims.md)** (claude.ai and Claude Code)
  Standing rules that make Claude label where each fact came from and say where it looked.
  Why: you can check a source in seconds, and "not found" stops turning into "does not exist".
  **A good place to start.**

## Keep work small and finished

- **[Scope and review](rules/scope-and-review.md)** (claude.ai and Claude Code)
  Rules for doing the smallest thing that works and capping review rounds up front.
  Why: Claude will happily plan and review forever; this makes it ship.

- **[House rules template](rules/house-rules-template.md)** (claude.ai and Claude Code)
  A starter set of standing instructions: voice, scope, safety, and a few habits.
  Why: a starting point you edit, instead of a blank page.

- **[Lessons](guides/lessons.md)** (claude.ai and Claude Code)
  Twenty-odd lessons from running Claude on real work every day.
  Why: each one cost someone a bad afternoon. Take the ones that fit.

## Stop redoing the same browser task

- **[Web app to API skill](skills/web-app-to-api-reference/SKILL.md)** (Claude Code)
  A skill that turns a task you do by clicking in a web app into a repeatable script, safely.
  Why: the task stops being manual and flaky, and the next run does not start from scratch.

- **[Map a web app, the long version](guides/map-a-web-app.md)** (worth reading anywhere; the work needs Claude Code)
  The full method behind that skill, with the reasons for each step.
  Why: read it once to understand what the skill is doing and why it is careful.

## Keep track of customers, vendors and deals

- **[Relationship file](templates/relationship-file/README.md)** (claude.ai and Claude Code)
  One folder per customer, vendor or deal: a status page where every fact has a source, and a log.
  Why: anyone (or any Claude) can pick it up cold and know where things stand.

- **[Memory as files](templates/memory-index.md)** (best in Claude Code)
  A way to give Claude a memory you can read and fix: small notes plus a one-line index.
  Why: corrections stick, and you can see exactly what Claude "remembers".

## Run a project too big for one chat

- **[Big projects](guides/big-projects.md)** and the **[Peachy Adventure kit](peachy/README.md)** (Claude Code)
  A method for work that spans many sessions: a map, small tickets, and a step that merges results.
  Why: long projects stop losing detail between chats, and research stops going down rabbit holes.

## Work by voice

- **[Voice while driving](guides/voice-while-driving.md)** (a voice Claude on your phone, plus a working session in Claude Code)
  Talk to Claude on your phone while other Claude sessions keep working, through two shared docs.
  Why: work keeps moving when you cannot look at a screen.

## Get more out of Claude Code

- **[Claude Code basics](guides/basics.md)** (Claude Code)
  How it works under the hood: instructions, skills, permission modes, settings worth knowing.
  Why: you tune it instead of fighting it.

- **Everyday skills** (Claude Code)
  Six small skills, each a single page you can read first:
  [commit](skills/commit/SKILL.md) (careful commits),
  [push](skills/push/SKILL.md) (checked pushes and pull requests),
  [grill-with-docs](skills/grill-with-docs/SKILL.md) (stress-tests a plan against real documentation),
  [right-plan](skills/right-plan/SKILL.md) (slices a big change into small safe steps),
  [gather-context](skills/gather-context/SKILL.md) (researches a codebase before work starts),
  [thermo-review](skills/thermo-review/SKILL.md) (a strict code-quality review).
  Why: good habits that run themselves. Most people keep two or three.

- **[Seatbelt hook](hooks/README.md)** (Claude Code, optional)
  A small guard that stops Claude from running a handful of destructive commands.
  Why: it works even when you have told Claude to stop asking permission.

- **[Keep your skills in GitHub](guides/skills-in-github.md)** (mostly Claude Code)
  Why to keep skills in a repository, and how.
  Why: every change is kept, a new laptop is one download, and sharing is a link.

- **[Public skills worth knowing](guides/public-installs.md)** (mostly Claude Code)
  A short list of skills other people publish, including the popular "grilling" skill.
  Why: get them from their source, always current.

## What came up on the call

- **[Notes from the call](guides/notes-from-the-call.md)** (read anywhere)
  What came up at the lunch and learn: which ideas have a piece here, and which do not.
  Why: a few of the best ideas on the call were other people's, and they are worth trying.

---

## Getting started

Open **[START-HERE.md](START-HERE.md)** and paste its prompt into your own Claude. It asks which
pieces you want and sets up only those, showing you any change before it makes it.

If you share your own copy of this kit later, have your Claude run the leak check described in
[FOR-CLAUDE.md](FOR-CLAUDE.md) first. Put the names you never want to ship in `.private-blocklist`,
which is never committed.
