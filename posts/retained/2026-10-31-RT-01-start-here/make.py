"""RT-01 slides. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from retained_kit import *

slides = [
    page(header("START HERE", True)
         + title("Keep more of what your business makes.", 128, 36)
         + para("Tax and money for business owners, from your first ABN to running a company. Explained plainly, checked against the ATO.", 38, "#E4DED2")
         + footer("General info only · Not personal advice", "SWIPE →", True), NAVY, BONE),
    page(header("WHO IT'S FOR", False)
         + title("Who this account is for.", 100)
         + rows([("You just got an ABN", "and nobody told you what happens at tax time"),
                 ("Your side hustle is getting serious", "and the money is starting to matter"),
                 ("You've been a sole trader a while", "and want to stop overpaying or under-saving"),
                 ("You run a company, trust or partnership", "and want to understand the moving parts")], False, 36)
         + footer("Retained · Tax Strategy AU", "→", False), BONE, NAVY),
    page(header("THE SERIES", False)
         + title("What you'll get each week.", 100)
         + rows([("First-year ABN", "what nobody tells you in year one"),
                 ("Set-aside", "how much to put away, worked out in dollars"),
                 ("Write it off?", "real purchases, real verdicts"),
                 ("GST or not?", "the $75K line, BAS and due dates"),
                 ("Structure", "sole trader, company or trust, and when to switch")], False, 34)
         + footer("Same labels every time, so you can binge the back catalogue", "→", False), STONE, NAVY),
    page(header("FREE", True)
         + title("Just got your ABN?", 124)
         + kit_box()
         + footer("General info only · Not personal advice", "→", True), NAVY, BONE),
    page(header("THE RULES", False)
         + title("How this account works.", 100)
         + rows([("General info, not personal advice", "your situation will differ from the example"),
                 ("Every figure is checked", "against ato.gov.au the week it's posted, with its income year"),
                 ("No selling", "this account teaches; it doesn't do your tax"),
                 ("Big decisions?", "talk to a registered tax agent first")], False, 36)
         + f'<span style="margin-top:auto;font-family:{SERIF};font-size:56px">Follow for the things nobody tells you.</span>', BONE, NAVY),
]

if __name__ == "__main__":
    render(slides, __file__)
