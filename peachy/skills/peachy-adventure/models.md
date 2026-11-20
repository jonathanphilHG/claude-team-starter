# Choosing the model and the effort

Every ticket carries a `Run at:` line naming a **tier** and an effort level, for example
`Run at: workhorse, high`. This file says how to pick them, and it holds the **one** table that says
which model each tier means today. It is read when a ticket is written, which is charting and the
gate, and by a worker checking its own launch at claim.

**Tickets and maps name tiers, never models.** Models are replaced far faster than this kit is
revised. A ticket that says "Claude Fable 5" goes stale the day a point release ships, and every
map carrying it needs editing; one said exactly that, a session launched on Fable 5.1, and the claim
check turned into a judgment call. A tier never goes stale. The lineup table below is the only place
a model name lives, and it is updated once per release.

---

## The axis that decides it

Not the subject matter. **Who is holding the plan, and whether anyone is there to redirect.**

- You can name the outcome but not the steps, the work runs long, and nobody is watching while it
  does: **frontier tier**.
- The steps already exist, or a human is in the loop reacting as it goes: **workhorse tier**.

Anthropic frames the same split as long horizon tasks with many connected steps, where you would
rather describe the outcome than plan the steps yourself, against deep research and analysis you
will question, redirect and build on. Their escalation test is worth remembering because it is
testable at charting: **if a task takes a lot of time, involves multiple steps, or is previously
unsolved, go up a class.**

## The two tiers this kit uses

| Role | For |
|---|---|
| **Frontier** | Open-ended research, exploration, creative work, a long deep dive nobody is watching |
| **Workhorse** | Everything else: directed work, live conversation, building against a written spec, a bounded deep dive |

### Current lineup

**Update this table once per model release, and nowhere else.** No ticket, map or template names a
model, so this edit is the whole migration.

| Tier | Model today | Updated |
|---|---|---|
| Frontier | Claude Fable 5.1 | 2026-09-28 |
| Workhorse | Claude Opus 5.5 | 2026-09-28 |

**Below the workhorse tier is not used here, and that is deliberate.** State the reason, because the
reason is what survives a lineup change: **cost per completed task, not cost per token.** A more
capable model at lower effort routinely finishes in fewer turns than a cheaper one grinding at high
effort, so reaching down usually costs more and takes longer. If a ticket looks too small for the
workhorse tier, the answer is lower effort, not a smaller model.

## Effort

**Effort is the cost lever, not the model.** Pick the tier first, then set effort to the work.
Reaching down a tier to save money is the wrong move for the reason above; spending `xhigh` on a
bounded ticket is the right tier at the wrong setting, and it is where the tokens went. His words:
"we're maybe overmuscling some of the tasks we do, and as a result I'm burning through
more tokens than I probably need to."

- **`max`**: correctness matters more than cost and you can say why on the ticket. Rare.
- **`xhigh`**: open-ended work. Research, grill, and a large or long execute batch.
- **`high`**: bounded work, where the steps are known or a human is reacting as it goes. A task, a
  prototype, a small execute batch, a single draft.
- **Below `high`**: a genuinely mechanical ticket. Say why on the ticket.

## Defaults by ticket type

The ticket type already encodes the axis above, so it carries the default. Deviate freely, and say
why on the `Run at:` line when you do.

| Type | Mode | Default |
|---|---|---|
| `research` | AFK | Frontier, `xhigh` |
| `grill` | HITL | Workhorse, `xhigh` |
| `prototype` | HITL | Workhorse, `high` |
| `task` | either | Workhorse, `high` |
| `execute` | either | Workhorse, `high`; `xhigh` on a large or long batch |

**One standing exception: the post-gate harvest.** It is an `execute` ticket, and it runs at
frontier, `xhigh`, because nobody can list its steps in advance: the session decides what is
structural, where it belongs, and what the queue missed. See `peachy-gate`, "After the gate".

## The launch is where this gets lost, so the worker checks it

A prompt cannot carry the model, because a session cannot set its own model: that is why
`peachy-gate` keeps model and effort out of the kickoff prompt and says them to the human alongside
it. The cost of that correct split is that nothing downstream verifies the human acted on it, and
three tickets went out on the wrong tier because of it.

**So the worker checks its own launch, before it claims.** Look up the ticket's tier in the lineup
table above and compare it with the model the system prompt names; halt on a mismatch, and write or
claim nothing until it passes. **A newer release of the same family is a match** (Fable 5.1 where
the table still says Fable 5): run, and say in the findings file that the table is behind. A
different family is a mismatch.

Check the model rather than the effort: the model is always visible to a session and the effort
usually is not. The full rule is in `peachy-work` and `peachy-build` at step 2, the banner is in
`templates/ticket.md`, and the reasoning is ADR-0012, with tiers-not-names in ADR-0013.

## One thing that changes how you write for the frontier tier

**Prompts written for older models are often too prescriptive for the frontier tier, and the extra
prescription lowers the quality of what comes back.** That is the tier research tickets run on, and
it is an independent argument for the kickoff prompt staying exactly as thin as `METHOD.md` says:
location, ticket, skill, goal, plus any hard rule the session must not discover late, and
everything else a pointer.

The temptation to fatten a prompt is strongest at a gate, which has just read everything and has it
all in hand. Resist it there in particular. The thin prompt was confirmed in the field across
fourteen launched tickets, and it is not a compromise that a better model makes safe to abandon; it
is the shape that better models prefer.
