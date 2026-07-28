---
type: Reference
---

## Tweet Drafts: GitHub halves bug-bounty payouts, blames AI-report flood

### Tier 1 — One-liner
**1a. Hot take**
> GitHub didn't fix the AI-spam problem. It just made triage someone else's problem.

**1b. Observation**
> AI can flood a bounty program faster than humans can judge it. GitHub's fix: fewer submitters.

### Tier 2 — Two-punch
**2a. Sardonic/ironic**
> GitHub cut public bounty payouts in half and blamed AI-generated reports. The bug wasn't the reports — it was expecting humans to triage them at AI speed.

**2b. Reframe**
> Halving payouts and gating access doesn't stop AI-generated noise. It just narrows who's allowed to submit it. The triage bottleneck never moved.

### Tier 3 — Paragraph
**3a. Data drop**
> GitHub just cut its critical bug bounty from $30k to a flat $10k for public researchers, reserving the bigger payouts for an invite-only tier. Stated reason: AI-generated reports flooding the queue faster than humans can review them. That's access control, not quality control.

**3b. Narrative**
> A researcher posts a bug. A triager reads it, decides if it's real, pays out. That loop worked for years. Then AI made submitting cheap and reviewing expensive — so GitHub just shrank who's allowed to submit. The queue problem didn't disappear. It got smaller by exclusion.

### Tier 4 — Long tweet
**4a. Structural critique**
> GitHub's bug bounty program just got smaller: critical payouts cut from $30k to a flat $10k for public researchers, top rewards moved behind an invite-only VIP tier, new researchers capped at four submissions. Stated cause: AI-generated reports flooding triage. Notice the actual fix — restrict who can submit, not improve how submissions get judged. Human review doesn't scale with AI-report volume, so the program shrinks the pool instead of scaling the judgment. The bottleneck was never bounty budget. It was verification throughput.

**4b. Builder's breakdown**
> Here's what changed in GitHub's bug bounty terms as of July 27: public critical-severity payouts flat at $10k (previously up to $30k), $30k+ rewards reserved for an invite-only VIP tier, new researchers below a reputation threshold capped at four submissions before review. The justification: low-effort AI-generated reports overwhelming the triage queue. It's a rate limit dressed as a tier system — the real constraint is how fast a human can tell a real vulnerability from a plausible-sounding fake one.

### Tier 5 — Thread opener
**5a. Thesis-first**
> GitHub just proved something every bounty program will eventually face: when AI makes submitting cheap, the bottleneck moves to judging — and most programs aren't built for that.
---
- GitHub cuts public critical bounty payouts from $30k to a flat $10k
- Top rewards ($30k+) now invite-only, reputation-gated
- New researchers capped at 4 submissions before review
- Stated cause: AI-generated reports flooding triage
- The fix is exclusion, not faster/better verification — worth asking why

**5b. Question**
> If a flood of AI-generated bug reports can break GitHub's triage process, what happens to every other system that still assumes a human reads every submission?
---
- GitHub's new tiered bounty structure, explained
- Why exclusion (fewer eligible submitters) was the chosen fix over automation
- The unstated assumption: human judgment doesn't scale, so shrink the pool
- What a verification bottleneck actually costs a program
- The broader pattern: submission is getting cheap everywhere AI touches it

**Best overall:** #4a — sharpest, most falsifiable structural read (restricting access vs. scaling judgment), grounded in concrete numbers ($30k→$10k, invite-only tier, 4-submission cap).
**Best per tier:** 1a (compression), 2a (sardonic), 3a (data drop), 4a (structural critique), 5a (thesis-first thread hook).
