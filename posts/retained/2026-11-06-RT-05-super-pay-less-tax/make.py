"""RT-05 Keep more: how business owners use super to pay less tax (2026-27). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from bold import slide, hl, bubble, penny, render_slides, SERIF, MONO, GREEN, BRASS, RED, BONE, NAVY

N = 7
LBL = f"{MONO};font-size:40px;color:{BRASS}"
BODY = "font-size:42px;line-height:1.38"
def row(k, v, c=BONE, s=40):
    return f'<div style="display:flex;justify-content:space-between;{MONO};font-size:{s}px;padding:16px 0;border-bottom:3px solid rgba(201,161,95,.35)"><span>{k}</span><span style="color:{c}">{v}</span></div>'

slides = [
 slide(f"""<div style="position:absolute;left:80px;top:190px;right:80px;{SERIF};font-size:120px;line-height:1.16">
 How business owners use {hl('super')} to pay less tax.</div>
 {bubble("Nobody pays your super when you're the boss. That's the opening.", 80, 880, 540)}
 {penny(300, 680, 860, wave=True)}""", 1, N, swipe=True),

 slide(f"""<div style="position:absolute;left:80px;top:170px;right:80px">
 <div style="{LBL}">THE MOVE</div>
 <div style="{SERIF};font-size:104px;line-height:1.04;margin-top:20px">Contribute to super. Claim it as a deduction.</div>
 <div style="display:flex;align-items:center;gap:40px;margin-top:60px">
  <div><div style="{MONO};font-size:30px;color:#9A9384">TAX AS PROFIT</div><div style="{MONO};font-size:150px;line-height:1;color:{RED}">32%</div><div style="{MONO};font-size:26px;color:#9A9384">30% + 2% MEDICARE</div></div>
  <div style="{MONO};font-size:90px;color:{BRASS}">→</div>
  <div><div style="{MONO};font-size:30px;color:#9A9384">TAX IN SUPER</div><div style="{MONO};font-size:150px;line-height:1;color:{GREEN}">15%</div><div style="{MONO};font-size:26px;color:#9A9384">CONTRIBUTIONS TAX</div></div></div></div>
 {bubble("Sole traders pay their own super, so this is the main lever.", 80, 1010, 560)}
 {penny(200, 820, 1000)}""", 2, N, swipe=True),

 slide(f"""<div style="position:absolute;left:80px;top:170px;right:80px">
 <div style="{LBL}">$120K PROFIT · $20K INTO SUPER</div>
 <div style="{SERIF};font-size:96px;line-height:1.04;margin-top:16px">Here's what changes the bill.</div>
 <div style="margin-top:40px;background:rgba(244,240,232,.06);border-radius:24px;padding:20px 40px">
  {row('TAXABLE INCOME', '$120K → $100K')}
  {row('TAX + MEDICARE', '$28,920 → $22,520')}
  {row('TAX SAVED', '$6,400', GREEN)}
  {row('FUND TAX (15%)', '−$3,000', RED)}
  <div style="display:flex;justify-content:space-between;align-items:baseline;{MONO};padding-top:20px"><span style="font-size:40px">KEPT</span><span style="font-size:110px;color:{GREEN}">$3,400</span></div></div>
 <div style="font-size:28px;color:#9A9384;margin-top:20px">Sole trader, 2026–27 resident rates, no other income or offsets.</div></div>""", 3, N, swipe=True),

 slide(f"""<div style="position:absolute;left:80px;top:170px;right:80px">
 <div style="{LBL}">THE LIMIT · 2026–27</div>
 <div style="{MONO};font-size:170px;line-height:1.05;color:{GREEN};margin-top:20px">$32,500</div>
 <div style="{BODY};margin-top:10px;max-width:880px">Concessional cap for the year, counting any super an employer pays for you.</div>
 <div style="{LBL};margin-top:70px">BIG PROFIT YEAR?</div>
 <div style="{SERIF};font-size:88px;line-height:1.05;margin-top:16px">{hl('Catch up')} on 5 years.</div>
 <div style="{BODY};margin-top:24px;max-width:880px">Unused cap from up to 5 past years carries forward if your super balance was under <b>$500,000</b> last 30 June.</div></div>""", 4, N, swipe=True),

 slide(f"""<div style="position:absolute;left:80px;top:170px;right:80px">
 <div style="{LBL}">THE PAPERWORK</div>
 <div style="{SERIF};font-size:100px;line-height:1.04;margin-top:20px">Miss this step and the deduction {hl('fails')}.</div>
 <div style="margin-top:50px;background:{BONE};color:{NAVY};border-radius:24px;padding:40px 46px">
  <div style="{MONO};font-size:32px;color:#4A5568">1 · SEND YOUR FUND A</div>
  <div style="font-size:46px;font-weight:700;margin:6px 0 24px">Notice of intent to claim</div>
  <div style="{MONO};font-size:32px;color:#4A5568">2 · GET THEIR</div>
  <div style="font-size:46px;font-weight:700;margin-top:6px">Written acknowledgement</div>
  <div style="font-size:34px;line-height:1.35;margin-top:24px">Both before you lodge your return (and no later than the end of the next income year).</div></div></div>
 {penny(190, 840, 1030)}""", 5, N, swipe=True),

 slide(f"""<div style="position:absolute;left:80px;top:170px;right:80px">
 <div style="{LBL}">THE CATCH</div>
 <div style="{SERIF};font-size:104px;line-height:1.04;margin-top:20px">Who it suits.</div>
 <div style="margin-top:40px">
  {row('LOCKED AWAY', 'UNTIL RETIREMENT', BRASS, 36)}
  {row('CASH LEAVES THE BUSINESS', 'NOW', BRASS, 36)}
  {row('INCOME OVER $250K', '+15% (DIV 293)', RED, 36)}
  {row('AGED 67–74', 'WORK TEST', BRASS, 36)}</div>
 <div style="{BODY};margin-top:40px;max-width:880px">Best fit: a good year, cash you won't need for a while, and room under the cap.</div></div>
 {bubble("Big contribution? Run it past a registered adviser first.", 80, 1060, 560)}
 {penny(180, 840, 1040)}""", 6, N, swipe=True),

 slide(f"""<div style="position:absolute;left:80px;top:190px;right:80px">
 <div style="{SERIF};font-size:130px;line-height:1.16">Save this for {hl('June')}.</div>
 <div style="font-size:44px;line-height:1.38;margin-top:50px;max-width:860px;color:#D8D2C6">The best time to plan a contribution is before 30 June, not after you've seen the tax bill.</div></div>
 {bubble("Follow for the moves good accountants make.", 80, 1010, 540)}
 {penny(260, 740, 950, wave=True)}""", 7, N),
]
if __name__ == "__main__":
    render_slides(slides, __file__)
