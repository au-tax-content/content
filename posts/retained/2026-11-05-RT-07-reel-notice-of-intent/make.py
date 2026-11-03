"""RT-07 Reel: the form that makes or breaks a super deduction. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "Skip [[this]] form, lose the deduction.", "SUPER DEDUCTIONS · SAVE THIS"), 3.0),
 (point(b, 1, "Notice of [[intent]]", steps(b, ["1 · SEND NOTICE TO FUND", "2 · FUND ACKNOWLEDGES", "3 · THEN CLAIM IT"]), "The fund must acknowledge it in writing before you claim."), 4.6),
 (point(b, 2, "Mind the [[deadline]]", steps(b, ["YOUR LODGEMENT DAY", "END OF NEXT INCOME YEAR"]) + stamp_el(b, "WHICHEVER IS FIRST", 1.3), "It counts towards your $32,500 concessional cap (2026–27)."), 4.6),
 (point(b, 3, "Aged [[67–74?]]", big(b, "40 HRS", "IN 30 DAYS", size=170), "You'll need to meet the work test, or its exemption, to claim.", wave=True), 4.4),
 (end(b, "Paperwork [[first.]] Deduction second.", "SAVE THIS FOR JUNE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
