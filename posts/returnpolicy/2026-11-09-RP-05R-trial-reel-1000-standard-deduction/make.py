"""Trial Reel re-cut of RP-05 (carousel → 9:16 Reel for non-follower reach)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, "brand")); import carousel_reel as c
c.render(os.path.join(ROOT, "posts/returnpolicy/2026-11-08-RP-05-1000-standard-deduction"), HERE, top='$1,000 off. No receipts needed.', hl=(255, 226, 77))
