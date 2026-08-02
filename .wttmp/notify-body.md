tweet drafts: Verdikta's rubric hardening — objective checks gate the AI jury

— one-liner —
1a. Verdikta patched a bounty exploit with a dumber rule, not a smarter AI.
1b. An AI jury can be gamed. A hard pass/fail check can't be argued with.

— two-punch —
2a. A hunter deleted a paid deliverable. Verdikta's fix: proof it stays online for 7 days, verified on archive.org.
2b. Everyone wants a smarter AI judge. Verdikta's actual fix for gaming was a boring HTTP-200 check that doesn't care what the models think.

— paragraph —
3a. A Verdikta bounty required a live URL. Cloudflare returned a 403. Four submissions scored zero — not because two AI models disagreed, but because the objective check ran first and failed. No appeal, no re-vote. That's the design working.
3b. Most "AI-judged" systems put the model in charge of everything, so gaming the model games the whole system. Verdikta's rubrics increasingly gate the AI jury behind deterministic checks — archive.org proofs, HTTP-200 pings — so consensus can't override a fact.

— long tweet —
4a. A hunter got paid for a bounty, then deleted the deliverable they were paid to keep live. Verdikta's response wasn't a smarter jury — it was archive.org. New bounties in that class now require a 7-day persistence proof before payout counts as final. Compare that to how most "AI-judged" systems handle gaming: retrain the model, add a prompt rule, hope it generalizes. Verdikta just closed the door with a fact the model can't argue with. Two independent models can disagree on quality. They can't disagree on whether a URL returns 200 or 403.
4b. The interesting part of Verdikta's bounty #153 rubric fix isn't that a hunter tried to game it — people always try. It's what "harden the rubric" meant in practice: not more AI, not a bigger jury, just a deterministic check (archive.org persistence, HTTP-200 accessibility) placed ahead of the two-model consensus. When four submissions on a content bounty hit a Cloudflare 403, they scored zero regardless of what the models thought of the writing. That's a design choice worth copying: let AI judge subjective quality, let dumb checks gate objective fact.

— thread opener —
5a. Verdikta's AI jury got gamed once. The fix wasn't a smarter model — it was a dumber check placed in front of it.
---
- Bounty #153: hunter got paid, then deleted the deliverable they were required to keep live
- Fix: rubric now requires a 7-day archive.org persistence proof before payout is final
- Second case: HTTP-200 accessibility check zeroed 4 submissions on Cloudflare 403 — the AI jury never got a vote
- Pattern: AI judges subjective quality, deterministic checks gate objective fact
- Why that split matters for anyone building an "AI-judged" system

5b. An on-chain bounty market with a two-model AI jury is going to get gamed. The interesting question is what you do next.
---
- What gaming an AI judge actually looks like in practice
- Verdikta's answer: out-fact the gaming, not out-AI it — archive.org proofs, HTTP-200 checks, deterministic gates
- The Cloudflare-403 case: 4 submissions zeroed, no AI consensus needed
- Contrast: most "AI-judged" systems respond to gaming by tuning the model — slower, never fully closes the hole
- Takeaway: the AI jury's job should shrink, not grow, as a protocol matures

best: #4b — long tweet / builder's breakdown, ties two dated examples to a reusable design principle

— two-punch —
2a. $200M in agent trading volume on Robinhood Chain in under a month. Impressive activity — but activity isn't the same as agents completing verified work.
2b. Everyone's celebrating agents trading $200M with each other. The harder problem — proving an agent actually did the job it was paid for — nobody's solved yet.

— paragraph —
3a. Virtuals crossed $200M in agent trading volume on Robinhood Chain — 5,600 agents in three weeks. Every headline treats volume as the metric that matters. But volume measures activity, not whether an agent delivered what it was paid for. Verification is still missing.
3b. $200M moved between AI agents in three weeks and the headline is "the agent economy is real." Sure, agents are real. Whether any of them completed the task they were paid for is a separate question nobody's tracking. Trading is easy. Judging outcomes is the hard part.

— long tweet —
4a. Virtuals crossed $200M in agent trading volume on Robinhood Chain — 5,600 agents, ramping $77M to $150M to $200M in three weeks. Real milestone for agent-to-agent commerce. But look at what's measured: volume between agents, not outcomes delivered by agents. Moving $200M proves liquidity exists — it proves nothing about whether an agent hired to do a task actually did it, or did it well. Agents that transact is one leg. Verifying what they transacted for is the other. Most of the industry is only building the first.
4b. Everyone keeps citing agent trading volume like it is the whole story. $200M on Robinhood Chain, 5,600 agents, three weeks — a real liquidity stat. But trading volume between agents is the easy half of agents that transact. The hard half is verifying an agent hired to do work actually did it before it gets paid. That is a judging problem, not a plumbing problem, and almost nobody tracks it. Until they do, agent economy numbers measure motion, not delivery.

— thread opener —
5a. $200M in AI agent trading volume just hit Robinhood Chain in three weeks. Impressive — and almost entirely beside the point.
5b. Robinhood Chain agents just moved $200M in three weeks. Here is the part nobody is asking: how many of those agents were verified to do what they were paid for?

best: #3a — tightest structural critique, lands "volume vs. delivered work" in one breath
