"""Write stats/README.md: a phone-friendly snapshot GitHub renders for free (no Claude needed).
Runs after every stats pull. Link: https://github.com/au-tax-content/content/blob/main/stats/README.md"""
import csv, json, os
from datetime import datetime, timezone, timedelta
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AEDT = timezone(timedelta(hours=11))
NAMES = {"retained": "Retained (@retained.au)", "returnpolicy": "Return Policy (@returnpolicy.au)"}
out = [f"# Instagram stats\n\nUpdated {datetime.now(AEDT):%a %d %b %Y, %-I:%M %p} (Sydney). Refreshes about every 4 hours.\n"]
for acct, name in NAMES.items():
    d = os.path.join(ROOT, "stats", acct)
    try:
        rows = list(csv.reader(open(os.path.join(d, "account.csv"))))[1:]
        followers = rows[-1][1] if rows else "0"
        week_ago = [r for r in rows if r[0] <= (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()]
        prev = week_ago[-1][1] if week_ago else (rows[0][1] if rows else "0")
        daily = list(csv.DictReader(open(os.path.join(d, "daily.csv"))))[-7:]
        media = json.load(open(os.path.join(d, "media.json")))
    except FileNotFoundError:
        continue
    out.append(f"## {name}\n\n**Followers: {followers}** ({int(followers) - int(prev):+d} in the last 7 days)\n")
    out.append("| Day | Reach | Profile visits |\n| --- | ---: | ---: |")
    out += [f"| {r['date']} | {r['reach']} | {r['profile_views']} |" for r in daily]
    top = sorted(media.values(), key=lambda v: v["metrics"].get("reach") or 0, reverse=True)[:5]
    out.append("\n**Top posts by reach**\n\n| Post | Type | Reach | Likes | Saves | Shares |\n| --- | --- | ---: | ---: | ---: | ---: |")
    for v in top:
        m = v["metrics"]
        out.append(f"| [{v.get('post_id') or '?'}]({v.get('permalink')}) | {v.get('type','').title()} | {m.get('reach') or 0} | {m.get('likes') or 0} | {m.get('saved') or 0} | {m.get('shares') or 0} |")
    out.append("")
open(os.path.join(ROOT, "stats", "README.md"), "w").write("\n".join(out) + "\n")
print("wrote stats/README.md")
