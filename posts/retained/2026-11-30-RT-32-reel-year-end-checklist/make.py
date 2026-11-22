"""RT-32 Reel: 5 things to do before 31 December to cut this year's tax. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (listloop(b, "5 things to do before [[31 December]] to cut this year's tax", "RETAINED · YEAR-END CHECKLIST", [
     ("Top up your super", "$32,500 CAP", "check employer contribs first; taxed at 15% in the fund"),
     ("Prepay deductible expenses", "12-MONTH RULE", "pay up to 12 months early; ends in next income year"),
     ("Buy and install assets under $20K", "WRITE IT OFF", "must be first used or installed before 30 June 2027"),
     ("Write off bad debts", "ACCRUALS ONLY", "must have been included in income and written off as bad"),
     ("Start a receipts folder", "START NOW", "photos, PDFs, bank statements — all deductions need proof"),
   ], head="RETAINED · YEAR-END CHECKLIST", foot="Every item verified on ato.gov.au · 2026–27 income year.", title_size=86, row_size=38), 11.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
