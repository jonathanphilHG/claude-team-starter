# Rule: anything another person will read

A short block of standing instructions that makes Claude write messages people actually read.

## Why

- Claude writes long by default. Teammates stop reading long messages, and the one line that
  mattered gets lost.
- The sender should do the thinking. If the reader has to work out what you meant, the message
  failed, however accurate it was.
- A draft that mixes notes to you with the message gets sent with the notes still in it.
- When a group started forwarding long Claude replies to each other, the complaint was never
  accuracy. It was length and volume. This rule is the fix.

## Where it goes

- Claude Code: paste it into your `CLAUDE.md` (the user-wide one applies everywhere).
- claude.ai: paste it into a project's instructions, or into your personal preferences.

## The block

Copy everything between the lines.

---

```
## Anything another person will read
Messages, email, texts, shared docs.

- Do the thinking before it goes out. The reader should never have to work out what I meant.
- Answer first. A message is one to three sentences. Detail goes behind a link (a doc, a sheet, a task).
- A draft is exactly what I would send. Notes to me (assumptions, "check X first") go beside the
  draft, not in it.
- Shorter than feels right. If it needs headers, it is a doc, not a message.
- A shared doc opens with a one-sentence headline and one line per action: owner first, date last.
  Evidence and history go in a separate section or tab.
- Conclusions, not process: no research files, ticket numbers or "Claude found" in anything a
  teammate reads.
- One post per topic or per person beats a reply in every thread.
- Nothing sends without my go on that exact text.
```

---

## Optional extra line

If you keep a voice file (see `templates/VOICE.md`), add this under the heading:

```
Before drafting any of these, read VOICE.md and use the section for that audience.
```
