"""Publish every queued post whose publish_at has arrived.

post.json fields:
  id, account (retained|returnpolicy), type (carousel|image|story), publish_at (ISO with offset),
  caption, images (file names in the same folder, JPEG, in order), status (queued|published|failed|skipped|draft)
Set DRY_RUN=1 to print what would happen without calling Instagram.
"""
import os, subprocess, time, urllib.request
from datetime import timedelta
from common import (CURRENT, ROOT, ACCOUNTS, IGError, token_for, ig_get, ig_post, iter_posts, save_json,
                    now_utc, parse_time, open_issue)

DRY = os.environ.get("DRY_RUN") == "1"
MAX_ATTEMPTS = 3
STALE_AFTER = timedelta(hours=36)   # don't post something far later than planned (e.g. a dated hook)


def raw_base():
    repo = os.environ.get("GITHUB_REPOSITORY", "au-tax-content/content")
    sha = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() or "main"
    return f"https://raw.githubusercontent.com/{repo}/{sha}"


def check_url(url):
    if DRY:
        return
    req = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(req, timeout=30) as r:
        ctype = r.headers.get("Content-Type", "")
        if r.status != 200 or "image" not in ctype:
            raise IGError(f"Image not reachable as an image: {url} ({r.status} {ctype})")


def wait_ready(cid, token, label):
    for _ in range(30):
        st = ig_get(cid, token, fields="status_code,status")
        code = st.get("status_code")
        if code == "FINISHED":
            return
        if code in ("ERROR", "EXPIRED"):
            raise IGError(f"Container {label} {code}: {st.get('status')}")
        time.sleep(4)
    raise IGError(f"Container {label} not ready after 2 minutes")


def publish(post, folder, token):
    rel = os.path.relpath(folder, ROOT).replace(os.sep, "/")
    urls = [f"{raw_base()}/{rel}/{name}" for name in post["images"]]
    for u in urls:
        check_url(u)
    kind = post["type"]
    if DRY:
        print(f"  DRY RUN: would publish {kind} with {len(urls)} image(s)")
        return {"id": "dry-run"}
    if kind == "carousel":
        if not 2 <= len(urls) <= 10:
            raise IGError("Carousel needs 2 to 10 images")
        children = []
        for i, u in enumerate(urls, 1):
            c = ig_post("me/media", token, image_url=u, is_carousel_item="true")
            wait_ready(c["id"], token, f"slide {i}")
            children.append(c["id"])
        parent = ig_post("me/media", token, media_type="CAROUSEL", children=",".join(children), caption=post.get("caption", ""))
    elif kind == "image":
        parent = ig_post("me/media", token, image_url=urls[0], caption=post.get("caption", ""))
    elif kind == "story":
        parent = ig_post("me/media", token, image_url=urls[0], media_type="STORIES")
    else:
        raise IGError(f"Unknown post type {kind}")
    wait_ready(parent["id"], token, "post")
    res = ig_post("me/media_publish", token, creation_id=parent["id"])
    return res


def main():
    now = now_utc()
    changed = False
    for path, post in iter_posts():
        if post.get("status") != "queued":
            continue
        due = parse_time(post["publish_at"])
        if due > now:
            continue
        acct = post["account"]
        label = f"{post['id']} ({ACCOUNTS[acct]['handle']})"
        if now - due > STALE_AFTER:
            post["status"] = "skipped"
            post["error"] = f"Not published: more than 36 hours past {post['publish_at']}"
            save_json(path, post); changed = True
            open_issue(f"Skipped post {post['id']}", f"{label} was due {post['publish_at']} but the publisher didn't run in time. Claude will reschedule it at the next weekly review.")
            continue
        token = token_for(acct)
        CURRENT["account"] = acct
        if not token:
            open_issue(f"Missing Instagram token for {acct}",
                       f"Add the repository secret `{ACCOUNTS[acct]['secret']}` (Settings → Secrets and variables → Actions). {label} is waiting.")
            continue
        print(f"Publishing {label}")
        try:
            res = publish(post, os.path.dirname(path), token)
            post["status"] = "published"
            post["media_id"] = res.get("id")
            post["published_at"] = now.isoformat()
            if not DRY and res.get("id"):
                try:
                    post["permalink"] = ig_get(res["id"], token, fields="permalink").get("permalink")
                except IGError:
                    pass
            post.pop("error", None)
        except Exception as e:
            post["attempts"] = post.get("attempts", 0) + 1
            post["error"] = str(e)
            print(f"  FAILED: {e}")
            if post["attempts"] >= MAX_ATTEMPTS:
                post["status"] = "failed"
                open_issue(f"Post failed: {post['id']}", f"{label} failed {MAX_ATTEMPTS} times.\n\nLast error:\n```\n{e}\n```\n\nTell Claude in the Tax Practice project and it will fix and requeue it.")
        if not DRY:
            save_json(path, post)
        changed = True
    print("changed" if changed else "nothing due")


if __name__ == "__main__":
    main()
