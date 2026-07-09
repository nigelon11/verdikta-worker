---
type: Reference
---

## Tweet Drafts: TEE-attested judges vs. multi-model consensus for on-chain payouts

### Tier 1 — One-liner
**1a. Reframe**
> TEE-attesting a biased AI judge doesn't fix the bias — it just makes the bias cryptographically provable.

**1b. Narrative**
> Two independent AI models scored a bounty tonight, agreed within a hair of each other, and the payout went out with zero humans in the loop.

### Tier 2 — Two-punch
**2a. Reframe**
> A TEE proves the model ran untampered. It doesn't prove the model was right. Those are different problems, and on-chain judges keep conflating them.

**2b. Data drop**
> Tonight, two independent models scored a submission 93.375 against a 90% bar. Neither knew the other's number. That's not attestation — that's agreement.

### Tier 3 — Paragraph
**3a. Observation**
> Everyone building AI oracles for on-chain payouts is solving "how do we prove the model ran." Almost nobody is solving "how do we catch the model being wrong." Attestation is a hardware guarantee. Correctness needs a second opinion.

**3b. Narrative**
> Watched a bounty get judged by two AI models against a public rubric, scored, and paid out on Base tonight — no dispute window, no human referee, no drama. The boring version of this technology is the one that actually ships.

### Tier 4 — Long tweet
**4a. Data-driven**
> The debate on X this week is single-model TEE judges vs multi-validator consensus. A TEE proves the model wasn't tampered with — it says nothing about whether the model's judgment was good. A biased or hallucinating model, faithfully attested, still pays the wrong wallet. The fix isn't more trust in hardware, it's a second independent model scoring the same rubric, paying out only when both agree. Tonight that's not theory: a submission cleared 93.375 against a 90 threshold from two models that never saw each other's score, and the payout hit Base with a public tx to check.

**4b. Builder's breakdown**
> "LLM-as-a-judge" research has spent two years cataloguing failure modes: position bias, verbosity bias, self-preference. Every one is a single-model problem. Bolt a TEE onto a biased judge and you get cryptographically verifiable bias. The fix isn't attesting the model — it's not trusting any one model's score by itself.

### Tier 5 — Thread opener
**5a. Reframe**
> Single-model AI judges have a bias problem a TEE can't fix — it can only prove the bias ran on real hardware.
---
- A TEE attests execution, not correctness
- Multi-model consensus catches what attestation can't
- Tonight: two models, one rubric, 93.375 vs a 90 threshold, real payout on Base
- The X debate this week (TEE judges vs validator consensus) is the right one to be having
- What actually needs to be true before anyone trusts an AI with a payout button

**5b. Question**
> Why would you trust a single AI model with a payout decision when you wouldn't trust a single human reviewer with one?
---
- Human review uses multiple reviewers because one person's judgment is noisy
- AI judges inherited the single-reviewer failure mode by default
- The fix already exists: two independent models, one public rubric, agreement required
- Real example from tonight: 93.375 vs a 90 threshold, paid out on Base
- Where TEE-attestation still matters (proving the model ran) vs where it can't help (proving the model was right)

**Best overall:** #4a — the only draft carrying both the live X debate and the verifiable on-chain number in one tweet.
**Best per tier:** 1a (reframe lands cleanest), 2b (concrete number beats abstraction), 3b (narrative, memorable "no drama" line), 4a (as above), 5a (bias framing sets up the thread better than the question does).
