"""RP-32 Reel: 5 tax mistakes employees make (easy to fix). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (listloop(b, "5 tax mistakes employees make — and how to fix them", "RETURN POLICY · EASY FIXES", [
     ("Claiming without receipts", "NO PROOF = NO CLAIM", "the ATO can ask for records up to 5 years later"),
     ("Missing the new $1,000 work deduction", "STANDARD DEDUCTION", "from 2026–27: up to $1,000 automatic, no receipts needed"),
     ("Ignoring carry-forward super", "BALANCE UNDER $500K?", "if super balance under $500K at prior 30 June you may carry unused cap"),
     ("Not deducting last year's tax agent fee", "DEDUCTIBLE", "this year's return claims *last* year's tax agent fee — yes, really"),
     ("Forgetting interest on investment loans", "IF INCOME EARNED", "interest on a loan used to earn taxable income is deductible"),
   ], head="RETURN POLICY · COMMON MISTAKES", foot="Every item checked ato.gov.au · 2026–27 income year.", title_size=80, row_size=36), 11.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
