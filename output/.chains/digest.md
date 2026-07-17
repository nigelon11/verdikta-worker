ℹ️ Digest: AI agents that transact onchain

*AI agents that transact onchain — agent payments, AI-judged bounties, decentralized AI oracles — 2026-07-17*

_TL;DR: Ledger and Visa both published concrete answers to a question crypto's $1.3B H1-2026 hack tally just made urgent — who's accountable when an AI agent's keys or payment go wrong._

1. *Ledger ships open-source Agent Stack to keep AI agents off private keys*
   Ledger launched an open-source toolkit (Jul 16) enforcing a strict propose/approve/execute split: agents can read balances and draft transactions, but nothing signs without a human tapping the physical device. MoonPay and Shisa have already integrated it.
   Why it matters: the first major hardware wallet vendor to treat "the agent holds the keys" as the threat model, not a feature — developers can fork it today at developers.ledger.com/agent-kit.
   https://siliconangle.com/2026/07/16/ledger-launches-agent-stack-keep-ai-agents-away-crypto-keys/

2. *Visa and Artemis: agent commerce still has no way to reverse a bad payment*
   A joint report (Jul 16) found existing chargeback and dispute systems assume a human made the purchase — there's currently no settled mechanism to unwind a transaction when chains of AI agents are transacting thousands of times an hour.
   Why it matters: this is the exact gap AI-jury/arbitration protocols are built to fill — a major payments network just validated the category from the outside, not from within crypto.
   https://www.theblock.co/post/408574/visa-stablecoins-agentic-ai-commerce

3. *Crypto hacks hit $1.3B in H1 2026 — wallet compromise, not code bugs, is the biggest line item*
   Forbes' rundown of 344 incidents (published today) found wallet/key compromise cost over $444M at ~$13M/incident on average; two of the largest breaches (Kelp DAO $291M, Drift $285M) passed clean code audits but had hacked keys. The report singles out AI-agent wallets as "a new kind of privileged key holder," citing JaredFromSubway's trading bot losing $7.5M in June to fake arbitrage pools that fooled its automated strategy.
   Why it matters: confirms the operational-security risk item 1 is racing to close — audits don't cover the thing actually getting exploited.
   https://www.forbes.com/sites/boazsobrado/2026/07/17/fewer-but-far-more-surgical-crypto-hacks-hit-13-billion-in-2026/