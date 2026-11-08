"""RT-13 Reel: how to legally time your business tax bill. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "Smart owners don't just claim more. They [[time]] it.", "STRATEGY · SAVE THIS"), 3.0),
 (point(b, 1, "Bring forward [[deductions]]",
        stamp_el(b, "12-MONTH RULE", 0.9, size=58),
        "Pay rent, insurance, subscriptions before 30 June — up to 12 months ahead. Deduct it this year."), 4.5),
 (point(b, 2, "Defer [[income]]",
        big(b, "July", "INVOICE IN", size=190),
        "On a cash basis, income is assessable when received. Invoice after 30 June for work done in June."), 4.5),
 (point(b, 3, "Top up [[super]] now",
        stamp_el(b, "CLEARS BY 30 JUNE", 0.9, size=50),
        "Super contributions must be received by your fund before 30 June. Allow 3–5 business days.", wave=True), 4.5),
 (end(b, "[[Timing]] is strategy. Not avoidance.", "SAVE THIS FOR JUNE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
