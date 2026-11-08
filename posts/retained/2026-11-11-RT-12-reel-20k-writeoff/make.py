"""RT-12 Reel: $20K instant asset write-off is now permanent. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "The [[$20K]] write-off just went permanent.", "SAVE THIS"), 3.0),
 (point(b, 1, "What [[it]] is",
        big(b, "<$20K", "PER ASSET", size=170),
        "Buy a business asset, install it this year, claim it in full — not over years."), 4.5),
 (point(b, 2, "Who [[qualifies]]",
        steps(b, ["Turnover < $10M", "Asset used this year", "New or second-hand"]),
        "Permanent from 1 July 2026. Covers equipment, tools, tech, fit-out items."), 4.5),
 (point(b, 3, "The [[catch]]",
        stamp_el(b, "BUSINESS-USE ONLY", 0.9, size=52),
        "Claim only the business-use portion. Personal use? Split it. Upgrade under $20K? Also qualifies.", wave=True), 4.5),
 (end(b, "Review your [[assets]] before 30 June.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
