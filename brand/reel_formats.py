"""Reel formats modelled on what gets outlier views for faceless tax/money accounts (benchmark study, 15 Nov 2026).

    from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
    ...
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)

- hook_c(b, text, tag, theme, strap=None)   full-colour hook cover. Themes: rp ink|mint|yellow|paper|red, rt navy|brass|green.
                                            strap="ATO UPDATE" adds a red news strap. Keep the claim under 8 words.
- card(b, title, visual, small)             a point card without the #number.
- listloop(b, title, kicker, items, ...)    ONE looping scene: a save-able list printing line by line
                                            (Return Policy: thermal receipt; Retained: ledger page). items = (label, tag, note).
- tier(b, title, kicker, items)             S-D ranking board; items in reveal order = (tier letter, chip label <=16 chars, reason <=80 chars).
- ladder(b, title, kicker, rows, foot)      rows = (left label, number, sub): numbers count up one row at a time.
- buckets(b, title, cols, note)             tax brackets as filling tubes; cols = (rate, slice label, fill 0-1, tax label, colour).

Why these: the faceless posts that beat their account median 100x+ were short looping lists ("7 deductions that sound
illegal (but aren't)"), tier lists, bracket explainers and milestone/number reveals. Hooks promise something; never copy a post.
Keep text between y=250 and y=1560 and render with cover_y=215 so the cover keeps the title. Check one contact sheet per Reel before queueing.
"""
from motion import (scene, scene_rp, words, coin_mascot, render_motion, BRASS, GREEN, RED, NAVY, BONE,
                    RP_INK, RP_PAPER, RP_MINT, RP_HL, RP_RED)
from returnpolicy_kit import receipt_mascot, tear
from reel_points import B, MONO, hook, point, end, big, stamp_el, steps  # noqa: F401 (re-exported)

RP_GREEN, RT_GREEN, RULE, MUTED_RP, MUTED_RT = "#0E7A4B", "#1F7A4D", "#BDB4A0", "#5B564C", "#6B6455"
# theme -> (ground, text, highlight bg, highlight fg, tag colour, dark ground?)
T = {
    "rp": {"ink": (RP_INK, RP_PAPER, RP_HL, RP_INK, RP_MINT, True), "mint": (RP_MINT, RP_INK, RP_INK, RP_MINT, RP_INK, False),
           "yellow": (RP_HL, RP_INK, RP_INK, RP_HL, RP_GREEN, False), "paper": (RP_PAPER, RP_INK, RP_GREEN, RP_PAPER, RP_RED, False),
           "red": (RP_RED, RP_PAPER, RP_PAPER, RP_RED, RP_HL, True)},
    "rt": {"navy": (NAVY, BONE, BRASS, NAVY, GREEN, True), "brass": (BRASS, NAVY, NAVY, BONE, NAVY, False),
           "green": (RT_GREEN, BONE, BONE, RT_GREEN, "#F6D58E", True)},
}
TIER_C = {"S": "#FF6B6B", "A": "#FFA94D", "B": "#FFE36E", "C": "#8CE99A", "D": "#74C0FC"}


def _mascot(b, size, wave=False, dark=True):
    if b == "rt":
        return coin_mascot(size, wave=wave)
    return receipt_mascot(size, wave=wave, limb=RP_PAPER if dark else RP_INK)


def _brand_fix(b, theme):
    """Retained's tag is brass, which disappears on the brass ground: repaint it navy."""
    if b == "rt" and theme == "brass":
        return f'<div style="position:absolute;left:80px;top:150px;{MONO};font-size:30px;letter-spacing:.16em;color:{NAVY}">RETAINED</div>'
    return ""


