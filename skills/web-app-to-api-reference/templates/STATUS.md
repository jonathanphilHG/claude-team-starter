# <App name> STATUS

**Last updated <YYYY-MM-DD>** by <who>.
**Created <YYYY-MM-DD>.** Nothing here is older than that date unless marked.

| Provenance | |
|---|---|
| App | `<https://app.example.com>` |
| API host(s) | `<api.example.com>` |
| Identity used | `<account, role>` |
| Source captures | `<name.har>` (<N> entries, <YYYY-MM-DD>), deleted <YYYY-MM-DD> |
| Reference | `API.md` in this folder |

## Newest change

<One short paragraph. What changed, when, and what it means for the next session.>

## Where things stand

| Capability | State | Evidence |
|---|---|---|
| <Read X> | working | live GET, <YYYY-MM-DD> |
| <Write Y> | proven live | `<METHOD /path/{id}>`, HTTP <code>, record <id>, fresh read confirmed <YYYY-MM-DD> |
| <Write Z> | UNTESTED | seen in HAR <YYYY-MM-DD>, not replayed |
| <Capability W> | broken as last seen | <code> `<exact error>` on <YYYY-MM-DD>, see Corrections |

States: working, proven live, UNTESTED, broken as last seen. Every claim carries a date.

## Rounds

### <YYYY-MM-DD> <Round name, for example "First capture">

- <What was done, which records, which ids>
- <What it settled>
- <What it did not settle>

## Corrections

Wrong claims stay here with the correction underneath. Do not silently edit them away.

- <YYYY-MM-DD> **Believed:** <the earlier claim>.
  **Actually:** <what is true>.
  **Found out by:** <fresh read, error text, vendor reply>.

## Open items

| Item | Owner | By when |
|---|---|---|
| <What is unknown> | <who> | <date> |

## What lives where

- `API.md`: how the app works, header names, proven calls, limits.
- `STATUS.md` (this file): where things stand, dated.
- Scripts: `har_summary.py`, in the skill's folder, reads a HAR safely.
- HAR files: outside this repo, `*.har` gitignored, deleted when done.
