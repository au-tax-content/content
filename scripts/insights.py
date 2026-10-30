"""Collect stats for both accounts into stats/<account>/.

Files written:
  account.csv   one row per run: followers, follows, media count
  daily.csv     one row per day: account-level reach/views/engagement/profile visits (yesterday, Melbourne-agnostic UTC day)
  media.json    latest metrics for every feed post and reel from the last 120 days, keyed by media id
  stories.json  metrics for stories (kept after Instagram deletes them; story stats only live 24h)
  comments.json recent comment text per post (no usernames), for content ideas
Metrics that Instagram rejects are recorded under "_errors" instead of failing the run.
"""
import csv, json, os
from datetime import timedelta
from common import CURRENT, ROOT, ACCOUNTS, IGError, token_for, ig_get, iter_posts, save_json, now_utc, parse_time, open_issue

FEED_METRICS = ["reach", "views", "likes", "comments", "saved", "shares", "total_interactions", "profile_visits", "follows"]
REEL_METRICS = ["reach", "views", "likes", "comments", "saved", "shares", "total_interactions"]
STORY_METRICS = ["reach", "views", "replies", "shares", "follows", "profile_visits", "navigation", "total_interactions"]
ACCOUNT_METRICS = ["reach", "views", "accounts_engaged", "total_interactions", "profile_views", "follows_and_unfollows", "profile_links_taps"]


def load(path, default):
    try:
        return json.load(open(path))
    except Exception:
        return default


def media_metrics(mid, metrics, token):
    """Ask for all metrics at once; if Instagram rejects the set, fall back one by one."""
    out, errors = {}, {}
    try:
        res = ig_get(f"{mid}/insights", token, metric=",".join(metrics))
        for m in res.get("data", []):
            vals = m.get("values") or [{}]
            out[m["name"]] = m.get("total_value", {}).get("value", vals[0].get("value"))
        return out, errors
    except IGError:
        pass
    for m in metrics:
        try:
            res = ig_get(f"{mid}/insights", token, metric=m)
            d = (res.get("data") or [{}])[0]
            vals = d.get("values") or [{}]
            out[m] = d.get("total_value", {}).get("value", vals[0].get("value"))
        except IGError as e:
            errors[m] = str(e)[:160]
    return out, errors


def append_csv(path, row):
    new = not os.path.exists(path)
    with open(path, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(row.keys()))
        if new:
            w.writeheader()
        w.writerow(row)


def post_ids_by_media():
    return {p.get("media_id"): p.get("id") for _, p in iter_posts() if p.get("media_id")}


def run(acct, token):
    d = os.path.join(ROOT, "stats", acct)
    os.makedirs(d, exist_ok=True)
    now = now_utc()
    ids = post_ids_by_media()

    me = ig_get("me", token, fields="username,followers_count,follows_count,media_count")
    append_csv(os.path.join(d, "account.csv"), {
        "fetched_at": now.isoformat(timespec="minutes"), "followers": me.get("followers_count"),
        "follows": me.get("follows_count"), "media_count": me.get("media_count")})

    # account-level daily totals for yesterday (UTC), once per day
    daily_path = os.path.join(d, "daily.csv")
    yday = (now - timedelta(days=1)).date().isoformat()
    done = os.path.exists(daily_path) and any(r.get("date") == yday for r in csv.DictReader(open(daily_path)))
    if not done:
        since = int(parse_time(yday + "T00:00:00+00:00").timestamp())
        row = {"date": yday}
        for m in ACCOUNT_METRICS:
            try:
                res = ig_get("me/insights", token, metric=m, period="day", metric_type="total_value",
                             since=since, until=since + 86400)
                dd = (res.get("data") or [{}])[0]
                tv = dd.get("total_value", {})
                if m == "follows_and_unfollows" and tv.get("breakdowns"):
                    row[m] = json.dumps(tv["breakdowns"])
                else:
                    row[m] = tv.get("value")
            except IGError as e:
                row[m] = f"ERR {str(e)[:60]}"
        append_csv(daily_path, row)

    # feed posts and reels
    media = load(os.path.join(d, "media.json"), {})
    cutoff = now - timedelta(days=120)
    res = ig_get("me/media", token, fields="id,caption,media_type,media_product_type,timestamp,permalink,like_count,comments_count", limit=50)
    comments = load(os.path.join(d, "comments.json"), {})
    for m in res.get("data", []):
        if parse_time(m["timestamp"].replace("+0000", "+00:00")) < cutoff:
            continue
        mets = REEL_METRICS if m.get("media_product_type") == "REELS" else FEED_METRICS
        vals, errs = media_metrics(m["id"], mets, token)
        media[m["id"]] = {
            "post_id": ids.get(m["id"]), "type": m.get("media_product_type") or m.get("media_type"),
            "timestamp": m["timestamp"], "permalink": m.get("permalink"),
            "caption_start": (m.get("caption") or "")[:80], "metrics": vals,
            "fetched_at": now.isoformat(timespec="minutes"), **({"_errors": errs} if errs else {})}
        if m.get("comments_count"):
            try:
                c = ig_get(f"{m['id']}/comments", token, fields="text,timestamp,like_count", limit=50)
                comments[m["id"]] = [{"text": x.get("text"), "timestamp": x.get("timestamp"), "likes": x.get("like_count")}
                                     for x in c.get("data", [])]
            except IGError:
                pass
    save_json(os.path.join(d, "media.json"), media)
    save_json(os.path.join(d, "comments.json"), comments)

    # stories (only visible for 24h, so this runs every few hours)
    stories = load(os.path.join(d, "stories.json"), {})
    try:
        sres = ig_get("me/stories", token, fields="id,timestamp,permalink,media_type")
        for s in sres.get("data", []):
            vals, errs = media_metrics(s["id"], STORY_METRICS, token)
            prev = stories.get(s["id"], {})
            stories[s["id"]] = {"post_id": ids.get(s["id"]), "timestamp": s["timestamp"],
                                "metrics": {**prev.get("metrics", {}), **{k: v for k, v in vals.items() if v is not None}},
                                "fetched_at": now.isoformat(timespec="minutes"), **({"_errors": errs} if errs else {})}
    except IGError as e:
        print(f"stories: {e}")
    save_json(os.path.join(d, "stories.json"), stories)


def main():
    for acct in ACCOUNTS:
        token = token_for(acct)
        CURRENT["account"] = acct
        if not token:
            print(f"{acct}: no token, skipping")
            continue
        try:
            run(acct, token)
            print(f"{acct}: ok")
        except IGError as e:
            print(f"{acct}: {e}")
            if "code 190" in str(e):
                open_issue(f"Instagram token expired or revoked: {acct}",
                           f"Generate a new token for {ACCOUNTS[acct]['handle']} in the Meta app and replace the secret `{ACCOUNTS[acct]['secret']}`.\n\n```\n{e}\n```")


if __name__ == "__main__":
    main()
