"""Crayon two-panel slides (the "X. Not Y." motivational format), 1080x1350.

Art: Canva generate-image (crayon on paper, ask for NO text) → insert both panels on the working canvas
design DAHZ2AHQfVk with edit-design → export-design PNG → download (export-download.canva.com is allowed)
→ crop each panel to a file. All words are added here so they're exact and checkable.

    from crayon import two_panel, render
    render([two_panel("top.png", "MOST PEOPLE HAVE <r>2 YEARS</r> TO FIX THEIR TAX RETURN.", "bot.png", "NOT <r>2 DAYS.</r>")], __file__)
<r>…</r> marks the red words. Every stat must be verified (ATO/ABS) and listed in figures_checked.
"""
import asyncio, io, os
from playwright.async_api import async_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = f"""@font-face{{font-family:H;src:url('file://{HERE}/fonts/patrick-hand-latin-400-normal.woff2')}}
body{{margin:0}} .w{{width:1080px;height:1350px;background:#FBF8F2;position:relative;overflow:hidden;font-family:H}}
.p{{position:absolute;left:40px;width:1000px;height:505px;object-fit:cover;border-radius:6px}}
.t{{position:absolute;left:40px;right:40px;text-align:center;line-height:1.02;color:#1A1A1A;letter-spacing:.02em}}
r{{color:#D7261E}} .k{{position:absolute;left:46px;top:493px;background:rgba(0,0,0,.6);color:#fff;font-family:sans-serif;font-size:21px;letter-spacing:.04em;padding:6px 14px;border-radius:20px}}
.n{{position:absolute;right:46px;top:52px;background:rgba(0,0,0,.55);color:#fff;font-family:sans-serif;font-size:22px;padding:6px 14px;border-radius:20px}}"""


def two_panel(top_img, top_text, bot_img, bot_text, n=None, of=None, top_size=76, bot_size=84, note=None):
    """note: small chip on the top panel for the condition/income year behind the figure (e.g. "30% RATE · 2026–27")."""
    def src(p): return "file://" + os.path.abspath(p)
    num = f'<div class="n">{n}/{of}</div>' if n else ""
    if note: num += f'<div class="k">{note}</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="w">
<img class="p" style="top:40px" src="{src(top_img)}">{num}
<div class="t" style="top:565px;font-size:{top_size}px">{top_text}</div>
<img class="p" style="top:745px" src="{src(bot_img)}">
<div class="t" style="top:1262px;font-size:{bot_size}px">{bot_text}</div></div></body></html>"""


def render(slides, make_file, quality=92):
    from PIL import Image
    folder = os.path.dirname(os.path.abspath(make_file))
    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 1080, "height": 1350})
            for i, html in enumerate(slides, 1):
                f = os.path.join(folder, "_crayon.html"); open(f, "w").write(html)
                await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready")
                png = await pg.screenshot(type="png")
                Image.open(io.BytesIO(png)).convert("RGB").save(os.path.join(folder, f"{i}.jpg"), "JPEG", quality=quality, optimize=True)
                os.remove(f)
            await b.close()
    asyncio.run(go())
    print(f"rendered {len(slides)} crayon slides -> {folder}")
