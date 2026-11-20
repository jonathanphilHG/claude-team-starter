# Map a web app you use

The long version of the `web-app-to-api-reference` skill (in `skills/`). Use the skill to do it;
read this page to understand it.

This page teaches one method: watch what a web app really sends to its server, write it down in a
small set of files, and keep those files honest over time. The result is a folder your Claude can
read before it touches the app, instead of guessing.

The running example is a made-up app, ExampleApp (`app.example.com`, with its API at
`api.example.com`). Every step works the same for any web app with a login, as long as its
terms of use allow it. If they forbid automated access, stop and use the app's official API or
export instead.

Expect the first pass to take an afternoon. A maintained reference pays that back the first time
you need the same answer twice.

## Why

- A reference your Claude can read beats re-discovering by trial and error. Trial and error against
  a live system means failed calls, wrong guesses, and sometimes writes you did not intend.
- A HAR file is the truth of what the app really calls. Documentation describes what someone meant
  to build. The HAR shows what the browser actually sent and what came back, byte for byte.
- Most web apps have two API surfaces: a public or documented one, and the internal one the app's
  own pages use. The internal one usually does more. The HAR is how you see it.
- Your Claude works from files. If the knowledge is only in your head or in a chat that scrolled
  away, the next session starts from zero.

## What you end up with

A folder, in a GitHub repo of your own, shaped like this:

```
exampleapp-kb/
  API.md        what the app calls, how auth works, what is proven, what is not
  STATUS.md     where things stand, dated, with corrections kept on record
  tools/        har_summary.py from this kit
  .gitignore    keeps HAR files and secrets out of git
```

Templates for the two Markdown files are in `skills/web-app-to-api-reference/templates/`. Start
the `.gitignore` with at least `*.har`, `.env` and `.env.*`.

## Step 0: cheaper sources first

A HAR capture is slow, needs you at the keyboard, and carries session secrets. Before you capture,
check whether the answer is already public.

1. **A published spec.** Many apps publish one. For ExampleApp you would try
   `https://api.example.com/openapi.json`, `/swagger.json` and `/api/docs`, and search the
   vendor's help center for "API". Ask your Claude to fetch the spec and list the operations. If
   an official API or an export already covers your task, use that and skip the rest.
2. **The app's JavaScript bundle.** Open DevTools, Sources tab, and look for a large file named
   like `index-<hash>.js` or `main.<hash>.js`. GraphQL apps embed their queries and mutations in
   this file as plain text. Your Claude can search a saved copy for `mutation ` and `query `.
3. **Validation errors.** For GraphQL, send a mutation with one made-up field name. The error
   message usually lists the fields the server does accept. This is a read of the schema, not a
   write: nothing is saved when validation fails.

A HAR is still the only reliable way to learn optional fields, the order the app calls things in,
and the headers it adds. Use the cheaper sources to shrink the list of what the HAR has to show you.

## Step 1: plan the capture

Write the list of actions before you open DevTools. One capture that answers ten questions beats
ten captures.

- **List the actions**, numbered, one line each. For example: "1. Open the projects list.
  2. Open one project. 3. Edit the project name and save. 4. Undo the edit and save."
- **One action at a time.** Click, wait for the page to settle, then move to the next number.
  Mixed clicks produce a HAR you cannot read back.
- **Throwaway records.** Every write goes to a record you created for this purpose and will delete
  after, never to a real customer. Name it so it is obvious, for example
  "ZZ TEST delete me".
- **Preserve log.** Tick it before the first click so a page navigation does not wipe the list.
- **One reload at the end.** After the last action, reload the page once. The reload shows every
  call the app makes on startup, which tells you what reads exist.
- **Write down the identity.** Which account you were signed in as, and roughly what time. These
  go into `API.md` later.

Hand the list to your Claude as well. It will use it to label the calls it finds.

## Step 2: capture in Chrome

