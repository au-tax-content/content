"""Story templates (1080x1920 JPEG) for both accounts. Stories via the API are images only (no stickers or links),
so there are two kinds: a "new post" push that shows the post's cover, and a one-slide tip.
Keep text between y=250 and y=1580 (Instagram's top bar and reply box cover the edges).

    from stories import rp_push, rp_tip, rt_push, rt_tip, render_story
    render_story(rp_push("Is it claimable? Office workers", "6 things. Guess before you swipe.", cover_path), __file__)
"""
import asyncio, base64, io, os
from playwright.async_api import async_playwright
import returnpolicy_kit as rp
from motion import coin_mascot, FONTS as RT_FONTS, NAVY, BONE, BRASS, GREEN

HERE = os.path.dirname(os.path.abspath(__file__))


def _img(path, w):
    data = base64.b64encode(open(path, "rb").read()).decode()
    return f'<img src="data:image/jpeg;base64,{data}" style="width:{w}px;display:block">'


def _page(body, bg, fg, font_css, base_font):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_css} body{{margin:0}} b{{font-weight:700}}</style></head><body>
<div style="width:1080px;height:1920px;position:relative;overflow:hidden;background:{bg};color:{fg};{base_font}">{body}</div></body></html>"""


# ---------- Return Policy ----------
def _rp(body, bg=rp.INK, fg=rp.PAPER):
    dark = bg in (rp.INK, rp.GREEN)
    glow = ("radial-gradient(1000px 900px at 10% 5%,rgba(63,208,127,.18),transparent 60%),radial-gradient(900px 900px at 100% 100%,rgba(255,227,110,.12),transparent 60%)"
            if dark else "none")
    sub = "#A8A193" if dark else rp.MUTED
    return _page(f"""<div style="position:absolute;inset:0;background:{glow}"></div>
<div style="position:absolute;left:90px;top:250px;{rp.MONO};font-size:30px;letter-spacing:.12em">RETURN POLICY</div>
{body}
<div style="position:absolute;left:90px;top:1560px;{rp.MONO5};font-size:24px;color:{sub}">General info only · Not personal advice</div>""",
                 bg, fg, rp.FONTS, rp.BODY)


def rp_push(title, sub, cover, label="NEW POST"):
    """Push the day's post: label stamp, title, the cover slide tilted like a receipt pinned to the board."""
    return _rp(f"""
<div style="position:absolute;left:90px;right:90px;top:320px;display:flex;flex-direction:column;align-items:flex-start;gap:28px">
 {rp.stamp(label, rp.HLY, -4, 44)}
 <div style="{rp.DISPLAY};font-size:88px;line-height:1">{title}</div>
 <div style="{rp.BODY};font-size:40px;line-height:1.3;color:#D9D3C5">{sub}</div>
 <div style="margin:24px 0 0 70px;transform:rotate(-3deg);box-shadow:0 30px 60px rgba(0,0,0,.5);border:10px solid {rp.PAPER}">{_img(cover, 440)}</div></div>
{rp.receipt_mascot(230, wave=True, x=770, y=1180, limb=rp.PAPER)}
<div style="position:absolute;left:90px;top:1500px;{rp.MONO};font-size:32px;color:{rp.HLY}">TAP OUR NAME → IT'S ON THE GRID</div>""")


def rp_tip(kicker, big, line, verdict=None, verdict_color=None, bg=rp.PAPER):
    fg = rp.INK if bg in (rp.PAPER, rp.PAPER2) else rp.PAPER
    v = f'<div style="margin-top:40px">{rp.stamp(verdict, verdict_color or rp.GREEN, -5, 56)}</div>' if verdict else ""
    return _rp(f"""
<div style="position:absolute;left:90px;top:360px">{rp.stamp("TODAY'S TIP", rp.GREEN if fg == rp.INK else rp.HLY, -3, 36)}</div>
<div style="position:absolute;left:90px;right:90px;top:490px">
 <div style="{rp.MONO5};font-size:36px;color:{rp.MUTED if fg == rp.INK else '#D9D3C5'}">{kicker}</div>
 <div style="{rp.DISPLAY};font-size:150px;line-height:1;margin-top:20px">{big}</div>{v}
 <div style="{rp.BODY};font-size:54px;line-height:1.3;margin-top:50px">{line}</div></div>
{rp.receipt_mascot(300, wave=True, x=700, y=1110, limb=rp.INK if fg == rp.INK else rp.PAPER)}""", bg, fg)


# ---------- Retained ----------
SERIF = "font-family:'DM Serif Display',serif;font-weight:400"
MONO = "font-family:'IBM Plex Mono',monospace;font-weight:600"


def _rt(body):
    return _page(f"""<div style="position:absolute;inset:0;background:radial-gradient(1100px 900px at 15% 5%,rgba(201,161,95,.22),transparent 60%),radial-gradient(900px 900px at 95% 95%,rgba(63,208,127,.09),transparent 60%)"></div>
<div style="position:absolute;left:90px;top:250px;{MONO};font-size:30px;letter-spacing:.16em;color:{BRASS}">RETAINED</div>
{body}
<div style="position:absolute;left:90px;top:1560px;font-family:Inter,sans-serif;font-size:24px;color:#8A8476">General info only · Not personal advice</div>""",
                 NAVY, BONE, RT_FONTS, "font-family:Inter,sans-serif")


def rt_push(title, sub, cover, label="NEW POST"):
    return _rt(f"""
<div style="position:absolute;left:90px;right:90px;top:320px;display:flex;flex-direction:column;align-items:flex-start;gap:28px">
 <div style="{MONO};font-size:40px;background:{BRASS};color:{NAVY};padding:10px 24px;border-radius:12px">{label}</div>
 <div style="{SERIF};font-size:88px;line-height:1.04">{title}</div>
 <div style="font-size:40px;line-height:1.35;color:#D8D2C6">{sub}</div>
 <div style="margin:24px 0 0 70px;transform:rotate(-3deg);box-shadow:0 30px 60px rgba(0,0,0,.5);border:10px solid {BONE};border-radius:6px">{_img(cover, 440)}</div></div>
{coin_mascot(230, wave=True, x=780, y=1180)}
<div style="position:absolute;left:90px;top:1500px;{MONO};font-size:32px;color:{GREEN}">TAP OUR NAME → IT'S ON THE GRID</div>""")


def rt_tip(kicker, big, line):
    return _rt(f"""
<div style="position:absolute;left:90px;top:360px;{MONO};font-size:36px;color:{BRASS}">{kicker}</div>
<div style="position:absolute;left:90px;right:90px;top:440px;{SERIF};font-size:120px;line-height:1.04">{big}</div>
<div style="position:absolute;left:90px;right:90px;top:900px;font-size:46px;line-height:1.35">{line}</div>
{coin_mascot(280, wave=True, x=720, y=1170)}""")


def render_story(html, make_file, name="1.jpg"):
    from PIL import Image
    folder = os.path.dirname(os.path.abspath(make_file))
    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": 1080, "height": 1920})
            f = os.path.join(HERE, "_story.html"); open(f, "w").write(html)
            await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready")
            png = await pg.screenshot(type="png")
            Image.open(io.BytesIO(png)).convert("RGB").save(os.path.join(folder, name), "JPEG", quality=92, optimize=True)
            await b.close(); os.remove(f)
    asyncio.run(go())
    print(f"story -> {os.path.join(folder, name)}")
