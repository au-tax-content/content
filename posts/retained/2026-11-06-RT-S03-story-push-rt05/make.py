"""RT-S03 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "retained/2026-11-06-RT-05-super-pay-less-tax/1.jpg")
if __name__ == "__main__":
    render_story(rt_push('How business owners use super to pay less tax.', '$120K profit, $20K into super: about $3,400 kept.', COVER), __file__)
