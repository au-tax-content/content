"""RP-S04 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "returnpolicy/2026-11-05-RP-04-reel-amend/cover.jpg")
if __name__ == "__main__":
    render_story(rp_push('Forgot a deduction? You can still claim it.', 'Most people have 2 years to amend.', COVER, 'NEW REEL'), __file__)
