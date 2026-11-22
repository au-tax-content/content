"""RT-33 Reel: 3 moves wealthy Australians use to pay less tax (legally). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "3 moves wealthy Australians use to [[legally]] pay less tax", "RETAINED · LEGAL STRATEGY", "brass", size=120), 3.0),
 (point(b, 1, "Max out [[concessional super]]",
        big(b, "$32,500", "cap per year", size=104),
        "Contributions taxed at 15% in the fund instead of your marginal rate. At 37%, that's a 22-point gap. Catch: locked until preservation age."), 4.5),
 (point(b, 2, "[[Structure]] the business right",
        big(b, "25% vs 45%", "company vs personal rate", size=96),
        "A company pays 25% (turnover under $50M). A sole trader can pay up to 47% with Medicare. The gap widens as profit rises. Worth a registered adviser to set up.", wave=True), 4.5),
 (point(b, 3, "Write off assets under [[$20K]]",
        big(b, "$20,000", "per asset, full year", size=104),
        "Deduct in the year the asset is first used or installed — not over several years. Must be for business use. Permanent from 1 July 2026 for turnover under $10M."), 4.5),
 (end(b, "Timing, structure, deductions. [[All legal.]]", "SAVE + SEND TO YOUR ACCOUNTANT", size=116), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
