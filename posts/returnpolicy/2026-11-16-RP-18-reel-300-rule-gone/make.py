"""RP-18 Reel: The $300 no-receipt rule ended on 1 July 2026. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "The [[$300]] no-receipt rule is [[gone.]]", "SINCE 1 JULY 2026", "red"), 3.0),
 (point(b, 1, "What [[changed]]",
        stamp_el(b, "ENDED 1 JULY 2026", 0.9, size=58),
        "You used to be able to claim up to $300 of work expenses with no receipts. From the 2026–27 return, that exception no longer applies."), 4.6),
 (point(b, 2, "What [[replaced]] it",
        big(b, "$1,000", "STANDARD · 2026–27", size=180),
        "A standard deduction of up to $1,000 for work expenses. Automatic, no receipts, for residents who earn wages.", wave=True), 4.6),
 (point(b, 3, "The [[catch]]",
        steps(b, ["Claim actual costs instead?", "Every dollar needs a record", "Laundry: $150 rule gone too"], start=0.7, gap=0.22),
        "Claiming your real expenses reduces the $1,000 dollar for dollar. It only pays off if they add up to more."), 4.6),
 (end(b, "Spend over [[$1,000]] on work? Keep every receipt.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
