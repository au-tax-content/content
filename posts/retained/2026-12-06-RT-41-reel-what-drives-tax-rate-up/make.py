"""RT-41 Reel: What drives your tax rate up faster than your income. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Why your [[tax rate]] rises faster than your income", "RETAINED · HOW MARGINAL RATES WORK", "green", size=108), 3.0),
 (point(b, 1, "[[Marginal]] rates are not flat",
        big(b, "30c → 37c", "at $135,000 profit", size=104),
        "You don't pay 37% on everything. You pay 30c on dollars between $45K and $135K, then 37c on each dollar above $135K. Only the top slice gets the top rate. But the slice grows fast."), 4.5),
 (point(b, 2, "[[Medicare]] adds to every dollar",
        big(b, "+2%", "on taxable income above the threshold", size=104),
        "Medicare levy is 2% of taxable income, on top of income tax. No marginal effect — it applies across the board. No private hospital cover? Add up to 1.5% more if income exceeds $105,000 (singles)."), 4.5),
 (point(b, 3, "[[Offsets]] phase out as you earn more",
        steps(b, ["LITO: $700 → $0 by $66,667", "Small biz offset: capped at $1,000", "Div 293 super tax kicks in at $250,000", "Company retains profit at 25% — not released"], start=0.55, gap=0.22),
        "The Low Income Tax Offset disappears as your income rises. The more you earn, the fewer buffers you have. Each dollar above $66,667 carries the full marginal rate — no offset left."), 5.0),
 (end(b, "Understand the rate. [[Plan]] around it.", "SAVE + SHARE WITH YOUR BUSINESS PARTNER", size=116), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
