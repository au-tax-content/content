"""RT-19 Reel: 7 business deductions that sound illegal (but aren't). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (listloop(b, "7 business deductions that sound [[illegal]] (but aren't)", "SMALL BUSINESS · CONDITIONS APPLY", [
     ("A $19,000 machine, in one year", "WRITE-OFF", "under $20,000 each, turnover under $10M"),
     ("Next year's insurance, this year", "PREPAY", "up to 12 months ahead"),
     ("Your own super", "DEDUCT", "sole traders, up to the $32,500 cap"),
     ("A debt nobody paid you", "BAD DEBT", ""),
     ("Interest on a business loan", "DEDUCT", ""),
     ("Your accountant's fee", "DEDUCT", "bookkeeper and tax agent too"),
     ("Part of your phone + internet", "BUSINESS %", "only the business share"),
   ], head="RETAINED · LEDGER", title_size=84, row_size=38), 11.5),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
