"""RT-02 bold carousel: $60K profit, what do you actually owe? Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from bold import slide, hl, bubble, penny, render_slides, SERIF, MONO, GREEN, BRASS, RED, BONE, NAVY

def row(a, b, c=BONE):
    return f'<div style="display:flex;justify-content:space-between;padding:20px 0;border-bottom:2px solid #2B3A52;{MONO};font-size:40px"><span style="color:#D8D2C6">{a}</span><span style="color:{c}">{b}</span></div>'

N = 4
slides = [
 slide(f"""<div style="position:absolute;left:80px;top:190px;right:80px;{SERIF};font-size:150px;line-height:1.02">
 <span style="color:{GREEN};{MONO};font-size:170px">$60K</span> profit.<br>What do you {hl('actually')} owe?</div>
 {bubble("Guess a number before you swipe.", 80, 900, 470)}
 {penny(300, 680, 860, wave=True)}""", 1, N, swipe=True),
 slide(f"""<div style="position:absolute;left:80px;top:170px;right:80px">
 <div style="{SERIF};font-size:92px;line-height:1.05;margin-bottom:30px">The real bill, 2026–27</div>
 {row("Profit", "$60,000")}{row("Income tax", "$8,520")}{row("Medicare levy 2%", "$1,200")}
 {row("Low income offset", "−$100", GREEN)}{row("Small business offset (16%)", "−$1,000", GREEN)}
 <div style="display:flex;align-items:baseline;justify-content:space-between;margin-top:40px">
 <span style="{MONO};font-size:150px;color:{GREEN}">$8,620</span><span style="{MONO};font-size:54px;color:{BRASS}">≈ 14%</span></div>
 <div style="font-size:30px;color:#9A9384;margin-top:10px">Resident, no HELP debt, all income from the business, turnover under $5M.</div></div>""", 2, N, swipe=True),
 slide(f"""<div style="position:absolute;left:80px;top:180px;right:80px">
 <div style="{SERIF};font-size:118px;line-height:1.04">So why do accountants say {hl('25%')}?</div>
 <div style="margin-top:60px;display:flex;flex-direction:column;gap:38px;font-size:42px;line-height:1.3">
 <div><span style="{MONO};color:{BRASS}">01 </span><b>Profit grows.</b> Every dollar over $45K is taxed at 30c, plus 2c Medicare.</div>
 <div><span style="{MONO};color:{BRASS}">02 </span><b>Year two hits twice.</b> Last year's bill plus PAYG instalments in advance.</div>
 <div><span style="{MONO};color:{BRASS}">03 </span><b>GST isn't yours.</b> If you're registered, 1/11 of every invoice goes back.</div></div></div>
 {penny(200, 820, 960)}""", 3, N, swipe=True),
 slide(f"""<div style="position:absolute;left:80px;top:200px;right:80px">
 <div style="{SERIF};font-size:120px;line-height:1.04">The habit that saves year two:</div>
 <div style="margin-top:50px;{MONO};font-size:300px;line-height:1;color:{GREEN}">25%</div>
 <div style="font-size:46px;line-height:1.35;margin-top:20px">of every payment → a separate tax account, <b>the day it lands.</b></div></div>
 {bubble("Save this for your next invoice.", 80, 1020, 500)}
 {penny(260, 720, 960, wave=True)}""", 4, N),
]
if __name__ == "__main__":
    render_slides(slides, __file__)
