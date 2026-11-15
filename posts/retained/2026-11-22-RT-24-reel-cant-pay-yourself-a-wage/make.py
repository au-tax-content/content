"""RT-24 Reel: Sole trader? You can't pay yourself a wage. Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Sole trader? You [[can't]] pay yourself a wage.", "MYTH BUSTED", "brass", size=136), 3.0),
 (point(b, 1, "It's all [[one]] pocket",
        stamp_el(b, "DISTRIBUTION OF PROFIT", 0.9, size=46),
        "The ATO treats any 'wage' a sole trader pays themselves as a distribution of profit. It isn't a business deduction."), 4.6),
 (point(b, 2, "You're taxed on [[profit]]",
        steps(b, ["Income − expenses = profit", "Profit = your taxable income", "Whether you spend it or not"], start=0.7, gap=0.3),
        "Take out $500 a week or nothing at all: the tax is the same.", wave=True), 4.6),
 (point(b, 3, "What [[is]] deductible",
        big(b, "15%", "TAX IN THE FUND", size=200),
        "Your own super contributions. Sole traders can usually claim them in their personal return, up to the $32,500 cap (2026–27)."), 4.6),
 (end(b, "Draw from profit. Plan tax on [[profit.]]", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
