"""RP-04 Reel (animated): Forgot a deduction? You can still claim it (amending a return). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from motion import scene_rp, words, render_motion, RP_INK, RP_PAPER, RP_GREEN, RP_MINT, RP_HL, RP_RED
from returnpolicy_kit import receipt_mascot

D = "font-family:'Space Grotesk',sans-serif;font-weight:700;letter-spacing:-0.03em"
MONO = "font-family:'IBM Plex Mono',monospace;font-weight:600"
SMALL = "font-size:42px;line-height:1.38;color:#D9D3C5"
W = lambda t, s, st=0.1: words(t, s, st, hl_bg=RP_HL, hl_fg=RP_INK)
def doc(size, x, y, wave=False): return receipt_mascot(size, wave=wave, x=x, y=y, limb=RP_PAPER)

def point(n, title, visual, small, wave=False):
    return scene_rp(f"""
<div style="position:absolute;left:80px;top:250px;right:80px">
  <div class="a" data-a="stamp" data-t="0" data-d="0.35" style="{MONO};font-size:110px;color:{RP_HL};display:inline-block">#{n}</div>
  <div style="{D};font-size:120px;line-height:1.02;margin-top:24px">{W(title, 0.25)}</div>
  <div style="margin-top:60px">{visual}</div>
  <div class="a" data-a="up" data-t="1.6" data-d="0.4" style="{SMALL};margin-top:50px;max-width:840px">{small}</div>
</div>
{doc(220, 800, 1300, wave)}""")

step = lambda txt, t: f'<div class="a" data-a="pop" data-t="{t}" data-d="0.35" style="display:inline-block;{MONO};font-size:44px;background:{RP_PAPER};color:{RP_INK};padding:16px 26px;margin:0 0 18px 0">{txt}</div>'

scenes = [
 (scene_rp(f"""
<div style="position:absolute;left:80px;top:300px;right:80px;{D};font-size:150px;line-height:1">{W("Forgot a deduction? You can [[still]] claim it.", -0.3)}</div>
<div class="a" data-a="up" data-t="1.2" data-d="0.35" style="position:absolute;left:80px;top:1080px;{MONO};font-size:46px;color:{RP_MINT}">AMEND YOUR RETURN · SAVE THIS</div>
<div class="a" data-a="pop" data-t="0.5" data-d="0.45" style="position:absolute;left:620px;top:1180px">{doc(320, 0, 0, True)}</div>"""), 3.0),

 (point(1, "You have [[2]] [[years]]",
   f"""<div style="display:flex;align-items:baseline;gap:30px"><span class="a" data-a="count" data-t="0.9" data-d="0.9" data-to="2" style="{MONO};font-size:220px;line-height:1;color:{RP_MINT}">0</span>
   <span class="a" data-a="up" data-t="1.2" data-d="0.3" style="{MONO};font-size:60px;color:{RP_MINT}">YEARS</span></div>""",
   "For most people, counted from the day after your notice of assessment is sent."), 4.3),

 (point(2, "Do it in [[myGov]]",
   f"""<div style="display:flex;flex-direction:column;align-items:flex-start">{step('ATO', 0.8)}{step('→ MANAGE TAX RETURNS', 1.0)}{step('→ AMEND', 1.2)}</div>""",
   "Or ask a registered tax agent. Wait until your original return is processed first."), 4.5),

 (point(3, "Online: about [[15]] [[days]]",
   f"""<div style="position:relative;height:300px">
   <div style="display:flex;align-items:baseline;gap:26px"><span class="a" data-a="count" data-t="0.8" data-d="1.0" data-to="15" style="{MONO};font-size:200px;line-height:1;color:{RP_MINT}">0</span>
   <span class="a" data-a="up" data-t="1.1" data-d="0.3" style="{MONO};font-size:48px;color:{RP_MINT}">BUSINESS DAYS</span></div>
   <div class="a" data-a="stamp" data-t="1.4" data-d="0.35" style="position:absolute;left:10px;top:225px;border:8px solid {RP_RED};color:{RP_RED};{MONO};font-size:48px;padding:8px 22px;border-radius:12px;white-space:nowrap">PAPER: UP TO 90</div></div>""",
   "That's for online amendments. Have the receipts for anything you add.", wave=True), 4.5),

 (scene_rp(f"""
<div style="position:absolute;left:80px;top:300px;right:80px;{D};font-size:140px;line-height:1.02">{W("Your money. Your [[two]] [[years.]]", 0.05, 0.16)}</div>
<div class="a" data-a="up" data-t="0.9" data-d="0.35" style="position:absolute;left:80px;top:900px;{MONO};font-size:56px;color:{RP_MINT}">SAVE THIS FOR LATER</div>
<div style="position:absolute;left:80px;top:1480px;{MONO};font-size:28px;color:#A8A193">General info only · Not personal advice</div>
<div class="a" data-a="pop" data-t="0.3" data-d="0.45" style="position:absolute;left:640px;top:1040px">{doc(300, 0, 0, True)}</div>"""), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
