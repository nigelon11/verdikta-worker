tweets = {
"1a": "x402's \"165M transactions\" headline is five months old. Nobody checks the date before retweeting it.",
"1b": "Real x402 settlement in July: $238,084. The headline number going around this week is 200x that.",
"2a": "Every few days someone posts the same April Coinbase stat like it happened this week. The agent-payment narrative runs on numbers nobody re-verifies.",
"2b": "\"Breaking: 165M agent transactions.\" It broke in April. It's still breaking, apparently, every time someone needs a tweet.",
"3a": "The real story in agent payments isn't the 165M-transaction headline — it's that someone had to build a thread just to explain which numbers are real. July's actual x402 settlement across seven chains was $238K. The gap between the headline and the receipt is the story.",
"3b": "Average x402 payment size dropped from $0.39 to $0.0396 this year. That's not adoption slowing — it's the opposite of what the \"$50B in payments\" headlines imply. Small, frequent, machine-to-machine. The volume numbers people cite don't match the payment-size numbers from the same rails.",
"4a": "Watched three separate accounts this week cite \"165M agent transactions, 69K agents, $50M volume\" as fresh news. It's an April report. Meanwhile the actual July settlement figure — $238,084 across seven chains, four cents average payment — barely circulates. This is the tell for any narrative running ahead of its infrastructure: the big round number travels, the small precise one doesn't. If you're building on these rails, the four-cent number is the one that tells you what's actually happening.",
"4b": "Spent twenty minutes this week tracing one stat back to its source. \"165M agent transactions\" — turns out that's from an April report, still getting quoted as breaking in August. The actual number from last month: $238K settled, seven chains, four cents average. Nobody's lying exactly. They're just not checking dates. In a space this new, the stale stat and the fresh one look identical in a screenshot. That's a problem for anyone building against real signal instead of vibes.",
"5a": "The agent-payment space has a verification problem, not a growth problem. Every headline stat traces back to the same handful of reports, re-dated by whoever's posting it this week.",
"5b": "Next time you see an agent-payment adoption number, ask one thing: what month is that from?",
}
for k, v in tweets.items():
    print(k, len(v))
