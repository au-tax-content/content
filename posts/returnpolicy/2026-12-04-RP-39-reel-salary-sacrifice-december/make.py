"""RP-39 Reel: Salary sacrifice this December. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "December is the [[best time]] to set up salary sacrifice", "RETURN POLICY · SUPER STRATEGY", "yellow", size=112), 3.0),
 (point(b, 1, "What [[salary sacrifice]] actually does",
        big(b, "15%", "tax on contributions in the fund", size=120),
        "You redirect part of your pre-tax salary into super. That portion is taxed at 15% inside the fund instead of your marginal income tax rate. At 30% marginal, you save 15 cents on every dollar."), 4.5),
 (point(b, 2, "Check your room before [[December]] ends",
        big(b, "$32,500", "total concessional cap 2026–27", size=104),
        "Your cap includes your employer's SG contributions (12% of your salary). Log into myGov or your super fund to see how much room you have. What's left is what you can still salary sacrifice this year."), 4.5),
 (point(b, 3, "How to [[set it up]]",
        steps(b, ["Contact your employer's payroll team", "Complete a salary sacrifice agreement", "Confirm how much per pay period", "Check it appears on your payslip"], start=0.6, gap=0.22),
        "Some employers offer salary sacrifice for super automatically. Others need a written request. It must be agreed before you earn the income — you can't salary sacrifice income you've already received."), 5.0),
 (end(b, "Start now. The year ends in [[6 weeks.]]", "SAVE + TAG SOMEONE WHO EARNS A SALARY", size=116), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
