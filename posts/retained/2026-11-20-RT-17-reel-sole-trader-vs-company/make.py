"""RT-17 Reel: Sole trader vs company — when does the maths change? Narrated (vo/). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Same business. Different structure. The tax gap can hit [[5]] [[figures.]]", "SAVE THIS", "green", size=118), 3.0),
 (point(b, 1, "[[Sole trader:]] you pay at your rate",
        big(b, "45%", "TOP RATE · 2026–27", size=190),
        "Above $190,000 you pay 45% plus 2% Medicare levy. Every dollar of profit is taxed at your marginal rate."), 4.5),
 (point(b, 2, "[[Company:]] one flat rate",
        big(b, "25%", "BASE RATE · TURNOVER <$50M", size=175),
        "Base rate entity company: 25% (2026–27). Profit taxed in the company — but to access it personally, you pay dividends and franking credits apply.", wave=True), 4.5),
 (point(b, 3, "When the [[switch]] makes sense",
        stamp_el(b, "RATE GAP > COSTS", 0.9, size=50),
        "When your marginal rate significantly exceeds 25% and profits stay in the business. Factor in set-up, compliance, Division 7A, and paying yourself."), 4.5),
 (end(b, "Worth paying a registered adviser to [[set up properly.]]", "SAVE THIS"), 3.2),
]
if __name__ == "__main__":
    from voice import voiced_render
    voiced_render(scenes, __file__, cover_scene=0, cover_y=215)
