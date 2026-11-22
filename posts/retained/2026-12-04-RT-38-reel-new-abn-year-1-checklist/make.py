"""RT-38 Reel: New ABN year 1 — 5 things to set up. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (listloop(b, "New ABN? Set these [[5 things]] up in year one", "RETAINED · FIRST-YEAR FOUNDATIONS", [
     ("Register for GST if near $75K", "21-DAY RULE", "turnover threshold; must register within 21 days of crossing"),
     ("Open a separate business account", "NON-NEGOTIABLE", "mixing personal & business money costs you at tax time"),
     ("Set aside tax from every invoice", "20–30%", "sole traders pay income tax on profit — no employer does it for you"),
     ("Pay yourself super voluntarily", "$32,500 CAP", "sole traders get no employer super; concessional contribs = 15% tax"),
     ("Keep a simple profit & loss", "MONTHLY", "income minus expenses — know your numbers before June"),
   ], head="RETAINED · FIRST-YEAR ABN", foot="Figures verified ato.gov.au · 2026–27 income year.", title_size=84, row_size=38), 11.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
