"""RT-04 Reel: 3 legal ways business owners pay less tax. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from reel import retained_card, render_reel

cards = [
    (retained_card("3 legal ways business owners pay less tax.", kicker="KEEP MORE", footer="Save this for June →", size=132), 2.8),
    (retained_card("Buy what you need before 30 June.", number="01", kicker="WRITE IT OFF",
                   sub="Assets under <b>$20,000</b> can be written off in full in the year they're used or installed ready for use. Turnover under $10M."), 4.5),
    (retained_card("Prepay up to 12 months.", number="02", kicker="TIMING",
                   sub="Small businesses can deduct prepaid rent, insurance or subscriptions this year if the service period is <b>12 months or less</b> and ends by next 30 June."), 4.8),
    (retained_card("Claim the small business offset.", number="03", kicker="SOLE TRADERS",
                   sub="Sole traders and partners in small businesses get <b>16%</b> off the tax on their business income, up to <b>$1,000</b> a year."), 4.5),
    (retained_card("Legal. Boring. Worth thousands.", kicker="FOLLOW", sub="Follow for the moves nobody tells you about.",
                   footer="General info only · Not personal advice", size=124), 3.0),
]

if __name__ == "__main__":
    render_reel(cards, __file__)
