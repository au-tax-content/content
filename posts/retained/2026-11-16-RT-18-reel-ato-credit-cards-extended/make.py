"""RT-18 Reel: ATO credit card payments extended to 30 June 2027. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Credit cards [[stay.]] Until 30 June 2027.", "WHAT CHANGED", "navy", size=140, strap="ATO UPDATE"), 3.0),
 (point(b, 1, "The [[original]] plan",
        stamp_el(b, "30 NOV 2026", 0.9, size=64),
        "The ATO had said it would stop taking credit card payments after 30 November 2026."), 4.2),
 (point(b, 2, "The [[extension]]",
        big(b, "30 JUNE 2027", "", size=104),
        "On 9 October 2026 the ATO extended the transition: credit card payments for tax obligations continue until 30 June 2027.", wave=True), 4.6),
 (point(b, 3, "What to do [[now]]",
        steps(b, ["Payment plan on a card?", "Line up a new method by mid-2027", "ato.gov.au → how to pay"], start=0.7, gap=0.25),
        "After the cut-off, a plan linked to a credit card needs another payment method or the payments will fail."), 4.6),
 (end(b, "Pay your BAS by card? The clock is [[running.]]", "SEND TO YOUR BOOKKEEPER", size=124), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
