# Evidence tiers and bounded forms

Two related disciplines. Tiers are **shape-gated**: mandatory for investigations, on for a
decision's inputs, on for factual claims inside an artifact, and off for rollouts and program
spines. Bounded forms apply to **every** shape, because nothing is ever allowed to block forever.

---

## Part 1: the tier ladder

Where tiers are on, every factual claim in the project carries a tier and a citation. No
exceptions, including in the Hotline.

| Tier | Meaning | Citation format |
|---|---|---|
| **A** | Executed document, filed return, signed contract, statute, or an authoritative third-party record | Document name, section, page. Or statute and subsection. |
| **B** | System of record: Airtable, QuickBooks, a bank or lender portal, a platform's own admin UI, a warehouse query | System, table, record, field, and the date you read it |
| **C** | Correspondence or conversation: email, Slack, a meeting transcript, someone told you | Sender or speaker, date, subject or meeting |
| **D** | Reasoned inference | State the inputs and the reasoning explicitly, in line |
| **E** | Assumption or external benchmark | State the source, its date, and an uncertainty range |

Write it inline so it survives a copy and paste out of context:

```
**[Tier B]** The business owes $250,000 of invoices across four suppliers.
*Source: the bills table in the accounting system, reconciled against each supplier's statement,
read 2026-01-01.*
```

### The rules that make the ladder worth having

**Never present D or E as A or B.** A confident wrong number is worse than an acknowledged gap.
This is the failure the ladder exists to prevent and it is easy to commit by accident: you infer
something on Tuesday, cite it on Thursday, and a week later it reads like a record.

**`UNKNOWN` is an acceptable answer.** Write it, plus the one thing that would resolve it.

**Do not estimate away a gap.** If a figure is unknown, it is unknown. Do not substitute a
plausible industry norm and then use that number downstream as though it were established. That is
how an assumption launders itself into a fact.

**Confidence downgrade.** If you check a prior claim and cannot reproduce it from its source, it
drops to `UNKNOWN` and goes in Contradictions. Do not quietly agree with earlier work. Silent
agreement is the likeliest single route to a wrong deliverable, and it gets more likely, not less,
as more sessions touch the project.

**Contradictions are findings.** Two sources disagreeing gets recorded with both citations, not
smoothed over. Resolving it is the gate's job, and sometimes the honest resolution is that it
stays live.

**A tier movement is a headline.** An assumption that became evidence, or a Tier A claim that
could not be reproduced, usually moves the answer more than any new fact does.

**A limit carries the surface it was measured on.** Tiers grade **confidence**. They say nothing
about **scope**, and scope is the half that fails in practice: on one map in one night, six separate
claims of absence were disproved, and every one was a limit recorded without the surface it was
measured on and then inherited as absolute. "There is no bulk-export route **in this MCP**" is a
finding; "unknowable from the API" is a different and much stronger claim, and it was false, with two
untried routes behind it. When you write a limit, the surface is part of the sentence, not context
around it. When you repeat someone else's limit, it travels with the surface attached.

**Confirmed absent is a real finding, and it carries its scope.** "Searched thoroughly and it does
not exist" is worth as much as finding it, and later sessions are told not to re-search it, so an
absence is load-bearing in a way an ordinary finding is not. Record it with **the surface you
actually queried and the query verbatim**, then a note on who would have an unobtainable document.

Three rules make that safe, and each one comes from an absence that turned out to be false:

- **Never assert absence from a surface you did not reach.** One charting session wrote "no industry
  primer exists in Drive, do not re-run this search" from a sweep that had never opened the folder.
  Two tickets then found a full curriculum there, including a 19-page primer that pre-empted most of
  a research ticket.
- **A query that cannot match the thing reads exactly like a real absence.** A chat search for one
  phrase returned nothing and became "nobody has asked about this" in two canonical files. It had
  been asked that morning, in a message that used a different name for the same thing. Writing
  the query down is what makes this catchable by the next reader.
- **State what the absence covers.** "Not in this folder" is a finding. "It does not exist" is a
  much larger claim and usually not the one you tested.
- **A refusal names the credential that was refused.** A 403 or a 401 is a fact about the key,
  token or login you used, and about what it was scoped or selected to, not about the resource. "Refused for key A" is a finding; "the endpoint
  does not allow writes" is a much larger claim, and on one map it was false. Re-run on every
  credential the project holds before you record it. See the write protocol in `peachy-build`.

### A person's report of an action is a claim, not a verification

The verify-before-you-record discipline covers the human too, for actions on live, outward-facing
systems: "I sent it", "that was filed", "it went in on Friday". Record it as **reported, not
observed**, and check it against the confirmation record (the Sent folder, the ticket id, the portal
receipt) before anything is built on it. This is not a trust question. He runs half a dozen sessions
at once and is often the only one who can perform the action, which makes him the only available
source and an easy one to misremember.

