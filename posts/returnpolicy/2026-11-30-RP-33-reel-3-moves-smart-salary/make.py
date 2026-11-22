"""RP-33 Reel: 3 things smart salary earners do to pay less tax (legally). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "3 things smart salary earners do to [[legally]] pay less tax", "RETURN POLICY · THE MOVES", "ink", size=120), 3.0),
 (point(b, 1, "[[Salary sacrifice]] into super",
        big(b, "$32,500", "total concessional cap 2026–27", size=104),
        "Pre-tax salary goes into super taxed at 15% instead of your marginal rate. At 30% marginal, that's a 15-point saving. Talk to your employer's payroll team to set it up."), 4.5),
 (point(b, 2, "Claim the [[new $1,000]] work deduction",
        big(b, "$1,000", "automatic from 2026–27", size=112),
        "From 2026–27 there's a standard $1,000 deduction for work-related expenses — no receipts needed. If your actual claims are higher, claim those instead. It doesn't stack."), 4.5),
 (point(b, 3, "Use [[carry-forward]] super if eligible",
        stamp_el(b, "BALANCE UNDER $500K?", 0.9, size=52),
        "If your super balance was under $500,000 at the last 30 June, you can use unused concessional cap from up to 5 prior years. That means a bigger pre-tax contribution — and a bigger deduction — this year."), 4.8),
 (end(b, "Three moves. All [[legal.]] All worth knowing.", "SAVE + SHARE WITH A WORKMATE", size=116), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
