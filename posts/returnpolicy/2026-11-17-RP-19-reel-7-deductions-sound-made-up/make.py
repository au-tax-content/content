"""RP-19 Reel: 7 deductions that sound made up (but are legal). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (listloop(b, "7 deductions that sound [[made]] [[up]] (but are legal)", "EMPLOYEES · CONDITIONS APPLY", [
     ("Sunscreen", "OUTDOOR JOBS", "if you work in the sun for long periods"),
     ("Sunglasses + a hat", "OUTDOOR JOBS", "work use only: split out private use"),
     ("Your tax agent's fee", "CLAIM", "registered agent, claimed in next year's return"),
     ("Washing your uniform", "$1 A LOAD", "a real uniform, not plain black pants"),
     ("Union + membership fees", "CLAIM", "on top of the $1,000 standard deduction"),
     ("Income protection cover", "CLAIM", "premiums you pay yourself"),
     ("Donations of $2+", "CLAIM", "to a registered charity, nothing in return"),
   ], head="RETURN POLICY · CLAIM CHECK", title_size=88), 11.5),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
