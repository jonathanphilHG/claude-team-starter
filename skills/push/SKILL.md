---
name: push
description: Validate the whole branch, push it, and open a PR when appropriate. Use when the user asks to push or types /push, and offer proactively when committed work on a feature branch reaches a shareable checkpoint.
---

# push

Validate the full branch, push it, and open a pull request when the repo warrants one.

## When to offer (proactive nudge)

Beyond the explicit `/push`, recommend a push at natural checkpoints so the habit becomes visible and learnable:

- One or more commits sit on a feature branch and a slice or feature is complete and validated.
- Before wrapping up a work session with committed-but-unpushed work.
- The branch is ready for review or a PR.

Make a single one-line offer that names the trigger, so the moment is teachable ("This slice is committed and green: push it and open a PR?"). Offer only, never auto-push, since push is outward-facing. Proceed on confirmation, respect a no, and do not re-ask in the same session.

## Steps

1. **Guard the branch.** Refuse to push a default branch (`main` or `master`). Require a feature branch.
2. **Validate the whole branch.** Run `.claude/validate` against the full branch diff, not just the last commit. Same rules as `commit`: block on a non-zero exit, offer to create the file if missing.
3. **Offer a review.** Before pushing a non-trivial diff, offer to run `thermo-review` first. This is a nudge, not a block. Proceed if the user declines.
4. **Push** the branch.
5. **Open a PR when it fits.** If the repo has a GitHub remote and a PR is wanted, open one with a Conventional Commits title and a structured body: Summary, Changes, Testing, Impact. For a solo repo with no PR, just push cleanly.
6. **Migration safety (only if SQL migrations are detected).** Check naming and order, never edit an already-applied migration, and flag destructive statements (DROP, RENAME, type changes) for sign-off.
7. **Tokens.** If a GitHub token is needed, use a fine-grained PAT scoped narrowly (one token per job).

## Slice nudge

On an oversized or mixed-concern branch, suggest splitting the work into atomic slices via `right-plan`. Suggest, never block.
