"""RP-41 Reel: 3 things high earners on $100K+ can still claim. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "On $100K+? Here are 3 things you can [[still claim]]", "RETURN POLICY · HIGH EARNER MOVES", "paper", size=112), 3.0),
 (point(b, 1, "[[Concessional super]] — your biggest lever",
        big(b, "$32,500", "cap total — most don't use it", size=104),
        "At $100K, your marginal rate is 30%. Every dollar into super is taxed at 15% — a 15-point saving. At $135K it's 37% marginal, so a 22-point gap. Catch: contributions go to preservation age."), 4.5),
 (point(b, 2, "[[Work expenses]] still count — with receipts",
        big(b, "30c off", "tax on every $1 deduction", size=104),
        "At $100K–$134,999 marginal rate is 30%. Every $1 of deductible expense saves 30c. That includes tools, subscriptions, self-education for your current role, and income protection premiums outside super."), 4.5),
 (point(b, 3, "[[Income protection]] outside super",
        big(b, "100%", "deductible if paid personally", size=112),
        "Income protection insurance premiums paid personally (not via super) are fully deductible. At the 30% bracket, a $2,000 annual premium saves $600 in tax. It also protects up to 70% of your income if you can't work."), 4.5),
 (end(b, "LITO's gone at your income. [[These still work.]]", "SAVE + SHARE WITH A HIGH-EARNING FRIEND", size=108), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
