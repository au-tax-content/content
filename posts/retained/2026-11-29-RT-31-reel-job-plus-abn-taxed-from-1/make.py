"""RT-31 Reel: Job + ABN: side income is taxed from the first dollar. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "Job + ABN? Side income is taxed from [[$1.]]", "FIRST-YEAR ABN", "green", size=136), 3.0),
 (point(b, 1, "One [[threshold,]] not two",
        big(b, "$18,200", "PER PERSON", size=170),
        "The tax-free threshold applies once, across all your income. Your salary usually uses it up."), 4.6),
 (point(b, 2, "It [[stacks]] on top",
        steps(b, ["Salary: $80,000", "ABN profit: $20,000", "Tax on the $20K: about $6,400"], start=0.7, gap=0.3),
        "The extra $20,000 sits in the 30% bracket, plus the 2% Medicare levy. Nobody withholds it for you.", wave=True), 4.8),
 (point(b, 3, "What [[helps]]",
        steps(b, ["Claim real business costs", "About 32c per $1 goes to tax", "SB offset: up to $1,000"], start=0.7, gap=0.3),
        "Deductions come off the profit before it's taxed. The offset then reduces the tax itself."), 4.8),
 (end(b, "New ABN. Same [[tax-free]] threshold.", "SEND TO A SIDE-HUSTLER"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
