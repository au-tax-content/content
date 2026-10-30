"""RT-03 slides. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from retained_kit import *

cover_rows = "".join(
    f'<div style="display:flex;gap:28px;padding:18px 0;border-bottom:2px solid #2B3A52"><span style="font-family:{MONO};color:{BRASS};font-weight:600">{i:02d}</span><span>{t}</span></div>'
    for i, t in enumerate(["Nobody takes tax out for you", "Year one's bill arrives in one hit",
                           "Then the ATO asks for it in advance", "$75K turnover means GST", "Nobody pays your super"], 1))

def shock(n, head, body, note):
    bg = BONE if n % 2 else STONE
    return page(header(f"FIRST-YEAR ABN · {n:02d} OF 05", False)
                + f'<span style="font-family:{MONO};font-weight:600;font-size:180px;line-height:0.9;color:{BRASS}">{n:02d}</span>'
                + title(head, 104)
                + para(body, 40)
                + (f'<div style="border-left:6px solid {BRASS};padding:8px 0 8px 28px;font-family:{SANS};font-size:32px;line-height:1.4;font-weight:500;color:#2B3A52">{note}</div>' if note else "")
                + footer("General info only · Not personal advice", "→", False), bg, NAVY)

slides = [
    page(header("FIRST-YEAR ABN · No. 003", True)
         + title("Five tax surprises in your first year on an ABN.", 116, 32)
         + f'<div style="display:flex;flex-direction:column;font-family:{SANS};font-weight:500;font-size:36px">{cover_rows}</div>'
         + footer("General info only · Not personal advice", "SWIPE →", True), NAVY, BONE, 44),
    shock(1, "Nobody takes tax out for you.",
          "An employer withholds tax from every pay. Clients paying your invoices don't. Every dollar lands in your account <b>gross</b>.",
          "Feels like a pay rise. It isn't."),
    shock(2, "Year one's bill arrives in one hit.",
          "You lodge after 30 June and the <b>whole year's tax</b> is due at once. Nothing's been paid along the way, so it's one big number.",
          "This is where a set-aside account earns its keep."),
    shock(3, "Then the ATO asks for it in advance.",
          "Once your return shows <b>$4,000+</b> of business income and <b>$1,000+</b> of tax payable (plus one more test), the ATO can put you on quarterly <b>PAYG instalments</b>.",
          "Year two: last year's bill and this year's instalments, together."),
    shock(4, "$75K turnover means GST.",
          "Turnover, not profit. Once you reach, or expect to reach, <b>$75,000</b>, you must register for GST within <b>21 days</b>.",
          "Rideshare and taxi drivers register from the first fare."),
    shock(5, "Nobody pays your super.",
          "There's no 12% super guarantee for yourself. Contributions are up to you, and you may be able to claim them as a <b>deduction</b>.",
          "Retirement doesn't fund itself."),
    page(header("FREE", True)
         + title("Just got your ABN?", 124)
         + kit_box()
         + f"""<div style="margin-top:auto;display:flex;flex-direction:column;gap:16px"><span style="font-family:{SERIF};font-size:52px">Send this to the mate who just went out on their own.</span>
<span style="font-family:{MONO};font-size:22px;color:#C9C2B4">General info only · Not personal advice</span></div>""", NAVY, BONE),
]

if __name__ == "__main__":
    render(slides, __file__)
