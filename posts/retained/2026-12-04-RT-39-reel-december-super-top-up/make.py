"""RT-39 Reel: December super top-up — cut this year's tax before June gets busy. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "December is the best time to top up your [[super]] — here's why", "RETAINED · SUPER STRATEGY", "brass", size=108), 3.0),
 (point(b, 1, "The [[cap]] resets on 1 July",
        big(b, "$32,500", "2026–27 concessional cap", size=104),
        "Your cap runs July to June. Contributions by employers plus anything you add must stay under $32,500. At 30 June, whatever's unused is gone — unless you have carry-forward room."), 4.5),
 (point(b, 2, "December = time to [[check your room]]",
        big(b, "15%", "tax rate on contributions in the fund", size=104),
        "Log in to your super fund or myGov and check how much your employer has contributed so far. What's left before $32,500 is your room to add more — taxed at 15% inside the fund instead of your marginal rate."), 4.5),
 (point(b, 3, "[[Carry-forward]] if balance under $500K",
        stamp_el(b, "PRIOR 30 JUNE", 0.9, size=56),
        "If your super balance was under $500,000 at the last 30 June, unused concessional cap from up to 5 prior years can be carried forward. That can mean a larger top-up for catch-up years."), 4.5),
 (end(b, "Waiting until June? The [[rush]] is real. Start now.", "SAVE + SHARE WITH SOMEONE WHO NEEDS THIS", size=104), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
