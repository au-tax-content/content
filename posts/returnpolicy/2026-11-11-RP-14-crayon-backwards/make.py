"""RP-14 crayon carousel: 5 tax facts most people have backwards ("X. Not Y."). Run: python3 make.py
Art: Canva generate-image (crayon, no text) -> working canvas sheet -> art/*.png. Slide 3 uses the approved mock panels."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "brand"))
from crayon import two_panel, render
A = lambda n: os.path.join(HERE, "art", n + ".jpg")
S = [
 ("1", "A <r>$1,000</r> DEDUCTION SAVES YOU ABOUT <r>$300.</r>", "NOT <r>$1,000.</r>", "30% TAX RATE · 2026–27"),
 ("2", "A HIGHER TAX BRACKET TAXES YOUR <r>NEXT DOLLAR.</r>", "NOT <r>EVERY DOLLAR.</r>", "2026–27 RATES"),
 ("3", "MOST PEOPLE HAVE <r>2 YEARS</r> TO FIX THEIR TAX RETURN.", "NOT <r>2 DAYS.</r>", "INDIVIDUALS · FROM YOUR NOTICE OF ASSESSMENT"),
 ("4", "SUPER YOU SALARY SACRIFICE IS TAXED AT <r>15%.</r>", "NOT <r>30%.</r>", "WITHIN THE $32,500 CAP · 2026–27"),
 ("5", "A WORK-FROM-HOME CLAIM NEEDS <r>A RECORD OF YOUR HOURS.</r>", "NOT <r>A GUESS.</r>", "FIXED RATE METHOD"),
]
slides = [two_panel(A(k + "a"), t, A(k + "b"), b, n=i, of=len(S), note=note) for i, (k, t, b, note) in enumerate(S, 1)]
if __name__ == "__main__":
    render(slides, __file__)
