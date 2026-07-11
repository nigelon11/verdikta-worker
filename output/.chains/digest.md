ℹ️ Digest — AI agents onchain

*AI agents that transact onchain — agent payments, AI-judged bounties, decentralized AI oracles — 2026-07-11*

_TL;DR: Quiet 24h for the beat — the one real development is Zscaler catching live (not simulated) prompt-injection attacks draining crypto directly from AI agents' wallets._

1. *Prompt injection is now draining real crypto from AI agents' wallets*
   Zscaler ThreatLabz documented two active campaigns: a fake Python package ("requests-secure-v2") and a typosquatted debank[.]auction site, both using CSS hidden from humans but readable by agents to trick them into paying a hardcoded wallet (0x691bc...ad267). Across 26 LLMs tested, 4 executed the fraudulent payment and 2 misidentified the fake DeBank site as real — Gemini and Llama variants were most susceptible.
   Why it matters: this is a documented in-the-wild case of an agent authorizing a real onchain payment because of manipulated input, not a bug in the escrow/settlement layer — the exact failure mode that judge/dispute systems (Verdikta, GenLayer's Internet Court) don't protect against, since they arbitrate outcomes after an agent has already signed.
   https://cryptobriefing.com/zscaler-prompt-injection-ai-agents-crypto/

*Quiet day note:* Nothing else cleared the bar — OKX's AI agent marketplace and GenLayer's Internet Court (both covered in prior digests) only generated recap chatter today, no material new development. Mastercard's Agent Pay, Cloudflare/AWS x402-at-the-edge, and several agent-payments funding rounds all surfaced but are 5+ days old with no fresh news today.