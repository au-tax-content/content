"""Setup check: confirm each Instagram token works and can publish. Posts nothing."""
from common import CURRENT, ACCOUNTS, IGError, token_for, ig_get

ok = True
for acct, cfg in ACCOUNTS.items():
    t = token_for(acct)
    CURRENT["account"] = acct
    if not t:
        print(f"{cfg['handle']}: MISSING secret {cfg['secret']}"); ok = False; continue
    try:
        me = ig_get("me", t, fields="username,followers_count")
        lim = ig_get("me/content_publishing_limit", t, fields="quota_usage,config")
        kind = 'Instagram-login token' if t.startswith('IG') else 'Facebook/system-user token'
        print(f"{cfg['handle']}: OK ({kind}) as @{me.get('username')} ({me.get('followers_count')} followers); publishing quota {lim}")
        if me.get("username") != cfg["handle"]:
            print(f"  WARNING: token belongs to @{me.get('username')}, expected @{cfg['handle']}"); ok = False
    except IGError as e:
        print(f"{cfg['handle']}: FAILED {e}"); ok = False
# Upload test: ask Instagram to fetch a real slide into an unpublished container (expires unused after 24h).
import subprocess, time, os
sha = subprocess.run(["git","rev-parse","HEAD"],capture_output=True,text=True).stdout.strip()
repo = os.environ.get("GITHUB_REPOSITORY","au-tax-content/content")
url = f"https://raw.githubusercontent.com/{repo}/{sha}/posts/retained/2026-11-04-RT-01-start-here/1.jpg"
CURRENT["account"] = "retained"
t = token_for("retained")
if t:
    try:
        from common import ig_post
        c = ig_post("me/media", t, image_url=url, is_carousel_item="true")
        for _ in range(15):
            st = ig_get(c["id"], t, fields="status_code"); 
            if st.get("status_code") in ("FINISHED","ERROR"): break
            time.sleep(4)
        print(f"Upload test (not published): {st.get('status_code')}")
        ok = ok and st.get("status_code") == "FINISHED"
    except IGError as e:
        print(f"Upload test FAILED: {e}"); ok = False
# Reel test: same idea for video (container only, never published).
reel = "posts/retained/2026-11-04-RT-04-reel-pay-less-tax/reel.mp4"
if t and os.path.exists(reel):
    try:
        c = ig_post("me/media", t, media_type="REELS", video_url=f"https://raw.githubusercontent.com/{repo}/{sha}/{reel}")
        for _ in range(60):
            st = ig_get(c["id"], t, fields="status_code,status")
            if st.get("status_code") in ("FINISHED", "ERROR"): break
            time.sleep(5)
        print(f"Reel test (not published): {st.get('status_code')} {st.get('status','')}")
        ok = ok and st.get("status_code") == "FINISHED"
    except IGError as e:
        print(f"Reel test FAILED: {e}"); ok = False
raise SystemExit(0 if ok else 1)
