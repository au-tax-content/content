"""RT-S02 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "retained/2026-11-04-RT-04-reel-pay-less-tax/cover.jpg")
if __name__ == "__main__":
    render_story(rt_push('3 legal ways business owners pay less tax.', 'Save it for June.', COVER, 'NEW REEL'), __file__)
