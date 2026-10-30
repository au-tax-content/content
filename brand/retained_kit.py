"""Retained brand kit: slide components (navy/bone/brass ledger look) and a JPEG renderer.

Use from a post folder's make.py:  from retained_kit import *  ...  render(slides, __file__)
"""
import os, asyncio
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

NAVY, BONE, BRASS, BRASS_D, STONE = "#0F1B2D", "#F4F0E8", "#B08D57", "#7A5C2E", "#E6DFD2"
HL = "#EADBC0"

FONTS = f"""
@font-face{{font-family:'DM Serif Display';src:url('file://{HERE}/fonts/dmserif.woff2') format('woff2');font-weight:400}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-400-normal.woff2') format('woff2');font-weight:400}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-500-normal.woff2') format('woff2');font-weight:500}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-600-normal.woff2') format('woff2');font-weight:600}}
"""
MONO = "'IBM Plex Mono','DejaVu Sans Mono',monospace"
SERIF = "'DM Serif Display',serif"
SANS = "Inter,sans-serif"


def page(body, bg, fg, gap=52):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{margin:0}} b{{font-weight:600}}
</style></head><body>
<div style="width:1080px;height:1350px;box-sizing:border-box;background:{bg};padding:96px;display:flex;flex-direction:column;gap:{gap}px;color:{fg};overflow:hidden">
{body}
</div></body></html>"""


def header(right, dark):
    rc = BRASS if dark else BRASS_D
    return f"""<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid {BRASS};padding-bottom:24px;font-family:{MONO};font-weight:600;font-size:24px;letter-spacing:0.14em">
<span>RETAINED</span><span style="color:{rc}">{right}</span></div>"""


def title(text, size=112, gap=32):
    return f"""<div style="display:flex;flex-direction:column;gap:{gap}px">
<h1 style="margin:0;font-family:{SERIF};font-weight:400;font-size:{size}px;line-height:1.02;letter-spacing:-0.01em">{text}</h1>
<span style="width:160px;height:6px;background:{BRASS}"></span></div>"""


def footer(left, right, dark):
    c = "#C9C2B4" if dark else "#4A5568"
    return f"""<div style="margin-top:auto;display:flex;justify-content:space-between;font-family:{MONO};font-size:22px;color:{c}"><span>{left}</span><span>{right}</span></div>"""


def rows(items, dark, size=36):
    rule = "#2B3A52" if dark else "#C9BFAE"
    numc = BRASS if dark else BRASS_D
    out = []
    for i, (a, b) in enumerate(items, 1):
        sub = f'<span style="font-size:28px;font-weight:400;opacity:.8;line-height:1.35">{b}</span>' if b else ""
        out.append(f"""<div style="display:flex;gap:28px;padding:20px 0;border-bottom:2px solid {rule}">
<span style="font-family:{MONO};color:{numc};font-weight:600;font-size:{size}px">{i:02d}</span>
<div style="display:flex;flex-direction:column;gap:6px"><span style="font-weight:600">{a}</span>{sub}</div></div>""")
    return f'<div style="display:flex;flex-direction:column;font-family:{SANS};font-weight:500;font-size:{size}px">{"".join(out)}</div>'


def para(html, size=36, color=None):
    c = f"color:{color};" if color else ""
    return f'<p style="margin:0;font-family:{SANS};font-weight:500;font-size:{size}px;line-height:1.4;{c}">{html}</p>'


def kit_box():
    return f"""<div style="background:{BONE};color:{NAVY};padding:48px 56px;display:flex;flex-direction:column;gap:24px">
<span style="font-family:{MONO};font-size:28px;font-weight:500;color:#4A5568">COMMENT THE WORD</span>
<span style="font-family:{MONO};font-size:128px;font-weight:600;letter-spacing:0.06em;line-height:1">ABN</span>
<span style="font-family:{SANS};font-size:36px;font-weight:500;line-height:1.38">and you'll be first to get the <b>New ABN Starter Kit</b> when it lands in December: a first-year checklist and a set-aside calculator.</span>
</div>"""



def ledger_row(a, b):
    return f'<div style="display:flex;justify-content:space-between;padding:16px 0;border-bottom:2px solid #C9BFAE"><span>{a}</span><span>{b}</span></div>'


def render(slides, make_file, quality=92):
    """Render a list of slide HTML strings to 1.jpg, 2.jpg ... next to make_file (1080x1350, JPEG for the Instagram API)."""
    import io
    from PIL import Image
    folder = os.path.dirname(os.path.abspath(make_file))
    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": 1080, "height": 1350})
            for i, html in enumerate(slides, 1):
                tmp = os.path.join(HERE, "_render.html")
                open(tmp, "w").write(html)
                await pg.goto("file://" + tmp)
                await pg.evaluate("document.fonts.ready")
                over = await pg.evaluate("(()=>{const d=document.body.firstElementChild;return d.scrollHeight>d.clientHeight+1})()")
                if over:
                    print(f"WARNING: slide {i} content overflows the frame")
                png = await pg.screenshot(type="png")
                Image.open(io.BytesIO(png)).convert("RGB").save(os.path.join(folder, f"{i}.jpg"), "JPEG", quality=quality, optimize=True)
            await b.close()
            os.remove(os.path.join(HERE, "_render.html"))
    asyncio.run(go())
    print(f"rendered {len(slides)} slides into {folder}")
