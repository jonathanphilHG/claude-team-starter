# HOTLINE: cross-ticket flags, append only

Something another **live** session needs now, not at the gate. Read it when you start and
again before you close.

**Append only.** Use `printf`, never Write and never Edit. That is what keeps it collision
free across concurrent sessions:

```bash
printf '%s\n' "- [T04 . $(date '+%Y-%m-%d %H:%M')] The orders table shows 20 records, not 10. T03: the total may cover more orders than assumed." >> HOTLINE.md
```

Format: `- [<ticket> . <date time>] <what you found> <which ticket needs it>`. The time comes from
`date`, which the example substitutes; never estimate it from the lines above.

Two or three entries per round is healthy. Twenty means the ticket boundaries were drawn
wrong, and that itself is worth flagging.

Do not use this for findings. Findings go in your own findings file and reach everyone at
the gate.

A reply is legitimate and often the most valuable entry in the file: two sessions each
holding half of an answer is exactly what this is for. Lead with `Replying to T0N <time>`.

---
