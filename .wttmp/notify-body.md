tweet drafts: AI judges bounties in a day, its own PRs wait weeks for a human

— one-liner —
1a. An AI jury can judge your bounty in a day. A human still hasn't reviewed last month's PR.
1b. 17 days: how long a real, mergeable bug-fix PR has sat unreviewed on an AI-judged bounty protocol's own repo.

— two-punch —
2a. Everyone's worried about AI PR floods drowning human reviewers. Verdikta's problem is the opposite: real human PRs sitting for weeks because nobody's reviewing at all.
2b. Two AI models can verify your bounty work and settle payment the same day. Getting a human to click merge takes noticeably longer.

— paragraph —
3a. The industry's panicking about AI agents flooding maintainers with low-effort PRs nobody can review fast enough. Verdikta has the inverse problem: a handful of real, tested, mergeable fixes from actual contributors, untouched for weeks. Same bottleneck, opposite cause.
3b. mumuzhong3 opened two working PRs fixing real bugs in Verdikta's app repo. Bingmokaka fixed the ETH-prepay flow. Both tested, both mergeable, both still sitting there almost a month later. The protocol judges bounty work in a day. It reviews its own code at a different speed.

— long tweet —
4a. Verdikta's whole pitch is that two independent AI models can score a bounty submission against a public rubric and settle it same-day, on-chain, no human in the loop needed. Meanwhile three genuinely good third-party PRs against its own app repo — real bug fixes, tested, one of them fixing a live ETH-prepay bug — have sat unreviewed for 17 to 27 days. The AI can judge a stranger's work in hours. The team can't review its own contributor's work in weeks. That gap is the actual adoption risk, not the protocol design.
4b. Right now the discourse is all about AI agents flooding repos with junk PRs nobody has time to review. Verdikta's repos show the opposite failure mode: three verified, mergeable, human-written fixes — including a real bug in the payment flow — stuck for 17, 26, and 27 days respectively. Not a slop problem. A capacity problem. And it's happening on the repo of a protocol built to solve exactly this with AI.

— thread opener —
5a. Verdikta judges bounty submissions with two AI models in about a day. Its own pull requests wait weeks for a human. That contradiction is worth a thread.
---
- Bounty #142: submission to on-chain payout, same day, no human in the loop
- verdikta-applications#27/#28 (mumuzhong3): real, tested fixes marked mergeable, ignored 17 days
- verdikta-applications#18 (bingmokaka): fixes a live ETH-prepay bug, ignored 26 days
- verdikta-arbiter#9: failing security scan, unresolved 27 days
- takeaway: AI verification was the easy problem — review capacity is the one nobody's shipped

5b. Everyone's arguing about AI agents flooding GitHub with PRs nobody can review. There's a quieter version of that story happening on an AI-judged bounty protocol's own repo.
---
- the discourse this week: AI agents flooding repos, drowning human reviewers
- Verdikta's repos are the inverse case — real, tested, human-written fixes, not AI slop
- three of them (17, 26, 27 days old) sit untouched despite being mergeable
- one fixes an actual bug in the payment flow
- the irony: instant AI judgment is the product, but the org around it can't keep pace with real contributors

best: #2a — sharpest hook, ties into this week's live AI-PR-flood discourse (confirmed via X search), most shareable
