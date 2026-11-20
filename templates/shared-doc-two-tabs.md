# Shared doc with two tabs: "Now" for people, "Reference" for Claude

A pattern for any document that both a person and a Claude read: a running doc with a
colleague, a vendor, a project partner.

## The problem it solves

Your colleague needs four lines. Their Claude (and yours) needs everything: the evidence, the
history, the reasons. One document that tries to serve both ends up too long for the person and
too thin for Claude.

## The pattern

Two tabs (or two clearly separated sections, if your editor has no tabs).

**Tab 1: Now** (for people)

- Opens with a one-sentence headline: where things stand.
- Then one line per action, grouped by when (this week, next week, later).
- Each line: owner first, the action, date last.
- Nothing else. No history, no evidence, no "as discussed".

**Tab 2: Reference** (for Claude, and for anyone who wants the detail)

- The evidence behind each line in Now, with sources and dates.
- History, decisions and their reasons, newest first.
- Open questions and what would settle them.

When something changes, update Reference first, then rewrite the affected line in Now.

## Skeleton

Copy this into a new document.

```
NOW

<One sentence: where things stand.>

This week
- <Owner>: <action>. <date>
- <Owner>: <action>. <date>

Next week
- <Owner>: <action>. <date>

Later
- <Owner>: <action>. <date>


REFERENCE

Evidence
- <Line from Now>: <source, date read, link>

Decisions (newest first)
- <YYYY-MM-DD>: <decision>. Why: <reason>.

History (newest first)
- <YYYY-MM-DD>: <what happened>.

Open questions
- <question>: <who is finding out, what would settle it>.
```

## Telling Claude to keep it this way

Add a line to your instructions: "In a shared doc, the Now tab is one headline and one line per
action (owner first, date last). Everything else goes in Reference."
