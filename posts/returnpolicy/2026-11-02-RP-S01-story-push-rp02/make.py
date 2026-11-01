"""RP-S01 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "returnpolicy/2026-11-02-RP-02-claimable-office/1.jpg")
if __name__ == "__main__":
    render_story(rp_push('Is it claimable? Office workers.', '6 things people try to claim. Guess before you swipe.', COVER), __file__)
