tweets = {
"1a": "Killing 20 candidate stories to publish zero is the job. Publishing 20 unverified ones is most of the industry.",
"1b": "Most 'AI x crypto news' is the same three stories wearing a new publish date.",
"2a": "Today's raw pull: about 20 candidate stories. Survivors after verification: zero. Third empty day this run — and every kill has a documented, checkable reason.",
"2b": "A hack from January reheated as breaking news. A December paper relaunched as fresh research. The same spam account making the same claim, fourth day running. Tuesday.",
"3a": "A zero-story day reads as a failure. It isn't. Every pitch that got killed today had a specific, checkable reason: already reported, verified stale by months, or a claim nobody could source past one promotional post. The actual failure is publishing the twenty that didn't survive that check.",
"3b": "Pulled about 20 candidate stories today. One 'hack' turned out to be from January. One 'new research' was a December paper wearing a fresh headline. One account has run the same unverifiable claim for four straight days. Checked all twenty, killed all twenty, published zero. That's the filter working, not failing.",
"4a": "Here's what a zero-story day actually involves: about 20 raw candidates in, each one checked against a publish date, a primary source, and whether it's already been reported in the last 72 hours. Today that killed a $27M 'AI-agent hack' that actually happened in January, a smart-contract research paper republished with a new headline three months late, an oracle exploit with zero AI angle padded in to look on-topic, and a recurring spam account running the identical unverified claim for a fourth straight day. Zero of the twenty survived. Nothing got published. That is not the process failing — publishing any of those twenty would have been the failure.",
"4b": "Why do so few outlets kill a story once they've already started writing it? We pulled about 20 AI-agent-x-crypto candidates today. Half were duplicates of stories already reported this week. A third turned out to be months old once we checked the actual publish date. The rest were single promotional posts with no verifiable claim behind them. Verifying and killing all twenty took longer than writing any one of them would have. Zero published today. That's the tradeoff nobody wants to make: speed, or being right.",
"5a": "The hardest part of covering AI-agent crypto isn't finding stories. It's killing the twenty that looked real for about five minutes.",
"5b": "Three empty news days this month, and each one took more verification work than a normal day did. That's not a coincidence.",
}
for k, v in tweets.items():
    print(k, len(v))
