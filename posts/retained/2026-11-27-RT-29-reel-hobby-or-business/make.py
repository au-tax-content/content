"""RT-29 Reel: Hobby or business? The 5 things the ATO looks at. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (listloop(b, "Hobby or business? The ATO asks [[5]] things", "THERE IS NO DOLLAR THRESHOLD", [
     ("Do you mean to run a business?", "INTENT", ""),
     ("Are you trying to make a profit?", "PROFIT", ""),
     ("Is it big enough to make one?", "SCALE", ""),
     ("Do you do it again and again?", "REPEAT", ""),
     ("Do you run it like a business?", "METHOD", "records, advertising, a plan, an ABN"),
   ], head="RETAINED · THE TEST", foot="No single answer decides it. Unsure? A registered agent can tell you.", title_size=88, row_size=38), 10.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
