"""Return Policy slide kit (1080x1350): thermal-receipt look, big Space Grotesk type, refund-green numbers,
rubber stamps, and the mascot Docket (an original receipt character) with speech bubbles.
Same structure as bold.py (Retained), so make.py files look alike.

    from returnpolicy_kit import slide, hl, bubble, docket, receipt, item, stamp, render_slides
    slides = [slide(body, n=1, of=5, swipe=True, bg=PAPER), ...]
    render_slides(slides, __file__)    # writes 1.jpg ... n.jpg

Colours come from the brand system tokens (return-policy theme).
"""
import asyncio, io, os
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER, PAPER2, INK, MUTED = "#F7F3EA", "#EDE6D6", "#1A1A1A", "#5B564C"
GREEN, HLY, RED, RULE = "#0E7A4B", "#FFE36E", "#C2361F", "#BDB4A0"
MINT = "#3FD07F"   # refund green, brightened for numbers on the ink ground

FONTS = f"""
@font-face{{font-family:'Space Grotesk';src:url('file://{HERE}/fonts/space-grotesk-latin-500-normal.woff2');font-weight:500}}
@font-face{{font-family:'Space Grotesk';src:url('file://{HERE}/fonts/space-grotesk-latin-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-400-normal.woff2');font-weight:400}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-500-normal.woff2');font-weight:500}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-600-normal.woff2');font-weight:600}}
"""
DISPLAY = "font-family:'Space Grotesk',sans-serif;font-weight:700;letter-spacing:-0.03em"
BODY = "font-family:'Space Grotesk',sans-serif;font-weight:500"
MONO = "font-family:'IBM Plex Mono',monospace;font-weight:600"
MONO5 = "font-family:'IBM Plex Mono',monospace;font-weight:500"

TEAR = ("height:{h}px;background:linear-gradient(45deg,{c} {q}px,transparent 0) 0 0/{s}px {s}px repeat-x,"
        "linear-gradient(-45deg,{c} {q}px,transparent 0) 0 0/{s}px {s}px repeat-x")


