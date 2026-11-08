"""RP-12 Reel: deductions most employees don't claim. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "These are [[legal.]] Most employees just don't claim them.", "SAVE THIS"), 3.0),
 (point(b, 1, "Professional [[memberships]]",
        stamp_el(b, "FULLY DEDUCTIBLE", 0.9, size=50),
        "Union fees, professional body subscriptions, industry association memberships — all deductible if work-related."), 4.5),
 (point(b, 2, "Self-[[education]]",
        big(b, "100%", "DEDUCTIBLE", size=200),
        "Courses, workshops, seminars — deductible if they relate to your CURRENT job. Not to get a new one.", wave=True), 4.5),
 (point(b, 3, "Tools under [[$300]]",
        stamp_el(b, "IMMEDIATE CLAIM", 0.9, size=55),
        "Work-related item costing $300 or less? Claim in full. Keep the receipt. No depreciation."), 4.5),
 (end(b, "The ATO won't [[remind]] you. We will.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
