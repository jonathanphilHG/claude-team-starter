# SOURCES: where things live

Written at charting from the source sweep, then merged into at every gate. A ticket session
adds to its own findings file's New sources section; the gate folds it in here.

The most valuable entries are the **search patterns that worked** and the **empty wells**.
Those are what a later session cannot re-derive cheaply.

---

## Reachability, confirmed at charting

<!-- One row per surface touched. Confirmed means you made a call and it answered, not that
the tool exists. -->

| Surface | Reachable | How, and the gotcha |
|---|---|---|
| | | |

---

## Documents

<!-- Folder paths and file IDs. Note which are local versus API-only, and anything where text
extraction is unreliable and a rendered page is needed. -->

## Systems of record

<!-- System, database, table, record ID. Be exact: "the production database, `sessions` table" not "the database". Note
the fields known to be wrong or stale. -->

## People

<!-- Who holds what that no system does. Name the artifact, not just the person. -->

## Search patterns that worked

<!-- Verbatim, and where you ran it. This section pays for the whole file. -->

## Out of reach

<!-- What could not be got and who holds it. Keep this distinct from an empty well: a surface you
never reached is not a surface that came back empty, and later sessions plan against both. -->

## Empty wells

<!-- Searched and it was not there. REQUIRED on every entry: the surface actually queried and the
query verbatim. These entries tell later sessions not to look again, so an absence asserted from a
surface nobody reached, or from a query that could not have matched, is worse than no entry at all.
See the kit's evidence-tiers.md. -->
