"""RP-S05 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
if __name__ == "__main__":
    render_story(rp_tip('PLAIN BLACK WORK PANTS', 'Nope.', 'Conventional clothing isn\'t deductible, even if you only ever wear it to work.', 'NOT CLAIMABLE', RED), __file__)
