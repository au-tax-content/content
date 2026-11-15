"""RT-28 Reel: Year 2 in business: PAYG instalments. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Year 2 in business comes with a [[surprise]] bill.", "PAYG INSTALMENTS", "brass", size=130), 3.0),
 (point(b, 1, "What [[triggers]] it",
        steps(b, ["$4,000+ instalment income", "$1,000+ tax on last assessment", "$500+ estimated tax"], start=0.7, gap=0.3),
        "Meet all three on your latest return and the ATO enters you into PAYG instalments automatically."), 4.8),
 (point(b, 2, "What it [[is]]",
        stamp_el(b, "TAX, IN ADVANCE", 0.9, size=60),
        "You pay this year's tax as you go, usually each quarter, instead of one lump after you lodge.", wave=True), 4.4),
 (point(b, 3, "Why it [[stings]]",
        steps(b, ["Last year's bill is due", "First instalments start", "Both within months"], start=0.7, gap=0.3),
        "The ATO tells you through myGov, online services or a letter: when to pay, how often and how much."), 4.8),
 (end(b, "Year 2: plan for [[two]] bills, not one.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
