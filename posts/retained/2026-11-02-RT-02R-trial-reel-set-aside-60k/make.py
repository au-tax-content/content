"""Trial Reel re-cut of RT-02."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, "brand")); import carousel_reel as c
c.render(os.path.join(ROOT, "posts/retained/2026-11-01-RT-02-set-aside-60k"), HERE, top='$60K profit. How much do you set aside?', hl=(201, 161, 95))
