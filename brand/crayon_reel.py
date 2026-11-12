"""Crayon two-panel slides -> a native-feeling 9:16 Reel where each slide slips in and the punchline lands.

Per slide: the slide slips in from the right (the previous one slips out left), the top panel + line show,
a beat later the bottom panel slides up and the "NOT ..." line pops. Ends on a question card.
Reuses the exact rendered slides (1.jpg ... n.jpg from crayon.render), so the words stay checked.

    from crayon_reel import render
    render(src_folder, out_folder, hook="5 tax facts people get backwards", end="Which one got you?", hl=(255, 226, 77))
Writes reel.mp4 (1080x1920, 30 fps, silent AAC; music via audio_id at publish) and cover.jpg.
"""
import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "fonts", "patrick-hand-latin-400-normal.woff2")
W, H, FPS = 1080, 1920, 30
BG = (251, 248, 242)
Y0 = 330            # where the 1080x1350 slide sits (keeps it inside the grid-safe middle)
SLIDE_S, FIRST_S, END_S, SLIP = 3.7, 4.0, 2.6, 0.32
REVEAL = 1.35       # when the punchline panel arrives (s after slide start)

def ease(t): t = max(0.0, min(1.0, t)); return 1 - (1 - t) ** 3
def back(t):  # small overshoot for the pop
    t = max(0.0, min(1.0, t)); c = 1.7; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2

def text_img(text, size, colour=(26, 26, 26), maxw=W - 140, hl=None):
    f = ImageFont.truetype(FONT, size)
    d = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) > maxw and cur: lines.append(cur); cur = w_
        else: cur = t
    lines.append(cur)
    lh = int(size * 1.08); h = lh * len(lines) + 30
    im = Image.new("RGBA", (W, h), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    for i, ln in enumerate(lines):
        tw = dr.textlength(ln, font=f); x = (W - tw) / 2; y = 12 + i * lh
        if hl: dr.rounded_rectangle((x - 22, y - 2, x + tw + 22, y + lh - 2), 16, fill=hl)
        dr.text((x, y), ln, font=f, fill=colour)
    return im

def parts(path):
    s = Image.open(path).convert("RGB")
    full = s.copy()
    top = s.crop((0, 0, W, 745))                     # top panel + its line
    bot_panel = s.crop((0, 745, W, 1252))
    bot_text = s.crop((0, 1252, W, 1350))
    return full, top, bot_panel, bot_text

def slide_frame(p, t, cover=False):
    """One slide's own layer (1080x1350, RGBA) at local time t."""
    full, top, bpan, btxt = p
    lay = Image.new("RGBA", (W, 1350), BG + (255,))
    # gentle push-in on the top half
    z = 1 + 0.025 * min(t / 3.5, 1)
    tz = top.resize((int(W * z), int(745 * z)), Image.LANCZOS)
    lay.paste(tz.crop(((tz.width - W) // 2, 0, (tz.width - W) // 2 + W, 745)), (0, 0))
    if cover or t >= REVEAL:
        k = 1.0 if cover else ease((t - REVEAL) / 0.38)
        y = int(745 + (1 - k) * 260)
        bp = bpan.copy().convert("RGBA"); bp.putalpha(int(255 * k))
        lay.alpha_composite(bp, (0, y))
        k2 = 1.0 if cover else back((t - REVEAL - 0.28) / 0.32)
        if cover or t >= REVEAL + 0.28:
            s = max(0.6, 0.6 + 0.4 * k2)
            bt = btxt.resize((int(W * s), int(98 * s)), Image.LANCZOS).convert("RGBA")
            lay.alpha_composite(bt, ((W - bt.width) // 2, 1252 + (98 - bt.height) // 2))
    return lay

def render(src, out, hook, end="Which one got you?", hl=(255, 226, 77), sub="Follow for part 2"):
    slides = sorted((f for f in os.listdir(src) if f[0].isdigit() and f.endswith(".jpg")), key=lambda f: int(f.split(".")[0]))
    P = [parts(os.path.join(src, s)) for s in slides]
    durs = [FIRST_S] + [SLIDE_S] * (len(P) - 1)
    starts = [sum(durs[:i]) for i in range(len(P))]
    total = sum(durs) + END_S
    hook_im = text_img(hook, 70, hl=hl)
    end_im = text_img(end, 110); sub_im = text_img(sub, 64, colour=(215, 38, 30))
    os.makedirs(out, exist_ok=True)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-t", f"{total:.2f}", "-i", "anullsrc=r=44100:cl=stereo",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest",
           "-movflags", "+faststart", os.path.join(out, "reel.mp4")]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = int(total * FPS)
    for fi in range(n):
        t = fi / FPS
        fr = Image.new("RGBA", (W, H), BG + (255,))
        if t < starts[-1] + durs[-1]:
            i = max(j for j in range(len(P)) if starts[j] <= t)
            lt = t - starts[i]
            if i > 0 and lt < SLIP:          # slip: previous out left, current in from right
                k = ease(lt / SLIP)
                fr.alpha_composite(slide_frame(P[i - 1], durs[i - 1]), (int(-W * k), Y0))
                fr.alpha_composite(slide_frame(P[i], lt), (int(W * (1 - k)), Y0))
            else:
                fr.alpha_composite(slide_frame(P[i], lt), (0, Y0))
            # hook band (drops in on frame 0, stays) + progress dots
            hk = ease(t / 0.35)
            fr.alpha_composite(hook_im, (0, int(Y0 - hook_im.height - 26 - (1 - hk) * 60)))
            dr = ImageDraw.Draw(fr)
            for j in range(len(P)):
                cx = W // 2 + (j - (len(P) - 1) / 2) * 34
                dr.ellipse((cx - 8, Y0 + 1350 + 40, cx + 8, Y0 + 1350 + 56), fill=(26, 26, 26) if j == i else (205, 198, 186))
        else:                               # end card slips in
            lt = t - (starts[-1] + durs[-1]); k = ease(lt / SLIP)
            fr.alpha_composite(slide_frame(P[-1], durs[-1]), (int(-W * k), Y0))
            card = Image.new("RGBA", (W, H), BG + (255,))
            s = back(min(1, lt / 0.45)); e = end_im.resize((max(1, int(W * s)), max(1, int(end_im.height * s))))
            card.alpha_composite(e, ((W - e.width) // 2, 760 - e.height // 2))
            if lt > 0.6: card.alpha_composite(sub_im, (0, 760 + end_im.height // 2 + 40))
            fr.alpha_composite(card.crop((0, 0, W, H)), (int(W * (1 - k)), 0))
        pr.stdin.write(fr.convert("RGB").tobytes())
    pr.stdin.close(); pr.wait()
    cov = Image.new("RGBA", (W, H), BG + (255,))
    cov.alpha_composite(slide_frame(P[0], 0, cover=True), (0, Y0)); cov.alpha_composite(hook_im, (0, Y0 - hook_im.height - 26))
    cov.convert("RGB").save(os.path.join(out, "cover.jpg"), quality=92)
    return total
