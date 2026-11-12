"""Save Instagram's currently trending licensed music (and a few searches) to stats/audio.json,
so the weekly run can pick a track for each Reel (post.json "audio_id")."""
import json, os
from common import CURRENT, ROOT, ACCOUNTS, IGError, token_for, ig_get, save_json, now_utc

out = {"fetched_at": now_utc().isoformat(timespec="minutes"), "trending": [], "searches": {}}
CURRENT["account"] = "retained"
t = token_for("retained")
uid = ACCOUNTS["retained"]["ig_id"]
def grab(**q):
    res = ig_get("ig_audio", t, audio_type="music", user_id=uid, **q)
    return [{k: a.get(k) for k in ("audio_id", "title", "display_artist", "duration_in_ms")} for a in res.get("audio", [])]
try:
    out["trending"] = grab()
    for q in ["lofi", "upbeat", "chill", "money", "corporate", "hip hop instrumental", "piano", "emotional", "inspirational", "acoustic", "motivational"]:
        try:
            out["searches"][q] = grab(search_query=q)[:10]
        except IGError as e:
            out["searches"][q] = f"ERR {e}"
except IGError as e:
    out["error"] = str(e)
save_json(os.path.join(ROOT, "stats", "audio.json"), out)
print(json.dumps(out)[:1500])
