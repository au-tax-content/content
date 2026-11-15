"""RP-31 Reel: 2 tax breaks for workers that are already law. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "[[2]] tax breaks for workers that are [[already]] law.", "NO FORMS NEEDED", "paper", size=128), 3.0),
 (point(b, 1, "[[$1,000]] standard deduction",
        big(b, "$1,000", "FROM 2026–27", size=180),
        "Automatic for residents who earn wages. No receipts. It first shows up in the return you lodge after 30 June 2027.", title_size=100), 4.6),
 (point(b, 2, "[[$250]] working Australians offset",
        big(b, "$250", "FROM 2027–28", size=190),
        "A new tax offset of up to $250 a year for residents with income from work. It passed Parliament in June 2026.", wave=True, title_size=92), 4.6),
 (point(b, 3, "The [[fine]] [[print]]",
        steps(b, ["Deduction: cuts taxable income", "Offset: comes off the tax", "Offset is non-refundable"], start=0.7, gap=0.25),
        "A $1,000 deduction saves about $300 at the 30% rate. The offset comes straight off your tax, but can't take it below zero."), 4.8),
 (end(b, "You don't apply. You just [[lodge.]]", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
