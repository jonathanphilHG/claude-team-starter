#!/usr/bin/env python3
"""Summarize a Chrome DevTools HAR file as Markdown, without leaking secrets.

Usage:
  python3 tools/har_summary.py capture.har [--host api.example.com]
         [--include-options] [--bodies] [--list-headers] [--out summary.md]

What it prints:
  - entry counts (total, kept, dropped)
  - the NAMES of auth-looking request headers it saw (never their values)
  - one row per unique METHOD + host + path (query string stripped,
    numeric path segments and UUIDs collapsed to {id}) with count,
    status codes seen, request content type, and whether a request body exists
  - with --bodies, one truncated sample request body and response body per row
  - with --list-headers, every request header name seen (names only)

Safety rules, in code below:
  - Never prints Cookie, Set-Cookie, Authorization, or any header whose name
    contains token, key, secret, session, csrf, xsrf, auth.
  - Never prints any header VALUE at all. Names only.
  - Never prints query strings (they often carry tokens).
  - Inside printed bodies, replaces with <redacted>: the value of any
    secret-looking key (password, pwd, pass, secret, token, auth, cookie,
    session, sid, key, api_key, otp, pin, ssn, card, cvv and similar, any case)
    in JSON at any depth, in form bodies (a=1&b=2) and in query-like strings;
    then JWTs and 32+ char hex or base64 runs.
  - Bodies can still hold personal or customer data (names, phone numbers,
    addresses), so --bodies output says so at the top. A plain summary (no
    --bodies) is the one you may show someone; a --bodies summary is for your
    own eyes only, never shared or committed, and deleted with the capture.

Standard library only. Python 3.8 or newer.
"""

import argparse
import base64
import json
import re
import sys
from collections import Counter, OrderedDict
from urllib.parse import unquote_plus, urlsplit

MAX_BODY_CHARS = 400

SENSITIVE_HEADER_EXACT = {"cookie", "set-cookie", "authorization", "proxy-authorization"}
SENSITIVE_HEADER_PARTS = ("token", "key", "secret", "session", "csrf", "xsrf", "auth")

# A body key is secret-looking if one of its words (split on case, digits and punctuation, so
# userPwd, user_pwd and user[pwd] all give "pwd") is in SECRET_KEY_WORDS, or if the whole key,
# lowercased, contains one of SECRET_KEY_PARTS.
SECRET_KEY_WORDS = {
    "password", "passwd", "pwd", "pass", "passcode", "secret", "token", "auth", "authorization",
    "cookie", "session", "sid", "key", "apikey", "otp", "pin", "ssn", "card", "cvv", "cvc",
    "csrf", "xsrf", "credential", "credentials",
}
SECRET_KEY_PARTS = (
    "password", "passwd", "secret", "token", "auth", "cookie", "session", "sessid", "apikey",
    "api_key", "csrf", "xsrf", "credential",
)

UUID_RE = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
NUMERIC_RE = re.compile(r"^\d+$")

JWT_RE = re.compile(r"[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}")
HEX_RUN_RE = re.compile(r"[0-9a-fA-F]{32,}")
B64_RUN_RE = re.compile(r"[A-Za-z0-9+/_-]{32,}={0,2}")
UUID_ANYWHERE_RE = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$")
KEY_WORD_RE = re.compile(r"[A-Z]+(?![a-z])|[A-Z]?[a-z]+|\d+")
# "key": value, or 'key': value, or key: value (JSON that failed to parse, JS, YAML-ish text)
KEY_COLON_VALUE_RE = re.compile(
    r'(["\']?)([A-Za-z0-9_.$\[\]-]+)\1(\s*:\s*)'
    r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|(?:(?:Bearer|Basic|Digest|Token)\s+)?[^\s,;&}\]]+)',
    re.IGNORECASE)
# key=value at the start, or after ? & ; whitespace or a comma (form bodies, query strings, cookies)
KEY_EQUALS_VALUE_RE = re.compile(r'(^|[?&;,\s])([^=&?;,\s"\']+)=([^&;,\s"\'#]*)')
FORM_BODY_RE = re.compile(r"^[^=&\s]+=[^&\s]*(?:&[^=&\s]+=[^&\s]*)*$")
REDACTED = "<redacted>"


def is_sensitive_header(name):
    n = name.lower()
    if n in SENSITIVE_HEADER_EXACT:
        return True
    return any(part in n for part in SENSITIVE_HEADER_PARTS)


def is_secret_key(name):
    """True when a body key looks like it names a secret. Case-insensitive."""
    name = unquote_plus(str(name))
    low = name.lower()
    if low.endswith("_token") or low.endswith("_secret") or any(p in low for p in SECRET_KEY_PARTS):
        return True
    return any(w.lower() in SECRET_KEY_WORDS for w in KEY_WORD_RE.findall(name))


