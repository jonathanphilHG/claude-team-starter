---
name: right-plan
description: Break a large change into small, ordered, independently-mergeable atomic slices (schema, logic, wiring, go-live). Offer this before starting a large or multi-step build.
---

# right-plan

Turn a large change into an ordered set of small, safe, independently-mergeable slices.

## Nudge, do not hijack

Offered proactively. When it triggers, make a single one-line offer and proceed only on confirmation. Respect a no, and do not re-ask in the same session.

## Scope

Deliberately narrow: this is the atomic-slicing layer, not a full planner. Hand each slice's contracts to the superpowers `writing-plans` skill rather than duplicating it.

## The slice plan

1. **Order by phase**, adapted per repo: schema and data first, then core logic, then wiring and interface, then the go-live flip that activates the feature.
2. **Keep early slices inert.** Nothing calls the new code yet, so a push or deploy stays a no-op until the flip.
3. **Validate each slice.** Every slice runs `.claude/validate`.
4. **Keep slices small.** Target roughly 5 files or 500 lines per slice where feasible, so a human and a model can both reason about the coupling.

On repos with a live deploy surface (a hosted web service, a deployed server, a scheduled job) this pays off directly. On scratch or script repos it is mostly habit-building.

## Provenance

Adapted from a colleague's "Right Plan" practice.