def hook_c(b, text, tag, theme=None, size=150, strap=None):
    k = B[b]
    theme = theme or ("ink" if b == "rp" else "navy")
    bg, fg, hb, hf, tc, dark = T[b][theme]
    top = 300
    strap_html = ""
    if strap:
        top = 410
        strap_html = (f'<div class="a" data-a="stamp" data-t="-0.4" data-d="0.3" style="position:absolute;left:80px;top:270px;display:inline-block;'
                      f'background:{RP_RED if b == "rp" else RED};color:#fff;{MONO};font-size:44px;letter-spacing:.08em;padding:10px 24px;border-radius:8px">{strap}</div>')
    body = f"""{_brand_fix(b, theme)}{strap_html}
<div style="position:absolute;left:80px;top:{top}px;right:80px">
  <div style="{k['head']};font-size:{size}px;line-height:1.04">{words(text, -1.2, 0.08, hl_bg=hb, hl_fg=hf)}</div>
  <div class="a" data-a="up" data-t="0.5" data-d="0.35" style="{MONO};font-size:48px;color:{tc};margin-top:54px">{tag}</div>
</div>
<div class="a" data-a="pop" data-t="-0.2" data-d="0.45" style="position:absolute;left:600px;top:1080px">{_mascot(b, 380, True, dark)}</div>"""
    return k["scene"](body, bg=bg, fg=fg)


def card(b, title, visual, small, wave=False, title_size=116):
    k = B[b]
    return k["scene"](f"""
<div style="position:absolute;left:80px;top:270px;right:80px">
  <div style="{k['head']};font-size:{title_size}px;line-height:1.04">{words(title, 0.0, 0.1, hl_bg=k['hl'][0], hl_fg=k['hl'][1])}</div>
  <div style="margin-top:56px">{visual}</div>
  <div class="a" data-a="up" data-t="1.6" data-d="0.4" style="{k['small']};margin-top:46px;max-width:840px">{small}</div>
</div>
<div style="position:absolute;left:800px;top:1300px">{k['mascot'](220, wave)}</div>""")


def _title(b, title, kicker, size, width=730):
    k = B[b]
    kc = k["num"]
    return (f'<div style="width:{width}px;{k["head"]};font-size:{size}px;line-height:1.05">{words(title, -1.2, 0.07, hl_bg=k["hl"][0], hl_fg=k["hl"][1])}</div>'
            f'<div class="a" data-a="up" data-t="0.3" data-d="0.3" style="{MONO};font-size:32px;letter-spacing:.06em;color:{kc};margin-top:22px">{kicker}</div>')


def listloop(b, title, kicker, items, head=None, foot=None, title_size=92, row_size=44, start=0.9, gap=0.7, tag_color=None):
    """One looping scene. items: (label, tag, note). Short labels (about 24 chars), tags <= 12 chars, notes <= 46 chars or ''."""
    k = B[b]
    rp = b == "rp"
    ink, mut, num_c = (RP_INK, MUTED_RP, MUTED_RP) if rp else (NAVY, MUTED_RT, "#8E6A2E")
    tc = tag_color or (RP_GREEN if rp else RT_GREEN)
    lab_font = ("font-family:'Space Grotesk',sans-serif;font-weight:700;letter-spacing:-0.02em" if rp else "font-family:'DM Serif Display',serif;font-weight:400")
    rows = ""
    for i, (label, tag, note) in enumerate(items):
        t = start + i * gap
        n = f'<div style="{MONO};font-size:28px;color:{mut};margin:3px 0 0 62px">{note}</div>' if note else ""
        rows += (f'<div class="a" data-a="up" data-t="{t:.2f}" data-d="0.3" style="padding:11px 0;border-bottom:3px {"dotted" if rp else "solid"} {RULE if rp else "#D9D2C2"}">'
                 f'<div style="display:flex;align-items:baseline;gap:20px"><span style="{MONO};font-size:30px;color:{num_c};width:42px">{i + 1:02d}</span>'
                 f'<span style="{lab_font};font-size:{row_size if rp else row_size + 4}px;line-height:1.1;flex:1;color:{ink}">{label}</span>'
                 f'<span style="{MONO};font-size:29px;color:{tc};white-space:nowrap">{tag}</span></div>{n}</div>')
    if foot:
        rows += (f'<div class="a" data-a="up" data-t="{start + len(items) * gap:.2f}" data-d="0.3" style="{MONO};font-size:27px;line-height:1.35;color:{ink};padding-top:16px">{foot}</div>')
    head = head or ("RETURN POLICY · CLAIM CHECK" if rp else "RETAINED · LEDGER")
    if rp:
        panel = (f'<div style="margin-top:34px;width:940px;filter:drop-shadow(0 14px 24px rgba(0,0,0,.4))">{tear(RP_PAPER)}'
                 f'<div style="background:{RP_PAPER};padding:20px 40px 26px"><div style="text-align:center;{MONO};font-size:26px;letter-spacing:.12em;color:{ink}">{head}</div>'
                 f'<div style="border-top:4px dashed {RULE};margin:16px 0 2px"></div>{rows}</div>{tear(RP_PAPER, flip=True)}</div>')
    else:
        panel = (f'<div style="margin-top:34px;width:940px;box-sizing:border-box;background:{BONE};border-radius:22px;border-top:14px solid {BRASS};padding:24px 44px 30px;'
                 f'box-shadow:0 18px 40px rgba(0,0,0,.45)"><div style="{MONO};font-size:26px;letter-spacing:.14em;color:#8E6A2E">{head}</div>'
                 f'<div style="border-top:3px solid {NAVY};margin:14px 0 2px"></div>{rows}</div>')
    return k["scene"](f"""
<div style="position:absolute;left:70px;top:250px;width:940px">{_title(b, title, kicker, title_size)}{panel}</div>
<div class="a" data-a="pop" data-t="0.1" data-d="0.4" style="position:absolute;left:815px;top:235px">{_mascot(b, 200, True)}</div>""")


