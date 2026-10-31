"""RT-03 bold carousel: 5 tax surprises in your first year on an ABN. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from bold import slide, hl, bubble, penny, render_slides, SERIF, MONO, GREEN, BRASS, RED, BONE, NAVY

N = 7
def shock(n, head, big, big_color, body, say=None):
    b = bubble(say, 80, 1010, 520) if say else ""
    return slide(f"""<div style="position:absolute;left:80px;top:170px;right:80px">
 <div style="{MONO};font-size:44px;color:{BRASS}">SURPRISE {n} OF 5</div>
 <div style="{SERIF};font-size:112px;line-height:1.04;margin-top:20px">{head}</div>
 <div style="{MONO};font-size:150px;line-height:1.05;color:{big_color};margin-top:40px">{big}</div>
 <div style="font-size:42px;line-height:1.38;margin-top:30px;max-width:700px">{body}</div></div>
 {b}{penny(200, 820, 960)}""", n + 1, N, swipe=True)

slides = [
 slide(f"""<div style="position:absolute;left:80px;top:190px;right:80px;{SERIF};font-size:124px;line-height:1.04">
 {hl('5 tax surprises')} in your first year on an ABN.</div>
 {bubble("Number 3 catches almost everyone.", 80, 900, 500)}
 {penny(300, 680, 860, wave=True)}""", 1, N, swipe=True),
 shock(1, "Nobody takes tax out for you.", "$0", RED, "withheld from ABN payments. Every dollar lands <b>gross</b>. Feels like a pay rise. It isn't."),
 shock(2, "Year one's bill lands in one hit.", "1 BILL", RED, "The whole year's tax is due after you lodge. Nothing was paid along the way."),
 shock(3, "Then the ATO wants next year's, early.", "$4K / $1K", BRASS, "Business income of $4,000+ and tax payable of $1,000+ (plus one more test) and you can be put on <b>quarterly PAYG instalments</b>. Two bills in one year."),
 shock(4, "$75K turnover means GST.", "$75,000", GREEN, "Turnover, not profit. Reach it (or expect to) and you have <b>21 days</b> to register. Rideshare: from the first fare."),
 shock(5, "Nobody pays your super.", "12% → 0%", RED, "No super guarantee for yourself. It's up to you, and contributions may be <b>tax-deductible</b>."),
 slide(f"""<div style="position:absolute;left:80px;top:190px;right:80px">
 <div style="{SERIF};font-size:130px;line-height:1.02">Just got your ABN?</div>
 <div style="margin-top:50px;background:{BONE};color:{NAVY};border-radius:24px;padding:44px 50px">
 <div style="{MONO};font-size:30px;color:#4A5568">COMMENT THE WORD</div>
 <div style="{MONO};font-size:150px;line-height:1;margin:10px 0">ABN</div>
 <div style="font-size:40px;line-height:1.35">and you'll be first to get the <b>New ABN Starter Kit</b> when it lands in December.</div></div></div>
 {bubble("Send this to the mate who just went out on their own.", 80, 1010, 560)}
 {penny(240, 760, 1000, wave=True)}""", 7, N),
]
if __name__ == "__main__":
    render_slides(slides, __file__)
