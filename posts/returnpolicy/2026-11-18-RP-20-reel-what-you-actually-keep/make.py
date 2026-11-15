"""RP-20 Reel: What you actually keep on $75K to $200K. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (ladder(b, "What you [[actually]] keep on your salary", "2026–27 · AFTER TAX + MEDICARE", [
     ("$75K", 60480, "about $1,163 a week"),
     ("$100K", 77480, "about $1,490 a week"),
     ("$125K", 94480, "about $1,817 a week"),
     ("$150K", 110430, "about $2,124 a week"),
     ("$200K", 140130, "about $2,695 a week"),
   ], "Resident rates + 2% Medicare levy. Before super. No HELP debt, offsets or surcharge."), 10.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
