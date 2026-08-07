ℹ️ Tweet Drafts

tweet drafts: Apple's bug bounty AI-slop failure

— one-liner —
1a. A real $200K macOS exploit sat unpatched because Apple's bug bounty inbox was buried in AI slop.
1b. Every bounty program has the same failure mode now: too much AI noise, not enough triage bandwidth.

— two-punch —
2a. Bynario found 50+ real macOS bugs with ChatGPT, one worth $200K. Apple's team was so buried in AI submissions they missed it — and only patched after direct outreach.
2b. The problem was never AI finding bugs. It's that nobody built triage for a world where anyone can generate hundreds of plausible-looking reports for free.

— paragraph —
3a. Bynario found a $200K macOS exploit chain using ChatGPT. Apple's bounty inbox was so flooded with AI slop the submission got capped and buried — until Bynario reached out directly. The bug got patched. The process didn't.
3b. Manual triage assumed submissions were expensive to produce. AI made them free. Apple's bug bounty is now proving what happens when a system built for scarcity meets a world of infinite cheap submissions: real signal gets lost in the noise.

— long tweet —
4a. Apple capped open bug bounty submissions because AI-generated slop reports overwhelmed the queue. Inside that noise: Bynario, using ChatGPT, found 50+ real macOS bugs — including a $200K exploit chain (CVE-2026-43760) — that got buried and only patched after direct outreach. The lesson isn't ban AI submissions. It's that triage built for a handful of expert reports a month can't survive a world where anyone can generate hundreds of plausible-sounding ones. You need a system built for that volume from day one, not a queue and a prayer.
4b. Here's the actual failure mode in Apple's bug bounty story: a first-come inbox has no way to rank submissions, so it either lets everything through or caps volume and buries the good ones with the bad. Both are the wrong axis. What you actually need is a way to score every submission against a fixed rubric regardless of how many arrive — that's the only design where a $200K exploit chain and a slop report get sorted correctly in the same pass, at any volume.

— thread opener —
5a. Apple's bug bounty just proved a rule that's about to hit every open submission system: once submissions are free to generate, first-come triage collapses. A $200K macOS exploit sat buried in AI slop for weeks. Here's what actually breaks, and what doesn't.
5b. Apple built one of the best bug bounty programs in the industry. AI just found the one thing it wasn't built for: infinite cheap submissions. A real $200K exploit got lost in the noise. Here's what that means for every bounty program still running the old model.

best: #4b — sharpest technical reframe (rank-by-arrival vs. score-by-rubric), no hype