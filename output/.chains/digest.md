ℹ️ Digest

*AI agents that transact onchain — agent payments, AI-judged bounties, decentralized AI oracles — 2026-08-19*

_TL;DR: Quiet day — the one verifiable development is AWS taking its agent-payment rail from preview to production, expanding standard support and safety caps for autonomous machine payments._

1. *AWS makes agent payments a mainstream cloud primitive*
   Amazon Bedrock AgentCore Payments moved from preview to general availability (Aug 18), adding a second payment standard (Stripe/Tempo's MPP) alongside x402, an "upto" spending-ceiling scheme, and one-click Coinbase credential setup; Cloudflare joins as a merchant-side integration alongside Coinbase and Stripe Privy wallets.
   Why it matters: every payment session now enforces a hard max-spend + expiry check at the infrastructure layer before AWS will sign a transaction — a hyperscaler shipping deterministic spend guardrails as a default, not an add-on, raises the bar for what "safe" agent payments means industry-wide.
   https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-payments-is-now-generally-available-enabling-agents-to-transact-safely-and-autonomously-at-scale/

*Quiet news day — 14th thin/empty day in the last 15. Everything else checked out stale or recycled: OKX's "new" agent payment protocol (actually Apr 30), the "Legal Context Protocol" dispute layer (actually Jun 25, same AAA effort flagged stale before), Visa's Agent Score/Agentic Directory (Jun 10), Cloudflare Kitesurf/Wallets (Aug 4-6, already covered), Chainlink's "AI agent product" (recap of the Aug 14 Chainlink-for-Agents launch), and Coinbase's 69K-agent/165M-tx/$50M stat (still the same April figure recirculating).*