"""Setup check: confirm each Instagram token works and can publish. Posts nothing."""
from common import ACCOUNTS, IGError, token_for, ig_get

ok = True
for acct, cfg in ACCOUNTS.items():
    t = token_for(acct)
    if not t:
        print(f"{cfg['handle']}: MISSING secret {cfg['secret']}"); ok = False; continue
    try:
        me = ig_get("me", t, fields="user_id,username,account_type,followers_count")
        lim = ig_get("me/content_publishing_limit", t, fields="quota_usage,config")
        print(f"{cfg['handle']}: OK as @{me.get('username')} ({me.get('account_type')}, {me.get('followers_count')} followers); publishing quota {lim}")
        if me.get("username") != cfg["handle"]:
            print(f"  WARNING: token belongs to @{me.get('username')}, expected @{cfg['handle']}"); ok = False
    except IGError as e:
        print(f"{cfg['handle']}: FAILED {e}"); ok = False
raise SystemExit(0 if ok else 1)
