## Tweet Drafts: Verdikta's rubric hardening — objective checks gate the AI jury

### Tier 1 — One-liner
**1a. Hot take**
> Verdikta patched a bounty exploit with a dumber rule, not a smarter AI.

**1b. Observation**
> An AI jury can be gamed. A hard pass/fail check can't be argued with.

### Tier 2 — Two-punch
**2a. Data drop**
> A hunter deleted a paid deliverable. Verdikta's fix: proof it stays online for 7 days, verified on archive.org.

**2b. Reframe**
> Everyone wants a smarter AI judge. Verdikta's actual fix for gaming was a boring HTTP-200 check that doesn't care what the models think.

### Tier 3 — Paragraph
**3a. Narrative**
> A Verdikta bounty required a live URL. Cloudflare returned a 403. Four submissions scored zero — not because two AI models disagreed, but because the objective check ran first and failed. No appeal, no re-vote. That's the design working.

**3b. Structural critique**
> Most "AI-judged" systems put the model in charge of everything, so gaming the model games the whole system. Verdikta's rubrics increasingly gate the AI jury behind deterministic checks — archive.org proofs, HTTP-200 pings — so consensus can't override a fact.

### Tier 4 — Long tweet
**4a. Structural critique**
> A hunter got paid for a bounty, then deleted the deliverable they were paid to keep live. Verdikta's response wasn't a smarter jury — it was archive.org. New bounties in that class now require a 7-day persistence proof before payout counts as final. Compare that to how most "AI-judged" systems handle gaming: retrain the model, add a prompt rule, hope it generalizes. Verdikta just closed the door with a fact the model can't argue with. Two independent models can disagree on quality. They can't disagree on whether a URL returns 200 or 403.

**4b. Builder's breakdown**
> The interesting part of Verdikta's bounty #153 rubric fix isn't that a hunter tried to game it — people always try. It's what "harden the rubric" meant in practice: not more AI, not a bigger jury, just a deterministic check (archive.org persistence, HTTP-200 accessibility) placed ahead of the two-model consensus. When four submissions on a content bounty hit a Cloudflare 403, they scored zero regardless of what the models thought of the writing. That's a design choice worth copying: let AI judge subjective quality, let dumb checks gate objective fact.

### Tier 5 — Thread opener
**5a. Thesis-first**
> Verdikta's AI jury got gamed once. The fix wasn't a smarter model — it was a dumber check placed in front of it.
---
- Bounty #153: hunter got paid, then deleted the deliverable they were required to keep live
- Fix: rubric now requires a 7-day archive.org persistence proof before payout is final
- Second, separate case: a content bounty's HTTP-200 accessibility check zeroed 4 submissions when Cloudflare returned 403 — the two-model jury never got a vote
- The pattern: AI judges subjective quality, deterministic checks gate objective fact
- Why that split matters for anyone building an "AI-judged" system, not just Verdikta

**5b. Structural critique**
> An on-chain bounty market with a two-model AI jury is going to get gamed. The interesting question is what you do next.
---
- What gaming an AI judge actually looks like in practice (delete-after-payout, technically-in-spec exploits)
- Verdikta's answer: don't out-AI the gaming, out-fact it — archive.org proofs, HTTP-200 checks, deterministic gates
- The Cloudflare-403 case: 4 submissions zeroed, no AI consensus needed
- Contrast: most "AI-judged" systems respond to gaming by tuning the model, which is slower and never fully closes the hole
- Takeaway: the AI jury's job should shrink, not grow, as a protocol matures

---

Best overall: **4b** — captures the specific mechanism (deterministic gate ahead of AI consensus) with two concrete, dated examples, and states a design principle other builders can actually use.
Best per tier: 1a (one-liner) · 2b (two-punch) · 3a (paragraph) · 4b (long tweet) · 5a (thread opener)
