# <App name> API surface

**Mapped <YYYY-MM-DD>** from <N> HAR capture(s) plus read-only calls against the live account.
Every endpoint below was observed in a capture or replayed on the date shown. Anything not
replayed is marked UNTESTED.

| Provenance | |
|---|---|
| App | `<https://app.example.com>` |
| API host(s) | `<api.example.com>` |
| Signed-in identity during capture | `<your account, role>` (no password, no token) |
| HAR file | `<name.har>`, <size> MB, <total> entries, <N> non-OPTIONS, <HH:MM to HH:MM local> |
| HAR location | outside this repo, deleted on <YYYY-MM-DD> or kept at <path> |
| Public spec checked | `<URL or "none found">` on <YYYY-MM-DD> |

Companion files: `STATUS.md` (where things stand), `har_summary.py` from the skill's folder (how the HAR was read).

---

## Auth

Pattern: <cookie session | cookie plus CSRF | bearer token | static app key>.

| Header name | Where the value comes from | Notes |
|---|---|---|
| `<Authorization>` | `<localStorage key "x" | meta tag | cookie "y">` | <rotates? how often?> |
| `<X-Custom-Header>` | <source> | <notes> |

How to call: <from a logged-in tab with `fetch` and `credentials: 'same-origin'` | from a script
with a key in a gitignored `.env`>. Values are never written in this file.

---

## <Capability 1, for example "Read projects">

`<GET> /<path>/{id}`

Request body: <none | shape below>

```json
<sample request body with values replaced by types, no real ids or names>
```

Response shape: <one line, or a short JSON sample>

**Proven:** <YYYY-MM-DD>, record <id>, HTTP <code>, verified by <fresh read on which call or screen>.

Notes: <ordering, pagination, required fields, side effects>

## <Capability 2, for example "Update a project">

`<PATCH> /<path>/{id}`

Status: **UNTESTED** (seen in HAR <YYYY-MM-DD>, not replayed).

---

## Limits and traps

Every entry names four things: what was refused, where, when, and the exact error.

- <YYYY-MM-DD> `<METHOD /path>` returned <code> `<exact error text>` on <account or role>. <What this means.>
- <YYYY-MM-DD> A 200 from `<METHOD /path>` carried `<"success": false>` in the body. Read the body, not the status.

## Open questions

- <What is unknown, who is finding out, by when>
