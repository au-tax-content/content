"""RP-28 Reel: 3 income lines that quietly change your tax. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "[[3]] income lines that quietly change your tax.", "2026–27", "red", size=132), 3.0),
 (point(b, 1, "Over [[$105,000]] and single",
        stamp_el(b, "MEDICARE LEVY SURCHARGE", 0.9, size=44),
        "No private hospital cover? A surcharge of 1% to 1.5% of your income applies on top of the 2% Medicare levy. Families: $210,000 combined.", title_size=104), 4.8),
 (point(b, 2, "Over [[$135,000]]",
        big(b, "37c", "PER EXTRA $1", size=200),
        "Only the dollars above $135,000 are taxed at 37%. Below it, nothing changes.", wave=True), 4.4),
 (point(b, 3, "Over [[$250,000]]",
        big(b, "+15%", "DIVISION 293", size=190),
        "Income plus concessional super contributions above $250,000: an extra 15% tax on some of those contributions."), 4.6),
 (end(b, "Know your [[line]] before 30 June.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
