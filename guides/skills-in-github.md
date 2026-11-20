# Keep your skills in a GitHub repo

A skill is a folder with a `SKILL.md` file in it. Claude Code reads skills from one folder on
your computer: `~/.claude/skills` on macOS or Linux, `%USERPROFILE%\.claude\skills` on Windows.
This page is about keeping those folders in a GitHub repository instead of loose on one machine.

## Why

- **Every change is kept.** You can see what a skill said last month and put it back.
- **It survives a new laptop or a cleanup.** Clone the repo and your skills are back.
- **Sharing is a link.** A teammate copies or forks the repo and takes the skills they want.
- **Edits go live.** If the skills folder points at the repo, editing a skill changes what
  Claude does in the next session, with nothing else to run.

## How

1. **Make a private repository** with a `skills/` folder inside it (and, if you like, your
   `CLAUDE.md` beside it). GitHub Desktop is the easiest way if you do not use a terminal.
2. **Put each skill in its own folder** under `skills/`. The folder name must match the `name:`
   line at the top of its `SKILL.md`.
3. **Connect it to Claude Code**, one of two ways:
   - **Link** (macOS or Linux): point Claude's skills folder at the repo, so edits are live.

     ```
     ln -s ~/code/<your-repo>/skills    ~/.claude/skills
     ln -s ~/code/<your-repo>/CLAUDE.md ~/.claude/CLAUDE.md
     ```

     Only do this if `~/.claude/skills` is empty or does not exist yet. Otherwise link single
     skill folders: `ln -s ~/code/<your-repo>/skills/<name> ~/.claude/skills/<name>`.
   - **Copy** (any operating system, simplest on Windows): copy the skill folders into the
     skills folder. Copy again after you change them.

   Or ask Claude Code to do it: "Link each folder in this repo's skills/ into my user skills
   folder. Show me what you will do first, and do not overwrite anything."
4. **Start a fresh session.** Skills load when a session starts. Type `/` and look for the names.

## Habits that keep it safe

- **Read a skill before you install it.** A skill is instructions Claude will follow. Have
  Claude read a stranger's `SKILL.md` to you first.
- **Never put secrets in the repo.** No passwords, keys, `.env` files or browser captures
  (`.har`). Something committed once stays in the history even after you delete the file. Add
  them to `.gitignore` before they exist.
- **Who can change it.** On a personal GitHub account, everyone you invite to a private repo can
  also edit it; GitHub offers nothing smaller there. If people should only read, use an
  organization's repo with read access, or have them fork it.
- **Clone, do not download a ZIP**, if you want to receive updates. A ZIP is a dead copy.

## In claude.ai

The folder trick above is for Claude Code. In claude.ai, add a skill as a custom skill if your
plan has that, and keep the repo as the master copy you upload from.
