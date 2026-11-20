# SESSIONS: who is working what, and how to reach them

**Append only.** Use `printf`, never Write and never Edit. Same discipline as `HOTLINE.md`, and for
the same reason: several sessions write this concurrently.

This file is the map's address book. It exists because `ListAgents` lists **every** Claude session
on the machine, including sessions working entirely different projects, so an orchestrator that
reaches for it has no way to tell which live sessions belong to this map. That is
cross-contamination by design, not by accident. This file shows only yours.

---

## How to find your own address

`ListAgents` **does not list self**, so no session can learn its own name or ref from the tool. But
every session runs under a `claude` process, and that process's PID names its socket in
`/tmp/cc-socks/`. Walk your process ancestry to it:

```bash
pid=$$
while :; do
  set -- $(ps -o pid=,ppid=,comm= -p "$pid" 2>/dev/null)
  [ -z "$1" ] && break
  case "$3" in *claude*) echo "uds:/tmp/cc-socks/$1.sock"; break;; esac
  pid=$2; [ "$pid" -le 1 ] && break
done
```

That path is a valid `SendMessage` `to` value.

**A socket path is unique to a process**, so a dead session fails the send cleanly rather than
reaching a stranger. A name can be reused and a ref can go stale; a socket cannot be silently wrong.
That is the whole safety property, and it is why this file records sockets rather than names.

---

## The protocol

**Register when you claim, before any work**, on the line after you write your `Claimed:` line:

```bash
printf '%s\n' "- [T05 . $(date '+%Y-%m-%d %H:%M')] uds:/tmp/cc-socks/71346.sock . claimed" >> SESSIONS.md
```

Append a second line when you close. Never edit the earlier one:

```bash
printf '%s\n' "- [T05 . $(date '+%Y-%m-%d %H:%M')] uds:/tmp/cc-socks/71346.sock . closed" >> SESSIONS.md
```

**Read the time from `date`, never estimate it.** The examples substitute it, so copy them as
they are. Sessions that pattern-matched the times on neighbouring lines ran over an hour
fast, and on a registry whose whole job is ordering, a plausible invented time is
indistinguishable from a real one. It is one shell call, and it is the only part of the guard a
session can get wrong on its own.

An execution session batching several tickets registers **once**, naming the batch: `[T06,T07,T08]`.

**Then you can reach the orchestrator directly.** Read the `ORCHESTRATOR` line below and use that
socket as your `to`. You do not need to be messaged first, and the orchestrator does not need to
broadcast and ask who is who. What to send and when is in `PROCESS.md`, under The relay.

**Orchestrator: read this file, not `ListAgents`,** when you need to reach a worker.

**If a map was charted before this file existed**, its workers have no addresses here and cannot
find yours. Fall back to the orchestrator initiating: message each worker first, and it replies by
copying your message's `from` attribute into its `to`. Then have it register, so the fallback is
needed once rather than every time.

---

## Not this map

<!-- Peers on other projects, recorded once so nobody messages them again. Only worth an entry
where a peer was mistaken for one of ours, or where its work touches this map even though it is not
on it. Note that second case explicitly: it is a courtesy check before a dependent ticket runs, not
a relay. -->

-

---

## Registry

**This section is last in the file, and it has to stay last.** Registration is a bare
`printf ... >> SESSIONS.md`, which always lands at end of file, so any heading placed below this one
silently collects every worker's line. That is not hypothetical: it happened on two maps, and on the
second one all five round-1 sessions registered under **Not this map** while this section stayed
empty. Append-only is the right discipline for concurrent writers, and the cost of it is that the
file can only ever grow at the bottom. **Do not add a section after this one, and do not add round
subheadings inside it**: a worker cannot append into the middle of a file, and the round is already
readable from the ticket ID and the date.

<!-- Charting writes the ORCHESTRATOR line at scaffold, from the snippet above, and it is the one
line in this file that is not appended by a worker. Everything after it is appended, in the order it
happened. -->

- [ORCHESTRATOR . <date time>] `uds:/tmp/cc-socks/<pid>.sock` . <what this session is, and how long
  it expects to be live>
