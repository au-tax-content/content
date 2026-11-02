"""Trial Reel re-cut of RT-03 (carousel → 9:16 Reel for non-follower reach)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, "brand")); import carousel_reel as c
c.render(os.path.join(ROOT, "posts/retained/2026-11-02-RT-03-first-year-surprises"), HERE, top='New ABN? Nobody warns you about these.', hl=(201, 161, 95))