Two occurrences. He reported a vendor email sent that was still an unsent draft holding a
placeholder; the session checked four ways before recording and caught it. And a `MISSION.md`
inherited "filed the twelve defects" from a prior map when the scripted filing had hit a 503 and
the source file said "Nothing filed yet", and a whole map was built on it. **Charting and every gate
check an inherited sent or filed claim against its confirmation record before carrying it forward.**

### A scan you have not tested is not a scan

The three rules above assume the tool did what you asked it to. Three times now it did not, and
every time it reported **clean**:

- A line-based `grep` for a multi-word phrase, on markdown that had wrapped the phrase across two
  lines with a blockquote marker landing between the words. It returned nothing on a file plainly
  containing the phrase, and the scan was a mandated pre-publish redaction check.
- BSD `grep` on macOS silently failing to match a multibyte character. It reported CLEAN twice on
  files holding nine em dashes, and the result was reported onward to the human twice.
- A `\b` word boundary against hyphenated UUIDs. It found zero in a repository holding nine; the
  same pattern without `\b` found them all.

Three different rules, three different tools, one failure. **A scan that cannot match its target
reports clean, which is the worst outcome available to a guard**, because a false alarm gets
investigated and a false all-clear gets believed and written down.

**So before you trust a zero, prove the matcher can find a known positive.** Seed one, or point the
matcher at a line you have already read with your own eyes, and confirm it comes back. If it does
not, the tool is wrong and the corpus is innocent. **A zero from an untested matcher is not an
absence, it is an unfinished check**, and it must not be recorded as either. Every one of the three
above was caught only because a human or a session noticed the zero contradicted something it had
already seen.

Prefer a matcher that cannot false-negative on the class of thing you are hunting. For text in
files, a Python read is a few lines, does not depend on the platform's `grep`, and handles
multibyte characters, wrapped lines and markdown markers without special cases:

```python
import pathlib, re
needle = "Example Phrase"
for p in pathlib.Path(".").rglob("*.md"):
    lines = p.read_text(encoding="utf-8").splitlines()
    flat = " ".join(re.sub(r"^\s*[>#*\-\s]*", "", ln) for ln in lines)
    if needle in " ".join(flat.split()):
        print(p)
```

This applies to every check this kit asks a session to run: no long dashes, no secrets, a redaction
or PII sweep before publishing, and the confirmed-absent findings above. **Where a rule is verified
mechanically, the positive control is part of the verification, not an optional extra**, and the
result you write down is "checked with a matcher proven against a known positive," not "grep found
nothing."

---

## Part 2: bounded forms

This is the mechanism behind invariant 7, "nothing blocks forever." When a session cannot resolve
its item, the item converts to a **declared, bounded, visible form** and the work proceeds. Never
leave a ticket open waiting for a document.

The form depends on the project shape.

### Investigation: a parameter with a range

```
**[Tier D]** Partner capital contributed to date: **$500,000**, range $400,000 to $600,000.
*Basis: four transfers in the ledger totalling $400,000; a fifth is mentioned in an email thread
but does not appear in the ledger; the signed commitment caps the total at $600,000.
Would be settled by: the partner's own account statement.*
```

Five parts, all required:

- **Value.** Your single best point estimate. Never blank, and never zero as a stand-in for
  unknown, which reads as a measurement.
- **Range.** Low and high, **always both**, even on a Tier A number where they equal the value. A
  range is the honest uncertainty input; a bare point estimate is a claim you cannot support.
- **Tier.**
- **Basis.** What bounds the range. This is what makes it auditable rather than a decorated guess.
- **What would settle it.** One line, so a later session or the human can act.

### Decision: an assumption with a reversal trigger

State the assumption, why it is the reasonable one, and **the observation that would flip the
decision**. A decision recorded without its reversal trigger cannot be revisited intelligently,
only re-argued.

```
Assuming the vendor holds the current rate through renewal.
Basis: two prior renewals held; no notice received.
Reverses if: any renewal quote arrives above +8%, in which case the second option wins.
```

### Knowledge artifact: a marked gap with an owner

Leave the gap **visible in the artifact itself**, not only in a notes file, with who can fill it.
A document that silently omits what nobody knew reads as complete and is worse than one with a
labelled hole.

### Operational rollout: a documented exception

The unit goes to **exception**, with the reason and what would clear it. Never "blocked." An
exception lets the rollout finish; a blocked unit stalls it.

### Program spine: a thread with an owner and a next action

A thread nobody owns and that has no next action is not a thread, it is a note. Close it or give
it both.

---

## The universal stop test

Whatever the shape: **a well characterized bounded form beats a false precision, and it beats
another two hours of hunting.** If closing the gap would change the deliverable by a rounding
error, write `UNKNOWN, immaterial` and move on.
