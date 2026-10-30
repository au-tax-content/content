"""Shared helpers: Instagram Graph API calls, GitHub issues, file paths. Standard library only."""
import json, os, glob, time, urllib.request, urllib.parse, urllib.error
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://graph.instagram.com/v25.0"
ACCOUNTS = json.load(open(os.path.join(ROOT, "accounts.json")))


class IGError(Exception):
    pass


def token_for(account):
    return os.environ.get(ACCOUNTS[account]["secret"], "").strip()


def _request(method, url, params=None, data=None, retries=3):
    if params:
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=body, method=method)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            txt = e.read().decode(errors="replace")
            try:
                err = json.loads(txt).get("error", {})
            except Exception:
                err = {"message": txt[:500]}
            last = IGError(f"HTTP {e.code}: {err.get('message')} (code {err.get('code')}, subcode {err.get('error_subcode')})")
            if e.code < 500 and e.code != 429:
                raise last
        except urllib.error.URLError as e:
            last = IGError(f"Network error: {e}")
        time.sleep(5 * (attempt + 1))
    raise last


FB_API = "https://graph.facebook.com/v25.0"


def _route(path, token):
    """Instagram-login tokens (IG...) use graph.instagram.com and 'me'.
    Facebook/system-user tokens (EAA...) use graph.facebook.com with the account's numeric IG id."""
    if token.startswith("EAA"):
        for cfg in ACCOUNTS.values():
            if os.environ.get(cfg["secret"], "").strip() == token and path.split("/")[0] == "me":
                return f"{FB_API}/{cfg['ig_id']}" + path[2:]
        return f"{FB_API}/{path}"
    return f"{API}/{path}"


def ig_get(path, token, **params):
    params["access_token"] = token
    return _request("GET", _route(path, token), params=params)


def ig_post(path, token, **data):
    data["access_token"] = token
    return _request("POST", _route(path, token), data=data)


def now_utc():
    return datetime.now(timezone.utc)


def parse_time(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def iter_posts():
    """Yield (path_to_post_json, post_dict) for every queued or published post."""
    for f in sorted(glob.glob(os.path.join(ROOT, "posts", "*", "*", "post.json"))):
        with open(f) as fh:
            yield f, json.load(fh)


def save_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def open_issue(title, body):
    """Open a GitHub issue (emails the repo owner). Skips if an open issue with the same title exists."""
    repo, tok = os.environ.get("GITHUB_REPOSITORY"), os.environ.get("GITHUB_TOKEN")
    if not repo or not tok:
        print(f"[issue skipped, no GitHub env] {title}\n{body}")
        return
    hdr = {"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json", "User-Agent": "content-bot"}
    try:
        q = urllib.request.Request(f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100", headers=hdr)
        with urllib.request.urlopen(q, timeout=30) as r:
            if any(i.get("title") == title for i in json.loads(r.read())):
                return
        req = urllib.request.Request(f"https://api.github.com/repos/{repo}/issues", method="POST",
                                     data=json.dumps({"title": title, "body": body}).encode(),
                                     headers={**hdr, "Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=30).read()
    except Exception as e:
        print(f"Could not open issue: {e}")
