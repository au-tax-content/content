"""RP-07 Reel: the $1,000 standard deduction (2026-27). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "[[$1,000]] off. No receipts.", "NEW FOR 2026–27 · SAVE THIS"), 3.0),
 (point(b, 1, "Starts [[this]] year", steps(b, ["2026–27 INCOME YEAR", "AUTOMATIC", "NOT IN 2025–26 RETURNS"]), "For residents earning wages or other labour income."), 4.6),
 (point(b, 2, "Costs under [[$1,000?]]", big(b, "$1,000", "EITHER WAY", size=180), "Any work costs you claim cut the $1,000 dollar for dollar."), 4.4),
 (point(b, 3, "Spend [[more?]]", big(b, "ITEMISE", "", size=150) + stamp_el(b, "KEEP RECEIPTS"), "Claim it all with records. Union and tax agent fees sit on top either way.", wave=True), 4.6),
 (end(b, "About [[$320]] back on the 30% rate.", "SAVE THIS FOR JULY 2027", size=120), 3.4),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
