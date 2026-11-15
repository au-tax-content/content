"""RT-22 Reel: New ABN? 5 things nobody tells you. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (listloop(b, "New ABN? [[5]] things nobody tells you", "FIRST-YEAR SOLE TRADERS", [
     ("Nobody withholds your tax", "SET ASIDE", "the bill comes after you lodge"),
     ("You can't pay yourself a wage", "PROFIT", "you're taxed on profit, not on drawings"),
     ("GST starts at $75K turnover", "21 DAYS", "to register once you reach it"),
     ("Nobody pays your super", "YOU DO", "the 12% is for employees"),
     ("Year 2 brings instalments", "PAYG", "the ATO starts collecting as you go"),
   ], head="RETAINED · YEAR ONE", foot="General info for sole traders, 2026–27.", title_size=96), 10.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
