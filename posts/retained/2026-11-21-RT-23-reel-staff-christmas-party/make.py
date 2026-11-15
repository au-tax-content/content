"""RT-23 Reel: Your staff Christmas party probably isn't deductible. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Your staff Christmas party probably [[isn't]] deductible.", "HERE'S WHY THAT'S OK", "green", size=118), 3.2),
 (point(b, 1, "The [[$300]] line",
        big(b, "$300", "PER PERSON", size=200),
        "Under $300 a head and occasional, a party or gift can be an exempt minor benefit: no fringe benefits tax."), 4.6),
 (point(b, 2, "The [[trade-off]]",
        steps(b, ["No FBT on the party?", "No income tax deduction", "No GST credits"], start=0.7, gap=0.3),
        "For entertainment like a party, the ATO's rule: if it isn't subject to FBT, you can't deduct it or claim the GST.", wave=True), 4.8),
 (point(b, 3, "On-site, work day, staff only",
        stamp_el(b, "NO FBT ON FOOD + DRINK", 0.9, size=46),
        "A party on your premises on a working day for current employees: no FBT on the food and drink. Same trade-off.", title_size=100), 4.8),
 (end(b, "Under $300: no tax, no claim. [[Simple.]]", "SEND TO THE BOSS"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