def tear(color=PAPER, flip=False, size=24):
    css = TEAR.format(h=size, c=color, q=size // 2, s=size)
    rot = "transform:rotate(180deg)" if not flip else ""
    return f'<div style="{css};{rot}"></div>'


def hl(text, color=HLY, fg=INK):
    # gradient starts 18% down so the highlight never paints over descenders on the line above
    return (f'<span style="background:linear-gradient(transparent 18%,{color} 18%,{color} 96%,transparent 96%);color:{fg};padding:0 12px;'
            f'box-decoration-break:clone;-webkit-box-decoration-break:clone">{text}</span>')


def stamp(text, color=GREEN, rot=-6, size=34):
    return (f'<span style="display:inline-block;{MONO};font-size:{size}px;letter-spacing:.06em;color:{color};border:5px solid {color};'
            f'border-radius:12px;padding:6px 16px;transform:rotate({rot}deg);white-space:nowrap">{text}</span>')


def item(label, right="", size=34, color=INK, right_html=None):
    r = right_html if right_html is not None else f'<span style="{MONO}">{right}</span>'
    return (f'<div style="display:flex;gap:14px;align-items:center;{MONO5};font-size:{size}px;color:{color}">'
            f'<span>{label}</span><span style="flex:1;border-bottom:4px dotted {RULE};transform:translateY(8px)"></span>{r}</div>')


def receipt(inner, x, y, w, head=None, sub=None, ground=PAPER):
    """A torn thermal receipt panel. inner = item() rows etc."""
    top = ""
    if head:
        top = (f'<div style="text-align:center;{MONO};font-size:26px;letter-spacing:.12em">{head}</div>'
               + (f'<div style="text-align:center;{MONO5};font-size:22px;color:{MUTED};margin-top:4px">{sub}</div>' if sub else "")
               + f'<div style="border-top:4px dashed {RULE};margin:22px 0"></div>')
    return f"""<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;filter:drop-shadow(0 14px 24px rgba(0,0,0,.28))">
{tear(ground)}<div style="background:{ground};color:{INK};padding:30px 44px;display:flex;flex-direction:column;gap:22px">{top}{inner}</div>{tear(ground, flip=True)}</div>"""


def bubble(text, x, y, w=420, tail="left", bg=INK, fg=PAPER):
    tail_css = ("left:60px" if tail == "left" else "right:60px")
    return f"""<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;background:{bg};color:{fg};border-radius:28px;padding:26px 30px;
{BODY};font-size:36px;line-height:1.25;box-shadow:0 12px 30px rgba(0,0,0,.25)">{text}
<div style="position:absolute;bottom:-22px;{tail_css};width:0;height:0;border-left:22px solid transparent;border-right:22px solid transparent;border-top:24px solid {bg}"></div></div>"""


def receipt_mascot(size=300, wave=False, x=0, y=0, extra="", limb="#1A1A1A"):
    """'Docket', an original thermal-receipt character: curled-top paper body, zigzag torn bottom, big eyes,
    a refund-green $ line item and a little total. Same class hooks as Penny (mascot/eye/arm) so motion.py animates it."""
    return f"""<div class="mascot" data-wave="{1 if wave else 0}" style="position:absolute;left:{x}px;top:{y}px;width:{size}px;height:{size*1.25}px;{extra}">
<svg viewBox="0 0 200 250" width="{size}" height="{size*1.25}">
 <line x1="78" y1="200" x2="70" y2="236" stroke="{limb}" stroke-width="9" stroke-linecap="round"/>
 <line x1="122" y1="200" x2="130" y2="236" stroke="{limb}" stroke-width="9" stroke-linecap="round"/>
 <ellipse cx="66" cy="240" rx="16" ry="7" fill="{limb}"/><ellipse cx="134" cy="240" rx="16" ry="7" fill="{limb}"/>
 <line x1="40" y1="120" x2="8" y2="150" stroke="{limb}" stroke-width="9" stroke-linecap="round"/><circle cx="6" cy="152" r="9" fill="#0E7A4B"/>
 <g class="arm" data-ox="160" data-oy="118"><line x1="160" y1="118" x2="192" y2="78" stroke="{limb}" stroke-width="9" stroke-linecap="round"/><circle cx="194" cy="74" r="9" fill="#0E7A4B"/></g>
 <path d="M40 34 q0 -18 18 -18 h84 q18 0 18 18 v162 l-10 -10 l-10 10 l-10 -10 l-10 10 l-10 -10 l-10 10 l-10 -10 l-10 10 l-10 -10 l-10 10 l-10 -10 l-10 10 z"
   fill="#F7F3EA" stroke="#1A1A1A" stroke-width="6" stroke-linejoin="round"/>
 <path d="M40 34 q0 -18 18 -18 h-6 q-20 2 -20 22 z" fill="#EDE6D6"/>
 <rect x="56" y="28" width="88" height="10" rx="3" fill="#1A1A1A"/>
 <g class="eye" data-cy="70"><ellipse cx="80" cy="70" rx="11" ry="14" fill="#1A1A1A"/><circle cx="84" cy="65" r="4" fill="#fff"/></g>
 <g class="eye" data-cy="70"><ellipse cx="120" cy="70" rx="11" ry="14" fill="#1A1A1A"/><circle cx="124" cy="65" r="4" fill="#fff"/></g>
 <path d="M66 48 q10 -7 20 -2" stroke="#1A1A1A" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M114 46 q10 -5 20 2" stroke="#1A1A1A" stroke-width="5" fill="none" stroke-linecap="round"/>
 <path d="M84 96 q16 16 32 0" stroke="#1A1A1A" stroke-width="6" fill="#C2361F" stroke-linecap="round"/>
 <ellipse cx="62" cy="92" rx="9" ry="6" fill="#FFB8A8" opacity=".8"/><ellipse cx="138" cy="92" rx="9" ry="6" fill="#FFB8A8" opacity=".8"/>
 <line x1="56" y1="124" x2="112" y2="124" stroke="#BDB4A0" stroke-width="5" stroke-dasharray="2 6" stroke-linecap="round"/>
 <line x1="56" y1="142" x2="104" y2="142" stroke="#BDB4A0" stroke-width="5" stroke-dasharray="2 6" stroke-linecap="round"/>
 <text x="144" y="133" text-anchor="end" font-family="IBM Plex Mono, monospace" font-weight="600" font-size="22" fill="#0E7A4B">$</text>
 <line x1="56" y1="160" x2="144" y2="160" stroke="#1A1A1A" stroke-width="4" stroke-dasharray="6 5"/>
 <rect x="104" y="166" width="40" height="12" rx="3" fill="#0E7A4B"/>
</svg></div>"""


def docket(size, x, y, wave=False, dark=False):
    """dark=True on INK/GREEN grounds: limbs turn cream so they stay visible."""
    return receipt_mascot(size, wave=wave, x=x, y=y, limb=PAPER if dark else INK)


def slide(body, n=None, of=None, swipe=False, bg=PAPER, fg=INK, tag=None):
    dark = bg in (INK, GREEN)
    sub = "#A8A193" if dark else MUTED
    counter = f'<div style="position:absolute;right:96px;top:80px;{MONO};font-size:26px;color:{sub}">{n}/{of}</div>' if n else ""
    tagh = (f'<div style="position:absolute;left:380px;top:72px;{MONO};font-size:22px;letter-spacing:.1em;color:{INK};background:{HLY};'
            f'border-radius:999px;padding:8px 22px">{tag}</div>') if tag else ""
    sw = (f'<div style="position:absolute;right:96px;bottom:64px;{MONO};font-size:26px;letter-spacing:.08em;border:4px solid {fg};'
          f'border-radius:999px;padding:10px 24px;color:{fg}">SWIPE →</div>') if swipe else ""
    glow = ("radial-gradient(900px 700px at 10% 0%,rgba(63,208,127,.16),transparent 60%),radial-gradient(800px 700px at 100% 100%,rgba(255,227,110,.10),transparent 60%)"
            if dark else "radial-gradient(900px 700px at 0% 0%,rgba(255,255,255,.6),transparent 60%)")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS} body{{margin:0}} b{{font-weight:700}}</style></head><body>
