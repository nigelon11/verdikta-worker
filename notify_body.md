tweet drafts: AI agents getting their wallets drained via prompt injection

— one-liner —
1a. An AI agent holding its own private key isn't automation. It's an attack surface with a bank balance.
1b. Every "AI agent with a wallet" story ends the same way: someone finds the prompt that empties it.

— two-punch —
2a. Zscaler just found sites hiding prompt injections that trick AI agents into paying out crypto. The agent isn't hacked. It's just doing what it was told.
2b. We spent years teaching agents to transact autonomously. Turns out the hard part was never the transacting. It's making sure the instruction came from you.

— paragraph —
3a. The pattern in every recent agent-wallet drain is the same: intelligence and authorization live in the same place. One poisoned prompt and the thing that reasons is also the thing that signs. Separate those and the exploit stops being catastrophic.
3b. A researcher tricked Grok's wallet integration with Morse code hidden in a prompt and drained funds. Not a bug. A design choice: one model with both judgment and signing power. Every agent wallet built that way is one clever prompt from empty.

— long tweet —
4a. Zscaler's latest research: malicious sites hiding prompt injections that quietly instruct AI agents to make crypto payments, poisoning the agent's context with fake "trusted" sources along the way. The agents aren't being tricked into bad reasoning — they're being handed fake instructions and reasoning correctly from bad premises. That distinction matters because it means better models don't fix this. Only separating "can reason" from "can authorize" does: per-transaction caps, allowlists, a second independent check before funds move.
4b. Every agent-payments postmortem this year has the same root cause. A single model holds both judgment and signing authority, so one successful injection is one successful theft. The fix nobody wants to build: authorization that doesn't trust any single model's output, backed by hard spend limits and a second, independent check before value moves. Slower. Also the only version that survives contact with an adversarial prompt.

— thread opener —
5a. Every AI-agent-drains-wallet story this month has the same root cause, and it isn't a smarter attacker. [+ 5-beat thread sketch]
5b. Nobody built agent-payment security. They bolted a wallet onto a chatbot and called it autonomy. [+ 5-beat thread sketch]

best: #4a — most specific and actionable: names the failure mode (poisoned context, not "bad reasoning") and the actual fix (separate reasoning from authorization), grounded in today's Zscaler research + the May Grok wallet drain.

source: xai=ok (http=200), 5 X posts pulled for sentiment context
