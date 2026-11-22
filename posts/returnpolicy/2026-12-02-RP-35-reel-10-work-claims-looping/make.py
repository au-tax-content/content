"""RP-35 Reel: 10 work claims employees miss every year. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (listloop(b, "10 work claims employees miss every year", "RETURN POLICY · THE SAVE-WORTHY LIST", [
     ("Work-from-home running costs", "CHECK RATE", "electricity, internet — keep an hourly record; check ato.gov.au for 2026–27 rate"),
     ("Union & professional memberships", "DEDUCTIBLE", "if related to earning your income"),
     ("Self-education to advance your career", "DEDUCTIBLE", "must relate to your *current* role, not a new one"),
     ("Tools and equipment under $300", "IMMEDIATE", "full deduction if used >50% for work; over $300 depreciate"),
     ("Phone and internet work portion", "DEDUCTIBLE", "must apportion; keep 4-week diary as evidence"),
     ("Income protection insurance", "OUTSIDE SUPER", "deductible if paid personally, not via super fund"),
     ("Tax agent fees from last year", "DEDUCTIBLE", "this year you claim last year's fee — save every invoice"),
     ("Occupation-specific clothing", "DEDUCTIBLE", "uniforms, PPE, protective gear — keep receipts"),
     ("Work-related car trips", "CENTS PER KM", "between work sites; not home to work — check current rate"),
     ("Personal super contributions", "CHECK CAPS", "salary sacrifice or personal; deductible if notice given to fund"),
   ], head="RETURN POLICY · 10 CLAIMS", foot="All items checked ato.gov.au · 2026–27 income year.", title_size=86, row_size=34), 14.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
