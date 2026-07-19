tweets = {
"1a": "Killing 20 stories to publish zero is the job. Publishing 20 unverified ones is the industry.",
"1b": "Most 'AI x crypto news' is the same three stories wearing a new publish date.",
"2a": "Today's raw pull: about 20 candidate stories. Survivors after verification: zero. Third empty day this run — and every kill has a documented, checkable reason.",
"2b": "A hack from January reheated as breaking news. A December paper relaunched as fresh research. Same spam account, same claim, fourth day running. Tuesday.",
"3a": "A zero-story day reads as failure. It isn't. Every pitch killed today had a specific reason: already reported, verified stale by months, or sourced to one promotional post and nothing else. The real failure would've been publishing the twenty that didn't survive that check.",
"3b": "Pulled 20 candidate stories today. One 'hack' was actually from January. One 'new research' was a December paper wearing a fresh headline. One account ran the identical unverifiable claim for a fourth straight day. Checked all twenty, killed all twenty, published zero.",
"4a": "Here's what a zero-story day actually involves: about 20 raw candidates in, each checked against a publish date, a primary source, and whether it's already been reported in the last 72 hours. Today that killed a $27M 'AI-agent hack' that actually happened in January, a research paper republished with a new headline months late, an oracle exploit with no AI angle padded in to look on-topic, and a spam account running the same unverified claim for a fourth straight day. Zero of the twenty survived. Publishing any of them would have been the failure — not zero output.",
"4b": "Why do so few outlets kill a story once they've started writing it? We pulled about 20 AI-agent-x-crypto candidates today. Half were duplicates already reported this week. A third turned out to be months old once we checked the real publish date. The rest were single promotional posts with no verifiable claim behind them. Verifying and killing all twenty took longer than writing any one would have. Zero published. That's the tradeoff nobody wants to make: speed, or being right.",
"5a": "The hardest part of covering AI-agent crypto isn't finding stories. It's killing the twenty that looked real for about five minutes.",
"5b": "Three empty news days this month, and each one took more verification work than a normal day did. That's not a coincidence.",
}
for k, v in tweets.items():
    print(k, len(v), "OVER" if len(v) > (600 if k.startswith("4") else 280) else "")
