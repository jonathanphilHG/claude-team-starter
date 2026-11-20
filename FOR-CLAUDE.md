# For Claude: installing pieces of this kit

This file is for the person's Claude. `README.md` is the person's menu; this file is how to set
up what they pick. The kit is a dated snapshot (2026-11-20) with no maintainer.

## How to run the install

1. Work out the setup:
   - **Claude Code**: you can read and write files on the person's computer.
   - **claude.ai chat** (web, desktop or phone app): you cannot write to their computer or
     change their settings. You give them exact text to paste and tell them what to do.
   If unsure, ask.
2. Show the menu from `README.md` as a short plain list, grouped by the README's sections, in
   at most 12 lines (piece, one line, where it works).
   Recommend starting with the two rules files: `rules/writing-for-people.md` and
   `rules/research-and-claims.md`. Ask which pieces they want.
3. Install only the pieces they named, plus any file dependency listed in the manifest below
   (say that you are adding it and why). Software a piece needs (Python 3, Chrome, git, bash) you
   only check, for example `python3 --version`. Never install software; tell the person what is
   missing and let them decide.
4. Report what was set up, where, and one thing to try first. In Claude Code, tell them to start
   a fresh session so new rules and skills load.

## Rules for the install

- **Existing instructions files:** before adding to or changing an existing `CLAUDE.md`, project
  instructions or personal preferences, show the exact text you will add or change and wait for
  a yes. Append the fenced block as it is (its first line is its heading). If the same block is
  already there word for word, say so and skip it. If a section with the same heading exists but
  the text differs, show both and ask which to keep.
- **Never overwrite** an existing file, skill folder or setting without asking. If a skill folder
  with the same name exists, stop and ask.
- **The hook is optional and Claude Code only.** Before setting it up, explain in two or three
  sentences what it blocks and that it is turned on in the user settings file. Set it up only on
  a clear yes, following `hooks/README.md` (test first, then wire).
- **Do not invent claude.ai menus.** In claude.ai, rules go into project instructions or personal
  preferences; templates are files the person copies; a skill folder can be added as a custom
  skill if their plan has that. Do not name menu paths or settings you have not seen.
- Never print secrets, and never ask the person for a password or token.
- Keep it OS-neutral. Paths below are given for macOS or Linux and for Windows.

## Where things go in Claude Code

