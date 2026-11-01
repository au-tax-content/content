"""RP-S06 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
if __name__ == "__main__":
    render_story(rp_tip('LAUNDRY · FROM 1 JULY 2026', '$1 a load.', 'Work clothes only. Mixed loads: 50c. For your 2026–27 return.', bg=PAPER2), __file__)
