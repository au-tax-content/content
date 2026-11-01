"""RP-02 Is it claimable? 01: office workers (2025-26 returns). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from returnpolicy_kit import *

N = 7
TAG = "IS IT CLAIMABLE? · 01"
YES = lambda: stamp("CLAIMABLE", GREEN, 4, 40)
NO = lambda: stamp("NOT CLAIMABLE", RED, -5, 40)
PART = lambda: stamp("PART · OVER TIME", INK, 3, 40)

def reveal(n, a, b, say=None, who=None):
    def block(num, name, verdict, why):
        return f"""<div style="border-top:4px dashed {RULE};padding-top:34px">
 <div style="{MONO5};font-size:30px;color:{MUTED}">{num:02d} / 06</div>
 <div style="{DISPLAY};font-size:84px;line-height:1.02;margin:10px 0 24px">{name}</div>
 {verdict()}
 <div style="{BODY};font-size:40px;line-height:1.32;margin-top:28px;max-width:880px">{why}</div></div>"""
    sb = bubble(say, 96, 1090, 520) if say else ""
    return slide(f"""<div style="position:absolute;left:96px;right:96px;top:170px;bottom:190px;display:flex;flex-direction:column;justify-content:space-evenly">
 {block(*a)}{block(*b)}</div>{sb}{docket(170, 840, 1040) if say else ''}""", n, N, swipe=True, tag=TAG)

slides = [
 slide(f"""<div style="position:absolute;left:96px;top:200px;right:96px;{DISPLAY};font-size:120px;line-height:.98">
 6 things office workers {hl('try')} to claim.</div>
 <div style="position:absolute;left:96px;top:600px;right:96px;{BODY};font-size:44px;color:#D9D3C5">Guess yes or no for each. Answers inside.</div>
 {receipt(''.join([item('GYM MEMBERSHIP', '?'), item('WORK LAPTOP', '?'), item('BLACK WORK PANTS', '?'),
                   item('+ 3 MORE', 'SWIPE →', 34, MUTED)]), 150, 760, 600)}
 {docket(220, 790, 940, wave=True, dark=True)}""", 1, N, bg=INK, fg=PAPER, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">Lock in your {hl('guesses')}.</div>
 {receipt(''.join([item('01 GYM MEMBERSHIP', 'Y / N'), item('02 LAPTOP, 60% WORK USE', 'Y / N'), item('03 PLAIN BLACK PANTS', 'Y / N'),
   item('04 UNION FEES', 'Y / N'), item('05 DRIVING HOME → OFFICE', 'Y / N'), item("06 LAST YEAR'S AGENT FEE", 'Y / N')]),
   96, 400, 888, head="RETURN POLICY", sub="OFFICE WORKERS · 2025–26 RETURNS")}
 {bubble("Most people get two wrong.", 96, 1100, 540)}{docket(130, 870, 1020)}""", 2, N, swipe=True, tag=TAG),

 reveal(3, (1, "Gym membership", NO, "Fitness is private. The rare exception: jobs where strenuous physical activity is an essential, regular part of the work."),
           (2, "Laptop, 60% work use", PART, "Over $300, so you claim the 60% work share of its decline in value over its effective life. Not all at once.")),
 reveal(4, (3, "Plain black work pants", NO, "Conventional clothing isn't claimable, even if you only ever wear it to work."),
           (4, "Union fees", YES, "Claimable. And from 2026–27 they sit outside the new $1,000 standard deduction.")),
 reveal(5, (5, "Driving home → office", NO, "Normal trips between home and work are private. Even long ones."),
           (6, "Last year's tax agent fee", YES, "Claimable in the year you paid it, if the agent is registered with the Tax Practitioners Board.")),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:100px;line-height:1">How did you {hl('score')}?</div>
 {receipt(''.join([item('GYM MEMBERSHIP', right_html=stamp('NO', RED, -5, 26)), item('LAPTOP (60% WORK)', right_html=stamp('PART', INK, 3, 26)),
   item('PLAIN BLACK PANTS', right_html=stamp('NO', RED, -3, 26)), item('UNION FEES', right_html=stamp('YES', GREEN, 4, 26)),
   item('HOME → OFFICE', right_html=stamp('NO', RED, -4, 26)), item('TAX AGENT FEE', right_html=stamp('YES', GREEN, 2, 26)),
   f'<div style="border-top:4px dashed {RULE}"></div>',
   f'<div style="display:flex;justify-content:space-between;{MONO};font-size:32px"><span>TOTAL</span><span>2 YES · 1 PART · 3 NO</span></div>']),
   96, 400, 888, head="RETURN POLICY", sub="IS IT CLAIMABLE? · 01 · ANSWERS")}""", 6, N, swipe=True, tag=TAG),

 slide(f"""<div style="position:absolute;left:96px;top:190px;right:96px;{DISPLAY};font-size:112px;line-height:1">Want the list for {hl('your')} job?</div>
 <div style="position:absolute;left:96px;right:96px;top:520px;background:{PAPER};color:{INK};padding:48px 56px">
  <div style="{MONO5};font-size:28px;color:{MUTED}">COMMENT THE WORD</div>
  <div style="{MONO};font-size:150px;letter-spacing:.06em;line-height:1;margin:12px 0">CLAIM</div>
  <div style="{BODY};font-size:40px;line-height:1.3">and you'll be first to get <b>The Claim Sheet</b> (what 20 common jobs can claim) when it lands in December.</div></div>
 {bubble("Tag the office mate who claims their gym.", 96, 1060, 560, bg=PAPER, fg=INK)}
 {docket(170, 830, 1010, wave=True, dark=True)}""", 7, N, bg=GREEN, fg=PAPER),
]
if __name__ == "__main__":
    render_slides(slides, __file__)
