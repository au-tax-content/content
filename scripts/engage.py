"""Find fresh posts worth commenting on (Daniel comments by hand, never automated).
Hashtag search needs Meta app review ("Instagram Public Content Access"), so this uses Business Discovery:
the latest posts from a watchlist of public business/creator accounts in each audience's world.
Writes stats/engage.json. Edit WATCH to add or remove accounts (bad handles are just skipped)."""
import os
from datetime import timedelta
from common import CURRENT, ROOT, ACCOUNTS, IGError, token_for, ig_get, save_json, now_utc, parse_time

WATCH = {
  "retained": ["smartcompany", "dynamicbusiness", "startupdaily", "flyingsolo", "myob", "xero", "quickbooksau",
               "forbesaustralia", "shopify", "canva", "squareau", "airtasker", "hipages"],
  "returnpolicy": ["barefootinvestor", "canstar", "finder.au", "mozo_au", "moneymagazineaus", "moneysmartgovau",
                   "realestate.com.au", "domain.com.au", "afrfinancialreview", "theaustralian", "news.com.au", "upbank", "raizinvest"],
}
out = {"fetched_at": now_utc().isoformat(timespec="minutes")}
cut = now_utc() - timedelta(days=5)
for acct, handles in WATCH.items():
    t = token_for(acct)
    if not t:
        continue
    CURRENT["account"] = acct
    posts, errs = [], {}
    for h in handles:
        try:
            res = ig_get("me", t, fields=f"business_discovery.username({h}){{username,followers_count,media.limit(6){{permalink,caption,timestamp,like_count,comments_count,media_type}}}}")
            bd = res.get("business_discovery", {})
            for m in bd.get("media", {}).get("data", []):
                ts = m.get("timestamp")
                if ts and parse_time(ts.replace("+0000", "+00:00")) < cut:
                    continue
                posts.append({"account": h, "followers": bd.get("followers_count"), "permalink": m.get("permalink"),
                              "timestamp": ts, "likes": m.get("like_count"), "comments": m.get("comments_count"),
                              "type": m.get("media_type"), "caption": (m.get("caption") or "")[:500]})
        except IGError as e:
            errs[h] = str(e)[:160]
    out[acct] = {"posts": posts, "errors": errs}
    print(acct, len(posts), "posts;", len(errs), "handles failed:", list(errs)[:20])
    if errs:
        print("  first error:", list(errs.values())[0])
save_json(os.path.join(ROOT, "stats", "engage.json"), out)
