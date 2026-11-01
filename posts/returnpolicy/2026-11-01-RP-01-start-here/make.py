"""RP-01 Start here (Return Policy foundation post 1). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from returnpolicy_kit import *

N = 5
def ok(t): return stamp(t, GREEN, -4, 24)

slides = [
 slide(f"""<div style="position:absolute;left:96px;top:200px;right:96px;{DISPLAY};font-size:136px;line-height:.98">
 Pay less tax. {hl('Legally.')}</div>
 <div style="position:absolute;left:96px;top:560px;right:300px;{BODY};font-size:44px;line-height:1.3;color:#D9D3C5">Tax for people on wages, renters and landlords. Plain English, every figure checked on ato.gov.au.</div>
 {bubble("Hi, I'm Docket. I read the fine print so you don't have to.", 96, 900, 520, bg=PAPER, fg=INK)}
 {docket(270, 700, 840, wave=True, dark=True)}""", 1, N, swipe=True, bg=INK, fg=PAPER),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:104px;line-height:1">Who this is {hl('for')}.</div>
 {receipt(''.join([item('YOU EARN A WAGE', right_html=ok('YES')), item('YOU RENT OR WORK FROM HOME', right_html=ok('YES')),
   item('YOU OWN A RENTAL OR TWO', right_html=ok('YES')), item('YOU DO YOUR OWN RETURN', right_html=ok('YES')),
   f'<div style="border-top:4px dashed {RULE}"></div>',
   f'<div style="{BODY};font-size:34px;line-height:1.35">Run a business? Our sister account <b>@retained.au</b> is for you.</div>']),
   96, 420, 888, head="RETURN POLICY", sub="WHO IT'S FOR · NOV 2026")}
 {docket(160, 860, 1010)}""", 2, N, swipe=True),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:104px;line-height:1">What you'll get {hl('each week')}.</div>
 {receipt(''.join([item('PAY LESS, LEGALLY', 'SUPER · OFFSETS', 32), item('IS IT CLAIMABLE?', 'GUESS Y/N', 32),
   item('WHAT CAN A ___ CLAIM?', 'BY JOB', 32), item('ATO LETTERS + MYTHS', 'DECODED', 32), item('TAX NEWS', 'IN 48H', 32),
   f'<div style="border-top:4px dashed {RULE}"></div>',
   f'<div style="display:flex;justify-content:space-between;{MONO};font-size:32px"><span>TOTAL</span><span style="color:{GREEN}">4 POSTS / WEEK</span></div>']),
   96, 520, 888, head="THE SERIES", sub="SAME LABELS EVERY TIME")}""", 3, N, swipe=True, bg=PAPER2),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:112px;line-height:1">Want the list for {hl('your')} job?</div>
 <div style="position:absolute;left:96px;right:96px;top:520px;background:{PAPER};color:{INK};padding:48px 56px">
  <div style="{MONO5};font-size:28px;color:{MUTED}">COMMENT THE WORD</div>
  <div style="{MONO};font-size:150px;letter-spacing:.06em;line-height:1;margin:12px 0">CLAIM</div>
  <div style="{BODY};font-size:40px;line-height:1.3">and you'll be first to get <b>The Claim Sheet</b> (what 20 common jobs can claim) when it lands in December.</div></div>
 {docket(150, 860, 1005, wave=True, dark=True)}""", 4, N, swipe=True, bg=GREEN, fg=PAPER),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:104px;line-height:1">The {hl('house rules')}.</div>
 <div style="position:absolute;left:96px;right:96px;top:440px;display:flex;flex-direction:column;gap:40px">
  <div>{stamp('GENERAL INFO ONLY', INK, -3, 34)}<div style="{BODY};font-size:36px;margin-top:14px;color:{MUTED}">Not personal advice. Your situation will differ.</div></div>
  <div>{stamp('CHECKED ON ATO.GOV.AU', GREEN, 2, 34)}<div style="{BODY};font-size:36px;margin-top:14px;color:{MUTED}">The week it's posted, with the income year.</div></div>
  <div>{stamp('ALWAYS LEGAL', GREEN, -2, 34)}<div style="{BODY};font-size:36px;margin-top:14px;color:{MUTED}">How it works, who it suits, and the catch.</div></div>
  <div>{stamp('NO SELLING', RED, 3, 34)}<div style="{BODY};font-size:36px;margin-top:14px;color:{MUTED}">We teach. We don't do your tax.</div></div></div>
 {bubble("Follow for one money move a week.", 96, 1080, 470)}
 {docket(220, 780, 1010, wave=True)}""", 5, N),
]
if __name__ == "__main__":
    render_slides(slides, __file__)
