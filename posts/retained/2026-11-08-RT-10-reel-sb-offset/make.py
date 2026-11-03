"""RT-10 Reel: the small business income tax offset (16%, up to $1,000). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "[[$1,000]] off your tax. Most never check it.", "SOLE TRADERS · SAVE THIS", size=136), 3.0),
 (point(b, 1, "[[16%]] off the tax", big(b, "16%", "ON BUSINESS INCOME", size=200), "Of the tax on your net small business income."), 4.4),
 (point(b, 2, "Capped at [[$1,000]]", big(b, "", "A YEAR, MAX", count_to=1000, pre="$", size=190), "Your business turnover has to be under $5 million."), 4.4),
 (point(b, 3, "No [[form]] to fill", steps(b, ["LODGE YOUR RETURN", "THE ATO WORKS IT OUT", "IT'S ON YOUR ASSESSMENT"]), "Partners and trust beneficiaries can get it on their share of small business income.", wave=True), 4.6),
 (end(b, "Check your [[assessment.]]", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