Menu steps as of Chrome 130 and later. The labels moved a few times before that, so if yours look
different, update Chrome first.

1. Sign in to the app in a normal Chrome window (not Incognito, so the session behaves as usual).
2. Open DevTools: `Cmd+Option+I` on a Mac, `F12` or `Ctrl+Shift+I` on Windows.
3. Click the **Network** tab.
4. Tick **Preserve log**. Optional: tick **Disable cache** so the reload at the end fetches
   everything rather than serving some of it from cache.
5. In the filter box, type `domain:api.example.com` (your app's API host). This only
   hides rows from view. The export still includes everything, so expect noise in the file.
6. Do your numbered actions, one at a time. Reload once at the end.
7. Export. In the Network panel action bar, click **Export HAR (sanitized)...**. Or right-click any
   row and choose **Save all as HAR (sanitized)**. Save it somewhere outside your repo, for example
   `~/Downloads/exampleapp-2026-11-20.har`.

**Sanitized versus with sensitive data.** Since Chrome 130 the default export is sanitized. That
removes exactly three headers: `Cookie`, `Set-Cookie`, and `Authorization`. Everything else stays:
URLs, query strings, every other header, request bodies, response bodies. A sanitized HAR is enough
to map what the app calls and what the payloads look like, which is the whole point of this page.

If you need the auth header values too (you usually do not; see Step 5), turn on DevTools
Settings, Preferences, Network, **Allow to generate HAR with sensitive data**. Since Chrome 133,
with that on, the Export HAR button opens a menu with both options and you pick **Export HAR (with
sensitive data)**.

**What survives sanitizing.** Tokens in URLs (`?access_token=`), tokens in custom headers
(anything not literally named Cookie, Set-Cookie, or Authorization, so `X-Api-Key` and
`X-CSRF-Token` stay), and tokens inside request and response bodies (a login response often
returns one). Treat every HAR as sensitive, sanitized or not.

## Step 3: treat the HAR as a secret

A HAR is a recording of your logged-in session. Someone with it can often act as you until the
session expires.

- **Never commit it.** Put `*.har` in `.gitignore` before the file exists in the folder. Check with `git check-ignore -v capture.har`
  before any `git add`.
- **Keep it out of the repo folder entirely** if you can. `~/Downloads` or a dated folder outside
  the repo is fine.
- **Delete it when done.** Once `API.md` says what you learned, the HAR has done its job. Decide a
  date and delete it.
- **Strip before sharing.** If someone else needs the file, run `tools/har_summary.py` without
  `--bodies` and send that plain summary, not the HAR. A summary made with `--bodies` is for your
  own eyes only: secret-looking values are redacted, but customer names, phone numbers and
  addresses in the bodies are not. Write every summary outside any repo or shared folder (next to
  the HAR is fine), and delete the `--bodies` one with the HAR. If they truly need the HAR, remove
  bodies and auth-looking headers first, and send it over a private channel, never in a chat room
  or an email thread with many people.
- **Your Claude must never print one raw.** Tell it so, every time. The summary tool exists so it
  never has to.

## Step 4: read the calls out

Do not read the HAR by hand. It is JSON, often tens of megabytes, with every image and font in it.
Run the summary tool instead:

```
python3 tools/har_summary.py ~/Downloads/exampleapp-2026-11-20.har --host api.example.com --bodies --out ~/Downloads/exampleapp-summary.md
```

The summary goes next to the HAR, outside any repo or shared folder. With `--bodies` it is for your
own eyes only and gets deleted with the HAR; a plain summary (no `--bodies`) is the one you may
show someone.

What it gives you, and what to look for in it:

- **Entry counts**: total, kept, dropped. If "kept" is tiny, your `--host` filter is wrong. Run it
  once without `--host` to see the hosts list, then pick the API host from that list.
- **Auth-looking header names**. Names only, never values. This is Step 5.
- **A table of unique calls**: method, host, path, how many times it fired, status codes, request
  content type, whether a request body exists. Numeric ids and UUIDs in paths are collapsed to
  `{id}` so `/projects/123` and `/projects/456` become one row.
- **One sample body per row** with `--bodies`, truncated to 400 characters. Secret-looking values
  are redacted; personal and customer data is not.

Things the tool handles that trip people up:

- **OPTIONS preflights** are dropped by default. They are the browser asking permission, not the
  app doing work. They are useful once: a preflight's `Access-Control-Request-Headers` lists the
  header names the real call will send, even in a sanitized export. Use `--include-options` if you
  want to see them.
- **Base64 bodies.** Chrome sometimes stores a response body as base64, with or without an
  `encoding` field saying so. The tool decodes both.
- **Noise.** Analytics, error reporters, fonts, images. The `--host` filter removes most of it.

Rules for reading what comes out:

- **Read the record, never the label.** A button that says "Archive" may call an endpoint named
  `delete`. A screen called "Reports" may call three unrelated services. The path and body are the
  fact. The UI text is a hint.
- **Never infer state from a HAR.** The HAR shows what was sent at capture time. It does not tell
  you what the record looks like now, whether the write stuck, or what the app would do today.
  Verify with a fresh read.
- **Map actions to rows.** Go down your numbered list from Step 1 and, for each action, note which
  rows fired. Reads fire on page open. Writes fire on save. Most of the value is in matching the
  write payload to the form you filled in.
- **GraphQL is one path, many operations.** A row like `POST /graphql` with count 40 hides forty
  different operations. Ask your Claude to group the sample bodies by `operationName`.

## Step 5: identify auth

The summary's "auth-looking header names" line tells you the pattern. You document the **names**
and where the value comes from. You never write a value down.

| Pattern | What you see in the summary | Where the value lives | How to call later |
|---|---|---|---|
| Cookie session | `cookie` on requests, `set-cookie` on a login response | the browser's cookie jar | from a logged-in tab, `fetch` with `credentials: 'same-origin'` |
| Cookie plus CSRF | `cookie` and `x-csrf-token` or `x-xsrf-token` | token in a `<meta>` tag or a cookie | read the token from the live page before each write |
| Bearer token | `authorization` | often `localStorage`, sometimes memory only | from a logged-in tab; the token may rotate |
| Static app key | a custom header such as `x-api-key` | fixed per app or per account | header value stored in a gitignored `.env`, never in docs |
| Token in the URL | a query parameter like `access_token` | the page's JavaScript | prefer a header pattern if the app offers one |

Whatever pattern you find, confirm it against your own capture before writing it into `API.md`,
and date the claim.

Two cautions:

- Tokens inside a HAR are stale by the time you read them. Do not plan to reuse one.
- Do not ask your Claude to enumerate `localStorage` or all cookies looking for a token. Learn the
  one key name the app uses, write the key name in `API.md`, and read only that key.

## Step 6: replay safely

Replaying a call is how you turn "the app sends this" into "this works when I send it". Order
matters.

1. **Read calls first.** Replay a `GET` or a read-only GraphQL query. Compare the response to what
   the UI shows. If they match, the auth pattern is right.
2. **Prefer calling from a logged-in browser tab.** Open the app, open DevTools Console, and run
   `fetch` there with `credentials: 'same-origin'`. The token never leaves the browser and you never
   have to copy it anywhere. Only move to a script on your machine once reads are proven and you
   have a reason (bulk work, scheduling).
3. **Writes only with a dry run.** Before the first write, print exactly what would be sent: the
   path, the method, the full body, the record id. Read it. Then send it once.
4. **One record.** The first write targets one throwaway record. Not two. Not a loop.
5. **Verify with a fresh read.** Read the record back through a different call than the one you
   wrote with, or in the UI. A write is proven when the fresh read shows the change.
6. **A 200 can still carry a failure.** Many apps return HTTP 200 with `{"success": false}` or an
   `errors` array in the body. Always read the response body, not just the status code.
7. **A failed call may still have executed.** A timeout or a network error on your side does not
   mean the server did nothing. Read before you retry.

Give your Claude this list as the rule for the session. "Read-only unless I say otherwise" is a
good default to say out loud at the start.

## Step 7: write API.md

`API.md` is the start-here file. Copy the `API.md` template and fill it in. The shape:

1. **Provenance block at the top.** Mapped date, host, signed-in identity, which HAR (file name,
   size, entry count, how many non-OPTIONS), time window. Not the HAR itself.
2. **Auth.** Header names, where each value comes from, how to call. No values.
3. **One section per capability.** Method, path, a sample request body, a sample response shape,
   and a "Proven" line with the date and the record id you proved it on.
4. **Limits and traps.** Every limit names four things: what was refused, where (which host,
   which account or role), when (date), and the exact error text. "It does not work" is not a
   finding. "`POST /v1/projects` returned 403 `{"detail":"insufficient_scope"}` on the staff
   account on 2026-11-20" is.
5. **UNTESTED, not "unavailable".** If you did not try it, say UNTESTED. The word "unavailable"
   gets copied forward and becomes a false fact nobody re-checks.

Keep the file readable in one sitting. If it passes 400 lines, split by domain (one file per area
of the app) and keep `API.md` as the index.

## Step 8: STATUS.md, and keeping it honest

`STATUS.md` says where things stand today. `API.md` says how things work. Copy the `STATUS.md`
template from the same folder.

- **"Last updated" at the top.** A reader with ten seconds learns how stale the file is.
- **Newest change first.** A short block at the top for whatever changed most recently.
- **A capability table.** Capability, state (working, proven, UNTESTED, broken), evidence with an
  id and a date.
- **Dated claims, "as last seen".** Write "returns 200 as of 2026-11-20", never "returns 200". The
  app will change under you.
- **Corrections stay on record.** When a claim turns out wrong, do not silently edit it. Add a
  dated "CORRECTED" line under it that says what was believed, what is true, and how you found out.
  The wrong version is evidence of how the app behaved then, and it stops the next person from
  re-learning the same wrong thing.
- **Open items with an owner.** What is unknown, who is finding out, by when.

## Step 9: promote learnings back

A learning left in a project folder, a chat, or your head gets re-learned the hard way. Every time
a session discovers something about the app (a new endpoint, a trap, a limit, a corrected claim):

1. Put it in `API.md` or `STATUS.md` the same day.
2. Commit with a message that says what was learned, for example
   `docs: projects PATCH requires full body, partial returns 422`.
3. If your Claude has a `CLAUDE.md` for this repo, add a one-line pointer there for anything a new
   session must know before its first call.

The test of a good knowledge base: a fresh session, given only the folder, can make a correct read
call on the first try and knows which writes are safe.

## Ask your Claude

Copy and paste, one at a time.

1. "Here is a HAR I exported. Run `tools/har_summary.py` on it with `--bodies` and list every unique
   method and path, grouped by host, with one sample body each. Never print cookies, tokens, or
   Authorization headers. Never open the HAR directly."

2. "From the summary, name the auth pattern. Give me header names only and tell me where each value
   probably comes from. Do not print any value."

3. "Here is my numbered action list from the capture. Match each action to the rows in the summary.
   For each write, show me the request body shape with the values replaced by field types."

4. "Fetch `https://api.example.com/openapi.json` and list the operations. Then tell me
   which paths from my HAR summary are not in the public spec."

5. "Draft `API.md` from the `API.md` template using the summary and the spec. Mark everything we have
   not replayed as UNTESTED. Put the provenance block at the top."

6. "Before we replay the first write: print the exact request you would send (method, path, full
   body, record id). Do not send it. Wait for me to say go."

7. "Every call this task needs is proven. Write a small script for it that dry-runs by default and
   only sends with `--send`. Save it beside `API.md` and note it in `STATUS.md`."
