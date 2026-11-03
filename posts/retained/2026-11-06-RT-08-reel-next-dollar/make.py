"""RT-08 Reel: what your next dollar of profit is taxed at (2026-27 rates). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "Your next [[$1]] of profit is taxed at…", "2026–27 RATES · SAVE THIS", size=140), 3.0),
 (point(b, 1, "Up to [[$45K]]", big(b, "15%", "PLUS MEDICARE", size=200), "Taxable income $18,201 to $45,000. The first $18,200 is tax-free."), 4.4),
 (point(b, 2, "Up to [[$135K]]", big(b, "30%", "+ 2% MEDICARE", size=200), "$45,001 to $135,000. Where a lot of sole traders sit."), 4.4),
 (point(b, 3, "Over [[$190K]]", big(b, "45%", "+ 2% MEDICARE", size=200) + stamp_el(b, "37% FROM $135K"), "The higher your rate, the more each legal deduction is worth.", wave=True), 4.6),
 (end(b, "Know your [[rate.]] Then plan.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
