"""RP-30 Reel: Side hustle this summer? There's no tax-free amount. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "Side hustle? There's [[no]] tax-free amount.", "MYTH BUSTED", "yellow", size=140), 3.0),
 (point(b, 1, "The [[$18,200]] is used once",
        big(b, "$18,200", "PER PERSON", size=170),
        "The tax-free threshold covers all your income added together. If your job already uses it, side income is taxed from the first dollar.", title_size=104), 4.8),
 (point(b, 2, "There's [[no]] minimum",
        stamp_el(b, "DECLARE ALL OF IT", 0.9, size=58),
        "If you're doing it to make money, the ATO says it goes in your return. No dollar limit makes it 'not count'.", wave=True), 4.6),
 (point(b, 3, "They can [[see]] it",
        steps(b, ["Ride share + delivery", "Short-stay rentals", "Selling + gig platforms"], start=0.7, gap=0.22),
        "Platforms report what they pay sellers to the ATO, and it's matched against your tax return."), 4.6),
 (end(b, "Side income has [[no]] tax taken out. Plan for it.", "SAVE THIS", size=124), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
