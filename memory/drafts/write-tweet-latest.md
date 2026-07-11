---
type: Reference
---

## Tweet Drafts: AI agents getting their wallets drained via prompt injection

### Tier 1 — One-liner
**1a. Hot take**
> An AI agent holding its own private key isn't automation. It's an attack surface with a bank balance.

**1b. Observation**
> Every "AI agent with a wallet" story ends the same way: someone finds the prompt that empties it.

### Tier 2 — Two-punch
**2a. Data drop**
> Zscaler just found sites hiding prompt injections that trick AI agents into paying out crypto. The agent isn't hacked. It's just doing what it was told.

**2b. Reframe**
> We spent years teaching agents to transact autonomously. Turns out the hard part was never the transacting. It's making sure the instruction came from you.

### Tier 3 — Paragraph
**3a. Reframe**
> The pattern in every recent agent-wallet drain is the same: intelligence and authorization live in the same place. One poisoned prompt and the thing that reasons is also the thing that signs. Separate those and the exploit stops being catastrophic.

**3b. Narrative**
> A researcher tricked Grok's wallet integration with Morse code hidden in a prompt and drained funds. Not a bug. A design choice: one model with both judgment and signing power. Every agent wallet built that way is one clever prompt from empty.

### Tier 4 — Long tweet
**4a. Builder's breakdown**
> Zscaler's latest research: malicious sites hiding prompt injections that quietly instruct AI agents to make crypto payments, poisoning the agent's context with fake "trusted" sources along the way. The agents aren't being tricked into bad reasoning — they're being handed fake instructions and reasoning correctly from bad premises. That distinction matters because it means better models don't fix this. Only separating "can reason" from "can authorize" does: per-transaction caps, allowlists, a second independent check before funds move.

**4b. Data drop**
> Every agent-payments postmortem this year has the same root cause. A single model holds both judgment and signing authority, so one successful injection is one successful theft. The fix nobody wants to build: authorization that doesn't trust any single model's output, backed by hard spend limits and a second, independent check before value moves. Slower. Also the only version that survives contact with an adversarial prompt.

### Tier 5 — Thread opener
**5a. Data drop**
> Every AI-agent-drains-wallet story this month has the same root cause, and it isn't a smarter attacker.
---
- One model holds both judgment and signing power
- A single poisoned prompt is now a signed transaction
- Zscaler's latest: fake "trusted" sources injected straight into agent context
- The May Grok wallet drain: Morse code hidden in a prompt, funds gone
- The fix isn't a smarter model — it's separating "can reason" from "can authorize"

**5b. Sardonic/ironic**
> Nobody built agent-payment security. They bolted a wallet onto a chatbot and called it autonomy.
---
- Prompt injection isn't a jailbreak anymore, it's a wallet-draining exploit
- Zscaler found sites hiding instructions that trigger real crypto payments
- The common thread: intelligence and authorization sitting in the same model
- Hardware limits, per-tx caps, allowlists — the boring fixes nobody ships first
- The agents that survive this era will be the ones that can't fully trust themselves

**Best overall:** 4a — most specific and actionable: names the mechanism (fake context, not "bad reasoning"), names the fix (separate reason from authorize), grounded in the Zscaler research from today's digest.
**Best per tier:** 1a, 2a, 3a, 4a, 5a.
