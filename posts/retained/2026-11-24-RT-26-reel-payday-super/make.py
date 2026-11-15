"""RT-26 Reel: Have staff? Super is now due every payday. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Have staff? Super is now due [[every]] [[payday.]]", "SINCE 1 JULY 2026", "green", size=130), 3.0),
 (point(b, 1, "What [[changed]]",
        stamp_el(b, "QUARTERLY → PAYDAY", 0.9, size=56),
        "From 1 July 2026 you pay super guarantee with each pay run, not once a quarter."), 4.4),
 (point(b, 2, "The [[deadline]]",
        big(b, "7", "BUSINESS DAYS", size=230),
        "Contributions must reach the employee's fund within 7 business days of payday. The rate is still 12%.", wave=True), 4.6),
 (point(b, 3, "If it's [[late]]",
        steps(b, ["ATO assesses the charge", "Interest compounds daily", "Plus an admin uplift"], start=0.7, gap=0.28),
        "The super guarantee charge is now worked out by the ATO on qualifying earnings."), 4.6),
 (end(b, "Is your payroll set to pay super [[each]] run?", "SEND TO YOUR BOOKKEEPER", size=124), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
