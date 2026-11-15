"""RP-26 Reel: HELP debt: what comes out of your pay in 2026–27. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "HELP debt? Here's what comes out in [[2026–27.]]", "STUDY LOANS", "ink", size=132), 3.0),
 (point(b, 1, "The first [[$69,528]] is repayment-free",
        big(b, "", "THRESHOLD", count_to=69528, pre="$", size=170),
        "Repayment income under that: no compulsory repayment this year.", title_size=100), 4.4),
 (point(b, 2, "Above it: [[15c]] per extra $1",
        steps(b, ["$80,000 → about $1,571", "$100,000 → about $4,571", "$120,000 → about $7,571"], start=0.7, gap=0.3),
        "Worked out only on the income above the threshold, not your whole income (up to $129,717).", wave=True, title_size=104), 4.8),
 (point(b, 3, "The [[catch]]",
        stamp_el(b, "APPLIED AT TAX TIME", 0.9, size=54),
        "What your employer withholds for HELP isn't taken off the loan each payday. The ATO applies it in one lump after you lodge your return."), 4.8),
 (end(b, "Told payroll about your [[HELP]] debt?", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
