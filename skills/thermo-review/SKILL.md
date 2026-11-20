---
name: thermo-review
description: Strict maintainability audit for giant files, spaghetti growth, and missed code-judo restructurings. Offer this as a first-pass review after changes are implemented and before pushing a non-trivial diff.
---

# thermo-review

A deliberately strict maintainability audit. It is a first pass before human review, not a replacement.

**Announce at start:** "Running a strict maintainability audit (thermo-review)."

## Nudge, do not hijack

This skill is offered proactively. When it triggers, make a single one-line offer and proceed only on confirmation. Respect a no, and do not re-ask in the same session.

## What to hunt

Be ambitious about structure, not cosmetic. Look for:

- The 1,000-line-file smell: a change pushing a file past 1,000 lines needs a strong reason. Prefer decomposition.
- Code judo: restructurings that keep behavior identical while making whole branches, helpers, modes, or layers disappear.
- Spaghetti: new ad-hoc conditionals bolted into unrelated flows. Push logic behind a dedicated abstraction instead.
- Canonical reuse: prefer an existing helper over a near-duplicate. Keep logic in the layer that owns the concept.
- Type and boundary cleanliness: question unnecessary casts, optionality, and loosely-shaped objects.
- Non-atomic updates that can leave state half-applied.

Prioritize a few high-conviction structural findings over a pile of nits.

## Two-step output

1. **Findings.** Produce the findings, clearly separated into **blocking** and **non-blocking**. Keep the structure so it stays automation-friendly.
2. **Fix on confirm.** On the user's confirmation, fix only the blocking findings. Do not auto-fix.

## Provenance

Adapted from Cursor's team kit (thermo-nuclear code quality review), with tool-specific wording removed.
