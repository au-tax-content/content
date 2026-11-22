"""RP-40 Reel: Side hustle this summer? Read this before you spend a dollar. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "Starting a [[summer side hustle?]] Read this before you spend a dollar.", "RETURN POLICY · SIDE HUSTLE RULES", "red", size=104), 3.0),
 (point(b, 1, "[[No minimum]] — the ATO taxes it all",
        big(b, "$1 of income", "= income you must declare", size=104),
        "There's no minimum threshold for side hustle income. Every dollar earned outside your salary is taxable. And platforms (Uber, Airtasker, Airbnb) now report to the ATO under the Sharing Economy Reporting Regime."), 4.5),
 (point(b, 2, "[[Business or hobby?]] It matters",
        big(b, "No $ threshold", "the ATO looks at intent", size=100),
        "Whether you're running a business depends on your intent, the scale, and how you operate — not how much you earn. A hobby can't deduct expenses against income. A business can. Get this wrong and you lose deductions."), 4.5),
 (point(b, 3, "[[Set aside]] tax from day one",
        stamp_el(b, "SET ASIDE NOW", 0.9, size=60),
        "If you're a sole trader, there's no employer withholding tax from your side-hustle income. Set aside around 20–30% of every payment. Keep records from your first invoice — receipts, bank statements, the lot."), 4.5),
 (end(b, "Start right. It's [[much harder]] to fix later.", "SAVE + SHARE WITH SOMEONE STARTING OUT", size=108), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