def _redact_json(value):
    if isinstance(value, dict):
        return {k: (REDACTED if is_secret_key(k) else _redact_json(v)) for k, v in value.items()}
    if isinstance(value, list):
        return [_redact_json(v) for v in value]
    return value


def _redact_form(text):
    out = []
    for pair in text.strip().split("&"):
        key, sep, _ = pair.partition("=")
        out.append(key + sep + REDACTED if sep and is_secret_key(key) else pair)
    return "&".join(out)


def _redact_key_colon(m):
    if not is_secret_key(m.group(2)):
        return m.group(0)
    return m.group(1) + m.group(2) + m.group(1) + m.group(3) + '"' + REDACTED + '"'


def _redact_key_equals(m):
    if not is_secret_key(m.group(2)):
        return m.group(0)
    return m.group(1) + m.group(2) + "=" + REDACTED


def redact(text):
    """Replace secret values and anything token-shaped inside a body with <redacted>."""
    if not text:
        return text
    stripped = text.strip()
    parsed = False
    if stripped[:1] in "{[":
        try:
            text = json.dumps(_redact_json(json.loads(stripped)), ensure_ascii=False)
            parsed = True
        except ValueError:
            pass
    if not parsed and FORM_BODY_RE.match(stripped):
        text = _redact_form(stripped)
    # Second pass for whatever the structured passes could not parse, and for secrets inside
    # string values (a URL carrying ?access_token=..., a cookie string).
    text = KEY_COLON_VALUE_RE.sub(_redact_key_colon, text)
    text = KEY_EQUALS_VALUE_RE.sub(_redact_key_equals, text)
    text = JWT_RE.sub("<redacted>", text)
    text = HEX_RUN_RE.sub("<redacted>", text)

    def b64_sub(m):
        s = m.group(0)
        if UUID_ANYWHERE_RE.match(s):
            return s
        return "<redacted>"

    text = B64_RUN_RE.sub(b64_sub, text)
    return text


def normalize_path(path):
    parts = path.split("/")
    out = []
    for p in parts:
        if p and (NUMERIC_RE.match(p) or UUID_RE.match(p)):
            out.append("{id}")
        else:
            out.append(p)
    return "/".join(out) or "/"


def decode_body(content):
    """Return body text from a HAR content/postData dict, or None.

    Handles `encoding: base64` and bodies that are base64 but lack the
    `encoding` field (seen in real exports). Binary bodies return a marker.
    """
    if not content:
        return None
    text = content.get("text")
    if text is None or text == "":
        return None
    encoding = (content.get("encoding") or "").lower()
    if encoding == "base64":
        return _from_b64(text)
    # Looks like JSON or plain text already
    stripped = text.lstrip()
    if stripped[:1] in "{[<" or " " in stripped[:80]:
        return text
    # Maybe base64 without the encoding field
    if re.fullmatch(r"[A-Za-z0-9+/=\r\n]+", text) and len(text) % 4 == 0 and len(text) >= 8:
        decoded = _from_b64(text)
        if decoded is not None and decoded != "<binary body>":
            return decoded
    return text


def _from_b64(text):
    try:
        raw = base64.b64decode(text, validate=False)
    except Exception:
        return None
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return "<binary body>"


def truncate(text, limit=MAX_BODY_CHARS):
    if text is None:
        return None
    text = " ".join(text.split())
    if len(text) > limit:
        return text[:limit] + " ...(truncated)"
    return text


