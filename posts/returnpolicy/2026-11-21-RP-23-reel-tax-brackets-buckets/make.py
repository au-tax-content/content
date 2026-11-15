"""RP-23 Reel: Tax brackets in buckets: a pay rise can't cost you money. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "Earn [[$100K.]] Pay [[30%]] on all of it?", "PAUSE AND GUESS", "paper"), 3.0),
 (buckets(b, "No. Tax fills [[buckets.]]", [
     ("0%", "first $18,200", 0.22, "$0", "#A8A193"),
     ("15%", "next $26,800", 0.36, "$4,020", "#FFE36E"),
     ("30%", "next $55,000", 0.74, "$16,500", "#3FD07F"),
   ], "Total on $100,000: $20,520. Not $30,000. (2026–27 rates, before the 2% Medicare levy.)"), 7.0),
 (card(b, "A [[raise]] can't shrink your pay",
       big(b, "37c", "PER EXTRA $1 · OVER $135K", size=190),
       "Cross $135,000 and only the dollars above it are taxed at 37%. Everything below stays exactly where it was.", wave=True), 4.6),
 (end(b, "Higher bracket. [[Never]] lower take-home.", "SEND TO THE GROUP CHAT"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
