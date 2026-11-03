"""Fast animated Reels in the RT-04 / RP-04 shape: hook → 3 point cards → end card, mascot on every card.

    from reel_points import hook, point, end, render_motion
    scenes = [(hook("rt", "Your next [[$1]] of profit…", "SAVE THIS"), 3.0),
              (point("rt", 1, "Title with [[one]] highlight", visual_html, "small print"), 4.4), ...,
              (end("rt", "Legal. Boring. [[Worth]] it.", "SAVE THIS FOR JUNE"), 3.2)]
    render_motion(scenes, __file__, cover_scene=0)

brand = "rt" (Retained: navy, DM Serif, brass, Penny) or "rp" (Return Policy: ink, Space Grotesk, highlighter, Docket).
[[…]] highlights one word; wrap each word separately ("[[2]] [[years]]").
Helpers big(), stamp_el(), steps() build the visual for a point card.
"""
from motion import (scene, scene_rp, words, coin_mascot, render_motion, BRASS, GREEN, RED, NAVY, BONE,
                    RP_INK, RP_PAPER, RP_MINT, RP_HL, RP_RED)
from returnpolicy_kit import receipt_mascot

MONO = "font-family:'IBM Plex Mono',monospace;font-weight:600"
B = {
    "rt": dict(scene=scene, head="font-family:'DM Serif Display',serif;font-weight:400", accent=BRASS, num=GREEN, red=RED,
               small="font-size:40px;line-height:1.4;color:#D8D2C6", hl=(BRASS, NAVY), muted="#9A9384",
               mascot=lambda s, w=False: coin_mascot(s, wave=w)),
    "rp": dict(scene=scene_rp, head="font-family:'Space Grotesk',sans-serif;font-weight:700;letter-spacing:-0.03em", accent=RP_HL,
               num=RP_MINT, red=RP_RED, small="font-size:42px;line-height:1.38;color:#D9D3C5", hl=(RP_HL, RP_INK), muted="#A8A193",
               mascot=lambda s, w=False: receipt_mascot(s, wave=w, limb=RP_PAPER)),
}


def _w(b, text, start, step=0.1):
    return words(text, start, step, hl_bg=B[b]["hl"][0], hl_fg=B[b]["hl"][1])


def big(b, value, label="", start=0.8, size=190, count_to=None, pre="", post="", color=None):
    """A count-up (count_to=number) or popped big number, with an optional mono label beside it."""
    c = color or B[b]["num"]
    if count_to is not None:
        n = f'<span class="a" data-a="count" data-t="{start}" data-d="1.0" data-to="{count_to}" data-pre="{pre}" data-post="{post}" style="{MONO};font-size:{size}px;line-height:1;color:{c}">{pre}0{post}</span>'
    else:
        n = f'<span class="a" data-a="pop" data-t="{start}" data-d="0.4" style="display:inline-block;{MONO};font-size:{size}px;line-height:1;color:{c}">{value}</span>'
    lab = f'<span class="a" data-a="up" data-t="{start + 0.3}" data-d="0.3" style="{MONO};font-size:46px;color:{c}">{label}</span>' if label else ""
    return f'<div style="display:flex;align-items:baseline;gap:26px;flex-wrap:wrap">{n}{lab}</div>'


def stamp_el(b, text, start=1.4, color=None, size=50):
    c = color or B[b]["red"]
    return (f'<div class="a" data-a="stamp" data-t="{start}" data-d="0.35" style="display:inline-block;margin-top:30px;border:8px solid {c};color:{c};'
            f'{MONO};font-size:{size}px;padding:8px 22px;border-radius:12px;white-space:nowrap">{text}</div>')


def steps(b, items, start=0.8, gap=0.22):
    bg, fg = (BONE, NAVY) if b == "rt" else (RP_PAPER, RP_INK)
    return '<div style="display:flex;flex-direction:column;align-items:flex-start">' + "".join(
        f'<div class="a" data-a="pop" data-t="{start + i*gap:.2f}" data-d="0.35" style="display:inline-block;{MONO};font-size:42px;'
        f'background:{bg};color:{fg};padding:16px 26px;margin:0 0 18px 0;border-radius:{10 if b == "rt" else 0}px">{t}</div>' for i, t in enumerate(items)) + "</div>"


def hook(b, text, tag, size=150):
    k = B[b]
    return k["scene"](f"""
<div style="position:absolute;left:80px;top:300px;right:80px;{k['head']};font-size:{size}px;line-height:1.04">{_w(b, text, -0.3)}</div>
<div class="a" data-a="up" data-t="1.2" data-d="0.35" style="position:absolute;left:80px;top:1090px;{MONO};font-size:46px;color:{k['num']}">{tag}</div>
<div class="a" data-a="pop" data-t="0.5" data-d="0.45" style="position:absolute;left:620px;top:1180px">{k['mascot'](320, True)}</div>""")


def point(b, n, title, visual, small, wave=False, title_size=116):
    k = B[b]
    return k["scene"](f"""
<div style="position:absolute;left:80px;top:250px;right:80px">
  <div class="a" data-a="stamp" data-t="0" data-d="0.35" style="{MONO};font-size:110px;color:{k['accent']};display:inline-block">#{n}</div>
  <div style="{k['head']};font-size:{title_size}px;line-height:1.04;margin-top:24px">{_w(b, title, 0.25)}</div>
  <div style="margin-top:56px">{visual}</div>
  <div class="a" data-a="up" data-t="1.6" data-d="0.4" style="{k['small']};margin-top:46px;max-width:840px">{small}</div>
</div>
<div style="position:absolute;left:800px;top:1300px">{k['mascot'](220, wave)}</div>""")


def end(b, text, cta, size=136):
    k = B[b]
    return k["scene"](f"""
<div style="position:absolute;left:80px;top:300px;right:80px;{k['head']};font-size:{size}px;line-height:1.04">{_w(b, text, 0.05, 0.16)}</div>
<div class="a" data-a="up" data-t="0.9" data-d="0.35" style="position:absolute;left:80px;top:920px;{MONO};font-size:54px;color:{k['num']}">{cta}</div>
<div style="position:absolute;left:80px;top:1480px;{MONO};font-size:28px;color:{k['muted']}">General info only · Not personal advice</div>
<div class="a" data-a="pop" data-t="0.3" data-d="0.45" style="position:absolute;left:640px;top:1040px">{k['mascot'](300, True)}</div>""")
