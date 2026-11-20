# Surface checklist

The inventory `peachy-sweep` walks. The discipline lives in that skill; this is just the list, so
the sweep does not miss the surface nobody would have thought of.

Most projects touch four or five of these. Walk the whole list anyway: the value is in the
unexpected one.

**Before trusting any surface, read what is already known about it.** Nearly all of these have a
gotcha that is not discoverable from the tool: a filter that hides rows, a field that lies, a
permission that needs a human tap, an ID that looks canonical and is not, a database that is dead
but still lists its tables from cache. Those live in memory, many flagged. Read the entry
**before** you build on the output.

---

## Documents and filing

- Google Drive, both the API tools and the local DriveFS mount. They fail differently.
- Local folders: the Desktop, prior project folders, Downloads, other repos.
- Attachments living inside a tracker (Airtable, Notion, Monday) rather than in Drive.
- **PDFs with an annotation layer.** Text extraction routinely drops these. Where a number is
  load-bearing, render the page and look at it.
- Spreadsheets attached to records, which often carry the real model rather than the summary.

## Systems of record

- A tracker or database (Airtable, Notion, Supabase): the schema first, then records.
- A reporting tool over a database, and be precise about which database. Two can look alike,
  and a stale one still lists its tables.
- The operational platform's own admin UI, and separately its API. They do not always agree.
- Accounting and banking: the ledger, the bank, the card platform. Each holds a different slice,
  and a transaction absent from one is routinely present in another.
- The password manager, both for credentials and as the inventory of what accounts exist.

## People and correspondence

- Gmail, including aliases and shared mailboxes, not just the primary.
- Slack, including channels you are not in but can search. Some artifact types live only here.
- Meeting transcripts and notes.
- Calendar, often the only record of who was actually in a room.

## Web and third party

- Vendor portals reachable only through a browser session.
- Public filings, registries, statutes.
- The vendor's own documentation, read as primary source rather than a write-up of it.

## Code and infrastructure

- Local repos, which often carry the mirror or the script that already answers the question.
- Issue trackers, for the decision history behind a current state.

---

## Reachability, not existence

The point of the sweep is not that a surface exists, it is that **it answers from this session**.
Confirm with one trivial call each: the tool responds, the account is the right account, the query
language behaves as expected. A surface that is listed and unreachable is worse than one you knew
was out of reach, because plans get written against it.
