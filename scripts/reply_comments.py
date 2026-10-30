"""Reply publicly to comments that contain the account's keyword (ABN / CLAIM) within minutes,
so commenters get an answer fast and the post gets an early engagement boost.

Only keyword comments get an automatic reply. Questions and everything else are left for the weekly
review (they show up in stats/<account>/comments.json). Replies rotate through accounts.json
keyword_replies, and each comment is answered once (ids tracked in stats/<account>/replied.json).
Edit keyword_replies when a lead magnet goes live (e.g. point to the link in bio).
"""
import json, os, re
from datetime import timedelta
from common import CURRENT, ROOT, ACCOUNTS, IGError, token_for, ig_get, ig_post, save_json, now_utc, parse_time

MAX_PER_RUN = 25

for acct, cfg in ACCOUNTS.items():
    token = token_for(acct)
    kw = cfg.get("keyword")
    if not token or not kw:
        continue
    CURRENT["account"] = acct
    path = os.path.join(ROOT, "stats", acct, "replied.json")
    try:
        replied = set(json.load(open(path)))
    except Exception:
        replied = set()
    pattern = re.compile(rf"\b{re.escape(kw)}\b", re.I)
    sent = 0
    try:
        media = ig_get("me/media", token, fields="id,timestamp,comments_count", limit=25).get("data", [])
    except IGError as e:
        print(f"{acct}: {e}"); continue
    cutoff = now_utc() - timedelta(days=14)
    for m in media:
        if not m.get("comments_count") or parse_time(m["timestamp"].replace("+0000", "+00:00")) < cutoff:
            continue
        try:
            comments = ig_get(f"{m['id']}/comments", token, fields="id,text,username", limit=100).get("data", [])
        except IGError as e:
            print(f"{acct}: comments {e}"); continue
        for c in comments:
            if c["id"] in replied or sent >= MAX_PER_RUN:
                continue
            if (c.get("username") or "").lower() == cfg["handle"].lower():
                replied.add(c["id"]); continue
            if pattern.search(c.get("text") or ""):
                msg = cfg["keyword_replies"][len(replied) % len(cfg["keyword_replies"])]
                try:
                    ig_post(f"{c['id']}/replies", token, message=msg)
                    sent += 1
                except IGError as e:
                    print(f"{acct}: reply failed {e}"); continue
            replied.add(c["id"])
    save_json(path, sorted(replied))
    print(f"{acct}: replied to {sent} keyword comment(s)")
