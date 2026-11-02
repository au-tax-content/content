"""Turn a finished carousel (1.jpg … n.jpg, 1080×1350) into a 9:16 Reel for non-follower reach.

Each slide sits on a 1080×1920 canvas filled with the slide's own edge colour, with a slow push-in
and a swipe transition to the next slide. Slide 1 (the hook) is short so the claim lands fast.
Writes reel.mp4 (30 fps, silent AAC: music is attached at publish via audio_id) and cover.jpg.

Usage from a post folder's make.py (or the command line):
    python3 brand/carousel_reel.py <carousel_folder> <out_folder> ["top hook line"]
    or render(src, out, top="...", hl=(255, 226, 77)) from Python.
"""
import os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

W, H, FPS = 1080, 1920, 30
XF = 0.35  # transition length (s)


def edge_colour(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    px = [im.getpixel((x, y)) for x in (4, w // 2, w - 5) for y in (4, h - 5)]
    r, g, b = (sorted(c[i] for c in px)[len(px) // 2] for i in range(3))
    return f"0x{r:02X}{g:02X}{b:02X}"


def banner(text, bg_hex, path, font="space-grotesk-latin-700-normal.ttf", hl=None):
    """Hook line for the empty band above the slide (the first thing seen in the Reels feed)."""
    r, g, b = (int(bg_hex[i:i + 2], 16) for i in (2, 4, 6))
    fg = (20, 20, 20) if (0.299 * r + 0.587 * g + 0.114 * b) > 140 else (250, 246, 236)
    im = Image.new("RGBA", (W, 285), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    size = 64
    while size > 36:
        f = ImageFont.truetype(os.path.join(FONTS, font), size)
        if d.textlength(text, font=f) <= W - 200:
            break
        size -= 2
    tw = d.textlength(text, font=f)
    x, y = (W - tw) / 2, 285 - size - 60
    if hl:  # highlighter pill behind the line
        d.rounded_rectangle((x - 22, y - 10, x + tw + 22, y + size + 16), 14, fill=hl)
        fg = (20, 20, 20)
    d.text((x, y), text, font=f, fill=fg)
    im.save(path)


def render(src, out, hook_s=2.4, slide_s=4.0, top=None, font="space-grotesk-latin-700-normal.ttf", hl=None):
    slides = sorted((f for f in os.listdir(src) if f[0].isdigit() and f.endswith(".jpg")), key=lambda f: int(f.split(".")[0]))
    os.makedirs(out, exist_ok=True)
    durs = [hook_s] + [slide_s] * (len(slides) - 1)
    durs[-1] += 0.8  # let the CTA slide breathe
    inputs, filt = [], []
    for i, (s, d) in enumerate(zip(slides, durs)):
        p = os.path.join(src, s)
        bg = edge_colour(p)
        n = int((d + XF) * FPS)
        inputs += ["-loop", "1", "-t", f"{d + XF:.2f}", "-i", p]
        # upscale before zoompan to avoid jitter; slide 1 gets a stronger punch-in
        zmax, zstep = (1.06, 0.06 / n) if i == 0 else (1.035, 0.035 / n)
        filt.append(
            f"[{i}:v]scale=2160:2700,zoompan=z='min(zoom+{zstep:.6f},{zmax})':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":d={n}:s={W}x1350:fps={FPS},pad={W}:{H}:0:285:color={bg},setsar=1,format=yuv420p[v{i}]")
    last, t = "v0", durs[0]
    for i in range(1, len(slides)):
        filt.append(f"[{last}][v{i}]xfade=transition=slideleft:duration={XF}:offset={t:.2f}[x{i}]")
        last, t = f"x{i}", t + durs[i]
    total = sum(durs) + XF
    extra = []
    if top:
        bp = os.path.join(out, "_banner.png")
        banner(top, edge_colour(os.path.join(src, slides[0])), bp, font, hl)
        extra = ["-i", bp]
        filt.append(f"[{last}][{len(slides) + 1}:v]overlay=0:0[top]")
        last = "top"
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs,
           "-f", "lavfi", "-t", f"{total:.2f}", "-i", "anullsrc=r=44100:cl=stereo", *extra,
           "-filter_complex", ";".join(filt), "-map", f"[{last}]", "-map", f"{len(slides)}:a",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-shortest", "-movflags", "+faststart", os.path.join(out, "reel.mp4")]
    subprocess.run(cmd, check=True)
    first = Image.open(os.path.join(src, slides[0])).convert("RGB")
    cover = Image.new("RGB", (W, H), tuple(int(edge_colour(os.path.join(src, slides[0]))[i:i + 2], 16) for i in (2, 4, 6)))
    cover.paste(first, (0, 285))
    if top:
        cover.paste(Image.open(bp), (0, 0), Image.open(bp))
        os.remove(bp)
    cover.save(os.path.join(out, "cover.jpg"), quality=92)
    return total


if __name__ == "__main__":
    a = sys.argv[1:]
    print(f"{render(a[0], a[1], top=a[2] if len(a) > 2 else None):.1f}s")
