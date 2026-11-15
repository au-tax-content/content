"""RP-22 Reel: 5 signs that 'ATO' message is a scam. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, card, listloop, tier, tier_len, ladder, buckets, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (listloop(b, "5 signs that [[“ATO”]] text is a [[scam]]", "SEND THIS TO YOUR PARENTS", [
     ("It has a link in it", "SCAM", "the ATO doesn't send unsolicited SMS links"),
     ("It wants your myGov login", "SCAM", "or your TFN or bank details by email"),
     ("It threatens arrest", "SCAM", "or demands you stay on the line"),
     ("Pay by gift card or crypto", "SCAM", "the ATO never asks for these"),
     ("A fee to release your refund", "SCAM", "refunds never cost money"),
   ], head="RETURN POLICY · SCAM CHECK", foot="Not sure? Don't reply. Call the ATO on 1800 008 540.", tag_color="#C2361F"), 10.0),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
