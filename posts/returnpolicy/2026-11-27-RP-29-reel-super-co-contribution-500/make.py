"""RP-29 Reel: The super co-contribution: up to $500 from the government. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "The government might add [[$500]] to your super.", "MOST PEOPLE MISS THIS", "mint", size=132), 3.0),
 (point(b, 1, "How it [[works]]",
        big(b, "50c", "PER $1 YOU ADD", size=200),
        "Put your own after-tax money into super and the government can add up to 50c for each dollar. Maximum $500 a year."), 4.6),
 (point(b, 2, "Who [[gets]] it",
        steps(b, ["Up to $49,293: full $500", "Fades to nil at $64,293", "10%+ of income from work"], start=0.7, gap=0.25),
        "2026–27 thresholds. You also need to be under 71, not on a temporary visa, and to lodge a tax return.", wave=True), 4.8),
 (point(b, 3, "The [[catch]]",
        stamp_el(b, "NOT IF YOU DEDUCT IT", 0.9, size=52),
        "It only counts on contributions you don't claim as a tax deduction. And the money is locked in super until you retire."), 4.6),
 (end(b, "No form. Lodge your return and it's [[automatic.]]", "SEND TO A PART-TIMER", size=124), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
