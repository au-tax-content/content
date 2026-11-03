"""RT-09 Reel: the $75K GST line. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "Hit [[$75K?]] The clock starts.", "GST · SAVE THIS"), 3.0),
 (point(b, 1, "[[$75,000]] turnover", big(b, "", "GST TURNOVER", count_to=75000, pre="$", size=170), "Turnover, not profit. That's the line for registering for GST."), 4.4),
 (point(b, 2, "[[21]] days", big(b, "", "TO REGISTER", count_to=21, size=200), "Counted from when your GST turnover goes over the threshold."), 4.4),
 (point(b, 3, "Rideshare? [[Day]] one.", stamp_el(b, "NO THRESHOLD", 0.9, size=64), "Taxi and ride-sourcing drivers must register whatever their turnover.", wave=True), 4.4),
 (end(b, "Watch your [[turnover]] monthly.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
