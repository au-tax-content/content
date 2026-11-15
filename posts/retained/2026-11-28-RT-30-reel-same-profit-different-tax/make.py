"""RT-30 Reel: Same $150K profit, $9,250 less tax. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Same [[$150K]] profit. [[$9,250]] less tax.", "HERE'S THE DIFFERENCE", "navy"), 3.0),
 (point(b, 1, "Owner A does [[nothing]]",
        big(b, "", "TAX + MEDICARE", count_to=38570, pre="$", size=170),
        "Sole trader, $150,000 profit, 2026–27 rates, after the $1,000 small business offset."), 4.6),
 (point(b, 2, "Owner B makes [[2]] moves",
        steps(b, ["$20,000 into their own super", "$15,000 machine, written off"], start=0.7, gap=0.35),
        "Both are deductions, so taxable income drops to $115,000.", wave=True), 4.6),
 (point(b, 3, "Owner B's [[bill]]",
        big(b, "", "INCL. SUPER TAX", count_to=29320, pre="$", size=170),
        "$26,320 personal tax plus $3,000 contributions tax in the fund. $9,250 less than Owner A."), 4.8),
 (end(b, "The catch: B spent [[$35,000]] to do it.", "ONLY IF YOU NEEDED BOTH"), 3.4),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
