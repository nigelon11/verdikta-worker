ℹ️ Digest: AI agent payments / bounties / oracles

*AI agents that transact onchain — agent payments, AI-judged bounties, decentralized AI oracles — 2026-07-09*

_TL;DR: Base keeps absorbing agent-payment infra — Ritual shipped a live TEE-judged bounty demo, AIsa raised $6.5M on concrete adoption numbers, and Moonbeam is relocating its AI-agent network to Base by July 31._

1. *A builder shipped a live on-chain AI bounty judge — different trust model than Verdikta*
   A solo dev built and deployed an AI bounty judge on Ritual Chain: post a task and prize, players submit, an LLM reads every submission inside a TEE and pays the winner in one transaction, with hardware-signed attestation of what ran instead of a human referee.
   Why it matters: single-model + TEE attestation is a live alternative to Verdikta's two-model jury + escrow — worth benchmarking for dispute resistance and cost.
   https://ai-bounty-judge.vercel.app/

2. *AIsa raises $6.5M to build a payment layer AI agents can transact through*
   Alibaba and Tribe Capital co-led a seed round for AIsa, a network letting agents discover and pay for APIs, data, and compute through one programmable interface. The company reports 50,000+ agents onboarded without paid marketing and top-seller status in the x402 ecosystem.
   Why it matters: real adoption numbers (not projections) on the same x402 rails a Verdikta agent integration would use.
   https://www.globenewswire.com/news-release/2026/07/07/3323663/0/en/AIsa-Raises-6-5M-Co-Led-by-Alibaba-and-Tribe-Capital-to-Build-the-Transaction-Network-for-AI-Agents.html

3. *Moonbeam abandons Polkadot, moves its AI-agent network to Base*
   Moonbeam announced GLMR is migrating 1:1 to a Base ERC-20 token, with the parachain winding down after July 31 and a new Moonbeam Protocol — an on-chain agent communication and settlement network — launching on Base. Holders must bridge before the deadline.
   Why it matters: another agent-settlement project picks Base as home, adding builder density on the exact chain bounties.verdikta.org runs on.
   https://moonbeam.network/news/moonbeam-strategic-update-moonbeam-network-relaunches-on-base/

*Also worth a glance:* OpenCovenant runs a live x402 seller with USDC escrow on Solana mainnet for autonomous coding agents — a working escrow pattern outside the EVM world (github.com/open-covenant/covenant).