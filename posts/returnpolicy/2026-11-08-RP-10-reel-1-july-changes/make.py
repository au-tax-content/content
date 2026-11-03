"""RP-10 Reel: 3 tax changes since 1 July 2026. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "[[3]] tax changes since 1 July.", "2026–27 · SAVE THIS"), 3.0),
 (point(b, 1, "[[16%]] is now 15%", big(b, "15%", "$18,201–$45,000", size=200), "From 2026–27. Worth up to $268 a year."), 4.4),
 (point(b, 2, "[[$1,000]] no receipts", big(b, "", "STANDARD DEDUCTION", count_to=1000, pre="$", size=180), "Automatic for wage earners from 2026–27."), 4.4),
 (point(b, 3, "Laundry: [[$1]] a load", big(b, "$1", "WORK CLOTHES", size=200) + stamp_el(b, "50c MIXED LOADS"), "And the old $300 no-receipts rule is gone.", wave=True), 4.6),
 (end(b, "New year. New [[rules.]]", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
