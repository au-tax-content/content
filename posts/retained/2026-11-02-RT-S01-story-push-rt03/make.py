"""RT-S01 story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "retained/2026-11-02-RT-03-first-year-surprises/1.jpg")
if __name__ == "__main__":
    render_story(rt_push('5 tax surprises in your first year on an ABN.', 'Number 3 catches almost everyone.', COVER), __file__)
