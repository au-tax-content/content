"""RT-02 slides. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from retained_kit import *

slides = [
    page(header("SET-ASIDE · No. 002", False)
         + f"""<div style="display:flex;flex-direction:column;gap:28px"><h1 style="margin:0;font-family:{SERIF};font-weight:400;font-size:96px;line-height:1.14">$60K profit. What do you <span style="background:linear-gradient(transparent 26%,{HL} 26%);padding:0 10px">actually</span> owe?</h1><span style="width:160px;height:6px;background:{BRASS}"></span></div>"""
         + f"""<div style="display:flex;flex-direction:column;font-family:{MONO};font-size:30px;font-weight:500">
{ledger_row("Profit (no other income)", "$60,000")}
{ledger_row("Income tax, 2026–27 rates", "$8,520")}
{ledger_row("Medicare levy (2%)", "$1,200")}
{ledger_row("Low income tax offset", "−$100")}
{ledger_row("Small business offset (16%, max $1k)", "−$1,000")}
<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:24px;border:3px solid {NAVY};padding:22px 28px;font-weight:600;font-size:40px"><span>TOTAL</span><span>≈ $8,620 · about 14%</span></div></div>"""
         + para("So why do accountants say put away <b>25%</b>? Swipe.", 36)
         + f'<div style="margin-top:auto;font-family:{MONO};font-size:20px;line-height:1.4;color:#4A5568">Resident, no HELP debt, all income from the business, turnover under $5M. General info only · Not personal advice</div>',
         BONE, NAVY, 40),
    page(header("SET-ASIDE · WHY 25%", False)
         + title("Three reasons 14% isn't enough.", 100)
         + rows([("Profit grows", "every dollar over $45,000 is taxed at 30c, plus 2c Medicare. Next year's bill is usually bigger."),
                 ("Year two, the ATO wants tax in advance", "PAYG instalments can start on top of last year's bill. Two bills, one year."),
                 ("GST was never yours", "if you're registered, 1/11 of every GST-inclusive invoice goes back at BAS time.")], False, 36)
         + footer("General info only · Not personal advice", "→", False), STONE, NAVY),
    page(header("THE HABIT", True)
         + title("Move it the day it lands.", 120)
         + f"""<div style="background:{BONE};color:{NAVY};padding:48px 56px;display:flex;flex-direction:column;gap:20px">
<span style="font-family:{MONO};font-size:28px;font-weight:500;color:#4A5568">EVERY PAYMENT IN</span>
<span style="font-family:{MONO};font-size:150px;font-weight:600;line-height:1">25%</span>
<span style="font-family:{SANS};font-size:36px;font-weight:500;line-height:1.38">goes to a separate tax account. Don't touch it until the ATO asks.</span></div>"""
         + f"""<div style="margin-top:auto;display:flex;flex-direction:column;gap:16px"><span style="font-family:{SERIF};font-size:56px">Save this for your next invoice.</span>
<span style="font-family:{MONO};font-size:22px;color:#C9C2B4">General info only · Not personal advice</span></div>""", NAVY, BONE),
]

if __name__ == "__main__":
    render(slides, __file__)
