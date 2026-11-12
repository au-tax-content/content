"""RT-14 crayon carousel: 5 things new business owners get backwards ("X. Not Y."). Run: python3 make.py
Art: Canva generate-image (crayon, no text; recurring cafe-owner character) -> working canvas sheet -> art/*.png."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "brand"))
from crayon import two_panel, render
A = lambda n: os.path.join(HERE, "art", n + ".jpg")
S = [
 ("1", "AN <r>$18,000</r> WRITE-OFF CUTS A COMPANY'S TAX BY ABOUT <r>$4,500.</r>", "NOT <r>$18,000.</r>", "25% BASE RATE ENTITY · 2026–27"),
 ("2", "YOU REGISTER FOR GST AT<br><r>$75K</r> OF TURNOVER.", "NOT <r>$75K OF PROFIT.</r>", "GST TURNOVER · REGISTER WITHIN 21 DAYS"),
 ("3", "THE <r>$20K</r> WRITE-OFF LIMIT APPLIES TO <r>EACH ASSET.</r>", "NOT <r>ONE ASSET A YEAR.</r>", "TURNOVER UNDER $10M · FROM 1 JULY 2026"),
 ("4", "<r>$1 OF EVERY $11</r><br>AT THE TILL IS GST.", "NOT <r>YOURS TO SPEND.</r>", "GST-REGISTERED · TAXABLE SALES · 10% GST"),
 ("5", "YOUR STAFF GET <r>12% SUPER</r><br>PAID FOR THEM.", "NOT <r>THEIR SOLE TRADER BOSS.</r>", "SUPER GUARANTEE · 2026–27"),
]
slides = [two_panel(A(k + "a"), t, A(k + "b"), b, n=i, of=len(S), note=note, top_size=72) for i, (k, t, b, note) in enumerate(S, 1)]
if __name__ == "__main__":
    render(slides, __file__)