def tier(b, title, kicker, items, title_size=86, start=1.3, gap=2.7, letters="SABCD"):
    """Ranking board. items in reveal order: (tier letter, chip label <=16 chars, reason <=80 chars). Scene length: tier_len(items)."""
    k = B[b]
    chip_bg, chip_fg = (RP_PAPER, RP_INK) if b == "rp" else (BONE, NAVY)
    rows = ""
    for L in letters:
        chips = "".join(
            f'<div class="a" data-a="pop" data-t="{start + i * gap:.2f}" data-d="0.4" style="display:inline-block;{MONO};font-size:36px;background:{chip_bg};color:{chip_fg};'
            f'padding:14px 16px;border-radius:8px;white-space:nowrap">{lab}</div>' for i, (t, lab, _) in enumerate(items) if t == L)
        rows += (f'<div style="display:flex;height:138px;border-bottom:5px solid {RP_INK if b == "rp" else NAVY}">'
                 f'<div style="width:136px;background:{TIER_C[L]};color:#1A1A1A;display:flex;align-items:center;justify-content:center;'
                 f'font-family:\'Space Grotesk\',sans-serif;font-weight:700;font-size:88px">{L}</div>'
                 f'<div style="flex:1;background:rgba(255,255,255,.09);display:flex;align-items:center;gap:14px;padding:0 18px">{chips}</div></div>')
    caps = "".join(
        f'<div class="a" data-a="win" data-t="{start + i * gap:.2f}" data-d="{gap if i < len(items) - 1 else gap + 2:.2f}" style="position:absolute;left:0;top:0;right:0">'
        f'<div style="{MONO};font-size:34px;color:{TIER_C[t]}">{t}-TIER · {lab}</div>'
        f'<div style="{k["small"]};font-size:40px;line-height:1.3;margin-top:10px">{why}</div></div>' for i, (t, lab, why) in enumerate(items))
    return k["scene"](f"""
<div style="position:absolute;left:70px;top:250px;width:940px">{_title(b, title, kicker, title_size)}</div>
<div class="a" data-a="pop" data-t="0.1" data-d="0.4" style="position:absolute;left:815px;top:235px">{_mascot(b, 200, True)}</div>
<div style="position:absolute;left:70px;top:640px;width:940px;border-radius:14px;overflow:hidden;box-shadow:0 18px 40px rgba(0,0,0,.45)">{rows}</div>
<div style="position:absolute;left:70px;top:1350px;width:940px;height:200px">{caps}</div>""")


def tier_len(items, start=1.3, gap=2.7):
    return round(start + len(items) * gap + 1.2, 1)


