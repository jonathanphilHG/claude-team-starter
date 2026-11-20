# House rules template

A starting point for your own standing instructions: the rules Claude reads at the start of
every conversation.

- Claude Code: this becomes your user-wide `CLAUDE.md` (`~/.claude/CLAUDE.md` on macOS or Linux,
  `%USERPROFILE%\.claude\CLAUDE.md` on Windows). Copy the fenced block; if you already have
  instructions, add only the sections you want.
- claude.ai: paste the parts that apply into your personal preferences or a project's
  instructions. Voice, Scope and Safety apply anywhere. Git, Secrets and Files only matter in
  Claude Code.

For each section: keep it, change it, or delete it. This loads into every session in full, so
every line costs a little. Short beats complete. The other files in `rules/` are add-on blocks
you can paste below these.

---

```
# House rules

These apply to every session and every skill.

## Voice
(Personal taste, not craft. Replace with your own.)
- Never use em dashes or en dashes. Use commas, colons, or parentheses.
- Be factual, not performative. No "great question", no flattery. State what changed and why.

## Scope
- Plan the smallest thing that runs end to end, and say what is out.
- Cap review rounds up front: one for docs, two for anything that runs for real.
  Fix only findings that change what someone would do.
- When more thoroughness stops changing the outcome, stop and say so.

## Git
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.
- Stage files explicitly by name. Never `git add -A`.
- Branch before committing on a default branch.

## Secrets vs config
- Never stage or commit secrets: `.env`, `secrets/`, `*.pem`, credentials, key files.
- Non-secret config files (including `.claude/validate`) are fine and must never be treated as secrets.
- When sharing setup with someone, share variable names, never values.

## Safety
- Read-only by default against anything live (a real account, a deployed app, someone else's data).
- Writes need explicit approval, and a mechanical guard where the tool supports one.
- Dry run first, then confirm.

## Files
- Put temp files in a scratch location, never in the repo.
- When pointing at a file, reveal it in the file browser: `open -R <path>` on macOS,
  `explorer /select,<path>` on Windows.
```

---

## Why these sections

Voice keeps output readable. Scope keeps work small enough to finish. Git keeps history
reviewable. Secrets keeps credentials out of version control, which is the one mistake that
cannot be quietly undone. Safety makes destructive actions deliberate instead of accidental.
Files keeps your working folders clean.

## Growing it

Add a rule when you notice you have said the same thing to Claude more than twice. That is the
signal it belongs here. Delete a rule when you notice it no longer changes anything.
