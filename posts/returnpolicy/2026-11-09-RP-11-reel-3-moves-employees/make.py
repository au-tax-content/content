"""RP-11 Reel: 3 legal moves that lower your tax (employees). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "[[3]] moves that actually lower your tax", "SAVE THIS"), 3.0),
 (point(b, 1, "Salary sacrifice to [[super]]",
        big(b, "15%", "TAX ON CONTRIBUTIONS", size=190),
        "Money goes in before PAYG. Taxed at 15%, not your marginal rate. The gap is your saving."), 4.5),
 (point(b, 2, "Work from [[home]]",
        big(b, "70c", "PER HOUR · 2026–27", size=200),
        "Fixed rate method — no receipts for individual expenses. Log your hours. Claim the deduction.", wave=True), 4.5),
 (point(b, 3, "Tools under [[$300]]",
        stamp_el(b, "IMMEDIATE CLAIM", 0.9, size=55),
        "Work-related items under $300? Claim in full this year. No depreciation schedule needed."), 4.5),
 (end(b, "Pick [[one.]] Pick three.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
