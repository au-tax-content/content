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
 (point(b, 2, "Buy [[before]] 30 June",
        big(b, "<$20K", "PER ASSET", size=170),
        "The instant write-off only counts once the asset is used or installed ready for use. In the box doesn't count."), 4.5),
 (point(b, 3, "Top up [[super]]",
        big(b, "$32,500", "CAP 2026–27", size=160),
        "A contribution counts in the year your fund receives it, so don't leave it to the last day.", wave=True), 4.5),
 (end(b, "[[Timing]] is planning. Legal and boring.", "SAVE THIS FOR JUNE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
