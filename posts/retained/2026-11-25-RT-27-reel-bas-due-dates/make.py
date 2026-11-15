"""RT-27 Reel: Quarterly BAS due dates to screenshot. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (listloop(b, "BAS due dates. [[Screenshot]] this.", "QUARTERLY LODGERS", [
     ("July – September", "28 OCT", ""),
     ("October – December", "28 FEB", "an extra month is already built in"),
     ("January – March", "28 APR", ""),
     ("April – June", "28 JUL", ""),
     ("Lodge late", "$364", "failure-to-lodge penalty per 28 days, small entities"),
   ], head="RETAINED · BAS CALENDAR", foot="Lodging online or through a registered agent can add time (not Oct–Dec).", title_size=104, row_size=44), 9.5),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
