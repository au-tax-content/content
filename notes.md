# Notes: what's working (newest first)

## 2 Nov 2026: traction push (Daniel: "find a way to start getting traction")

- Day-3 stats: 0 followers on both accounts (Retained 2 posts, Return Policy 1); reach 0 on every post; the only comments are spam bots. Carousels on accounts with no followers get no distribution.
- **Change:** Reels-first via **trial Reels** (non-followers first, auto-share to followers on performance). `scripts/publish.py` now sends `trial_params` for `"trial": true` Reels, with a fallback to a normal Reel. New `brand/carousel_reel.py` re-cuts any carousel into a 9:16 Reel with a hook band.
- **Queued:** RP-02R (Tue 3 Nov 12:30), RT-03R (Tue 12:45), RP-03R (Wed 4 Nov 12:30), RT-05R (Sat 7 Nov 12:30), RP-05R (Mon 9 Nov 12:30). RT-04 and RP-04 switched to trial. That's 7 Reels this week instead of 2.
- **Check on 8 Nov:** did `trial_used` come back true? Reach on the R posts vs the carousels they came from.

## November 2026 monthly summary (first Sunday)

- **Followers:** Retained 0, Return Policy 0 (accounts live 30 Oct). Posts out: 1 (RT-01, 31 Oct). Too early for best/worst: RT-01 has 1 like and 1 spam comment, reach not reported yet.
- **What changes in November:** Return Policy starts (brand kit, Docket mascot, RP-01–05, a story every day). Both accounts lead with the "pay less / keep more, legally" pillar. First experiments run this week. Lead magnets must be built this month for the December promise.

## 1 Nov 2026: weekly run (week of 2–8 Nov)

**Scorecard (last week):** RT-01 Start here (31 Oct): reach 0 so far, 1 like, 1 comment (spam, ignore), 0 saves/shares/follows. Followers: Retained 0, Return Policy 0. Nothing published on Return Policy yet. No failed or skipped posts. RT-02 (today 5 pm) and RT-03 (Mon) still queued.

**Built this run:**
- `brand/returnpolicy_kit.py` (receipt look from the launch canvas + brand tokens: Space Grotesk, cream/ink, refund green, highlighter, stamps, torn receipts) and **Docket**, Return Policy's original receipt mascot (`receipt_mascot()`, same animation hooks as Penny; `dark=True` gives cream limbs on ink/green grounds).
- `brand/motion.py`: `scene_rp()` for Return Policy Reels, `words(..., hl_bg, hl_fg)`. Note `[[…]]` highlights one word only: write `[[2]] [[years]]`, not `[[2 years]]` (RT-04's "[[30 June]]" and "[[12 months]]" don't highlight).
- `brand/stories.py`: story templates for both accounts (`rp_push`, `rp_tip`, `rt_push`, `rt_tip`, `render_story`). Space Grotesk font added to `brand/fonts/`.
- Highlight gotcha: a highlight on line 2 paints over line 1's descenders (g, y, p). RP kit's `hl()` now starts the fill 18% down; in `bold.py` use line-height ≥1.14 on headlines with `hl()`.

**Queued:**
- Return Policy: RP-01 Start here (Sun 1 Nov 7:30 pm), RP-02 Is it claimable? office workers (Mon 7 pm), RP-03 Same $90K, $3,200 less tax (Tue 7 pm), RP-04 Reel: forgot a deduction? amend (Thu 7:30 pm), RP-05 The $1,000 standard deduction (Sun 8 Nov 4:30 pm). Stories daily Mon–Sun (RP-S01–S07: 4 post pushes, 3 tips).
- Retained: RT-03 (Mon, already queued), RT-04 Reel (Wed, already queued), RT-05 How business owners use super to pay less tax (Fri 7:30 pm). Stories Mon/Wed/Fri pushes (RT-S01–S03).

**Decisions / watch-outs:**
- **Big legislated change to know before any CGT or negative gearing post:** a secondary source says the Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Royal Assent 26 June 2026) replaces the 50% CGT discount with cost-base indexation for gains accruing from 1 July 2027 (30% minimum tax on gains for individuals) and stops residential rental losses offsetting other income from 2027–28 (new builds and properties bought before 7:30 pm 12 May 2026 exempt). The ATO's new-legislation index still shows these as "announced". Verify on ato.gov.au before using; never present the CGT discount as permanent. Strong "news decoded" candidate for Return Policy landlords once verified. Also listed there: a new "Working Australians tax offset" (announced).
- 2026–27 figures in use: rates 15%/30%/37%/45% (thresholds $18,200/$45,000/$135,000/$190,000), concessional cap $32,500, standard deduction $1,000.
- Comment shortlist: already published for the week of 1 Nov (engage.json unchanged since 31 Oct), not rebuilt.
- **Carried over, top priority:** lead magnets (New ABN Starter Kit, The Claim Sheet) in `leadmagnets/`, then the Kit form steps for Daniel. Not built this run; must be done by the 8 Nov run at the latest to make December.

## 1 Nov 2026: Kit account ready

- Daniel created a free Kit account (name "Retained", retained.au@gmail.com), confirmed the email and added a mailing address. No forms yet.
- **Priority this week:** build both lead magnets (New ABN Starter Kit, The Claim Sheet) as PDFs in `leadmagnets/`, then send Daniel one short list of steps to create two Kit forms (tags Retained / Return Policy, incentive email with the PDF, double opt-in) and ask him to send back each form's embed code. Then build the GitHub Pages signup pages and switch `keyword_replies` to "link in bio".

## 1 Nov 2026: direction change

- Daniel wants the content to lead with "how to legally pay less tax / keep more" (Karlton Dennis-style framing). See "Content direction" in CLAUDE.md.
- Reels are now possible (brand/reel.py). RT-04 Reel "3 legal ways business owners pay less tax" queued for Wed 4 Nov 7:30 pm. Count it as Retained's Reel for the week of 2 Nov.

## 31 Oct 2026: setup

- Accounts live since 30 Oct 2026, 0 posts. Automation built: publisher, stats, token refresh.
- Queued: Retained foundation posts pulled forward so the grid fills fast: RT-01 (Sat 31 Oct 7 pm), RT-02 (Sun 1 Nov 5 pm), RT-03 (Mon 2 Nov 7:30 pm). Regular Retained cadence starts after RT-03.
- Return Policy has no posts yet: queue RP-01–03 as soon as possible (one a day from the next day you can), then the regular cadence.
- To do: Return Policy foundation posts (RP-01..03) and the Return Policy brand kit; story templates (1080×1920); Starter Kit and Claim Sheet lead magnets plus ManyChat/email (phase 2, by early Dec).
- Correction learned: the small business income tax offset is 16% (capped at $1,000) from 2021–22, not 8%. The old content pipeline spreadsheet still has 8% in RT-02; don't reuse its figures without checking.
- The content pipeline spreadsheet (Instagram_Content_Pipeline.xlsx, 28 posts for 3–30 Nov) lives outside this repo; its hooks are a starting point, but re-verify every figure.
- No stats yet. Story stats need 5+ viewers before Instagram reports them.
