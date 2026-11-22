"""RT-35 Reel: December receipts folder — what to collect now. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (listloop(b, "December receipts folder: what to collect [[right now]]", "RETAINED · START THE HABIT EARLY", [
     ("Business asset receipts", "UNDER $20K", "purchase date, supplier, amount — needed for write-off"),
     ("Subscriptions & software", "RECURRING COSTS", "accounting, cloud tools, professional memberships"),
     ("Vehicle logbook", "12-WEEK RULE", "start now if you use a car for work — cents per km or logbook"),
     ("Super fund statements", "CONCESSIONAL", "confirm employer paid SG and any extra you contributed"),
     ("Bank & card statements", "ALL ACCOUNTS", "one PDF per account — saves time at tax time"),
   ], head="RETAINED · BUILD THE HABIT", foot="Deductions require records. ato.gov.au · 2026–27 income year.", title_size=84, row_size=38), 11.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