def ladder(b, title, kicker, rows, foot, title_size=92, start=0.9, gap=0.75, pre="$", post="", num_size=88):
    """rows: (left label, number or text, sub). Numbers count up; text pops."""
    k = B[b]
    chip_bg, chip_fg = (RP_PAPER, RP_INK) if b == "rp" else (BONE, NAVY)
    out = ""
    for i, (left, val, sub) in enumerate(rows):
        t = start + i * gap
        if isinstance(val, (int, float)):
            num = (f'<span class="a" data-a="count" data-t="{t + 0.1:.2f}" data-d="0.9" data-to="{val}" data-pre="{pre}" data-post="{post}" '
                   f'style="{MONO};font-size:{num_size}px;line-height:1;color:{k["num"]}">{pre}0{post}</span>')
        else:
            num = f'<span class="a" data-a="pop" data-t="{t + 0.1:.2f}" data-d="0.4" style="display:inline-block;{MONO};font-size:{num_size}px;line-height:1;color:{k["num"]}">{val}</span>'
        out += (f'<div class="a" data-a="up" data-t="{t:.2f}" data-d="0.3" style="display:flex;align-items:center;gap:26px;margin-bottom:26px">'
                f'<div style="width:236px;text-align:center;{MONO};font-size:52px;background:{chip_bg};color:{chip_fg};padding:16px 0;border-radius:{0 if b == "rp" else 12}px">{left}</div>'
                f'<div style="{MONO};font-size:44px;color:{k["muted"]}">→</div>'
                f'<div>{num}<div style="{MONO};font-size:27px;color:{k["muted"]};margin-top:6px">{sub}</div></div></div>')
    return k["scene"](f"""
<div style="position:absolute;left:70px;top:250px;width:940px">{_title(b, title, kicker, title_size)}
<div style="margin-top:50px">{out}</div>
<div class="a" data-a="up" data-t="{start + len(rows) * gap + 0.2:.2f}" data-d="0.3" style="{MONO};font-size:27px;line-height:1.4;color:{k['muted']};margin-top:8px">{foot}</div></div>
<div class="a" data-a="pop" data-t="0.1" data-d="0.4" style="position:absolute;left:815px;top:235px">{_mascot(b, 200, True)}</div>""")


def buckets(b, title, cols, note, title_size=104, start=0.9, gap=1.3):
    """Tax brackets as filling tubes. cols: (rate label, slice label, fill 0-1, tax label, colour)."""
    k = B[b]
    tubes = ""
    for i, (rate, slice_label, fill, tax, colour) in enumerate(cols):
        t = start + i * gap
        tubes += (f'<div style="width:270px;text-align:center"><div class="a" data-a="pop" data-t="{t:.2f}" data-d="0.35" style="display:inline-block;{MONO};font-size:72px;color:{colour}">{rate}</div>'
                  f'<div style="position:relative;height:430px;margin:14px 16px 0;border:7px solid {RP_PAPER if b == "rp" else BONE};border-top:none;border-radius:0 0 26px 26px;overflow:hidden">'
                  f'<div class="a" data-a="growh" data-t="{t + 0.15:.2f}" data-d="0.9" data-h="{int(fill * 100)}" style="position:absolute;left:0;right:0;bottom:0;height:0;background:{colour}"></div></div>'
                  f'<div style="{MONO};font-size:29px;color:{k["muted"]};margin-top:14px">{slice_label}</div>'
                  f'<div class="a" data-a="pop" data-t="{t + 0.9:.2f}" data-d="0.35" style="display:inline-block;{MONO};font-size:50px;color:{colour};margin-top:6px">{tax}</div></div>')
    return k["scene"](f"""
<div style="position:absolute;left:70px;top:270px;width:940px">
  <div style="{k['head']};font-size:{title_size}px;line-height:1.04">{words(title, 0.0, 0.1, hl_bg=k['hl'][0], hl_fg=k['hl'][1])}</div>
  <div style="display:flex;justify-content:space-between;margin-top:50px">{tubes}</div>
  <div class="a" data-a="up" data-t="{start + len(cols) * gap + 0.5:.2f}" data-d="0.4" style="{k['small']};margin-top:40px;max-width:700px">{note}</div>
</div>
<div style="position:absolute;left:830px;top:1300px">{k['mascot'](200, True)}</div>""")
