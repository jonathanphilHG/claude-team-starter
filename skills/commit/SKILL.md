---
name: commit
description: Review changes and commit them with per-repo validation and a Conventional Commits message. Use when the user asks to commit or types /commit, and offer proactively when a coherent unit of work reaches a validated, checkpoint-worthy state.
---

# commit

Review the working changes, validate them, and commit in a clean, conventional style.

## When to offer (proactive nudge)

Beyond the explicit `/commit`, recommend a commit at natural checkpoints so the habit becomes visible and learnable:

- A coherent unit of work (a feature, fix, or refactor) reaches a working, validated state.
- Uncommitted changes have grown large enough to be worth a checkpoint before going further.
- Before switching to an unrelated concern while the tree is still dirty.

Make a single one-line offer that names the trigger, so the moment is teachable ("Tests pass and this fix is self-contained: commit it as a checkpoint?"). Offer only, never auto-commit. Proceed on confirmation, respect a no, and do not re-ask for the same change in the same session.

## Steps

1. **Review.** Run `git status` and `git diff`. Note anything that looks wrong before staging.
2. **Validate.** Look for `.claude/validate` in the repo root.
   - Present: run that single shell command. If it exits non-zero, stop and report. Do not commit red.
   - Absent: offer to create it, suggesting a command detected from the repo (a `tests/` plus `pytest` layout, a `package.json` test script, or a Makefile target). Create it on confirmation, then proceed. If the user declines, proceed without a gate.
3. **Stage deliberately.** Add only the intended files by name. Never `git add -A`.
   - Never stage secrets: `.env`, `secrets/`, `*.pem`, credentials, or key files.
   - Non-secret config, including `.claude/validate`, is fine to stage.
4. **Commit.** Write a Conventional Commits message (`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`). Add body bullets for anything non-obvious.

## Not this skill

- Do not commit with failing validation.
- Do not push. That is the `push` skill.
