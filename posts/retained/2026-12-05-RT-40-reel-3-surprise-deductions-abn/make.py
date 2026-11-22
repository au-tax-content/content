"""RT-40 Reel: 3 business deductions that surprise first-year ABN holders. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "3 deductions that [[surprise]] most first-year ABN holders", "RETAINED · FIRST-YEAR FACTS", "navy", size=112), 3.0),
 (point(b, 1, "Your [[own]] super contributions",
        big(b, "$32,500", "concessional cap 2026–27", size=104),
        "Unlike employees, sole traders get no employer super. But contributions you make yourself are deductible up to the $32,500 concessional cap — taxed at 15% in the fund. You have to lodge a Notice of Intent with your fund."), 4.5),
 (point(b, 2, "Tax agent and [[accounting fees]]",
        big(b, "100%", "deductible business expense", size=112),
        "Your bookkeeper, accountant and tax agent fees are deductible business expenses. Even if you haven't lodged a return yet — fees for getting set up and registered count. Keep the invoice."), 4.5),
 (point(b, 3, "Part of your [[home]]",
        steps(b, ["Must use a room exclusively for work", "Electricity, internet, office decline", "Must be your principal place of business", "Can't claim if on WFH arrangement for employer"], start=0.6, gap=0.22),
        "Sole traders who run their business from a dedicated home office can claim a portion of occupancy costs. The portion is based on the floor area used. This doesn't apply to employees working from home for their employer."), 5.0),
 (end(b, "Year one sets the habits. [[Get them right.]]", "SAVE + SEND TO A FRIEND WHO JUST GOT AN ABN", size=108), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
