"""Bold carousel slides for Retained (1080x1350): big type, green numbers, Penny with speech bubbles.
Same look as the animated Reels (motion.py) so the grid and Reels feel like one brand.

    from bold import slide, hl, bubble, penny, render_slides
    slides = [slide(body, n=1, of=5), ...]
    render_slides(slides, __file__)    # writes 1.jpg ... n.jpg
"""
import asyncio, io, os
from playwright.async_api import async_playwright
from motion import coin_mascot, FONTS, NAVY, BONE, BRASS, GREEN, RED

HERE = os.path.dirname(os.path.abspath(__file__))
SERIF = "font-family:'DM Serif Display',serif;font-weight:400"
MONO = "font-family:'IBM Plex Mono',monospace;font-weight:600"


def hl(text, color=BRASS, fg=NAVY):
    return f'<span style="background:{color};color:{fg};padding:0 14px;border-radius:12px;box-decoration-break:clone;-webkit-box-decoration-break:clone">{text}</span>'


def bubble(text, x, y, w=420, tail="left"):
    tail_css = ("left:60px" if tail == "left" else "right:60px")
    return f"""<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;background:{BONE};color:{NAVY};border-radius:28px;padding:26px 30px;
font-family:Inter,sans-serif;font-weight:600;font-size:36px;line-height:1.25;box-shadow:0 12px 30px rgba(0,0,0,.35)">{text}
<div style="position:absolute;bottom:-22px;{tail_css};width:0;height:0;border-left:22px solid transparent;border-right:22px solid transparent;border-top:24px solid {BONE}"></div></div>"""


def penny(size, x, y, wave=False):
    return coin_mascot(size, wave=wave, x=x, y=y)


def slide(body, n=None, of=None, swipe=False, bg=NAVY, fg=BONE):
    counter = f'<div style="position:absolute;right:80px;top:70px;{MONO};font-size:28px;color:#9A9384">{n}/{of}</div>' if n else ""
    sw = f'<div style="position:absolute;right:80px;bottom:60px;{MONO};font-size:30px;color:{BRASS}">SWIPE →</div>' if swipe else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS} body{{margin:0}} b{{font-weight:700}}</style></head><body>
<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:{bg};color:{fg};font-family:Inter,sans-serif">
<div style="position:absolute;inset:0;background:radial-gradient(1000px 800px at 15% 5%,rgba(201,161,95,.20),transparent 60%),radial-gradient(800px 800px at 95% 95%,rgba(63,208,127,.09),transparent 60%)"></div>
<div style="position:absolute;left:80px;top:70px;{MONO};font-size:28px;letter-spacing:.16em;color:{BRASS}">RETAINED</div>
{counter}
{body}
<div style="position:absolute;left:80px;bottom:60px;font-size:24px;color:#8A8476">General info only · Not personal advice</div>
{sw}
</div></body></html>"""


def render_slides(slides, make_file, quality=92):
    from PIL import Image
    folder = os.path.dirname(os.path.abspath(make_file))
    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": 1080, "height": 1350})
            for i, html in enumerate(slides, 1):
                f = os.path.join(HERE, "_bold.html"); open(f, "w").write(html)
                await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready")
                over = await pg.evaluate("(()=>{const d=document.body.firstElementChild;return [...d.querySelectorAll('*')].some(e=>{const r=e.getBoundingClientRect();return r.right>1081||r.bottom>1351})})()")
                if over:
                    print(f"WARNING: slide {i} has something past the frame edge")
                png = await pg.screenshot(type="png")
                Image.open(io.BytesIO(png)).convert("RGB").save(os.path.join(folder, f"{i}.jpg"), "JPEG", quality=quality, optimize=True)
            await b.close()
            os.remove(os.path.join(HERE, "_bold.html"))
    asyncio.run(go())
    print(f"rendered {len(slides)} slides -> {folder}")
