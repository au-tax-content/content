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
raise SystemExit(0 if ok else 1)
