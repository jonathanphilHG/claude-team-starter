# T<NN>: <ticket name>

Session: <date> . Model and effort: <what you ran at> . Bounded by: <what made you stop>

<!-- Model and effort is a RECORD here, not a check. The check is the ticket's `Run at:` line, read
against the model you actually are, and it happens BEFORE the claim line: see step 2 of peachy-work
and peachy-build. A mismatch found at this point has already cost the whole ticket.

The gate parses these headings, so keep the names literal and include every one even when empty.
Write "None." rather than deleting a heading. -->

## Facts

<!-- Every established claim, one bullet each. Where the shape has tiers on, a tier tag and citation
on every single one:

**[Tier B]** <claim text>
*Source: system, table, record, field, date.*

For an execute ticket this section records WHAT CHANGED: the objects touched, before and after, and
the verification. That record is what separates a completed rollout from an unauditable one. -->

## Bounded items

<!-- Whatever you could not establish, in the form this shape calls for: a parameter with a range, an
assumption plus a reversal trigger, a marked gap with an owner, a documented exception, or a thread
with an owner and a next action. See the kit's evidence-tiers.md, part 2. -->

## Decided below the bar

<!-- Every fork you resolved yourself rather than asking, one line each: the fork, the pick, and the
one-line reason. The gate batches these so the human can overrule cheaply.

This section is the price of the asking rule. If it is empty on a substantial ticket, either the
ticket was unusually clean or you asked too much. If it is long, one of these should probably have
been escalated. -->

## Contradictions

<!-- Any source conflict, both sides cited. Also any prior claim you could not reproduce, which drops
to UNKNOWN per the confidence-downgrade rule. Do not resolve a conflict here unless you can do it
with evidence; flagging it live is a legitimate outcome. -->

## New questions

<!-- Questions this raised. Do NOT create tickets for them. Only a gate promotes one, against the
materiality bar. -->

## New sources

<!-- Every file ID, folder, table, record ID, portal, person, and every search pattern that actually
worked, verbatim. Merged into SOURCES.md at the gate. -->

## Dead ends

<!-- What you tried that returned nothing, and where. This is what stops the next session
re-searching an empty well. Also anything you can now mark CONFIRMED ABSENT, with how thoroughly you
looked.

Name the surface you actually queried and the query VERBATIM. These entries stop other people
looking, so they carry more weight than an ordinary finding: never assert absence from a surface you
did not reach, and remember that a query which cannot match the thing returns nothing in exactly the
way a real absence does. State what the absence covers: "not in this folder" is a finding, "it does
not exist" is usually not what you tested.

Where the absence came from a mechanical scan, name the POSITIVE CONTROL you ran alongside the
query: the known positive you proved the matcher could find before you believed the zero. A zero
from an untested matcher is an unfinished check, not an absence. See the kit's evidence-tiers.md. -->

## Outside scope

<!-- One line each for material problems you found that are not this project. -->

## Handoff

<!-- Two or three lines: what is now known or changed that was not, what is still open, and whether
anything you found should change another ticket. -->

<!-- OPTIONAL, and only if this ticket was reopened after it closed: add `## Addendum <date>` below,
holding the new work in the same shape as the sections above. Do not add the heading pre-emptively.
The gate expects the headings above on every file and this one on almost none. -->

