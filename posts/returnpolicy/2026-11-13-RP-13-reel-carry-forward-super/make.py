"""RP-13 Reel: carry-forward concessional super rule. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "If your super is under [[500K,]] this rule is worth knowing.", "SAVE THIS"), 3.0),
 (point(b, 1, "The [[carry-forward]] rule",
        big(b, "5", "PRIOR YEARS", size=200),
        "Unused concessional cap space from the last 5 years can be used in a single year. Automatically applied."), 4.5),
 (point(b, 2, "Who [[qualifies]]",
        steps(b, ["Balance < $500K at prior 30 June", "Any unused cap from 2021–22 on"]),
        "Your super fund balance, not your salary. Check it in MyGov."), 4.5),
 (point(b, 3, "What it [[means]]",
        big(b, "$32,500", "BASE CAP 2026–27", size=160),
        "If you've underpaid super for years, your effective cap could be much higher than $32,500 this year.", wave=True), 4.5),
 (end(b, "Check MyGov for your [[available]] cap.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
