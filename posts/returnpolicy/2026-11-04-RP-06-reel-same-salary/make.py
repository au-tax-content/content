"""RP-06 Reel: same $90K salary, $3,200 less income tax (salary sacrifice, 2026-27). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "Same $90K salary. [[$3,200]] less tax.", "SALARY SACRIFICE · 2026–27"), 3.0),
 (point(b, 1, "Sam pays [[full]] rate", big(b, "", "TAX + MEDICARE", count_to=19320, pre="$", size=170), "$90K salary, 2026–27 resident rates, no other income or offsets."), 4.4),
 (point(b, 2, "Alex sacrifices [[$10K]]", big(b, "", "TAX + MEDICARE", count_to=16120, pre="$", size=170), "That $10K of before-tax pay goes to super. Taxable income: $80K."), 4.4),
 (point(b, 3, "Super takes [[15%]]", big(b, "", "AHEAD OVERALL", count_to=1700, pre="$", size=190) + stamp_el(b, "LOCKED TILL RETIREMENT"), "2026–27 cap: $32,500, including your employer's 12%.", wave=True), 4.6),
 (end(b, "Same job. [[Less]] tax.", "SAVE THIS FOR YOUR PAY REVIEW"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
