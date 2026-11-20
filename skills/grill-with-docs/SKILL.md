---
name: grill-with-docs
description: Relentlessly interrogate a plan and ground every external or API assumption against real docs and reference repos before building. Offer this before starting API-touching or multi-step work.
---

# grill-with-docs

A relentless interview that sharpens a plan and grounds it in reality before any code is written. Built for API-integration work, where the gap between the docs and what is actually true causes most breakage.

## Nudge, do not hijack

Offered proactively. When it triggers, make a single one-line offer and proceed only on confirmation. Respect a no, and do not re-ask in the same session.

## Steps

1. **Grill.** Generate nitty-gritty questions about the change: the real request shape, the real response shape, real permissions and scopes, pagination, rate limits, error modes, and edge cases.
2. **Ground every assumption.** For each external or API assumption, verify it against real truth: the actual vendor docs, a real response you captured, or your own notes on that API if you keep them. Never accept assumed behavior.
3. **Surface gotchas.** Call out contradictions between the docs and reality.
4. **Record.** Write a short decision record of what was confirmed or corrected.
5. **Pin it, where it fits.** Offer to encode confirmed API truths as offline learning tests when the repo has somewhere to put them (a test setup exists or is trivial to add). In a setup-less or throwaway repo, stop at findings plus the decision record. Do not force a test harness onto an MVP.

## Provenance

From Matt Pocock's `grill-me` ("a relentless interview to sharpen a plan or design"), elaborated with the team's docs-grounding and learning-tests practice.
