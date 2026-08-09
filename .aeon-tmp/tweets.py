tweets = {
"1a": "Spend caps stop agents from overspending. They don't stop agents from doing bad work.",
"1b": "A wallet that caps how much an agent can spend still can't tell you if the spend was worth it.",
"2a": "MetaMask just gave AI agents spend caps and $10K in loss coverage. Good start - but a cap only bounds the damage. It doesn't verify the agent did the job right.",
"2b": "Everyone's racing to solve 'how much can an agent spend.' Almost nobody's solving 'was what it did any good.' That's the harder, more valuable problem.",
"3a": "MetaMask's Agent Wallet ships allowlists, spend caps, and loss coverage for AI agents moving money on-chain. Genuinely useful infrastructure. But every layer contains failure after the fact - nothing checks whether the agent's output was actually correct before the funds move.",
"3b": "Insurance against agent mistakes is a bet that agents will keep making them. $10K/mo loss coverage is a good hedge. It's also an admission that nobody's cracked verifying agent output before payment - so the industry is pricing the failure instead of preventing it.",
"4a": "Agent-payment infra has spent 2026 solving the wrong layer of the problem. Spend caps, allowlists, transaction simulation, threat detection, loss coverage - MetaMask's Agent Wallet stacks all of it, and it's genuinely good work. But every one of those controls answers 'how much can this agent move' or 'is this destination safe.' None of them answer 'did the agent actually do what it was paid to do.' An agent can stay under its cap, hit an allowlisted address, and still deliver garbage. Spend control and output verification are different problems.",
"4b": "Watched three different teams ship 'safety' for AI agent payments this year - wallets with caps, escrow with timeouts, insurance with payout ceilings. Not one of them asks whether the work behind the payment was any good. That's not a safety feature, it's a liability cap. The actual hard problem - verifying an agent's output before money moves, not just bounding what happens if it's wrong - is still mostly unsolved, and it's the one worth building.",
"5a": "MetaMask's Agent Wallet solves how much an agent can spend. It doesn't solve whether what it did was worth paying for.",
"5b": "The AI-agent-payments stack has three layers: custody, spend control, and verification. Everyone's shipping the first two.",
}

for k, v in tweets.items():
    print(k, len(v))
