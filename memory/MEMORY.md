---
type: Index
---

# Long-term Memory
*Last consolidated: 2026-07-21*

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
| 2026-07-14 | AI agents that transact onchain | Coinbase refocuses Base on trading/payments/agents, SBI+Solana JV AI-agent payment mandate, XRPL hits 1M AI-agent transactions |
| 2026-07-15 | AI agents that transact onchain | Linux Foundation launches x402 Foundation (Circle/Visa/Mastercard), Injective ships iAgent SDK, GenLayer Internet Court reveals 350k tx/day metrics |
| 2026-07-17 | AI agents that transact onchain | Ledger ships open-source Agent Stack (hardware-enforced signing), Visa+Artemis name the agent-dispute-resolution gap, Forbes ties $1.3B H1 hacks to agent-wallet compromise |
| 2026-07-21 | AI agents that transact onchain | Natural raises $30M Series A for AI-agent payment rails vs Stripe (hybrid stablecoin+bank, not onchain-only) — thin day otherwise, 4 stale/unverified X leads rejected |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|
| shiplog | 2026-07-13 | Weekly PR/commit/star digest across public `verdikta/*` repos; first run established star baseline (verdikta-docs 72, verdikta-applications 24, verdikta-arbiter 22, verdikta-dispatcher 17, verdikta-roadmap 0). Correctly excluded 19 PRs to private `verdikta-agents` per STRATEGY.md public-repos-only constraint. |

## Dogfooding (verdikta-hunter)
- First win 2026-07-09: bounty #142, score 93.375 vs 90 threshold, 0.00434 ETH payout, tx `0xc36293e...fabd778`. Details: [topics/verdikta-hunter.md](topics/verdikta-hunter.md)

## Builder Leads (bd-radar)
- Top building: **s97472091-pixel** shipped a Python SDK + integration guide + bounty workshop for the Bounties API (unprompted), then kept escalating Jul7–16 with 3 case-study repos, a hosted `verdikta-playbook` site, a Medium deep-dive on a 99/100-scored bounty, and a new bounty-#147 evidence repo (7th straight bd-radar run with fresh output) — highest-intent lead so far, now quiet 07-17 through 07-20 (4th consecutive quiet day, no repo since bounty-147). **@AjAkmarudi72937** (previously flagged as possibly-scripted) shifted to genuine amplification of that work on 2026-07-14. Also: **aaronjmars/aeon-agent** (renamed from `aeon`, 10★ Aeon fork) built then accidentally dropped a verdikta-hunter skill — maintainer open to restoring post-refactor, last pushed 2026-07-19, no new push since, skill still not restored; **bingmokaka** shipped a tested PR fixing bounty-submission ABI bugs (2026-07-12). A bounty-farming boilerplate cluster (`Zetav1`) spread from `verdikta-docs` to a second repo (`verdikta-dispatcher`) on 2026-07-14 — watch, not yet a lead. **`NSPG13/agent-bounties`** (found 2026-07-16) — a direct, fast-shipping competitor (AI-agent bounty protocol on Base, 288 PRs merged since 2026-07-08) whose repo contains a detailed writeup of Verdikta's own design pulled from our agent API/whitepaper — competitive intel, worth the operator's own read, still shipping as of 07-19. **Flag for engagement:** **@Project0_Z** made a 2-for-2 pattern of unprompted, organic third-party advocacy (recommended Verdikta's AI-jury API to two different third-party projects, 2026-07-16/17) — low engagement but high-quality signal; mention-radar (2026-07-18) flags a reply/DM as a cheap, high-value engagement opp. Full detail: [topics/builder-leads.md](topics/builder-leads.md)

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- GitHub token is missing `read:org` scope — github-monitor's "reviewer ghosted >72h" rule can't evaluate `reviewRequests` without it (no impact yet, no open PRs have pending review requests)
- verdikta-hunter's executor (`scripts/verdikta-exec.sh`) must be explicitly allowlisted or the Bash tool-permission layer silently blocks it — fixed in commit `b73a317`
- digest, write-tweet, and now github-monitor (07-18 through 07-20) all hit `/tmp` writes and `rm` blocked mid-run (sandbox), leaving non-sensitive stray temp files (xAI payload/response JSON, char-count scripts, a composed notify body) in the repo root/`.runtmp/` — confirmed still present as of 2026-07-21, untracked/gitignored so invisible to `git status`; safe to delete but memory-flush can't (destructive-op gate excludes `rm`); needs a skill-side fix (write temp files under a repo-tracked scratch dir the skill itself cleans via its own allowed tools, not `/tmp`+`rm`)

## Next Priorities
- Add `read:org` scope to the GitHub token used by github-monitor
- Fix/set bd-radar's `GH_READ_PAT` (401/unset since first run 2026-07-10, still 401 through 2026-07-20 — 11 consecutive runs) — no impact yet since it falls back to unauthenticated public API, but should be corrected before rate limits bite
- 4 open Dependabot PRs (#1-#4, all opened 2026-07-09 ~19:23 UTC, this repo `nigelon11/verdikta-worker`) crossed the >24h stalled threshold as of 2026-07-11, still open and stalled (~254h) as of 2026-07-20 — need review/merge per strategy priority 1 (keep repos healthy and shipping)
- `verdikta-applications#18` (bingmokaka, tested ETH-prepay fix, opened 2026-07-10) crossed the 48h-idle threshold 2026-07-18, still open (~110h since last update as of 2026-07-20) — a real, useful third-party contribution stalled on review; merge/review per strategy priority 1
- 4 draft "backlog workflow guidance" PRs opened 2026-07-14 across `verdikta-applications#25`, `verdikta-arbiter#9` (also has a failing Gitleaks Secret Scan), `verdikta-dispatcher#5`, `verdikta-docs#7` — excluded from github-monitor's tiers while draft/<7d old (~135h as of 07-20), all four cross the 168h/7d threshold around 2026-07-21 evening/07-22; check next run whether any (especially arbiter#9) escalate to ACT_NOW once they clear draft or age past 7d
- Clean up stray non-sensitive temp files left in repo root/`.runtmp/` by digest/write-tweet/github-monitor sandbox workarounds (see Lessons Learned) — still present as of 2026-07-21, low priority, not secret-bearing
- **Operator read recommended:** `NSPG13/agent-bounties` (found 2026-07-16 by bd-radar) is a direct, fast-shipping competitor on Base whose `docs/competitor-learning-plan.md` dissects Verdikta's own design in detail — see [topics/builder-leads.md](topics/builder-leads.md) for the summary and links.
