"""RP-27 Reel: 6 things you can claim on top of the $1,000 standard deduction. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (listloop(b, "6 claims that sit [[on]] [[top]] of the $1,000", "STANDARD DEDUCTION · 2026–27", [
     ("Union + association fees", "ON TOP", ""),
     ("Donations to charity", "ON TOP", "$2 or more, to a registered charity"),
     ("Your tax agent's fee", "ON TOP", "the cost of managing your tax affairs"),
     ("Income protection cover", "ON TOP", "premiums you pay yourself"),
     ("Personal super contributions", "ON TOP", "conditions apply"),
     ("Investment + rental costs", "ON TOP", "they aren't work expenses"),
   ], head="RETURN POLICY · EXTRAS", foot="These don't reduce the $1,000. Keep records for each.", title_size=88), 10.5),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
