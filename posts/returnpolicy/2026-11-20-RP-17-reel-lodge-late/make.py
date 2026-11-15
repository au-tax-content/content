"""RP-17 Reel: What it costs to lodge your tax return late. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "Lodge late? Here's what the ATO actually [[charges.]]", "SAVE THIS"), 3.0),
 (point(b, 1, "[[Failure to lodge]] penalty",
        big(b, "$364", "PER 28 DAYS · 2026–27", size=185),
        "One penalty unit per 28-day period (or part of one). Max 5 periods = $1,820. The penalty unit rose from $330 to $364 on 1 July 2026."), 4.5),
 (point(b, 2, "[[Interest]] on what you owe",
        stamp_el(b, "GIC APPLIES", 0.9, size=58),
        "The General Interest Charge runs daily on any unpaid tax debt from the due date. It compounds. The longer you wait, the more it adds up.", wave=True), 4.5),
 (point(b, 3, "What to do if you're [[already late]]",
        steps(b, ["Lodge now — even if you can't pay", "FTL stops accruing once lodged", "Call ATO or use a registered agent", "Payment plans are available"], start=0.6, gap=0.18),
        "The ATO penalises not lodging more than not paying. Lodge first, sort the payment after."), 4.5),
 (end(b, "Late is better than [[never.]] Lodge first.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
