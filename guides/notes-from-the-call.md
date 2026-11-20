# Notes from the call (2026-11-20)

A short record of what came up at the AI lunch and learn, without names. For each idea: where
this kit has something for it, or a note that it does not.

## Ideas this kit has a piece for

| What came up | In this kit |
|---|---|
| Long Claude output forwarded to colleagues, leaving the reader to do the thinking | [Writing for people](../rules/writing-for-people.md) |
| A personal voice so drafts sound like you, with a different register per audience | [Voice file template](../templates/VOICE.md) |
| Telling Claude to slow down, research first and say which sources it read; a confidence label on research | [Research and claims](../rules/research-and-claims.md) |
| A skill that red-teams a plan or document before it goes out | [grill-with-docs](../skills/grill-with-docs/SKILL.md), and the public "grilling" skill in [Public skills worth knowing](public-installs.md) |
| One running file per customer that anyone, or anyone's Claude, can pick up | [Relationship file](../templates/relationship-file/README.md) and the [two-tab shared doc](../templates/shared-doc-two-tabs.md) |
| A browser task that works one day and not the next; turning it into a skill | [Web app to API skill](../skills/web-app-to-api-reference/SKILL.md) |
| Writing down how a task worked after one clean run, so the next run does not relearn it | Step 7 of [Map a web app](map-a-web-app.md), and [Memory as files](../templates/memory-index.md) |
| Working by voice while driving | [Voice while driving](voice-while-driving.md) |
| Keeping skills in GitHub so a file cleanup does not lose them | [Keep your skills in GitHub](skills-in-github.md) |
| A list of the skills people actually use | [Public skills worth knowing](public-installs.md) |

## Ideas worth trying that are not in this kit

These came from other people on the call. If one interests you, ask the person who described it.

- **Three levels of automation.** Claude clicking in a browser is fine for a one-off, but it is
  slow, costs a lot of usage and gets unreliable at volume. For anything you repeat, have Claude
  write a script and keep it in a skill, so running it costs almost nothing. For a process the
  business depends on, ask engineering for a proper connection. The web app skill in this kit is
  the second level.
- **An assistant that runs on a schedule.** An hourly or morning run that reads email, meeting
  notes and chat, drafts replies for review, updates a to-do board, and suggests one new idea a
  day. Nothing sends without a person's review.
- **Edits that feed back into skills.** Every time you correct a draft, the correction updates the
  skill that wrote it. The voice file template in this kit is the by-hand version of that.
- **A customer file that refreshes itself nightly**, with a section per business function, and a
  flag when a document changed in a way no meeting discussed.
- **A voice skill that proposes its own update each evening**, seeded by recording spoken answers
  to thirty questions about the company.
- **Several named skills run against one problem**, each with a different point of view, then a
  neutral pass that weighs them.
- **A brand system kept in a skill**, built up over time from logos, colours and corrected drafts,
  so every deck and document uses the current brand.
- **A cheap always-on computer at home** as the place Claude runs, so the laptop does not have to
  stay open.
- **Claude in the browser for chores**: updating the same details across many pages, or working
  through an awkward website by reading its help pages first. Kept away from bank accounts and
  anything critical.
- **A vocabulary checker while you write**: a list of words and topics you may not use, checked as
  you draft.
