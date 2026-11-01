"""RP-S03 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
if __name__ == "__main__":
    render_story(rp_tip('TAX AGENT FEES', 'Claimable.', 'Paid a registered tax agent for last year\'s return? Claim it in the year you paid it.', 'CLAIMABLE', GREEN), __file__)
