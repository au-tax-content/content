"""RP-S02 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "returnpolicy/2026-11-03-RP-03-same-salary-less-tax/1.jpg")
if __name__ == "__main__":
    render_story(rp_push('Same $90K. $3,200 less income tax.', 'How salary sacrifice works, and the catch.', COVER), __file__)
