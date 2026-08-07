---
type: Reference
---

## Tweet Drafts: Apple's bug bounty AI-slop failure

### Tier 1 — One-liner
**1a. Data drop**
> A real $200K macOS exploit sat unpatched because Apple's bug bounty inbox was buried in AI slop.

**1b. Observation**
> Every bounty program has the same failure mode now: too much AI noise, not enough triage bandwidth.

### Tier 2 — Two-punch
**2a. Data drop**
> Bynario found 50+ real macOS bugs with ChatGPT, one worth $200K. Apple's team was so buried in AI submissions they missed it — and only patched after direct outreach.

**2b. Reframe**
> The problem was never AI finding bugs. It's that nobody built triage for a world where anyone can generate hundreds of plausible-looking reports for free.

### Tier 3 — Paragraph
**3a. Narrative**
> Bynario found a $200K macOS exploit chain using ChatGPT. Apple's bounty inbox was so flooded with AI slop the submission got capped and buried — until Bynario reached out directly. The bug got patched. The process didn't.

**3b. Structural critique**
> Manual triage assumed submissions were expensive to produce. AI made them free. Apple's bug bounty is now proving what happens when a system built for scarcity meets a world of infinite cheap submissions: real signal gets lost in the noise.

### Tier 4 — Long tweet
**4a. Data drop**
> Apple capped open bug bounty submissions because AI-generated slop reports overwhelmed the queue. Inside that noise: Bynario, using ChatGPT, found 50+ real macOS bugs — including a $200K exploit chain (CVE-2026-43760) — that got buried and only patched after direct outreach. The lesson isn't ban AI submissions. It's that triage built for a handful of expert reports a month can't survive a world where anyone can generate hundreds of plausible-sounding ones. You need a system built for that volume from day one, not a queue and a prayer.

**4b. Structural critique**
> Here's the actual failure mode in Apple's bug bounty story: a first-come inbox has no way to rank submissions, so it either lets everything through or caps volume and buries the good ones with the bad. Both are the wrong axis. What you actually need is a way to score every submission against a fixed rubric regardless of how many arrive — that's the only design where a $200K exploit chain and a slop report get sorted correctly in the same pass, at any volume.

### Tier 5 — Thread opener
**5a. Builder's breakdown**
> Apple's bug bounty just proved a rule that's about to hit every open submission system: once submissions are free to generate, first-come triage collapses. A $200K macOS exploit sat buried in AI slop for weeks. Here's what actually breaks, and what doesn't.
---
- The economics: AI made bug reports free to produce, triage capacity didn't scale with it
- What happened: Bynario's real $200K exploit chain (CVE-2026-43760) buried in the queue, only surfaced after direct outreach
- The pattern: security researchers and outlets calling it "AI slop" drowning real signal
- The actual fix: score every submission against a fixed rubric instead of ranking by arrival order
- Where this already exists: rubric-scored, two-model AI juries running bounty escrow on-chain today

**5b. Sardonic/ironic**
> Apple built one of the best bug bounty programs in the industry. AI just found the one thing it wasn't built for: infinite cheap submissions. A real $200K exploit got lost in the noise. Here's what that means for every bounty program still running the old model.
---
- The irony: one of the best-run programs in the industry, beaten by volume, not quality
- The Bynario case: 50+ real bugs found via ChatGPT, the $200K one nearly lost entirely
- Why "hire more reviewers" doesn't fix a scaling problem
- What changes when a rubric plus AI judges do the scoring instead of a human queue
- The real tradeoff: automation risk vs. triage collapse — only one of those scales

---

Best overall: **4b** — the sharpest technical reframe (rank-by-arrival vs. score-by-rubric), sets up the real implication without hype.
Best per tier: 1a (one-liner) · 2a (two-punch) · 3b (paragraph) · 4b (long tweet) · 5a (thread opener)
