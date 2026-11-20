# Harvest queue: <project name>

Kept by the orchestrator. One row per learning that should change a surface OUTSIDE this project
folder: a flow or runbook, a trap or API note, a template other people work from, a reference repo,
the kit itself. Seeded at each gate from the round's findings files, the relays, the premise
corrections and his rulings; appended between gates as relays arrive.

**How it runs.** After each gate one harvest ticket (`execute`, frontier tier, `xhigh`) works this
queue. The queue is its starting list, not its scope: it also scans the findings files, the
Hotline, the log and the sweeps since the last harvest, and adds the rows this list missed. It
lands directly what only touches our own working files, holds template text, team documents and
ADRs for one table on his yes, and never writes a file a live ticket owns. See the `peachy-gate`
skill, "After the gate".

Only the harvest ticket changes a status. Status: queued / landed by T<NN> / held (his table) /
dropped, with the reason.

| # | Learning | Source | Target | Status |
|---|---|---|---|---|
| 1 | <what is now known, in one or two sentences, stated as the rule or the fact> | <findings file, Hotline line, or his words with the date> | <the file, template or repo it belongs in> | queued |
