"""RP-21 Reel: Ranking 6 ways employees pay less tax, S to D tier. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
ITEMS = [
    ("D", "BUYING TO CLAIM", "Spend $1 to get about 30c back. You're still 70c down."),
    ("C", "HOSPITAL COVER", "Single, over $105,000, no cover? The surcharge is 1% to 1.5% of income."),
    ("B", "$1,000 STANDARD", "Automatic and receipt-free from 2026–27. Easy, but it's the floor."),
    ("A", "ITEMISING", "Real work costs over $1,000? Claim them with records instead."),
    ("A", "CARRY-FORWARD", "Unused super cap from up to 5 years. Only with a balance under $500K."),
    ("S", "SALARY SACRIFICE", "Taxed at 15% in the fund, not your rate. Capped, and locked till you retire."),
]
scenes = [
 (tier(b, "I ranked [[6]] ways employees pay less tax.", "LEGALLY · GENERAL INFO · 2026–27", ITEMS), tier_len(ITEMS)),
 (end(b, "Which one are you [[not]] using?", "SAVE + SEND TO A MATE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
