"""RT-16 Reel: The small business income tax offset — $1,000 back. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel_formats import hook_c, point, end, big, stamp_el, steps, render_motion
b = "rt"
scenes = [
 (hook_c(b, "The government gives sole traders [[money]] [[back.]] Most don't claim it.", "SAVE THIS", "brass", size=118), 3.0),
 (point(b, 1, "The [[small business]] offset",
        big(b, "$1,000", "MAX · 2026–27", size=170),
        "16% of tax on your net small business income. Max $1,000. Turnover under $5M."), 4.5),
 (point(b, 2, "Who [[qualifies]]",
        steps(b, ["✓ Sole traders", "✓ Partners in a small business", "✗ Companies", "✗ Trusts"], start=0.7, gap=0.20),
        "Only the individual gets it — not the entity. The business must be a small business entity."), 4.5),
 (point(b, 3, "How to [[claim]] it",
        stamp_el(b, "TICK THE BOX", 0.9, size=58),
        "It's calculated in your individual tax return. Your accountant does this automatically — but check.", wave=True), 4.5),
 (end(b, "Legal. Boring. [[Worth]] claiming every year.", "SAVE THIS FOR TAX TIME"), 3.2),
]
if __name__ == "__main__":
    render_motion(scenes, __file__, cover_scene=0, cover_y=215)
