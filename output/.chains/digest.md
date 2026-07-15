ℹ️ Digest: AI agents onchain

*AI agents that transact onchain — agent payments, AI-judged bounties, decentralized AI oracles — 2026-07-15*

_TL;DR: Circle, Visa, Mastercard and Google just gave the AI-agent payment rail (x402) formal governance under the Linux Foundation, while Injective shipped a packaged SDK for building onchain trading agents and GenLayer's AI-jury system published its first real cost/throughput numbers._

1. *Circle, Visa, Mastercard join x402 Foundation as Linux Foundation formalizes AI-agent payments*
   The Linux Foundation operationally launched the x402 Foundation on July 14 — open governance for the HTTP-402 payment protocol AI agents use for micropayments. Circle joined as a premier member alongside Visa, Mastercard, AWS, Google, Stripe, Coinbase, Ripple, and 30+ others. The protocol already clears ~75M transactions / $24M value monthly (30-day rolling, ~32¢ avg).
   Why it matters: the rail agents already move money through just gained vendor-neutral governance and mainstream financial backing — lower platform risk for anyone building agent-payment flows on it.
   https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications

2. *Injective ships installable SDK for autonomous onchain trading agents*
   Injective launched its iAgent SDK (`npm install -g @injectivelabs/ainj`) on July 14 — market data, wallet queries, order execution, and cross-chain bridging bundled for Claude Code/Cursor-style MCP agents, on a chain with 650ms finality and ~$0.0003/tx fees.
   Why it matters: agent tooling is moving from bespoke integration to packaged SDKs — the same maturation curve bounty-hunter agents are on.
   https://www.theblock.co/post/327262/injective-launches-sdk-that-lets-users-create-their-own-onchain-ai-agent

3. *GenLayer's AI-jury "Internet Court" reveals real numbers: 350k cases/day, $0.85–1.45 each*
   Mainstream coverage this week quantified GenLayer's multi-LLM jury system (first reported 07-10): a 27-company consortium (OKX, MetaMask, BNB Chain, ZKsync) is running it in beta at ~350k transactions/day, with 5-validator juries — each a different LLM — resolving disputes in 30–60 minutes for $0.85–1.45/case.
   Why it matters: first hard cost/latency benchmark from the closest AI-jury comparable to Verdikta's two-model design.
   https://www.forbes.com/sites/ninabambysheva/2026/07/10/all-rise-internet-court-for-ai-agents-is-in-session/

*Also worth a glance:* TermiX launched an escrow-based agent marketplace on BNB Chain (announced 07-07; mainnet timing/metrics still unverified) · OttoAI's claimed "20k+ x402 payments in 5 days" remains a single-source, unconfirmed number.