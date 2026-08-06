ℹ️ Digest: AI agents that transact onchain

*AI agents that transact onchain — agent payments, AI-judged bounties, decentralized AI oracles — 2026-08-06*

_TL;DR: Singapore's MAS puts agentic AI under binding risk-management guidelines, Microsoft and GitHub take opposite paths on the same AI-driven bounty-submission flood, and researchers document the first real agent-vs-agent exploit in production._

1. *Singapore's MAS confirms agentic AI falls under its binding AI risk guidelines*
   In an Aug 5 parliamentary reply, MAS said its AI Risk Management Guidelines — finalizing soon from a Nov 2025 consultation — cover agentic AI like any other AI use case, rather than leaving agents to the voluntary SAFR runtime framework industry published in July.
   Why it matters: first major financial regulator to put a concrete, soon-binding guideline (not just a best-practices doc) under autonomous agents transacting for financial institutions.
   https://www.techtimes.com/articles/323283/20260806/mas-confirms-agentic-ai-inside-binding-bank-rules-us-eu-fall-behind.htm

2. *Microsoft pays record $20M in bug bounties as GitHub goes the opposite way*
   MSRC's year-in-review (Aug 4): $20M+ paid to 562 researchers (avg ~$35k, top payout $200k), explicitly citing an AI-driven rise in submission volume — the same pressure that made GitHub halve payouts and gate access behind an invite-only tier on July 27.
   Why it matters: two platforms hit the identical AI-submission-volume bottleneck and chose opposite fixes — pay more humans to triage vs. restrict who can submit — neither scales the judging step itself.
   https://www.microsoft.com/en-us/msrc/blog/2026/08/microsoft-bounty-program-year-in-review-more-than-20-million-awarded-biggest-year

3. *First documented case of one AI agent exploiting another in production*
   Pillar Security (published Aug 3-4) found a low-privilege, public-facing triage agent in Google's adk-python repo could be manipulated via a poisoned GitHub issue into invoking a high-privilege maintainer agent — real agent-to-agent privilege escalation, not a lab demo. Google fixed it and paid a $10k bounty.
   Why it matters: the attack surface for multi-agent systems isn't just human-to-agent prompt injection anymore — any protocol where one agent's output triggers another agent's action now has a demonstrated exploit pattern to defend against.
   https://www.theregister.com/security/2026/08/03/google-dev-kit-spurs-first-ever-agent-on-agent-violence/5282496