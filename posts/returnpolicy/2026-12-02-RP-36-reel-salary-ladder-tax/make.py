"""RP-36 Reel: Exact tax at $60K, $80K, $100K, $120K — 2026-27. Run: python3 make.py"""
# Tax calc 2026-27 (verified figures.md 15 Nov 2026):
# Rates: nil to $18,200; 15c to $45,000; $4,020+30c to $135,000; $31,020+37c to $190,000; 45% above
# LITO: $700 to $37,500; less 5c/$1 to $45,000 ($325); less 1.5c/$1 to $66,667; then $0
# Medicare levy: 2% of taxable income (no surcharge at these incomes)
# $60K: IT=$8,520; ML=$1,200; LITO=$100 → NET $9,620
# $80K: IT=$14,520; ML=$1,600; LITO=$0 (phases out at $66,667) → NET $16,120
# $100K: IT=$20,520; ML=$2,000; LITO=$0 → NET $22,520
# $120K: IT=$26,520; ML=$2,400; LITO=$0 → NET $28,920
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (ladder(b, "Exact [[tax]] on your salary — 2026–27", "RETURN POLICY · WHAT DOES THE ATO TAKE?", [
     ("$60,000", 9_620, "income tax $8,520 + Medicare $1,200 − LITO $100 = $9,620"),
     ("$80,000", 16_120, "income tax $14,520 + Medicare $1,600 (LITO phases out at $66,667)"),
     ("$100,000", 22_520, "income tax $20,520 + Medicare $2,000 − no LITO above $66,667"),
     ("$120,000", 28_920, "income tax $26,520 + Medicare $2,400 − no LITO above $66,667"),
   ], "No HELP debt, no surcharge. LITO applied. Medicare levy 2%. Verify on ato.gov.au · 2026–27.", pre="$", post=" tax", title_size=88), 10.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
