"""RP-38 Reel: December receipts folder — 7 categories to start collecting now. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (listloop(b, "December receipts folder: 7 categories to start collecting [[now]]", "RETURN POLICY · BUILD THE HABIT", [
     ("Work tools & equipment", "KEEP ALL", "anything you bought for work — receipts or bank statement"),
     ("Home office expenses", "LOG HOURS", "start an hours log now if you work from home"),
     ("Self-education & courses", "MUST RELATE", "to your *current* job — save enrolment + payment proof"),
     ("Professional memberships", "ANNUAL FEES", "union dues, industry body fees — deductible"),
     ("Work-related car trips", "ODOMETER NOTE", "note start km for the year if doing logbook method"),
     ("Uniform & protective clothing", "LAUNDRY TOO", "photo the receipt; note cost per wash if claiming laundry"),
     ("Income protection premiums", "OUTSIDE SUPER", "personal payments only — not premiums inside super"),
   ], head="RETURN POLICY · RECEIPT CATEGORIES", foot="All categories checked ato.gov.au · 2026–27 income year.", title_size=80, row_size=34), 12.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
