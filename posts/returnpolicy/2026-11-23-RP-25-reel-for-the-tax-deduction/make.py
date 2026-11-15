"""RP-25 Reel: Stop buying things 'for the tax deduction'. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "Stop buying things for the [[tax]] [[deduction.]]", "DO THIS MATHS FIRST", "yellow", size=140), 3.0),
 (point(b, 1, "A deduction is [[not]] a refund",
        big(b, "30c", "BACK PER $1", size=200),
        "A deduction lowers your taxable income. On the 30% rate ($45,001 to $135,000, 2026–27) each $1 claimed saves 30c, plus 2c Medicare levy.", title_size=104), 4.8),
 (point(b, 2, "The [[$1,000]] laptop",
        steps(b, ["Spend: $1,000", "Tax saved: about $320", "Still out of pocket: $680"], start=0.7, gap=0.3),
        "And a work item over $300 is usually claimed over several years, not all at once.", wave=True), 4.6),
 (point(b, 3, "When it [[is]] worth it",
        stamp_el(b, "YOU NEEDED IT ANYWAY", 0.9, size=52),
        "If you'd buy it for work regardless, claim it. If you're buying it because it's 'deductible', you're spending a dollar to save about 32 cents."), 4.8),
 (end(b, "A deduction is a [[discount.]] Not free money.", "SEND TO THAT FRIEND"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
