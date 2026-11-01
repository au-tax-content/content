"""RP-05 News decoded: the $1,000 standard deduction (2026-27). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from returnpolicy_kit import *

N = 6
TAG = "NEWS DECODED"
def big(t, c=GREEN, s=150): return f'<span style="{MONO};font-size:{s}px;line-height:1;color:{c}">{t}</span>'
def para(t, s=38): return f'<div style="{BODY};font-size:{s}px;line-height:1.3">{t}</div>'
DASH = f'<div style="border-top:4px dashed {RULE}"></div>'

def person(name, spent, claim, std, total, x, note):
    rows = ''.join([item('WORK COSTS', spent, 30), item('CLAIMED', claim, 30), item('STANDARD', std, 30), DASH,
                    f'<div style="{MONO5};font-size:24px;color:{MUTED}">TOTAL DEDUCTION</div>',
                    f'<div style="{MONO};font-size:64px;color:{GREEN}">{total}</div>',
                    f'<div style="{BODY};font-size:28px;line-height:1.25;color:{MUTED}">{note}</div>'])
    return receipt(rows, x, 430, 420, head=name, sub="2026–27")

slides = [
 slide(f"""<div style="position:absolute;left:96px;top:200px;right:96px;{DISPLAY};font-size:122px;line-height:.98">
 {hl('$1,000')} off your taxable income. No receipts.</div>
 <div style="position:absolute;left:96px;top:620px;right:300px;{BODY};font-size:44px;line-height:1.3;color:#D9D3C5">The new standard deduction starts this income year. Here's who wins, and when to keep itemising.</div>
 {bubble("It's law, and it starts with 2026–27.", 96, 1010, 500, bg=PAPER, fg=INK)}
 {docket(250, 700, 900, wave=True, dark=True)}""", 1, N, swipe=True, bg=INK, fg=PAPER, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">What it {hl('is')}.</div>
 {receipt(''.join([item('AMOUNT', 'UP TO $1,000'), item('RECEIPTS NEEDED', right_html=stamp('NONE', GREEN, -4, 26)),
   item('HOW', 'AUTOMATIC'), item('STARTS', '2026–27 YEAR'), item('IN YOUR 2025–26 RETURN?', right_html=stamp('NO', RED, 4, 26)), DASH,
   para('<b>Who:</b> residents earning wages or other labour income.', 34),
   para('<b>Not:</b> business or investment income only. Capped at your labour income.', 34)]),
   96, 330, 888, head="STANDARD DEDUCTION", sub="ATO · CHECKED 1 NOV 2026")}""", 2, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:96px;line-height:1">Take it or {hl('itemise')}?</div>
 {person('MIA', '$400', '$400', '$600', '$1,000', 96, 'Claims cut the $1,000 dollar for dollar. Same total either way.')}
 {person('JO', '$2,400', '$2,400', '$0', '$2,400', 564, 'Over $1,000 with records? Claim the lot instead.')}""", 3, N, swipe=True, bg=PAPER2, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:88px;line-height:1">Still claimed {hl('on top')}.</div>
 <div style="position:absolute;left:96px;top:320px;right:96px;{BODY};font-size:38px;color:{MUTED}">These don't shrink the $1,000.</div>
 {receipt(''.join([item('UNION + PROFESSIONAL FEES', right_html=stamp('ON TOP', GREEN, -3, 24)), item('TAX AGENT FEES', right_html=stamp('ON TOP', GREEN, 3, 24)),
   item('GIFTS + DONATIONS', right_html=stamp('ON TOP', GREEN, -4, 24)), item('PERSONAL SUPER CONTRIBUTIONS', right_html=stamp('ON TOP', GREEN, 2, 24)),
   item('INCOME PROTECTION', right_html=stamp('ON TOP', GREEN, -2, 24)), item('RENTAL + INVESTMENT COSTS', right_html=stamp('ON TOP', GREEN, 4, 24))]),
   96, 440, 888)}
 {docket(130, 880, 1000)}""", 4, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">What it's {hl('worth')}.</div>
 <div style="position:absolute;left:96px;right:96px;top:380px;display:flex;flex-direction:column;gap:50px">
  <div><div style="{MONO5};font-size:30px;color:{MUTED}">ON THE 30% RATE ($45K–$135K)</div>{big('$320')}
   <div style="{BODY};font-size:36px;margin-top:10px">less tax, including the 2% Medicare levy.</div></div>
  <div><div style="{MONO5};font-size:30px;color:{MUTED}">ON THE 15% RATE ($18,201–$45K)</div>{big('$170', INK, 120)}</div>
  <div style="border-top:4px dashed {RULE};padding-top:30px">{para('<b>Also from 1 July 2026:</b> the old $300 no-receipts rule is gone. Laundry is a flat $1 a load for work clothes, 50c for mixed loads.', 36)}</div></div>""", 5, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:200px;right:96px;{DISPLAY};font-size:116px;line-height:1">Save this for {hl('July 2027')}.</div>
 <div style="position:absolute;left:96px;top:520px;right:96px;{BODY};font-size:42px;line-height:1.32;color:#D9D3C5">That's when your first return with it is due. Spending over $1,000 on work costs this year? Keep every receipt.</div>
 {bubble("Follow for tax news, decoded within 48 hours.", 96, 1010, 520, bg=PAPER, fg=INK)}
 {docket(240, 720, 920, wave=True, dark=True)}""", 6, N, bg=INK, fg=PAPER),
]
if __name__ == "__main__":
    render_slides(slides, __file__)
