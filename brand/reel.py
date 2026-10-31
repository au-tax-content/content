"""Faceless text-on-screen Reels (1080x1920, 30 fps, H.264 + silent AAC) for the Instagram API.

Usage from a post folder's make.py:
    from reel import retained_card, render_reel
    cards = [(retained_card(...), seconds), ...]
    render_reel(cards, __file__)          # writes reel.mp4 and cover.jpg next to make.py

Each card is drawn once as a still, held for its duration with a short fade in/out, encoded as its
own clip, then the clips are joined with the concat demuxer and a silent audio track is added
(Instagram processes Reels more reliably with an audio stream). Add a trending sound by hand in
the app later if wanted; the API can't attach licensed music.
"""
import asyncio, os, subprocess, tempfile, shutil
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, FADE = 1080, 1920, 30, 0.3
NAVY, BONE, BRASS = "#0F1B2D", "#F4F0E8", "#B08D57"
FONTS = f"""
@font-face{{font-family:'DM Serif Display';src:url('file://{HERE}/fonts/dmserif.woff2')}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-500-normal.woff2');font-weight:500}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-600-normal.woff2');font-weight:600}}
"""
MONO = "'IBM Plex Mono','DejaVu Sans Mono',monospace"
SERIF = "'DM Serif Display',serif"
SANS = "Inter,sans-serif"


def retained_card(headline, sub="", kicker="RETAINED", number="", footer="", dark=True, size=118):
    """A Retained-style vertical card. Keep text inside the middle 1080x1350 (Instagram crops the grid view)."""
    bg, fg, muted, rule = (NAVY, BONE, "#C9C2B4", "#2B3A52") if dark else (BONE, NAVY, "#4A5568", "#C9BFAE")
    num = f'<span style="font-family:{MONO};font-weight:600;font-size:150px;line-height:.9;color:{BRASS}">{number}</span>' if number else ""
    subh = f'<p style="margin:0;font-family:{SANS};font-weight:500;font-size:46px;line-height:1.38;color:{fg}">{sub}</p>' if sub else ""
    foot = f'<span style="font-family:{MONO};font-size:26px;color:{muted}">{footer}</span>' if footer else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS} body{{margin:0}} b{{font-weight:600}}</style></head><body>
<div style="width:{W}px;height:{H}px;box-sizing:border-box;background:{bg};color:{fg};padding:285px 96px;display:flex;flex-direction:column;gap:44px">
<div style="display:flex;justify-content:space-between;border-bottom:2px solid {BRASS};padding-bottom:24px;font-family:{MONO};font-weight:600;font-size:28px;letter-spacing:.14em"><span>RETAINED</span><span style="color:{BRASS}">{kicker}</span></div>
{num}
<h1 style="margin:0;font-family:{SERIF};font-weight:400;font-size:{size}px;line-height:1.04">{headline}</h1>
<span style="width:160px;height:6px;background:{BRASS}"></span>
{subh}
<div style="margin-top:auto">{foot}</div>
</div></body></html>"""


def render_reel(cards, make_file):
    folder = os.path.dirname(os.path.abspath(make_file))
    tmp = tempfile.mkdtemp()
    stills = []

    async def draw():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": W, "height": H})
            for i, (html, _) in enumerate(cards):
                f = os.path.join(HERE, "_reel.html")
                open(f, "w").write(html)
                await pg.goto("file://" + f)
                await pg.evaluate("document.fonts.ready")
                out = os.path.join(tmp, f"{i}.png")
                await pg.screenshot(path=out)
                stills.append(out)
            await b.close()
            os.remove(os.path.join(HERE, "_reel.html"))
    asyncio.run(draw())

    clips = []
    for i, ((_, dur), png) in enumerate(zip(cards, stills)):
        part = os.path.join(tmp, f"c{i}.part.mp4")
        vf = (f"format=yuv420p,loop=-1:1,trim=duration={dur},"
              f"fade=t=in:st=0:d={FADE},fade=t=out:st={dur - FADE}:d={FADE}")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", png, "-vf", vf,
                        "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                        "-pix_fmt", "yuv420p", "-profile:v", "high", part], check=True)
        final = part.replace(".part.mp4", ".mp4")
        os.rename(part, final)
        clips.append(final)
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
    joined = os.path.join(tmp, "joined.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined], check=True)
    total = sum(d for _, d in cards)
    out = os.path.join(folder, "reel.part.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", joined, "-f", "lavfi", "-i",
                    "anullsrc=channel_layout=stereo:sample_rate=48000", "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-t", str(total), "-movflags", "+faststart", out], check=True)
    os.replace(out, os.path.join(folder, "reel.mp4"))
    # cover: first card, cropped to the 4:5 grid view
    from PIL import Image
    Image.open(stills[0]).convert("RGB").crop((0, 285, 1080, 1635)).save(os.path.join(folder, "cover.jpg"), "JPEG", quality=92)
    shutil.rmtree(tmp)
    print(f"reel.mp4 ({total:.1f}s) and cover.jpg written to {folder}")
