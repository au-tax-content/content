"""RT-04 Reel v2 (animated): 3 legal ways business owners pay less tax. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from motion import scene, words, coin_mascot, render_motion, BRASS, GREEN, RED, BONE, NAVY

SERIF = "font-family:'DM Serif Display',serif;font-weight:400"
MONO = "font-family:'IBM Plex Mono',monospace;font-weight:600"
SMALL = "font-size:40px;line-height:1.4;color:#D8D2C6"

def point(n, title, visual, small, wave=False):
    return scene(f"""
<div style="position:absolute;left:80px;top:250px;right:80px">
  <div class="a" data-a="stamp" data-t="0" data-d="0.35" style="{MONO};font-size:120px;color:{BRASS};display:inline-block">#{n}</div>
  <div style="{SERIF};font-size:118px;line-height:1.05;margin-top:24px">{words(title, 0.25, 0.1)}</div>
  <div style="margin-top:60px">{visual}</div>
  <div class="a" data-a="up" data-t="1.6" data-d="0.4" style="{SMALL};margin-top:50px;max-width:820px">{small}</div>
</div>
{coin_mascot(230, wave=wave, x=790, y=1300)}""")

scenes = [
 (scene(f"""
<div style="position:absolute;left:80px;top:300px;right:80px;{SERIF};font-size:150px;line-height:1.04">
  {words("How business owners [[legally]] pay less tax", -0.3, 0.1)}
</div>
<div class="a" data-a="up" data-t="1.2" data-d="0.35" style="position:absolute;left:80px;top:1060px;{MONO};font-size:46px;color:{GREEN}">3 LEGAL MOVES · SAVE THIS</div>
<div class="a" data-a="pop" data-t="0.5" data-d="0.45" style="position:absolute;left:600px;top:1180px">{coin_mascot(330, wave=True)}</div>"""), 3.0),

 (point(1, "Buy before [[30 June]]",
   f"""<div style="display:flex;align-items:baseline;gap:24px"><span class="a" data-a="count" data-t="0.9" data-d="1.1" data-to="20000" data-pre="$" style="{MONO};font-size:170px;color:{GREEN}">$0</span></div>
   <div class="a" data-a="up" data-t="1.3" data-d="0.3" style="{MONO};font-size:34px;color:{BRASS};letter-spacing:.06em">WRITTEN OFF IN FULL · PER ASSET UNDER $20K</div>""",
   "Has to be used or installed ready for use that year. Turnover under $10M."), 4.3),

 (point(2, "Prepay up to [[12 months]]",
   f"""<div class="a" data-a="fill" data-t="0.9" data-d="1.0" data-on="{BRASS}" style="display:grid;grid-template-columns:repeat(6,120px);gap:16px">
   {''.join(f'<div style="height:96px;border:4px solid {BRASS};border-radius:14px;display:flex;align-items:center;justify-content:center;{MONO};font-size:30px;color:{NAVY}">{m}</div>' for m in range(1,13))}</div>""",
   "Rent, insurance, subscriptions: deductible this year if the period is 12 months or less and ends by next 30 June."), 4.3),

 (point(3, "Claim the [[16%]] offset",
   f"""<div style="position:relative;height:330px">
   <div class="a" data-a="pop" data-t="0.8" data-d="0.4" style="{MONO};font-size:200px;color:{GREEN};line-height:1">16%</div>
   <div class="a" data-a="stamp" data-t="1.3" data-d="0.35" style="position:absolute;left:10px;top:225px;border:8px solid {RED};color:{RED};{MONO};font-size:54px;padding:10px 24px;border-radius:12px;white-space:nowrap">UP TO $1,000 OFF</div></div>""",
   "Off the tax on business income, for sole traders and partners in small businesses.", wave=True), 4.3),

 (scene(f"""
<div style="position:absolute;left:80px;top:300px;right:80px;{SERIF};font-size:140px;line-height:1.05">{words("Legal. Boring. [[Worth thousands.]]", 0.05, 0.16)}</div>
<div class="a" data-a="up" data-t="0.9" data-d="0.35" style="position:absolute;left:80px;top:900px;{MONO};font-size:52px;color:{GREEN}">SAVE THIS FOR JUNE</div>
<div class="a" data-a="up" data-t="1.2" data-d="0.35" style="position:absolute;left:80px;top:990px;font-size:44px;color:#D8D2C6">Follow for the moves nobody tells you.</div>
<div style="position:absolute;left:80px;top:1480px;font-size:28px;color:#9A9384">General info only · Not personal advice</div>
<div class="a" data-a="pop" data-t="0.3" data-d="0.45" style="position:absolute;left:640px;top:1120px">{coin_mascot(300, wave=True)}</div>"""), 3.2),
]

if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
