"""Refresh both long-lived Instagram tokens (valid 60 days; refreshing resets the clock).

If Instagram returns a different token string, the new one is saved back to the repository secret
using the GH_PAT secret (a fine-grained token with 'Secrets: read and write' on this repo).
If GH_PAT isn't set and the token changed, an issue explains what to add.
"""
import os, subprocess, urllib.request, json
from common import ACCOUNTS, IGError, token_for, open_issue

for acct, cfg in ACCOUNTS.items():
    old = token_for(acct)
    if not old:
        print(f"{acct}: no token")
        continue
    try:
        with urllib.request.urlopen(
                f"https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token={old}",
                timeout=60) as r:
            res = json.loads(r.read())
    except Exception as e:
        print(f"{acct}: refresh failed {e}")
        open_issue(f"Token refresh failed: {acct}", f"Refreshing the token for {cfg['handle']} failed. If posts stop, generate a new token in the Meta app and replace `{cfg['secret']}`.\n\n```\n{e}\n```")
        continue
    new = res.get("access_token", "")
    days = int(res.get("expires_in", 0)) // 86400
    if not new or new == old:
        print(f"{acct}: refreshed, same token, valid ~{days} days")
        continue
    if os.environ.get("GH_TOKEN"):
        p = subprocess.run(["gh", "secret", "set", cfg["secret"], "--body", new,
                            "--repo", os.environ.get("GITHUB_REPOSITORY", "")], capture_output=True, text=True)
        print(f"{acct}: new token saved" if p.returncode == 0 else f"{acct}: could not save new token: {p.stderr[:200]}")
        if p.returncode != 0:
            open_issue(f"Could not save refreshed token: {acct}", p.stderr[:500])
    else:
        open_issue(f"Refreshed token needs saving: {acct}",
                   "Instagram issued a new token on refresh, but the workflow can't update secrets yet. "
                   "Create a fine-grained personal access token for this repo with 'Secrets: Read and write' and save it as the secret `GH_PAT`, then tell Claude.")
