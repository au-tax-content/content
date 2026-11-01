"""One-off: build the week-of-2-Nov-2026 stories (folders, make.py, 1.jpg, post.json)."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(ROOT, "posts", *a)

STORIES = [
 ("returnpolicy", "2026-11-02", "RP-S01", "push-rp02", "2026-11-02T20:15:00+11:00",
  "rp_push('Is it claimable? Office workers.', '6 things people try to claim. Guess before you swipe.', COVER)", "returnpolicy/2026-11-02-RP-02-claimable-office/1.jpg", []),
 ("returnpolicy", "2026-11-03", "RP-S02", "push-rp03", "2026-11-03T20:15:00+11:00",
  "rp_push('Same $90K. $3,200 less income tax.', 'How salary sacrifice works, and the catch.', COVER)", "returnpolicy/2026-11-03-RP-03-same-salary-less-tax/1.jpg",
  ["2026-27 tax and Medicare figures as in RP-03"]),
 ("returnpolicy", "2026-11-04", "RP-S03", "tip-agent-fee", "2026-11-04T19:30:00+11:00",
  "rp_tip('TAX AGENT FEES', 'Claimable.', 'Paid a registered tax agent for last year\\'s return? Claim it in the year you paid it.', 'CLAIMABLE', GREEN)", None,
  ["Cost of managing tax affairs: registered agent fees deductible in the year paid (ATO, checked 1 Nov 2026)"]),
 ("returnpolicy", "2026-11-05", "RP-S04", "push-rp04", "2026-11-05T20:15:00+11:00",
  "rp_push('Forgot a deduction? You can still claim it.', 'Most people have 2 years to amend.', COVER, 'NEW REEL')", "returnpolicy/2026-11-05-RP-04-reel-amend/cover.jpg",
  ["Amendment time limit generally 2 years for individuals (ATO, checked 1 Nov 2026)"]),
 ("returnpolicy", "2026-11-06", "RP-S05", "tip-black-pants", "2026-11-06T19:30:00+11:00",
  "rp_tip('PLAIN BLACK WORK PANTS', 'Nope.', 'Conventional clothing isn\\'t deductible, even if you only ever wear it to work.', 'NOT CLAIMABLE', RED)", None,
  ["Conventional clothing not deductible (ATO public servant toolkit / clothing page, checked 1 Nov 2026)"]),
 ("returnpolicy", "2026-11-07", "RP-S06", "tip-laundry", "2026-11-07T12:30:00+11:00",
  "rp_tip('LAUNDRY · FROM 1 JULY 2026', '$1 a load.', 'Work clothes only. Mixed loads: 50c. For your 2026–27 return.', bg=PAPER2)", None,
  ["Laundry $1/load work clothes, 50c mixed, from 1 July 2026 (ATO standard deduction page, updated 14 Sep 2026, checked 1 Nov 2026)"]),
 ("returnpolicy", "2026-11-08", "RP-S07", "push-rp05", "2026-11-08T17:15:00+11:00",
  "rp_push('$1,000 off. No receipts.', 'The new standard deduction, decoded.', COVER)", "returnpolicy/2026-11-08-RP-05-1000-standard-deduction/1.jpg",
  ["$1,000 standard deduction from 2026-27 (ATO, checked 1 Nov 2026)"]),
 ("retained", "2026-11-02", "RT-S01", "push-rt03", "2026-11-02T20:30:00+11:00",
  "rt_push('5 tax surprises in your first year on an ABN.', 'Number 3 catches almost everyone.', COVER)", "retained/2026-11-02-RT-03-first-year-surprises/1.jpg", []),
 ("retained", "2026-11-04", "RT-S02", "push-rt04", "2026-11-04T20:30:00+11:00",
  "rt_push('3 legal ways business owners pay less tax.', 'Save it for June.', COVER, 'NEW REEL')", "retained/2026-11-04-RT-04-reel-pay-less-tax/cover.jpg", []),
 ("retained", "2026-11-06", "RT-S03", "push-rt05", "2026-11-06T20:30:00+11:00",
  "rt_push('How business owners use super to pay less tax.', '$120K profit, $20K into super: about $3,400 kept.', COVER)", "retained/2026-11-06-RT-05-super-pay-less-tax/1.jpg",
  ["As RT-05 (2026-27 rates, 15% contributions tax)"]),
]

for acct, date, sid, slug, when, call, cover, figs in STORIES:
    folder = P(acct, f"{date}-{sid}-story-{slug}")
    os.makedirs(folder, exist_ok=True)
    cov = f'COVER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "{cover}")\n' if cover else ""
    open(os.path.join(folder, "make.py"), "w").write(f'''"""{sid} story. Run: python3 make.py"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "brand"))
from stories import *
from returnpolicy_kit import GREEN, RED, PAPER2
{cov}if __name__ == "__main__":
    render_story({call}, __file__)
''')
    subprocess.run([sys.executable, "make.py"], cwd=folder, check=True)
    json.dump({"id": sid, "account": acct, "type": "story", "series": "Story", "pillar": "Story", "publish_at": when,
               "caption": "", "images": ["1.jpg"], "figures_checked": figs, "status": "queued"},
              open(os.path.join(folder, "post.json"), "w"), indent=2, ensure_ascii=False)