def load_entries(path):
    with open(path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        if "log" in data and isinstance(data["log"], dict):
            return data["log"].get("entries", [])
        if "entries" in data:
            return data["entries"]
    if isinstance(data, list):
        return data
    raise SystemExit("Could not find log.entries in this file. Is it a HAR?")


def summarize(entries, host_filter, include_options, want_bodies):
    rows = OrderedDict()
    auth_header_names = set()
    all_header_names = set()
    hosts = Counter()
    dropped_options = 0
    dropped_host = 0
    kept = 0

    for e in entries:
        req = e.get("request", {}) or {}
        resp = e.get("response", {}) or {}
        method = (req.get("method") or "?").upper()
        url = req.get("url") or ""
        parts = urlsplit(url)
        host = parts.hostname or "?"
        hosts[host] += 1

        if method == "OPTIONS" and not include_options:
            dropped_options += 1
            continue
        if host_filter and host.lower() != host_filter.lower():
            dropped_host += 1
            continue
        kept += 1

        for h in req.get("headers", []) or []:
            name = h.get("name", "")
            if not name or name.startswith(":"):
                continue
            all_header_names.add(name.lower())
            if is_sensitive_header(name):
                auth_header_names.add(name.lower())
        for h in resp.get("headers", []) or []:
            name = h.get("name", "")
            if name and is_sensitive_header(name):
                auth_header_names.add(name.lower() + " (response)")

        path = normalize_path(parts.path or "/")
        key = (method, host, path)
        row = rows.get(key)
        if row is None:
            row = {"count": 0, "statuses": set(), "req_types": set(), "has_body": False,
                   "req_sample": None, "resp_sample": None}
            rows[key] = row
        row["count"] += 1
        status = resp.get("status")
        if status is not None:
            row["statuses"].add(str(status))
        post = req.get("postData") or {}
        mime = (post.get("mimeType") or "").split(";")[0].strip()
        if mime:
            row["req_types"].add(mime)
        if post.get("text"):
            row["has_body"] = True
            if want_bodies and row["req_sample"] is None:
                row["req_sample"] = truncate(redact(decode_body(post)))
        if want_bodies and row["resp_sample"] is None:
            body = decode_body(resp.get("content") or {})
            if body:
                row["resp_sample"] = truncate(redact(body))

    return {
        "total": len(entries), "kept": kept,
        "dropped_options": dropped_options, "dropped_host": dropped_host,
        "hosts": hosts, "rows": rows,
        "auth_header_names": sorted(auth_header_names),
        "all_header_names": sorted(all_header_names),
    }


def render(summary, source_name, want_bodies, list_headers, host_filter):
    out = []
    out.append("# HAR summary: %s" % source_name)
    out.append("")
    if want_bodies:
        out.append("> **For your own eyes only.** This summary includes sample bodies. Secret-looking "
                   "values are redacted, but bodies can still contain personal or customer data "
                   "(names, phone numbers, addresses). Never share or commit it, and delete it with "
                   "the capture. To show someone, make a summary without `--bodies`.")
        out.append("")
    out.append("- Entries: total %d, kept %d, dropped %d (OPTIONS %d, other hosts %d)" % (
        summary["total"], summary["kept"],
        summary["dropped_options"] + summary["dropped_host"],
        summary["dropped_options"], summary["dropped_host"]))
    if host_filter:
        out.append("- Host filter: %s" % host_filter)
    out.append("- Hosts seen (all entries): " + ", ".join(
        "%s (%d)" % (h, c) for h, c in summary["hosts"].most_common()))
    if summary["auth_header_names"]:
        out.append("- Auth-looking header names seen (values never printed): " +
                   ", ".join(summary["auth_header_names"]))
    else:
        out.append("- Auth-looking header names seen: none (a sanitized export strips "
                   "Cookie, Set-Cookie and Authorization)")
    out.append("")
    out.append("## Unique calls")
    out.append("")
    out.append("| # | Method | Host | Path | Count | Status | Request type | Request body |")
    out.append("|---|---|---|---|---|---|---|---|")
    for i, ((method, host, path), row) in enumerate(summary["rows"].items(), 1):
        out.append("| %d | %s | %s | `%s` | %d | %s | %s | %s |" % (
            i, method, host, path, row["count"],
            ", ".join(sorted(row["statuses"])) or "?",
            ", ".join(sorted(row["req_types"])) or "",
            "yes" if row["has_body"] else "no"))
    if want_bodies:
        out.append("")
        out.append("## Sample bodies (one per row, redacted, max %d chars)" % MAX_BODY_CHARS)
        for i, ((method, host, path), row) in enumerate(summary["rows"].items(), 1):
            out.append("")
            out.append("### %d. %s %s `%s`" % (i, method, host, path))
            out.append("Request body: " + (("`%s`" % row["req_sample"]) if row["req_sample"] else "(none)"))
            out.append("Response body: " + (("`%s`" % row["resp_sample"]) if row["resp_sample"] else "(none or empty)"))
    if list_headers:
        out.append("")
        out.append("## Request header names seen (names only)")
        out.append("")
        for n in summary["all_header_names"]:
            flag = " (sensitive, value never printed)" if is_sensitive_header(n) else ""
            out.append("- %s%s" % (n, flag))
    out.append("")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Summarize a HAR file as Markdown without printing secrets.")
    ap.add_argument("har", help="path to the .har file")
    ap.add_argument("--host", help="keep only entries to this host, for example api.example.com")
    ap.add_argument("--include-options", action="store_true", help="keep OPTIONS preflights (dropped by default)")
    ap.add_argument("--bodies", action="store_true", help="include one redacted sample request and response body per row")
    ap.add_argument("--list-headers", action="store_true", help="list every request header name seen (names only)")
    ap.add_argument("--out", help="write the Markdown here instead of stdout")
    args = ap.parse_args(argv)

    entries = load_entries(args.har)
    summary = summarize(entries, args.host, args.include_options, args.bodies)
    text = render(summary, args.har.split("/")[-1], args.bodies, args.list_headers, args.host)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("Wrote %s (%d unique calls from %d kept entries)" % (args.out, len(summary["rows"]), summary["kept"]))
        if args.bodies:
            print("It includes sample bodies: for your own eyes only. Never share or commit it, "
                  "and delete it with the capture.")
    else:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
