"""RP-16 Reel: How salary sacrifice actually saves you money. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "[[Salary sacrifice]] saves more than most people realise. Here's the actual maths.", "SAVE THIS"), 3.0),
 (point(b, 1, "The [[gap]] is your saving",
        big(b, "15c", "PER DOLLAR · 2026–27", size=190),
        "30% marginal rate minus 15% fund tax = 15 cents per dollar you keep. The bigger the gap, the bigger the win."), 4.5),
 (point(b, 2, "The [[cap]]",
        big(b, "$32,500", "CONCESSIONAL · 2026–27", size=165),
        "This includes your employer's 12% super guarantee. So if you earn $80K, employer puts in ~$9,600 — you can sacrifice up to ~$22,900 more.", wave=True), 4.5),
 (point(b, 3, "The [[catch]]",
        stamp_el(b, "LOCKED AWAY", 0.9, size=55),
        "It's preserved until ~age 60. And if your income plus contributions top $250K, Division 293 adds 15% extra tax on some contributions."), 4.5),
 (end(b, "Tax the [[gap,]] not the whole dollar.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