<div style="width:1080px;height:1350px;position:relative;overflow:hidden;background:{bg};color:{fg};{BODY}">
<div style="position:absolute;inset:0;background:{glow}"></div>
<div style="position:absolute;left:96px;top:80px;{MONO};font-size:26px;letter-spacing:.12em;color:{fg}">RETURN POLICY</div>
{tagh}{counter}
{body}
<div style="position:absolute;left:96px;bottom:72px;{MONO5};font-size:22px;color:{sub}">General info only · Not personal advice</div>
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
                f = os.path.join(HERE, "_rp.html"); open(f, "w").write(html)
                await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready")
                over = await pg.evaluate("(()=>{const d=document.body.firstElementChild;return [...d.querySelectorAll('*')].some(e=>{const r=e.getBoundingClientRect();return r.right>1081||r.bottom>1351})})()")
                if over:
                    print(f"WARNING: slide {i} has something past the frame edge")
                png = await pg.screenshot(type="png")
                Image.open(io.BytesIO(png)).convert("RGB").save(os.path.join(folder, f"{i}.jpg"), "JPEG", quality=quality, optimize=True)
            await b.close()
            os.remove(os.path.join(HERE, "_rp.html"))
    asyncio.run(go())
    print(f"rendered {len(slides)} slides -> {folder}")
