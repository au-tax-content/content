"""RT-20 Reel: How much to set aside from every invoice, by profit. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (ladder(b, "How much tax to [[set]] [[aside]] from every invoice", "SOLE TRADERS · 2026–27", [
     ("$75K", 20, "profit → about $14,520 tax + Medicare"),
     ("$100K", 23, "profit → about $22,520"),
     ("$125K", 25, "profit → about $30,520"),
     ("$150K", 27, "profit → about $39,570"),
     ("$200K", 30, "profit → about $59,870"),
   ], "Income tax + 2% Medicare levy on profit, before offsets. Registered for GST? That's extra.", pre="", post="%", title_size=84), 10.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
