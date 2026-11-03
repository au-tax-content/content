"""RT-06 Reel: $120K profit, $20K into super, $3,400 kept (2026-27). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook(b, "Same profit. [[$3,400]] more kept.", "$120K PROFIT · 2026–27 · SAVE THIS"), 3.0),
 (point(b, 1, "Profit: [[$120K]]", big(b, "", "TAX + MEDICARE", count_to=28920, pre="$", size=170), "Sole trader, 2026–27 resident rates, no other income or offsets."), 4.4),
 (point(b, 2, "[[$20K]] into super", big(b, "", "LESS TAX", count_to=6400, pre="$", size=190), "Claimed as a deduction, so taxable income drops to $100K."), 4.4),
 (point(b, 3, "Fund takes [[15%]]", big(b, "", "KEPT", count_to=3400, pre="$", size=190) + stamp_el(b, "−$3,000 FUND TAX"), "The catch: it's locked in super until retirement. Cap: $32,500 in 2026–27.", wave=True), 4.6),
 (end(b, "Same profit. [[Less]] tax.", "SAVE THIS FOR JUNE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
