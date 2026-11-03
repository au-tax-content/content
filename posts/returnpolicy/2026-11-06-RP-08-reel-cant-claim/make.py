"""RP-08 Reel: 3 things you can't claim at work (2025-26 returns). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "3 work costs you [[can't]] claim.", "MYTH BUST · 2025–26 RETURNS"), 3.0),
 (point(b, 1, "Gym [[membership]]", stamp_el(b, "NOT CLAIMABLE", 0.9, size=64), "Unless strenuous physical activity is an essential, regular part of your job."), 4.2),
 (point(b, 2, "Plain black [[pants]]", stamp_el(b, "NOT CLAIMABLE", 0.9, size=64), "Conventional clothing isn't deductible, even if you only wear it to work."), 4.2),
 (point(b, 3, "Driving to the [[office]]", stamp_el(b, "NOT CLAIMABLE", 0.9, size=64), "Normal trips between home and work are private. Even long ones.", wave=True), 4.2),
 (end(b, "Claim what's [[real.]] Keep receipts.", "COMMENT CLAIM", size=128), 3.4),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
