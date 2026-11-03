"""RP-09 Reel: working from home fixed rate, 70c an hour (2025-26). Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_points import hook, point, end, big, stamp_el, steps, render_motion
b = "rp"
scenes = [
 (hook(b, "Work from home? [[70c]] an hour.", "2025–26 RETURNS · SAVE THIS"), 3.0),
 (point(b, 1, "[[70c]] per hour", big(b, "70c", "PER WORK HOUR", size=200), "Covers energy, phone, internet and stationery in one rate."), 4.4),
 (point(b, 2, "Log [[real]] hours", steps(b, ["TIMESHEET", "ROSTER", "DIARY"]) + stamp_el(b, "NO ESTIMATES", 1.3), "A record of the actual hours you worked from home, all year."), 4.6),
 (point(b, 3, "Claim on [[top]]", steps(b, ["LAPTOP (OVER ITS LIFE)", "DESK + CHAIR", "REPAIRS"]), "Equipment over $300 is claimed over its effective life.", wave=True), 4.6),
 (end(b, "Keep the [[log.]] Claim the hours.", "SAVE THIS", size=124), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0)
