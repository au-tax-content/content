"""RP-34 Reel: Ranking every way employees pay less tax. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
ITEMS = [
    ("D", "TWEAKING RECEIPTS", "Claiming things you can't actually claim. The ATO data-matches everything."),
    ("C", "THE $1,000 RULE", "Standard deduction of $1,000 without receipts — only for laundry and uniform, not everything."),
    ("C", "WORK-FROM-HOME", "Up to 70c/hr for running costs. Good, but you need a real hourly log."),
    ("B", "DEDUCTIBLE EXPENSES", "Tools, subscriptions, memberships, self-ed — solid if you have receipts."),
    ("B", "CARRY-FORWARD SUPER", "Unused concessional cap from prior years — if balance under $500K at prior 30 June."),
    ("A", "SALARY SACRIFICE", "Pre-tax super contributions — reduces taxable income, taxed at 15% in the fund."),
    ("S", "CONCESSIONAL SUPER", "$32,500 cap total. The most tax-effective move for most employees."),
]
scenes = [
 (tier(b, "I ranked every way [[employees]] pay less tax", "LEGAL · GENERAL INFO · 2026–27", ITEMS), tier_len(ITEMS)),
 (end(b, "Which tier are you [[playing in?]]", "SAVE + SHARE WITH A WORKMATE"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
