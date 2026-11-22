"""RT-36 Reel: Company or sole trader? Here's what changes your tax. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Company or sole trader? This is what changes your [[tax]]", "RETAINED · STRUCTURE BASICS", "navy", size=120), 3.0),
 (point(b, 1, "[[Sole trader:]] you pay at your rate",
        big(b, "up to 47%", "income tax + Medicare levy", size=104),
        "All profit flows to your personal return. If you earn $120K profit, you're in the 30% bracket — plus 2% Medicare. No corporate buffer."), 4.5),
 (point(b, 2, "[[Company:]] flat 25% on profit",
        big(b, "25%", "base rate entity tax", size=120),
        "Turnover under $50M, passive income ≤ 80%: 25% rate. The profit that stays in the company isn't taxed again until paid out. Watch Division 7A.", wave=True), 4.5),
 (point(b, 3, "The [[catch]] with a company",
        steps(b, ["Setup cost: $500–$1,500+", "Ongoing ASIC fees each year", "Must pay yourself properly (wages or div)", "Division 7A applies to loans from the company"], start=0.6, gap=0.22),
        "A company makes sense at higher profit levels. For most sole traders under $80K, the small business tax offset and super contributions do the job. Talk to a registered adviser."), 5.0),
 (end(b, "Structure shapes every dollar. Get it [[right.]]", "SAVE + SEND TO YOUR ACCOUNTANT", size=116), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
