ℹ️ Digest: AI agents that transact onchain

*AI agents that transact onchain — agent payments, AI-judged bounties, decentralized AI oracles — 2026-07-25*

_TL;DR: A new academic audit found exploitable vulnerabilities in every major x402 payment facilitator tested — including Coinbase's own — the exact rail this month's agent-payment announcements have been built on._

1. *Academic audit finds exploitable holes in every x402 payment facilitator, including Coinbase's*
   Researchers from EPFL, Zhejiang University, and an independent auditor tested all 15 major x402 facilitators (99% of transaction volume, 60K+ sellers, 360K+ buyers) and found 49 security-rule violations translating to 31 previously unknown vulnerabilities — payment replay, wallet drain via overpayment, prompt-injection-triggered fraudulent payments, and privacy leakage. Coinbase, the largest facilitator in the sample ($26.85M of the volume tested), acknowledged the findings via responsible disclosure and shipped mitigations, as did the other vendors.
   Why it matters: x402 is the rail nearly every agent-payments story this month has run on (Coinbase Business, AWS Bedrock AgentCore, Binance Agentic Wallet, the x402 Foundation) — a systemic, cross-vendor security finding outweighs any single integration announcement.
   https://arxiv.org/abs/2607.19545

Quiet day otherwise: Coinbase's follow-up stats on its Business x402 rollout (~$1B cumulative volume, ~5,000 customers) are the same story already led on 07-24, not a new one. A wave of OKX/BNB/AEON/Ledger X posts recycled older launches (OKX Agentic Wallet, BNB Chain's ERC-8183 escrow SDK from May, Ledger Agent Stack from 07-16). Natural's $30M round, GenLayer Internet Court, and the OpenAI/Hugging Face autonomous-hack story were all confirmed already-covered or off-topic (no onchain angle) on verification.