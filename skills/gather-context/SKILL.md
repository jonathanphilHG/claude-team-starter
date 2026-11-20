---
name: gather-context
description: Gather relevant codebase context before beginning work by self-generating questions and launching parallel research agents
---

# gather-context

Systematically gather the context needed to complete a task by formulating targeted questions and answering them in parallel with subagents.

## When to Use

Use **before** starting any non-trivial work:

- Implementing a feature from a spec or ticket
- Investigating an unfamiliar area of the codebase
- Making changes that touch multiple subsystems
- Picking up work you haven't touched before
- Any time you'd otherwise spend 10+ minutes reading code to orient yourself

## Process

### Step 1: Understand the Task

Read the user's request plus any linked plan, spec, decision record, or ticket the repo keeps. Common homes are `docs/plans/`, `docs/specs/`, `docs/adr/`, a `README`, or an issue tracker. Identify:

- **What** needs to happen (the goal)
- **Where** it likely lives (subsystem, layer)
- **What you don't know** (the gaps)

### Step 2: Formulate 3-5 Questions

Generate 3-5 specific questions whose answers would give you enough context to begin work confidently. Good questions target:

| Category | Example Question |
|----------|-----------------|
| **Existing patterns** | "How do existing services in this area handle X? What files/patterns should I follow?" |
| **Data model** | "What tables/models are involved and how do they relate?" |
| **Integration points** | "What calls this code? What does this code call? Where are the boundaries?" |
| **Constraints** | "Are there multi-tenancy, auth, or transaction patterns I need to follow here?" |
| **Prior work** | "Has anything similar been built? Are there recent commits or PRs that touch this area?" |

**Rules for good questions:**
- Each question should be answerable by reading code, git history, or docs
- Questions should be independent of each other (parallelizable)
- Questions should fill genuine knowledge gaps, not confirm things you already know
- Be specific: "How does the token store handle refresh when a request races an expiry, and where is that tested?" not "How does auth work?"

**Announce your questions to the user before launching agents:**

```
I need to gather context before starting. Here are my questions:

1. [Question 1]
2. [Question 2]
3. [Question 3]
...

Launching research agents now.
```

### Step 3: Launch Parallel Research Agents

Launch one `Explore` subagent per question, **all in a single message** so they run concurrently.

```
Agent(subagent_type="Explore", description="Context: [short label]", prompt="
  I'm about to work on [TASK SUMMARY].

  Question: [THE QUESTION]

  Search the codebase to answer this thoroughly. Look at:
  - Relevant source files, models, services, and tests
  - Related patterns in similar features
  - Recent git history if relevant

  Report your findings thoroughly: key files (with paths and line numbers),
  patterns to follow, and anything surprising or non-obvious.
  Be as detailed as needed, since longer and more thorough answers are preferred.
")
```

**Important:**
- All agents launch in a single message (parallel, not sequential)
- Each agent gets the full task summary for context
- Each agent gets exactly one question to focus on
- Agents are told to be thorough, since longer answers are preferred over brevity
- If your harness has no `Explore` agent type, use its general-purpose research agent instead. The pattern matters, the agent name does not.

### Step 4: Consolidate and Present

After all agents complete, synthesize their findings into a single context summary for the user:

```markdown
## Context Summary: [Task Name]

### Key Files
| File | Purpose | Relevance |
|------|---------|-----------|
| `path/to/file.py` | [What it does] | [Why it matters for this task] |

### Patterns to Follow
- [Pattern 1]: found in `path/to/example.py`, [brief description]
- [Pattern 2]: found in `path/to/example2.py`, [brief description]

### Constraints & Considerations
- [Constraint 1]
- [Constraint 2]

### Findings

**Q1: [Question]**
[Concise answer with file references]

**Q2: [Question]**
[Concise answer with file references]

...

### Ready to Begin
[1-2 sentences on recommended approach based on gathered context]
```

## What This Is NOT

- **Not a replacement for reading the plan or decision records.** Read those first, then gather context about the codebase.
- **Not a plan.** Use `right-plan` to slice the work, then `superpowers:writing-plans` to write the plan itself.
- **Not exhaustive research.** 3-5 targeted questions, not 20. Enough to start, not to finish.

## Example

User says: "Add rate limiting to the public API, per the spec."

**Step 1:** Read the spec and any relevant project notes.

**Step 2:** Formulate questions:
1. "How is the middleware stack ordered and registered today, and where would a new middleware hook in?"
2. "Is there already a shared cache or store this could use for counters, and how is it configured per environment?"
3. "How do existing tests fake time and external services, so a rate-limit test stays fast and offline?"
4. "How does configuration reach the code (env vars, config file, both), and where is the single place it is read?"
5. "Has anything similar been attempted before, in recent commits, reverted branches, or TODOs?"

**Step 3:** Launch 5 research agents in parallel, in a single message.

**Step 4:** Consolidate into a context summary, present it, and be ready to proceed.
