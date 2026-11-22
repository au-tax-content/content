"""RP-37 Reel: 2 jobs? Here's exactly how your tax works. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook_c(b, "2 jobs? Here's [[exactly]] how your tax works", "RETURN POLICY · THE 2-JOB RULE", "mint", size=120), 3.0),
 (point(b, 1, "The [[tax-free threshold]] is claimed once",
        big(b, "$18,200", "one job only", size=112),
        "You can only claim the tax-free threshold from one employer. Your second employer must withhold tax at the higher rate — no tax-free threshold. This is on your Tax File Number declaration."), 4.5),
 (point(b, 2, "Income from [[both jobs]] is added together",
        big(b, "combined income", "= your tax bracket", size=96),
        "The ATO taxes your total income, not each job separately. If Job 1 is $60K and Job 2 is $20K, you're taxed as if you earned $80K. The second employer often withholds too little — leading to a tax bill at return time."), 4.5),
 (point(b, 3, "Fix it: [[voluntary PAYG]] withholding",
        steps(b, ["Ask second employer to withhold extra", "Or log into myGov and enter a PAYG instalment", "Track both payment summaries at tax time", "No penalties if you pay the right total"], start=0.6, gap=0.22),
        "You can ask your second employer to withhold more tax each pay. It avoids a surprise bill in July. The ATO's tax withheld calculator on ato.gov.au helps you work out the right amount."), 5.0),
 (end(b, "Two jobs, one tax bracket. [[Know the rules.]]", "SAVE + TAG A FRIEND WITH A SIDE JOB", size=116), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
