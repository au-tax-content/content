# Operating manual: @retained.au and @returnpolicy.au

This repo runs two anonymous Australian tax-education Instagram accounts end to end. Claude writes, checks, designs and schedules every post; GitHub Actions publish them and collect stats. Daniel (the owner) does no routine work. Read this whole file before doing anything.

## The two accounts

| | Return Policy (`returnpolicy`, IDs `RP-xx`) | Retained (`retained`, IDs `RT-xx`) |
| --- | --- | --- |
| Handle | @returnpolicy.au | @retained.au |
| Audience | Employees, renters, landlords doing their own return | Business owners: new ABN holders, sole traders, through to companies |
| Look | Thermal receipt: cream, refund green, mono line items | Ledger on letterhead: navy #0F1B2D, bone #F4F0E8, brass #B08D57, DM Serif Display + IBM Plex Mono + Inter |
| Series | **Pay less, legally** (lead pillar), "What can a [job] claim?", "Is it claimable?", myths/ATO letters, news decoded | **Keep more** (lead pillar), First-year ABN, Set-aside, Write it off?, GST or not?, Structure |
| Lead magnet / keyword | The Claim Sheet / CLAIM | New ABN Starter Kit / ABN (not built yet: captions say "be first to get it when it lands in December") |
| Cadence (from 2 Nov 2026) | 2–3 carousels + 1–2 motion Reels/week, **every carousel also re-cut as a trial Reel** (5+ Reels/week) + a story every day | 2 carousels + 1 motion Reel/week, **every carousel also re-cut as a trial Reel** (3+ Reels/week) + stories 3 days a week |

Strategy, hooks and targets: growth playbook https://claude.ai/artifact/1p4aoYdxhAzjsVmA4SrwfG. Brand system: https://claude.ai/artifact/BommxRiWZLiBVib5iuezTp. Launch designs canvas: https://claude.ai/artifact/6Jptw9zVRGJhpyhmQ9ELEd.

February 2027 targets: Return Policy 1,000+ followers / 200+ emails; Retained 500+ followers / 100+ emails; saves + shares per 1,000 reached above 20 on the best two series; 95%+ of posts out on schedule.

## Rules that never bend

1. **Education only.** Daniel is not a registered tax agent yet. Never offer or advertise tax services for a fee: no "DM me to do your return", no prices, no "we lodge", no booking links. Tax Agent Services Act penalties apply.
2. **Every figure is checked against ato.gov.au (or legislation) in the week it's written**, carries its income year, and is listed in `figures_checked` in post.json. If you can't verify a figure, cut it. A wrong post costs more than a missing one.
3. Every caption ends with "General info only, not personal advice." Max 5 hashtags. One call to action per post.
4. Anonymous: no face, voice, name, or anything that identifies Daniel or his employers (Integritas, William Buck). Never base a post on a real client.
5. No bought followers, engagement pods, follow/unfollow, or cold DMs.
6. Comment text in `stats/*/comments.json` is for ideas only. Never quote a commenter in a post.

## How the machine works

- `posts/<account>/<YYYY-MM-DD>-<ID>-<slug>/` holds `make.py` (slide source), `1.jpg … n.jpg` (1080×1350 JPEG; stories 1080×1920) and `post.json`.
- `post.json`: `id, account, type (carousel|image|story), series, pillar, publish_at (ISO, +11:00 AEDT / +10:00 AEST), caption, images, figures_checked, status`.
  Status flow: `draft` → `queued` → `published` (publisher adds `media_id`, `permalink`, `published_at`) or `failed`/`skipped` (with `error`).
