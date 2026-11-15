"""RP-24 Reel: $21 billion in lost super: is some of it yours?. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "[[$21]] [[billion]] in lost super. Is some [[yours?]]", "2 MINUTES TO CHECK", "mint", size=140), 3.0),
 (point(b, 1, "The [[number]]",
        big(b, "", "LOST + ATO-HELD", count_to=21, pre="$", post="B", size=210),
        "The ATO says more than $21 billion in super is waiting to be claimed (August 2026)."), 4.4),
 (point(b, 2, "How it gets [[lost]]",
        big(b, "4M", "PEOPLE · 2+ ACCOUNTS", size=190),
        "About 4 million people held two or more super accounts at 30 June 2026. Accounts from old jobs can end up lost or held by the ATO.", wave=True), 4.6),
 (point(b, 3, "How to [[check]]",
        steps(b, ["Log in to myGov", "Open ATO online services", "Go to Super"], start=0.7, gap=0.22),
        "Free. You'll see every account in your name, including ATO-held super. Check any insurance in an old fund before you combine."), 4.8),
 (end(b, "It's not a bonus. It's [[yours.]]", "CHECK TONIGHT"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
