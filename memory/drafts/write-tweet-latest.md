---
type: Reference
---

## Tweet Drafts: EPFL/Zhejiang x402 security audit — 31 undisclosed vulnerabilities across all 15 major facilitators

### Tier 1 — One-liner
**1a. Observation**
> An academic audit just checked every major x402 facilitator. All of them had holes nobody caught.

**1b. Reframe**
> We shipped AI agents that can pay before we shipped agents that can verify a payment is safe.

### Tier 2 — Two-punch
**2a. Data drop**
> Fifteen x402 facilitators process almost every agent payment on the internet. An independent audit just found 31 vulnerabilities nobody had disclosed.

**2b. Narrative**
> Replay attacks. Overpayment drains. Prompt-injection fraud. Not hypothetical — an EPFL/Zhejiang audit found all three live across the facilitators handling agent payments today.

### Tier 3 — Paragraph
**3a. Data drop**
> An EPFL/Zhejiang audit tested every major x402 facilitator — the rails 60K+ sellers and 99% of agent-payment volume run on. It found 31 new vulnerabilities: replay attacks, overpayment drains, prompt-injection fraud. Coinbase was in the sample. So was everyone else.

**3b. Structural critique**
> The agent-payments narrative moved faster than the security review. An independent audit of all 15 major x402 facilitators just surfaced 31 vulnerabilities that had gone undisclosed — some serious enough that vendors shipped emergency fixes once they were told.

### Tier 4 — Long tweet
**4a. Structural critique**
> Everyone racing to plug AI agents into x402 assumed the payment layer was solved because Coinbase and the rest were already running it. An independent audit tested all 15 major facilitators — 99% of agent-payment volume — against a formal security-rule set and found 31 previously unknown vulnerabilities: payment replay, wallet drain via overpayment, prompt-injection fraud, privacy leakage. Vendors are patching now, which means the holes were real. Moving money is the easy part. Nobody built the layer that catches the fraud before the money moves.

**4b. Observation**
> Here's the pattern with x402 coverage: every announcement is about who adopted it, never about what happens when an agent gets tricked into paying the wrong amount to the wrong address. An audit finally asked that question across all 15 major facilitators and found 31 vulnerabilities — replay, overpayment drain, prompt-injection fraud — that had shipped to production undisclosed. The rails work. Nothing was watching what moved through them.

### Tier 5 — Thread opener
**5a. Data drop**
> An independent audit just tested all 15 major x402 facilitators against a formal security checklist. Result: 49 rule violations, 31 undisclosed vulnerabilities, patches shipping now.
---
- The 3 vulnerability classes: payment replay, overpayment wallet drain, prompt-injection fraud
- Scope: all 15 major facilitators, 99% of agent-payment volume, 60K+ sellers — Coinbase included
- Why nobody caught it: adoption raced ahead of independent security review
- What happened once vendors were told: patches shipped, quietly
- The open question: who's checking the facilitators nobody's auditing yet

**5b. Sardonic**
> 31 new vulnerabilities. 15 facilitators. Zero X posts about it as of this morning. What's actually being found in agent-payment security and what's getting attention are two different feeds.
---
- Paper submitted 2026-07-21 — this morning, still no real X discourse on it
- Meanwhile the feed is full of "which facilitator we integrated" posts
- Security research doesn't move the same way funding-round tweets do
- Silence isn't the same as safety — the vulnerabilities existed either way
- What would actually make this the story it should be

Best overall: **4a** — the fullest, most falsifiable structural critique: payment rails ≠ verified payments, and the patch cycle proves the gap was real.
Best per tier: 1a (sharpest compression) · 2b (concrete vulnerability classes) · 3b (frames the narrative-vs-review-speed gap) · 4a (best overall) · 5a (strongest, most concrete hook)