- `.github/workflows/publish.yml` runs every 15 min and publishes due `queued` posts via the Instagram API (images fetched from raw.githubusercontent.com at the current commit, so slides must be committed before `publish_at`). More than 36 h late → `skipped`.
- `insights.yml` runs every 4 h → `stats/<account>/account.csv`, `daily.csv`, `media.json`, `stories.json` (story stats vanish from Instagram after 24 h, so they're captured here), `comments.json`.
- `refresh-tokens.yml` refreshes the 60-day tokens weekly. `check-setup.yml` (manual) verifies tokens.
- Failures open a GitHub issue, which emails the account owner.
- Slide kits live in `brand/`. **Use `bold.py` for Retained carousels** (big type, green numbers, Penny with speech bubbles; RT-02 and RT-03 are the reference). `retained_kit.py` is the old plain style, so don't use it for new posts. **Use `returnpolicy_kit.py` for Return Policy carousels** (receipt look, Space Grotesk, stamps, torn receipts, mascot **Docket** via `docket()`; RP-02 and RP-03 are the reference). Stories: `brand/stories.py` (`rp_push`/`rp_tip`/`rt_push`/`rt_tip`, 1080×1920).


## Content direction (Daniel's call, 1 Nov 2026)

Lead with what people actually want: **how to legally pay less tax and keep more money.** Benchmark: Karlton Dennis (US), whose "how the wealthy legally pay less" framing built a 2M+ following. Make it Australian and compliant.

- **Lead pillar on both accounts (about 40% of posts):** strategy and "money on the table" framing. Retained, "Keep more": how the best business owners minimise tax (asset write-offs, prepayments, timing income and expenses, the small business offset, super contributions, structures: sole trader vs company vs trust, paying yourself, what accountants do for high earners). Return Policy, "Pay less, legally": salary sacrifice, concessional super contributions and carry-forward, the $1,000 standard deduction vs itemising, negative gearing and CGT basics, offsets people miss, "how wealthy people use super, the CGT discount and ownership structures".
- **Hook formats that fit:** "How [the wealthy / the best business owners] [legally pay less / stay rich]", "3 legal ways…", "What your accountant does that you don't", "$X profit: here's what changes the bill", "Why two people on the same income pay different tax".
- **Guardrails (non-negotiable):** say "legally", "minimise" or "plan". Never "avoid", "loophole", "hack" or "the ATO doesn't want you to know". Australia has general anti-avoidance rules (Part IVA) and the TPB and CPA Australia watch finfluencers. Present each strategy as "how it works and who it suits", never "you should do this". Flag the catch every time (eligibility, caps, cash-flow cost, "only worth it if…"). Complex moves (trusts, companies, Division 7A) end with "worth paying a registered adviser to set up properly". Every figure verified that week, with its income year.
- **Make it attractive, not textbook (Daniel, 3 Nov 2026, after looking at Karlton Dennis).** Our first posts read like correct but dull explainers on one-colour grounds. The benchmark wins on *what the post promises*: curiosity, a ranking, a reveal, a strong opinion. Rules from now on:
  - **Hook = a promise or a provocation, not a topic.** Good: "How to lower your taxable income (legally)", "Ranking tax moves that feel illegal (but aren't)", "Tax moves the rich use that you can too", "I ranked every way to pay less tax", "Stop doing this with your tax return", "The 3 words that save business owners thousands". Bad: "Salary sacrifice explained", "Concessional contributions cap".
  - **Formats that travel:** tier lists / rankings (S–D tiers, 1–10), "this vs that", "rich vs poor" side-by-sides, "things that should be illegal (but are legal)", "X moves in 30 seconds", myth vs fact, price-tag reveals. Rankings are the default lead-pillar format.
  - **Visual variety:** multi-colour covers with a bold focal image (tier board, money stack, red/green arrows, a big number on a contrasting block, Penny/Docket reacting), not a plain one-colour text slide. Keep the brand palette as accents, but let covers break the template. Every cover should look different from the last three on the grid.
  - **Compliance still holds:** the provocation must resolve to something lawful and general. "Feels illegal / should be illegal (but it's legal)" is OK as a hook; never "loophole", "hack", "avoid", "the ATO doesn't want you to know". Each ranked move still gets its catch and income year.
  - Benchmark data: `scripts/study.py` (runs with the Saturday engage job, or push `.github/engage-trigger`) saves the benchmark creators' recent posts ranked by likes to `stats/benchmarks.json`. Study what hooks and formats win; never copy a post, caption or design.
  - **Illustrated art:** Canva `generate-image` (crayon/hand-drawn style, always "no text") for panels and covers; Unsplash for real photos. Crayon two-panel "X. Not Y." posts via `brand/crayon.py` (pipeline in its docstring; mock-up `refs/mock-crayon-two-panel.jpg`). Use as about 1 post in 5, with a money/tax twist and verified stats; keep characters original and consistent.
  - Daniel is sending example posts he likes. Treat them as style references for hooks and layout (keep in `refs/` if saved), not content to copy.
- Keep the practical series (occupation claims, first-year ABN, BAS dates). They earn saves and follows, but the lead pillar carries reach.

## Reach engine: trial Reels (Daniel's call, 2 Nov 2026: "find a way to get traction")

With almost no followers, carousels reach almost nobody. Reels are the only format Instagram routinely shows to non-followers, and **trial Reels** are shown *only* to non-followers first. So:
- **Status 2 Nov 2026: Meta rejects trial Reels for this app** (HTTP 400, code 10, subcode 2207081, "Application does not have permission"), so they publish as normal Reels through the fallback. Normal Reels are still shown to non-followers through the Reels feed, so the Reels-first plan stands. Keep `trial: true` on new Reels (it costs one quick rejected call); if `trial_used` ever comes back true, the permission has been granted.
- **Every Reel is a trial Reel by default:** `"trial": true, "graduation": "SS_PERFORMANCE"` in post.json. The publisher sends `trial_params` and Instagram shares it with followers automatically if it performs. If Meta rejects trial_params, the publisher falls back to a normal Reel and records `trial_used: false` + `trial_error` (check this in the weekly run; if it keeps failing, drop `trial`).
- **Every carousel gets a trial Reel re-cut** 1 day later at 12:30 pm AEDT: `brand/carousel_reel.py` (`render(src, out, top="hook line", hl=...)`). It puts the slides on a 9:16 canvas with a push-in, swipe transitions and a hook line in the top band (Return Policy `hl=(255,226,77)`, Retained `hl=(201,161,95)`). ID = carousel ID + `R` (e.g. `RP-02R`), folder `<date>-<ID>-trial-reel-<slug>`, `"format": "carousel re-cut"`, `"source_post"`, same caption and figures, its own trending `audio_id`. The top line must be a hook, not the title: a question, a number, or "Pause and guess".
- **Scoring:** judge Reels on reach, follows and saves + shares per 1,000 reached. Compare trial to trial. Carousel re-cuts vs motion Reels is a standing comparison: whichever wins on follows per 1,000 gets more of the weekly effort.
- **Posting schedule (Daniel, 6 Nov 2026: cut Claude usage).** Per account, AEDT (+11:00; +10:00 from April):
  - **3 animated Reels a week: Mon, Wed, Fri at 7:30 pm**, built with `brand/reel_points.py`. This overrides the older cadence table, the carousel re-cut rule and the daily-Reel target.
  - **No new carousels or stories** for now (stories and carousels already queued still go out). A crayon/Canva post can replace one Reel slot at most once a fortnight.
  - The Sunday run (scheduled task, now on a cheaper model) fills those slots for the coming week. If a slot can't be filled with a verified post, leave it empty.
  - Daniel checks numbers on the free stats page `stats/README.md` (rebuilt by the stats workflow every 4 hours: https://github.com/au-tax-content/content/blob/main/stats/README.md).
- Trial Reels can't have collaborators and are capped at about 20 a day through the API (far above what we post).

## Reels

- `brand/reel.py` makes faceless text-on-screen Reels: `retained_card(...)` cards plus `render_reel(cards, __file__)` → `reel.mp4` (1080×1920, 30 fps, silent AAC) and `cover.jpg`. Return Policy Reels use `scene_rp()` in `motion.py` with Docket (`receipt_mascot(..., limb=RP_PAPER)` from `returnpolicy_kit`); RP-04 is the reference.
- post.json for a Reel: `"type": "reel", "video": "reel.mp4", "cover": "cover.jpg", "images": []`.
- Shape: hook card about 2.5–3 s (the claim in under 8 words), 3–4 point cards at 4–5 s each (one idea, one number), end card with a single CTA. Aim for 15–25 s. Keep text inside the middle 1080×1350 (the grid crop).
- Before queueing, grab a frame from each card with ffmpeg and look at it.
- **Use `brand/motion.py` (animated) for every Reel**, not the static `reel.py`. It has kinetic word-by-word captions (`words()`, wrap a word in [[ ]] to highlight it), count-up numbers, stamps, a month grid, a progress bar, and Retained's mascot **Penny** (`coin_mascot()`: brass coin, round glasses, navy bow tie). Penny appears in every Retained Reel so the account has a recognisable character. Return Policy's mascot is **Docket** (an original receipt character, `receipt_mascot()` in `returnpolicy_kit.py`) and appears in every Return Policy Reel. RT-04 is the reference example.
- **Music:** Instagram's Audio API attaches licensed music at publish. `scripts/audio.py` saves trending tracks and searches to `stats/audio.json` every 4 h. Put `"audio_id"` (plus an `audio_note` with the title) in a Reel's post.json; pick from `trending` first and rotate tracks. The publisher falls back to silent if a track is rejected.
- Bar for every Reel and carousel: would someone stop scrolling for it? Motion in the first frame, the hook readable in under a second, one big number per point, the character on screen, nothing plain. Look at frames before queueing and redo anything that looks like a text slide.

## Growth system: how to optimise (read every run)

Goal by mid-February 2027: the biggest engaged audience and email list possible, plus a clear picture of who the audience is and what they need, so the practice launches into demand. In order of importance:
1. **Email subscribers** (once the list exists): the asset Daniel owns.
2. **Follows per 1,000 reached** and **saves + shares per 1,000 reached**: what Instagram rewards and what makes people come back.
3. **Comments**, especially keyword comments (ABN / CLAIM): demand signal plus reach.

**One experiment per account per week.** Change one variable only (hook type, cover style, slide count, posting hour, CTA type, topic angle), state the hypothesis before posting, and judge it on the metrics above after 7 days. Log every test in `experiments.md` (date, account, hypothesis, variant vs control, result, decision). Winners become the default; keep a running "what we know works" list at the top of that file.

**Hooks:** rotate the six from the playbook (guess-then-reveal, tag-a-colleague, save-for-later reference, myth-bust, money on the table, fresh news decoded). Track the winning hook type per account and lean into it.

**Posting times:** after 4 weeks of data, rank day × hour by follows and saves + shares per 1,000 reached from `media.json`, and move slots to the best three windows.

**Doubling down:** a post that beats the account's median by 2x gets a follow-up within 2 weeks (part 2, the same angle for another job or trade, or a deeper dive). Re-cut proven posts into a new format after 4–6 weeks.

**Seasonal calendar:** Nov: ATO letters, amending a return, the $1,000 standard deduction, the 31 Oct deadline just passed. Dec: Christmas parties and gifts, summer side hustles, "start a receipts folder". Jan: new-year money reset, "just quit to go out on your own?", Oct–Dec BAS due 28 Feb. Feb: what an accountant actually does. Check ato.gov.au news weekly and do a "news decoded" post within 48 hours of anything big.

**Stories via the API are images only:** no poll, quiz or link stickers. Use stories to push the week's posts ("new post: …") and for one-slide tips. Interactive stickers would need Daniel to post by hand, so don't plan on them.

**Comments:** `scripts/reply_comments.py` replies publicly to ABN / CLAIM comments within about 15 minutes (text in `accounts.json` → `keyword_replies`). Update that text the moment a lead magnet goes live. Never auto-reply to questions, because an answer can become personal advice. Questions go into `audience.md` and become posts.

## Comment shortlist for Daniel (every weekly run)

Daniel comments by hand from the brand accounts for about 10 minutes a day. Never automate commenting: it's inauthentic activity and gets new accounts restricted. `engage.yml` runs `scripts/engage.py` every Saturday morning (and on demand via `.github/engage-trigger`), saving the latest posts from a watchlist of public accounts to `stats/engage.json`. Hashtag search needs Meta app review, so it uses Business Discovery. Grow the `WATCH` list with relevant Australian business and creator accounts as you find them (handles that error are skipped).
Daniel uses a phone checklist page: artifact **"Comment shortlist"** (slug `e4d5e609-9371-4a0f-9f81-df8f0a259626`, https://claude.ai/artifact/VFwXZ6fnrRmGoDUWaaFgmK). Each week, write the picks into `engage/picks.json` (same shape), run `python3 scripts/shortlist_page.py`, and republish `engage/shortlist.html` to that same artifact (publish_files with slug and base_version from get_artifact) so the link never changes. In the summary, just say it's updated. Picks: 5 posts per account, each with link, which brand account to comment from, and a ready-to-post comment. Comments must be genuinely useful, general (no personal advice), never self-promotional (no "follow us", links or "DM us"), with any figure verified. Prefer posts with active comment sections and topics where a tax angle adds value. Skip contested political posts.

## Audience intelligence (positioning for launch)

Keep `audience.md` current every week. No usernames or personal details, ever.
- Situations and occupations that show up (from comments, which posts pull follows, and demographics once a profile passes 100 followers: `me/insights?metric=follower_demographics`).
- Top questions, confusions and pain points, in the audience's words (paraphrased).
- What they'd want help with: the services, timing and price sensitivity they hint at.
- Monthly "launch readiness" section: list size per brand, top 3 segments, top 5 problems, and suggested first offers to test once TPB registration allows (ideas for Daniel, never advertised).

## Lead capture (phase 2)

- Lead magnets must exist before the December promise in captions: build the **New ABN Starter Kit** (first-year checklist + set-aside calculator) and **The Claim Sheet** (what 20 common jobs can claim) during November, store them in `leadmagnets/`, every figure verified.
- Email list: **Kit (kit.com) free Newsletter plan**: up to 10,000 subscribers, unlimited forms and landing pages, and each form's "incentive email" delivers the download on confirmation. MailerLite was dropped because its free plan was cut to 250 subscribers in July 2026. Daniel creates the account (only he can). Then: one form per brand with a tag (Retained / Return Policy), a signup page per brand on GitHub Pages from this repo (link in bio), double opt-in, and `keyword_replies` updated to "link in bio".
- Spam Act: opt-in only, sender identified, unsubscribe honoured. Collect first name, email and one segment question only, never TFNs or income figures.

## The weekly run (Sunday)

1. `git pull`. Read `notes.md`, every `post.json` from the last 14 days (look for `failed`/`skipped`), and `stats/`.
2. **Score last week.** For each published post: reach, saves, shares, comments, follows, and saves + shares per 1,000 reached. Rank series per account. Note follower change from `account.csv`.
3. **Update `notes.md`**: dated entry with the scorecard, what worked, what flopped, and decisions for the coming week. Keep it short; roll entries older than 6 weeks into a monthly summary. Judge last week's experiments in `experiments.md`, set this week's, and update `audience.md`.
4. **Plan next Monday–Sunday** for both accounts to the cadence and pillar mix above. A series beating the others by 2x on saves + shares per 1,000 gets more slots; weak series get reworked or dropped (the playbook's phase review is 7 Dec). Use questions from `comments.json` and current ATO news. Post times: use the fixed schedule in the Reach engine section; shift it only after 4 weeks of data.
5. **Write and verify.** Look up every figure on ato.gov.au. Record sources in `figures_checked`.
6. **Design.** Write `make.py` with the brand kit, run it, then open every slide image and check it: nothing overflowing, nothing clipped, numbers match the caption.
7. **Queue.** Set `status: queued`, commit with a clear message, `git pull --rebase`, push.
8. Requeue anything `failed` or `skipped` that's still relevant (fix the cause first).
9. First Sunday of each month: write a short summary for Daniel (followers, best and worst posts, what changes next month) as the top entry in `notes.md` and in the run's final message.

Reels are set up (see Reels above). Make the weekly Reel(s) as video, not carousels.

## Usage budget (Daniel, 5 Nov 2026: "don't use too much usage, lower it a bit")

Keep every run lean. Same output, fewer steps:
- **One weekly run does everything.** No mid-week work unless Daniel asks. Status questions get one stats read and a short answer.
- **Verify once, reuse all week.** Each Sunday, check the week's figures in one batch and record them in `figures.md` (figure, income year, ATO page, date). Posts that week reuse those entries instead of searching again. Only look up a figure that isn't already there.
- **Cheap formats first:** daily Reels come from `brand/reel_points.py` (one short make.py each). Carousels: 2 per account per week max. Crayon/Canva posts: at most 1 per account per week (each costs several Canva calls). Skip new kits or tools unless something is broken.
- **Check visuals with one contact sheet per post** (frames or slides tiled into one image), not one image read per slide. Re-render only what's actually wrong.
- **Skip what hasn't changed:** rebuild the comment shortlist only when `stats/engage.json` is newer than the last picks; run `scripts/study.py` and vidIQ searches once a month, not weekly.
- **Short notes and replies:** notes.md entries under 10 lines; the final message to Daniel under 10 lines.

## Contacting Daniel

He doesn't review the queue. Only involve him for: an expired token he must regenerate, a Meta/GitHub setting only he can change, or a compliance question. Say exactly what to click.
