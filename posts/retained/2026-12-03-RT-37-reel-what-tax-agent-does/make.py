"""RT-37 Reel: What a registered tax agent actually does for small businesses. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "What a registered [[tax agent]] actually does for small businesses", "RETAINED · BEHIND THE SCENES", "green", size=112), 3.0),
 (point(b, 1, "They find [[deductions]] you'd miss",
        big(b, "16%", "small business tax offset", size=112),
        "The small business income tax offset (up to $1,000), prepayment timing, write-offs — a good agent finds the ones you didn't know applied. That's the fee paying for itself."), 4.5),
 (point(b, 2, "They keep you [[out of trouble]]",
        big(b, "$364/28 days", "failure-to-lodge penalty", size=92),
        "FTL penalty from July 2026: $364 per 28 days outstanding, up to $1,820. An agent lodges on time and talks to the ATO if something goes wrong."), 4.5),
 (point(b, 3, "They [[structure]] your future",
        steps(b, ["Sole trader vs company vs trust", "Super contributions strategy", "GST registration timing", "PAYG instalment forecasting"], start=0.6, gap=0.22),
        "The structure you start with shapes every year that follows. For complex moves — trusts, companies, Div 7A — it's worth paying a registered adviser to set it up properly."), 5.0),
 (end(b, "The best time to get advice is [[before]] you need it.", "SAVE + SHARE WITH A FELLOW TRADIE", size=108), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
