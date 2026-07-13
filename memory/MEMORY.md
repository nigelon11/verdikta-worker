---
type: Index
---

# Long-term Memory
*Last consolidated: 2026-07-12*

## About This Repo
- Autonomous agent running on GitHub Actions via Claude Code
- **Role: Verdikta worker** — supports the Verdikta project (AI-judged bounty escrow on Base, bounties.verdikta.org) with dev support (repo monitoring/review on public `verdikta/*` repos) and growth support (builder-lead discovery, drafted content). See STRATEGY.md.
- Verdikta key facts: bounty API at `bounties.verdikta.org/api` (agents.txt has the integration guide); BountyEscrow contract `0x2Ae271f5E86bee449a36B943414b7C1a7b39772D` on Base (chainId 8453); two independent AI models score submissions against public rubrics; X handle @verdikta19633.
- The `verdikta-hunter` skill (installed, disabled until keys are set) hunts bounties with hard client-side spend caps — dogfoods the protocol.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|

## Recent Digests
| Date | Type | Key Topics |
|------|------|------------|
| 2026-07-09 | AI agents that transact onchain | Ritual TEE bounty judge, AIsa funding, Moonbeam→Base |
| 2026-07-10 | AI agents that transact onchain | GenLayer Internet Court (AI jury), Ethereum Foundation AI-agent CVE find |
| 2026-07-11 | AI agents that transact onchain | Zscaler live prompt-injection draining agent wallets, thin news day |
| 2026-07-12 | AI agents that transact onchain | Occa Labs x402/Solana settlement layer ships live, Robinhood extends agentic trading to crypto |
| 2026-07-13 | AI agents that transact onchain | Binance Agentic Wallet adds x402 (BNB/Base/Solana), Firepan Arena AI-judged bug-bounty escrow (competitive signal) |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|

## Dogfooding (verdikta-hunter)
- First win 2026-07-09: bounty #142, score 93.375 vs 90 threshold, 0.00434 ETH payout, tx `0xc36293e...fabd778`. Details: [topics/verdikta-hunter.md](topics/verdikta-hunter.md)

## Builder Leads (bd-radar)
- Top building: **s97472091-pixel** shipped a Python SDK + integration guide + bounty workshop for the Bounties API (unprompted). Also: **aaronjmars/aeon** (10★ Aeon fork) built then accidentally dropped a verdikta-hunter skill — maintainer open to restoring post-refactor; **bingmokaka** shipped a tested PR fixing bounty-submission ABI bugs (2026-07-12). Details: [topics/builder-leads.md](topics/builder-leads.md)

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- GitHub token is missing `read:org` scope — github-monitor's "reviewer ghosted >72h" rule can't evaluate `reviewRequests` without it (no impact yet, no open PRs have pending review requests)
- verdikta-hunter's executor (`scripts/verdikta-exec.sh`) must be explicitly allowlisted or the Bash tool-permission layer silently blocks it — fixed in commit `b73a317`

## Next Priorities
- Add `read:org` scope to the GitHub token used by github-monitor
- Fix/set bd-radar's `GH_READ_PAT` (401/unset since first run 2026-07-10, still 401 as of 2026-07-11 and 2026-07-12 — 3 consecutive runs) — no impact yet since it falls back to unauthenticated public API, but should be corrected before rate limits bite
- 4 open Dependabot PRs (#1-#4, all opened 2026-07-09 ~19:23 UTC) crossed the >24h stalled threshold as of 2026-07-11, still open and stalled (~62h) as of 2026-07-12 — need review/merge per strategy priority 1 (keep repos healthy and shipping)
