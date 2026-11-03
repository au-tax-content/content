"""Study benchmark creators: their recent public posts (caption, likes, comments, format) via Business Discovery.
Ideas only: never copy a post, caption or design; never quote them. Writes stats/benchmarks.json, ranked by likes."""
import os
from common import CURRENT, ROOT, IGError, token_for, ig_get, save_json, now_utc

BENCH = ["karltondennis", "humphreytalks", "grahamstephan"]
out = {"fetched_at": now_utc().isoformat(timespec="minutes"), "accounts": {}, "errors": {}}
t = token_for("retained")
CURRENT["account"] = "retained"
for h in BENCH:
    try:
        res = ig_get("me", t, fields=f"business_discovery.username({h}){{username,followers_count,media_count,"
                                     f"media.limit(50){{permalink,caption,timestamp,like_count,comments_count,media_type,media_product_type}}}}")
        bd = res.get("business_discovery", {})
        posts = [{"permalink": m.get("permalink"), "timestamp": m.get("timestamp"), "likes": m.get("like_count"),
                  "comments": m.get("comments_count"), "type": m.get("media_product_type") or m.get("media_type"),
                  "caption": (m.get("caption") or "")[:400]} for m in bd.get("media", {}).get("data", [])]
        posts.sort(key=lambda p: p.get("likes") or 0, reverse=True)
        out["accounts"][h] = {"followers": bd.get("followers_count"), "media_count": bd.get("media_count"), "posts": posts}
        print(h, bd.get("followers_count"), len(posts), "posts")
    except IGError as e:
        out["errors"][h] = str(e)[:200]
        print(h, "failed:", str(e)[:200])
save_json(os.path.join(ROOT, "stats", "benchmarks.json"), out)
