"""RP-S07 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "returnpolicy/2026-11-08-RP-05-1000-standard-deduction/1.jpg")
if __name__ == "__main__":
    render_story(rp_push('$1,000 off. No receipts.', 'The new standard deduction, decoded.', COVER), __file__)
