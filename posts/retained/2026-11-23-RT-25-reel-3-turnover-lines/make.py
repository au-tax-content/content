"""RT-25 Reel: 3 turnover lines that change your tax. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "[[3]] turnover lines that change your tax.", "2026–27", "navy", size=140), 3.0),
 (point(b, 1, "[[$75,000:]] GST switches on",
        big(b, "21", "DAYS TO REGISTER", size=210),
        "That's turnover (sales), not profit. Reach $75,000 and GST registration is compulsory.", title_size=104), 4.6),
 (point(b, 2, "Under [[$5M:]] the offset",
        big(b, "$1,000", "OFF YOUR TAX", size=180),
        "Sole traders and partners get the small business tax offset: 16% of the tax on business income, capped at $1,000.", wave=True, title_size=104), 4.6),
 (point(b, 3, "Under [[$10M:]] the write-offs",
        steps(b, ["$20K instant asset write-off", "12-month prepayment rule"], start=0.7, gap=0.3),
        "Both are small business concessions. Go past $10 million in turnover and they fall away.", title_size=104), 4.6),
 (end(b, "Watch [[turnover,]] not just profit.", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
