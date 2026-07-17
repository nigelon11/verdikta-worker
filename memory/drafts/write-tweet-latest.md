---
type: Reference
---

## Tweet Drafts: agent custody vs. agent adjudication (Ledger Agent Stack + Visa/Artemis dispute-layer gap)

### Tier 1 — One-liner
**1a. Hot take**
> Ledger secured who can sign. Nobody secured who's right.

**1b. Observation**
> Custody got solved this week. Adjudication didn't. That's the real gap in agent commerce.

### Tier 2 — Two-punch
**2a. Data drop**
> Visa and Artemis just said it out loud: no dispute layer exists for agent-initiated payments. Ledger secured the button. Nobody secured the outcome.

**2b. Reframe**
> Every headline this week is about who's allowed to press send. The actual question — who was right when the agent sent it — still has no answer.

### Tier 3 — Paragraph
**3a. Structural critique**
> Ledger just shipped hardware sign-off so a hacked agent can't drain a wallet. Good. But Visa and Artemis flagged the bigger hole: nobody's built the layer that says an agent's output was wrong after a human already approved it.

**3b. Sardonic**
> Agent commerce security in one sentence: we solved "can a stranger steal your money" and left "was your own agent right" completely open. Guess which one actually happens thousands of times an hour.

### Tier 4 — Long tweet
**4a. Data-driven**
> Three stories, one week, same blind spot. Ledger ships hardware-gated signing so a compromised agent can't move funds. Visa and Artemis flag that nobody's built reconciliation for agent-initiated transactions. Forbes ties $1.3B in H1 hacks to agent-wallet compromise — including a bot that lost $7.5M to a fake arbitrage pool a human never would've approved by hand. Custody is getting solved. Adjudication — was the agent's decision actually correct — isn't even being attempted.

**4b. Narrative**
> A bot lost $7.5M this year draining into a fake arbitrage pool. Not because someone stole its keys — because it decided, on its own authority, that the trade was good. Ledger's new hardware sign-off would've stopped a thief. It wouldn't have stopped this. The industry keeps building better locks for a door nobody's actually walking through wrong. The real losses are coming from agents making bad calls inside their own permissions, and there's still no mechanism to catch that before the money moves.

### Tier 5 — Thread opener
**5a. Thesis-first**
> Ledger just solved agent wallet security. It didn't solve agent trust — and that gap is where the real money is about to leak.
---
- Ledger Agent Stack: propose/approve/execute, hardware-enforced human sign-off
- Visa + Artemis report: names the missing reconciliation/dispute layer for agent-initiated transactions
- Forbes: $1.3B H1 hack losses tied to agent-wallet compromise, incl. $7.5M lost to a fake arbitrage pool
- Signing ≠ judging: a human tapping approve doesn't know if the agent's decision was correct
- Where this actually gets solved: verifiable adjudication of agent outputs, not just custody of agent keys

**5b. Question**
> Ledger just answered "who's allowed to move this money." Nobody's answering the harder question: when an autonomous agent moves it wrong, who decides — and how fast?
---
- The custody story: hardware-enforced propose/approve/execute, MoonPay and Shisa already integrated
- The gap story: Visa + Artemis say there's no reconciliation layer for agent-initiated transactions at scale
- The cost of the gap: $1.3B in H1 hacks tied to agent-wallet compromise per Forbes
- Signing solves theft. It doesn't solve bad judgment inside a legitimate agent
- Agent commerce won't scale past pilots until disputes resolve as fast as the transactions do

Best overall: 4a — ties all three stories (Ledger, Visa/Artemis, Forbes) into one throughline without pitching a solution.
Best per tier: 1a (tier 1), 2a (tier 2), 3a (tier 3), 4a (tier 4), 5a (tier 5)
