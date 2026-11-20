# Public skills and plugins worth knowing

Things other people publish and maintain. This kit points at them instead of copying them, so
you always get their current version. Install lines are as last used in November 2026; if one
fails, the source page has the current line. Read a skill before you install it: it is
instructions Claude will follow.

Most of these are for Claude Code.

## superpowers

A plugin that teaches Claude to brainstorm before building, plan, debug systematically, write
tests first, and check its own work before saying it is done.

- Source: https://github.com/obra/superpowers
- Install, in Claude Code:

  ```
  claude plugin marketplace add anthropics/claude-plugins-official
  claude plugin install superpowers@claude-plugins-official
  ```

## mattpocock/skills (grilling, grill-me, research, handoff, wayfinder)

A public skill collection (MIT licence). The one people ask for most is **grilling**: Claude
interviews you one question at a time, each with its recommended answer, until the holes in a
plan show. Also: `research` (answers from primary sources, written to a file), `handoff`
(compacts a session for the next one), `wayfinder` (plans a code project bigger than one
session).

- Source: https://github.com/mattpocock/skills
- Install, in Claude Code:

  ```
  claude plugin marketplace add mattpocock/skills
  claude plugin install mattpocock-skills@mattpocock
  ```

- It brings about 27 skills, and some overlap with superpowers. Two skills that fire on the same
  request fight each other, so turn off the duplicates you do not want (`skillOverrides`, see
  `basics.md`).

## Anthropic document skills (Word, PowerPoint, PDF, Excel)

Lets Claude Code read and write Office files and PDFs.

- Source: https://github.com/anthropics/skills
- Install, in Claude Code:

  ```
  claude plugin marketplace add anthropics/skills
  claude plugin install document-skills@anthropic-agent-skills
  ```

- Some claude.ai accounts already include these. Type `/` in a Claude Code session and check
  first; two copies of the same skill both fire.

## sop-maintenance

Keeps standard operating procedures current: versioning, updating, retiring.

- Source: https://github.com/thebushidocollective/han (found through skills.sh)
- Install (needs Node; Claude Code can set it up):

  ```
  npx skills add https://github.com/thebushidocollective/han --skill sop-maintenance -g
  ```

## skills.sh

A public directory of skills, run by Vercel (not by Anthropic). Each page shows its install
line. Good for browsing.

- Source: https://skills.sh

## Jam

Records a bug with the screen, console and network attached, and its CLI adds skills for turning
screenshots and recordings into bug reports.

- Source: https://jam.dev, docs at https://jam.dev/docs
