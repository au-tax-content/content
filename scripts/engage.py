"""Find fresh posts worth commenting on (for Daniel to comment on by hand, never automated).
Uses Instagram hashtag search (limit: 30 unique hashtags per account per 7 days, so keep the list short).
Writes stats/engage.json: per account, recent posts from relevant hashtags with permalink, caption start, likes, comments, age."""
import os
from datetime import timedelta
from common import CURRENT, ROOT, ACCOUNTS, IGError, token_for, ig_get, save_json, now_utc, parse_time

TAGS = {
  "retained": ["smallbusinessaustralia", "soletraderaustralia", "australiansmallbusiness", "tradieaustralia", "sidehustleaustralia"],
  "returnpolicy": ["moneytipsaustralia", "personalfinanceaustralia", "taxtimeaustralia", "firsthomebuyeraustralia", "nurseaustralia"],
}
out = {"fetched_at": now_utc().isoformat(timespec="minutes")}
cut = now_utc() - timedelta(days=4)
for acct, tags in TAGS.items():
    t = token_for(acct)
    if not t:
        continue
    CURRENT["account"] = acct
    uid = ACCOUNTS[acct]["ig_id"]
    posts, errs = [], {}
    for tag in tags:
        try:
            hid = ig_get("ig_hashtag_search", t, user_id=uid, q=tag)["data"][0]["id"]
            for edge in ("top_media", "recent_media"):
                res = ig_get(f"{hid}/{edge}", t, user_id=uid, limit=25,
                             fields="id,caption,permalink,timestamp,like_count,comments_count,media_type")
                for m in res.get("data", []):
                    ts = m.get("timestamp")
                    if ts and parse_time(ts.replace("+0000", "+00:00")) < cut:
                        continue
                    posts.append({"tag": tag, "edge": edge, "permalink": m.get("permalink"), "timestamp": ts,
                                  "likes": m.get("like_count"), "comments": m.get("comments_count"),
                                  "type": m.get("media_type"), "caption": (m.get("caption") or "")[:400]})
        except (IGError, KeyError, IndexError) as e:
            errs[tag] = str(e)[:200]
    seen, uniq = set(), []
    for p in posts:
        if p["permalink"] and p["permalink"] not in seen:
            seen.add(p["permalink"]); uniq.append(p)
    out[acct] = {"posts": uniq, "errors": errs}
    print(acct, len(uniq), "posts", errs)
save_json(os.path.join(ROOT, "stats", "engage.json"), out)
