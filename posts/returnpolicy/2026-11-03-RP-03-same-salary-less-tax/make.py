"""RP-03 Pay less, legally: same $90K salary, different tax (salary sacrifice, 2026-27). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from returnpolicy_kit import *

N = 7
TAG = "PAY LESS, LEGALLY"
def big(t, c=GREEN, s=150): return f'<span style="{MONO};font-size:{s}px;line-height:1;color:{c}">{t}</span>'

def person(name, sac, taxable, tax, x, win=False):
    rows = ''.join([item('SALARY', '$90,000', 30), item('SACRIFICED', sac, 30), item('TAXABLE', taxable, 30),
                    f'<div style="border-top:4px dashed {RULE}"></div>',
                    f'<div style="{MONO5};font-size:24px;color:{MUTED}">INCOME TAX + MEDICARE</div>',
                    f'<div style="{MONO};font-size:64px;color:{GREEN if win else INK}">{tax}</div>'])
    return receipt(rows, x, 470, 420, head=name, sub="2026–27 · RESIDENT")

slides = [
 slide(f"""<div style="position:absolute;left:96px;top:200px;right:96px;{DISPLAY};font-size:116px;line-height:.98">
 Same $90K salary. {hl('$3,200')} less income tax.</div>
 <div style="position:absolute;left:96px;top:620px;right:300px;{BODY};font-size:44px;line-height:1.3;color:#D9D3C5">Same job, same pay. One move most people never ask payroll about.</div>
 {bubble("No tricks. It's built into the super rules.", 96, 1010, 520, bg=PAPER, fg=INK)}
 {docket(250, 700, 900, wave=True, dark=True)}""", 1, N, swipe=True, bg=INK, fg=PAPER, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:84px;line-height:1">Meet {hl('Sam')} and {hl('Alex')}.</div>
 <div style="position:absolute;left:96px;top:320px;right:96px;{BODY};font-size:38px;color:{MUTED}">Alex salary-sacrifices $10,000 into super.</div>
 {person('SAM', '$0', '$90,000', '$19,320', 96)}{person('ALEX', '$10,000', '$80,000', '$16,120', 564, True)}
 <div style="position:absolute;left:96px;top:1130px;right:96px;{MONO5};font-size:24px;color:{MUTED}">2026–27 resident rates + 2% Medicare levy. No other income, deductions or offsets.</div>""", 2, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">How it {hl('works')}.</div>
 <div style="position:absolute;left:96px;top:380px;right:96px;{BODY};font-size:42px;line-height:1.32">Part of your <b>before-tax</b> pay goes straight to super, so it never hits your taxable income.</div>
 <div style="position:absolute;left:96px;right:96px;top:620px;display:flex;align-items:center;gap:40px">
  <div><div style="{MONO5};font-size:28px;color:{MUTED}">TAX AS SALARY</div>{big('32%', RED)}<div style="{MONO5};font-size:26px;color:{MUTED}">30% + 2% MEDICARE</div></div>
  <div style="{MONO};font-size:90px">→</div>
  <div><div style="{MONO5};font-size:28px;color:{MUTED}">TAX IN SUPER</div>{big('15%')}<div style="{MONO5};font-size:26px;color:{MUTED}">CONTRIBUTIONS TAX</div></div></div>
 {bubble("Your employer still has to pay your full 12% super on top.", 96, 1010, 600)}
 {docket(170, 830, 990)}""", 3, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">Where Alex's $10K {hl('goes')}.</div>
 {receipt(''.join([item('SACRIFICED', '$10,000'), item('FUND TAX (15%)', '−$1,500'), item('LANDS IN SUPER', '$8,500'),
   f'<div style="border-top:4px dashed {RULE}"></div>',
   item('INCOME TAX SAVED', '$3,200'), item('TAKE-HOME DROPS BY', '$6,800'),
   f'<div style="border-top:4px dashed {RULE}"></div>',
   f'<div style="display:flex;justify-content:space-between;align-items:baseline;{MONO};font-size:34px"><span>AHEAD OVERALL</span><span style="font-size:72px;color:{GREEN}">$1,700</span></div>']),
   96, 420, 888, head="ALEX · 2026–27", sub="SALARY SACRIFICE $10,000")}""", 4, N, swipe=True, bg=PAPER2, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">The {hl('limits')}.</div>
 <div style="position:absolute;left:96px;right:96px;top:380px;display:flex;flex-direction:column;gap:56px">
  <div><div style="{MONO5};font-size:30px;color:{MUTED}">CONCESSIONAL CAP 2026–27</div>{big('$32,500')}
   <div style="{BODY};font-size:38px;line-height:1.32;margin-top:14px">Includes your employer's 12%. On $90K that's $10,800, leaving about $21,700 of room.</div></div>
  <div><div style="{MONO5};font-size:30px;color:{MUTED}">CARRY-FORWARD</div>{big('5 YEARS', INK, 110)}
   <div style="{BODY};font-size:38px;line-height:1.32;margin-top:14px">Unused cap from up to 5 past years, if your super balance was under $500,000 last 30 June.</div></div></div>""", 5, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">The {hl('catch')}.</div>
 {receipt(''.join([
   f'<div style="{BODY};font-size:38px;line-height:1.3"><b>Locked away.</b> Super is generally untouchable until retirement.</div>',
   f'<div style="border-top:4px dashed {RULE}"></div>',
   f'<div style="{BODY};font-size:38px;line-height:1.3"><b>Lower incomes gain less.</b> At the 15% rate, the gap to 15% in super is tiny.</div>',
   f'<div style="border-top:4px dashed {RULE}"></div>',
   f'<div style="{BODY};font-size:38px;line-height:1.3"><b>Over $250K?</b> Division 293 adds another 15% on contributions.</div>',
   f'<div style="border-top:4px dashed {RULE}"></div>',
   f'<div style="{MONO};font-size:30px;color:{GREEN}">SUITS: STEADY INCOME + CASH TO SPARE</div>']), 96, 380, 888)}""", 6, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:200px;right:96px;{DISPLAY};font-size:120px;line-height:1">Save this for your next {hl('pay chat')}.</div>
 <div style="position:absolute;left:96px;top:620px;right:96px;{BODY};font-size:42px;line-height:1.32;color:#D9D3C5">Ask payroll if they offer salary sacrifice. No arrangement? Personal contributions you claim as a deduction work in a similar way.</div>
 {bubble("Follow for one legal money move a week.", 96, 1010, 520, bg=PAPER, fg=INK)}
 {docket(240, 720, 920, wave=True, dark=True)}""", 7, N, bg=INK, fg=PAPER),
]
if __name__ == "__main__":
    render_slides(slides, __file__)