| What | macOS or Linux | Windows |
|---|---|---|
| User instructions (all sessions) | `~/.claude/CLAUDE.md` | `%USERPROFILE%\.claude\CLAUDE.md` |
| User skills (one folder per skill) | `~/.claude/skills/<name>/` | `%USERPROFILE%\.claude\skills\<name>\` |
| User settings (for the hook) | `~/.claude/settings.json` | `%USERPROFILE%\.claude\settings.json` |

- **Rules:** append the block inside the rules file (the fenced part) to the user `CLAUDE.md`.
  Create the file if it does not exist. The "Why" text in the rules files is for the person, not
  for `CLAUDE.md`.
- **House rules template:** if no user `CLAUDE.md` exists, write the fenced template there and
  remind them the Voice section is personal taste. If one exists, merge section by section with
  their approval.
- **Skills:** copy the skill folder into the user skills folder, keeping the folder name (it
  must match the `name:` line in its `SKILL.md`). Linking instead of copying is fine on macOS or
  Linux if the person keeps the kit in a stable place (see `guides/skills-in-github.md`).
  Exception: always copy `web-app-to-api-reference`, never link it. It writes the person's own
  app notes into its folder, and a linked copy would put them inside a kit they may share later.
- **Templates:** copy them where the person keeps that kind of work, and fill in the
  placeholders together. Add any instruction line the template suggests to `CLAUDE.md` only with
  approval.

## Where things go in claude.ai

- **Rules and house rules:** give the fenced block to paste into a project's instructions or
  their personal preferences. Drop the Git, Secrets and Files sections of the house rules there.
- **Templates and guides:** files to copy and keep. A template can also be added to a project as
  a file.
- **Skills:** add as a custom skill if their plan has that. Most skills here assume Claude Code
  (they run commands or read local files); say so before they spend time on it.

## Manifest

| Piece | Path | Works in | Depends on |
|---|---|---|---|
| Writing for people | `rules/writing-for-people.md` | both | none (the optional extra line points at a voice file: offer it only if they also take the voice file) |
| Research and claims | `rules/research-and-claims.md` | both | none |
| Scope and review | `rules/scope-and-review.md` | both | none |
| House rules template | `rules/house-rules-template.md` | both (Git, Secrets, Files: Claude Code) | none |
| Voice file | `templates/VOICE.md` | both | none; one line in instructions makes Claude read it |
| Relationship file | `templates/relationship-file/README.md`, `LOG.md` | both | none; take both files |
| Shared doc, two tabs | `templates/shared-doc-two-tabs.md` | both | none |
| Memory as files | `templates/memory-index.md` | Claude Code (claude.ai: kept by hand) | one line in `CLAUDE.md` |
| Web app to API skill | `skills/web-app-to-api-reference/` | Claude Code | self-contained: the folder carries its own `har_summary.py` and `templates/`. Needs Python 3 and Chrome for the capture (check, do not install) |
| Map a web app guide | `guides/map-a-web-app.md` | read anywhere; doing it needs Claude Code | `tools/har_summary.py`, templates in `skills/web-app-to-api-reference/templates/` |
| HAR summary tool | `tools/har_summary.py` | Claude Code | Python 3.8 or newer, standard library only |
| commit, push | `skills/commit/`, `skills/push/` | Claude Code | git; optional `.claude/validate` per repo (the skill offers to create it); push offers `thermo-review` and `right-plan` but works without them |
| grill-with-docs | `skills/grill-with-docs/` | Claude Code (claude.ai: custom skill, if the plan has that) | none |
| right-plan | `skills/right-plan/` | Claude Code (claude.ai: custom skill, if the plan has that) | hands off to the public superpowers `writing-plans` skill if it is installed; works without it |
| gather-context | `skills/gather-context/` | Claude Code | subagents; hands off to the public superpowers `writing-plans` skill if it is installed; works without it |
| thermo-review | `skills/thermo-review/` | Claude Code | a code change to review |
| Seatbelt hook | `hooks/guard.sh`, `hooks/README.md` | Claude Code, optional | bash (Git Bash on Windows, untested there) |
| Peachy Adventure | `peachy/` | Claude Code | all six folders in `peachy/skills/` go together (`peachy-adventure` is shared material with no `SKILL.md`); `peachy/wire.sh` links them (bash), or copy them |
| Big projects guide | `guides/big-projects.md` | read anywhere | points at `peachy/` |
| Claude Code basics | `guides/basics.md` | Claude Code | none |
| Lessons | `guides/lessons.md` | both | none |
| Skills in GitHub | `guides/skills-in-github.md` | Claude Code | none |
| Voice while driving | `guides/voice-while-driving.md` | phone voice Claude plus a Claude Code working session | two shared docs both sides can read and write |
| Public installs | `guides/public-installs.md` | mostly Claude Code | network access to each source |
| Notes from the call | `guides/notes-from-the-call.md` | read anywhere | none; nothing to install |
| Leak checker | `check.sh` | Claude Code | bash and Python 3 |

## The leak checker, for anyone sharing a copy

Before the person shares their own fork, run `bash check.sh` from the kit folder. It scans every
file for names on their private block list, email addresses, phone numbers, personal folder
paths, cloud-drive links, document-ID-looking strings, unknown GitHub accounts, long dashes, and
broken skill frontmatter. GREEN means nothing found. Put the names you never want to ship in
`.private-blocklist` in the kit folder (one word or phrase per line), which is never committed:
`.gitignore` lists it and the checker skips it. Without that file only the generic checks run.
