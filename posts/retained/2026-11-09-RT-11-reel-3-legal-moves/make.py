"""RT-11 Reel: 3 legal moves that cut your business tax bill. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "[[3]] legal moves most business owners miss", "SAVE THIS"), 3.0),
 (point(b, 1, "Max your [[concessional]] super",
        big(b, "$32,500", "CAP 2026–27", size=170),
        "Taxed at 15% — not your marginal rate. The bigger the gap, the bigger the saving."), 4.5),
 (point(b, 2, "Instant [[asset]] write-off",
        big(b, "<$20K", "PER ASSET · PERMANENT", size=160),
        "Buy equipment, install it, claim it in full. Turnover under $10M qualifies.", wave=True), 4.5),
 (point(b, 3, "Prepay deductible [[expenses]]",
        stamp_el(b, "12-MONTH RULE", 0.9, size=58),
        "Pay rent, insurance, subscriptions before 30 June — up to 12 months ahead. Deduct it this year."), 4.5),
 (end(b, "Legal. Boring. [[Worth]] doing every year.", "SAVE THIS FOR JUNE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
