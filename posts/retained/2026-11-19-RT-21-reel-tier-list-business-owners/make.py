"""RT-21 Reel: Ranking 6 tax moves for business owners, S to D tier. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
ITEMS = [
    ("D", "BUYING TO CLAIM", "Spending $1 to save about 30c still costs 70c. Only for things you'd buy anyway."),
    ("C", "PREPAYING", "Pay up to 12 months early. It moves a deduction forward, it doesn't create one."),
    ("B", "SB TAX OFFSET", "Up to $1,000 off for sole traders, automatically. Nice, but capped."),
    ("A", "$20K WRITE-OFF", "Deduct an asset under $20,000 in the year you first use it. Costs cash up front."),
    ("A", "RIGHT STRUCTURE", "25% company rate vs up to 45% personal. Complex: use a registered adviser."),
    ("S", "YOUR OWN SUPER", "Up to $32,500 a year, taxed at 15% in the fund. Locked until you retire."),
]
scenes = [
 (tier(b, "I ranked [[6]] tax moves for business owners.", "LEGAL · GENERAL INFO · 2026–27", ITEMS), tier_len(ITEMS)),
 (end(b, "Which one are you [[missing?]]", "SAVE + SEND TO A MATE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
