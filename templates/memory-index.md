# Memory as files: one fact per file, one index

A pattern for giving Claude a memory you can read, edit and fix: small note files, plus a
one-line-per-note index that Claude reads at the start of every session.

## Why

- A long instructions file gets skimmed. A short index that points at small notes stays
  readable, and Claude opens a note only when it is relevant.
- When Claude gets something wrong, you fix one small file, and the reason is kept with it.
- It is plain text, so you can see exactly what Claude "remembers" and delete what is stale.

## Where it works

- Claude Code: keep a `memory/` folder (inside a project, or one for you), and tell Claude in
  your `CLAUDE.md`: "Read memory/MEMORY.md at the start of every session. Save new notes there
  when I correct you." Claude can then write notes as you go.
- claude.ai: Claude cannot write files for you there, so you keep the index and notes yourself
  and add them to a project as files.

## The index: `MEMORY.md`

One short line per note. It loads every session, so keep it lean.

```
# Memory index
One line per note. A star means: read the note before acting on this topic.

- * [Vendor emails](vendor_emails.md): warm first line, ask in sentence two, Cc my manager
- [Report format](report_format.md): totals first, one table, no charts
- [Main supplier](supplier_main.md): contact, account number lives in the password manager
```

Conventions that help:

- A marker (here a star) for "read the note before acting", so Claude knows which ones matter.
- When the index grows past what fits comfortably, move dormant topics to a second index file
  that is read only when needed.

## A note file

One topic per file. The rule first, then why, then how to apply it.

```
---
name: vendor_emails
description: How I want first emails to outside vendors written
type: feedback
---

Warm first line, the ask in the second sentence, Cc my manager on anything with a price.

**Why:** a vendor ignored a cold one-line ask (2026-11-04). My manager needs to see pricing.
**How to apply:** any first email to a new vendor. Not replies inside an existing thread.

- 2026-11-18 correction: "Cc my manager only when there is a price, not on every email."
```

## Corrections

When a note turns out wrong, do not just overwrite it. Add a dated line with what changed and
why, as in the last line above. The reason is what stops the same mistake coming back.
