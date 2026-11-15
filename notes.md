# Notes: what's working (newest first)

## 15 Nov 2026 (night): voiceover on 12 Reels

- Daniel asked whether more posting alone will grow the accounts. Honest read: not by itself. Every Reel stalls near 100 reach, with 0 follows from posts. Agreed to test an Australian AI voice (Charlie, via vidIQ) after he rejected the free voice as too AI.
- 12 queued Reels now narrated (6 per account, 18–29 Nov), used 140 vidIQ credits this month (all of them; resets 3 Dec). Publisher keeps the voice and plays music quietly underneath when `voiceover: true`.
- Fixed crowded hook screens on RT-16, RP-16 and RT-17 (text ran into the tag and the mascot) from the earlier run.
- To do: add Reel watch time to insights.py so the voice test can be judged.

## 15 Nov 2026 (evening): content push on the stronger model (Daniel: "generate as much content as you can", model it on what gets views)

- Benchmark study (vidIQ outliers + `stats/benchmarks.json`): faceless winners are short looping lists ("7 deductions that sound illegal (but aren't)", up to 190x a creator's median), tier lists (6.2M), bracket explainers (1.5M), rule-change news (832K on an Australian tax account), "money waiting for you" and milestone reveals. Details in `refs/benchmark-notes.md`.
- New kit `brand/reel_formats.py`: list loop (receipt / ledger page), tier board, number ladder, bracket buckets, full-colour hook covers, news strap. motion.py now renders safely 4 at a time.
- Queued 28 new Reels (RP-18…31, RT-18…31): every day 16–29 Nov at 7:30 pm, plus 12:30 pm on Mon 16, Wed 18, Fri 20. With RT/RP-11, 16, 17 that's 17 Reels per account over two weeks. Every figure checked on ato.gov.au today (figures.md).
- New facts worth reusing: $300 no-receipt rule ended 1 July 2026; ATO credit cards extended to 30 June 2027; MLS $105K/$210K; HELP threshold $69,528; co-contribution $49,293/$64,293; $250 working Australians offset from 2027–28; Payday Super; $21B lost super.
- Experiment (both accounts, judge 23 Nov): list loops and tier lists vs 5-card motion Reels on reach and saves+shares per 1,000.
- Unsplash is blocked until Daniel confirms his email with Unsplash, so no photo backgrounds yet; covers use colour grounds instead.
- Next Sunday (22 Nov): score this week by format; the week of 23–29 Nov is already full, so plan 30 Nov onward and double down on whichever format wins.

## 15 Nov 2026: weekly run (week of 16–22 Nov)

**Scorecard (9–15 Nov):** Retained 4 followers (+1 from last week), Return Policy 3 (unchanged). Best reach: RT-14R (crayon re-cut) 101, RP-14R (crayon re-cut) 99 with 1 share (10.1 s+s/1k). RP-13 (carry-forward super) 46 reach. RT-13 (timing) 24 reach. Carousels RT-14/RP-14 near-zero reach (2 and 0). RT-15/RP-15 skipped correctly — crayon reels cancelled per Daniel's 13 Nov rule. Crayon re-cuts still the best Reel format; motion Reels trail. No saves this week.

**Plan 16–22 Nov:** Mon RT-11 (3 legal moves) + RP-11 (3 moves employees miss) already queued. Wed RT-16 (small business offset, $1K back) + RP-16 (salary sacrifice maths). Fri RT-17 (sole trader vs company) + RP-17 (lodge late costs, timely post-31 Oct). All 7:30 pm AEDT. Figures verified 15 Nov (SBITO 16% capped $1K re-confirmed; FTL penalty $364/period from 1 Jul 2026 new).

**Experiment (continuing):** crayon re-cuts vs motion Reels on reach — RT-14R and RP-14R both ≈100 reach, outperforming all motion Reels. Next data point this week from motion Reels on new topics.

## 12 Nov 2026: restart + first crayon carousels (Daniel: "run it now", make it eye-catching)

- Posting was paused 8–12 Nov at Daniel's request. Restarted today.
- New: crayon "X. Not Y." carousels RP-14 (5 tax facts people have backwards) and RT-14 (5 things new owners get backwards), 5 two-panel slides each, plus Reel re-cuts RP-14R / RT-14R tonight 7:30 pm. Characters to keep: Return Policy = woman, brown bun, green hoodie; Retained = cafe owner, dark curly hair, beard, navy shirt, mustard apron.
- Pipeline that works: Canva generate-image (max ~3 jobs in flight, else "quota_exceeded") → insert_fill all panels on one 2160-wide sheet page of design DAHZ2AHQfVk (pages 2 and 3) → commit → export that page → crop 1080×540 cells. `crayon.two_panel(note=...)` adds a small chip for the condition/income year.
- Schedule: Fri 13 RT-13/RP-13, Sat 14 RT-12/RP-12, Mon 16 RT-11/RP-11 (all 7:30 pm). RP-11 and RT-13 rewritten: the 70c WFH rate isn't published for 2026–27, and "defer income" was cut.
- Captions no longer end with the disclaimer (Daniel); end with a question to pull comments.
- Experiment this week (both accounts): crayon carousel + re-cut vs reel_points Reels, on reach and saves+shares per 1,000.

## 8 Nov 2026: weekly run (week of 9–15 Nov)

**Scorecard (last 7 days):** Retained 3 followers (+3), Return Policy 2 followers (+2). Reels dominate: RT-04 led at 105 reach, RT-06 90, RT-09 53 (1 save). Carousels: 0–1 reach. No shares or follows yet from any post. Best saves/1k: RT-05R 24.4, RT-09 18.9. Trial Reels still rejected (fallback to normal Reels). Experiment (2 Nov): RT-05 carousel vs RT-04 animated Reel — inconclusive (RT-04 Reel won on reach 105 vs 1); need more data. RP experiment: too little reach on both to call.

**Plan 9–15 Nov:** 3 animated Reels per account Mon/Wed/Fri 7:30 pm. RT-11 (3 legal moves), RT-12 ($20K write-off permanent), RT-13 (timing income/expenses). RP-11 (3 moves employees miss), RP-12 (deductions employees forget), RP-13 (carry-forward super). Figures verified on ATO 8 Nov (see figures.md).

## 6 Nov 2026: cut usage (Daniel)

- From 9 Nov: 3 animated Reels per account a week (Mon/Wed/Fri 7:30 pm), no new carousels or stories. Weekly scheduled task moved to a cheaper model with a shorter prompt.
- Free stats page `stats/README.md`, rebuilt by the stats workflow; Daniel checks it instead of asking.

## 3 Nov 2026: fixed posting schedule (Daniel)

- Reel every day 7:30 pm both accounts; carousels 12:30 pm (RT Tue/Thu, RP Tue/Thu/Sat); stories 8:30 pm (RP daily, RT Mon/Wed/Fri). In CLAUDE.md.
- This week's Reels moved to 7:30 pm; added Sat/Sun Reels RT-09 (GST $75K), RT-10 (small business offset), RP-09 (WFH 70c/hour), RP-10 (3 changes since 1 July). Figures checked on ATO 3 Nov.
- From Monday 9 Nov the Sunday run fills every slot.

## 3 Nov 2026: connectors + crayon two-panel style

- Daniel connected Canva, Unsplash and vidIQ. He likes Karlton Dennis's crayon two-panel motivational carousel ("The average millionaire is 57. Not 21."; 10.6K likes, 3.5K shares).
- Canva `generate-image` makes good crayon illustrations (ask for "no text"; add all words ourselves so they're exact). Mock-up: `refs/mock-crayon-two-panel.jpg` ("Most people have 2 years to fix their tax return. Not 2 days.").
- Pipeline: generate-image → place on the working canvas design `DAHZ2AHQfVk` (edit-design insert_fill) → export-design PNG → download → compose text in HTML.
- Daniel allowed `export-download.canva.com` and `images.unsplash.com` (3 Nov): Canva exports and Unsplash photos now download fine. Reusable kit: `brand/crayon.py` (`two_panel`, `render`).
- Use the style as ~1 in 5 posts, money/tax twist, every stat verified (ABS/ATO), never his stats or characters.

## 3 Nov 2026: content looks too plain (Daniel)

- Daniel: the posts are correct but boring and one-colour; look at Karlton Dennis ("how to lower your taxable income", "ranking tax moves that should be illegal"). He's sending example posts he likes.
- Pulled Karlton Dennis and Humphrey Yang's last 50 posts (`scripts/study.py` → `stats/benchmarks.json`); takeaways in `refs/benchmark-notes.md`. New rules in CLAUDE.md under "Make it attractive, not textbook".
- Next: redesign covers (comparison, tier list, giant list, curiosity question), multi-colour, fewer words. Apply to everything made from now on, including Sunday's run. The 6 Reels queued for Wed–Fri stay as they are.

## 3 Nov 2026: daily animated Reels (Daniel: go ahead)

- Stats at 4 pm: RT-04 (animated, Penny) reached 95 and is still climbing; every carousel re-cut stalled at 1–44; carousels 0. Retained 127 reach / 3 profile visits on 2 Nov; Return Policy 36. Followers 0 / 0.
- Decision: one animated Reel per account per day instead of bursts. New `brand/reel_points.py` (hook → 3 point cards → end, both brands, mascot on every card) makes these fast. Don't render two Reels in parallel: motion.py shares one temp HTML file.
- Queued 12:30 pm: Wed RT-06 ($120K profit, $20K super) + RP-06 (same $90K salary); Thu RT-07 (notice of intent) + RP-07 ($1,000 deduction); Fri RT-08 (2026–27 rates, next dollar) + RP-08 (3 things you can't claim). All figures from the 1 Nov ATO checks.
- Test this week: motion Reels vs carousel re-cuts on reach and follows per 1,000.

## 2 Nov 2026: traction push (Daniel: "find a way to start getting traction")

- Day-3 stats: 0 followers on both accounts (Retained 2 posts, Return Policy 1); reach 0 on every post; the only comments are spam bots. Carousels on accounts with no followers get no distribution.
- **Change:** Reels-first via **trial Reels** (non-followers first, auto-share to followers on performance). `scripts/publish.py` now sends `trial_params` for `"trial": true` Reels, with a fallback to a normal Reel. New `brand/carousel_reel.py` re-cuts any carousel into a 9:16 Reel with a hook band.
- **Queued:** RP-02R (Tue 3 Nov 12:30), RT-03R (Tue 12:45), RP-03R (Wed 4 Nov 12:30), RT-05R (Sat 7 Nov 12:30), RP-05R (Mon 9 Nov 12:30). RT-04 and RP-04 switched to trial. That's 7 Reels this week instead of 2.
- **Brought forward (Daniel: stop timing, act urgently):** all 13 queued feed posts plus a new RT-02R re-cut now go out 2 Nov between 4:30 and 7:30 pm, 30 min apart per account. Stories unchanged. Rule now in CLAUDE.md: no timing until 100 followers.
- **Trial Reels rejected by Meta** (code 10 / 2207081, no permission for this app). RP-02R and RT-03R went out 4:35 pm as normal Reels via the fallback.
- **Check on 8 Nov:** Reach on the R posts vs the carousels they came from.

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
