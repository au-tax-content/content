"""RT-34 Reel: Ranking 7 tax moves for small business owners. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
ITEMS = [
    ("D", "SPEND TO CLAIM", "Spending $1 to save 25–30c still costs 70–75c. Only buy what you'd buy anyway."),
    ("C", "SMALL BIZ OFFSET", "Up to $1,000 off for sole traders. Automatic, capped, no action needed."),
    ("C", "PREPAY EXPENSES", "Move a deduction forward — but it must be for a service period ≤12 months."),
    ("B", "TIMING INCOME", "Defer invoicing past 30 June if cash-flow allows. One year's saving only."),
    ("A", "$20K WRITE-OFF", "Deduct an asset under $20,000 in the year you use it. Permanent from July 2026."),
    ("A", "RIGHT STRUCTURE", "Company rate 25% vs up to 45% personal. Set up with a registered adviser."),
    ("S", "YOUR OWN SUPER", "Up to $32,500 a year, taxed at 15% in the fund. Locked until preservation age."),
]
scenes = [
 (tier(b, "I ranked [[7]] tax moves for small business owners", "LEGAL · GENERAL INFO · 2026–27", ITEMS), tier_len(ITEMS)),
 (end(b, "Which one are you [[missing?]]", "SAVE + SEND TO YOUR ACCOUNTANT"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
