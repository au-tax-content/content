"""Trial Reel re-cut of RP-03 (carousel → 9:16 Reel for non-follower reach)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, "brand")); import carousel_reel as c
c.render(os.path.join(ROOT, "posts/returnpolicy/2026-11-03-RP-03-same-salary-less-tax"), HERE, top='Same salary. One pays $3,200 less.', hl=(255, 226, 77))
