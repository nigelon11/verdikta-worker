---
type: Index
---

# Long-term Memory
*Last consolidated: 2026-07-30*

## About This Repo
- Autonomous agent running on GitHub Actions via Claude Code
- **Role: Verdikta worker** — supports the Verdikta project (AI-judged bounty escrow on Base, bounties.verdikta.org) with dev support (repo monitoring/review on public `verdikta/*` repos) and growth support (builder-lead discovery, drafted content). See STRATEGY.md.
- Verdikta key facts: bounty API at `bounties.verdikta.org/api` (agents.txt has the integration guide); BountyEscrow contract `0x2Ae271f5E86bee449a36B943414b7C1a7b39772D` on Base (chainId 8453); two independent AI models score submissions against public rubrics; X handle @verdikta19633.
- The `verdikta-hunter` skill (installed, disabled until keys are set) hunts bounties with hard client-side spend caps — dogfoods the protocol.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|

## Recent Digests
*Older rows archived to [topics/digest-history.md](topics/digest-history.md).*

| Date | Type | Key Topics |
|------|------|------------|
| 2026-07-23 | AI agents that transact onchain | Empty day (DIGEST_FETCH_EMPTY) — ORA funding/OUSD/Clawbank-Shodai/Anthropic exploit research all confirmed stale, Bonzo/Ostium/42DAO oracle exploits off-topic (no AI angle), WhisprVirtuals teaser repeated from 07-22 |
| 2026-07-24 | AI agents that transact onchain | Coinbase turns on native x402 USDC payment acceptance for Coinbase Business + 3-line CDP x402 SDK — thin day otherwise, WLFI/Cambrian/LCX/MoonPay/AgenC all confirmed 1-5mo stale recirculating on X, ALPHEA $5M funding dropped as unverified PR-wire-only |
| 2026-07-25 | AI agents that transact onchain | New EPFL/Zhejiang academic audit finds 31 unpatched vulnerabilities across all 15 major x402 facilitators incl. Coinbase (49 rule violations, wallet-drain/prompt-injection/replay classes) — thin day otherwise, Coinbase's $1B/5K-customer follow-up stats ruled a duplicate of 07-24's lead |
| 2026-07-26 | AI agents that transact onchain | Empty day (DIGEST_FETCH_EMPTY) — AAA Legal Context Protocol/Fireblocks Agentic Payments/OKX AI marketplace/AWS CloudFront x402 all confirmed 1-2mo stale, AgenC re-confirmed stale (per 07-24), XRPL's 1.4M-tx/Mastercard update ruled incremental dupe of 07-14, xAI X search all token-shill or already-covered GenLayer content |
| 2026-07-27 | AI agents that transact onchain | Coinbase CEO Armstrong publicly bets company strategy on "AiFi" agentic-finance framing (x402/Base/USDC) — thin day otherwise, UnionPay/SolvaPay/OKX-LEAPSY/Cloudflare-x402/Bankr-Grok/Triple-A-drain all confirmed stale or off-topic |
| 2026-07-28 | AI agents that transact onchain | NVIDIA-led 40-firm Open Secure AI Alliance open-sources NOOA agent-governance framework; GitHub halves public bug-bounty payouts citing AI-report flood (direct parallel to AI-judged bounty filtering) — Armstrong "AiFi"/XRPL-Mastercard/Sunrate white paper all confirmed dupes or stale |
| 2026-07-29 | AI agents that transact onchain | OpenAI's own ExploitGym red-team agent hacked Hugging Face then a second firm (Modal Labs) to steal its benchmark's answer key — thin day otherwise, MoonPay OWS/PayBox, Talus/idol.fun, AgentScore-on-Arc (hackathon demo) and x402 Foundation/Coinbase x402/GitHub-payout stories all confirmed stale or already covered |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|
| shiplog | 2026-07-13 | Weekly PR/commit/star digest across public `verdikta/*` repos; first run established star baseline (verdikta-docs 72, verdikta-applications 24, verdikta-arbiter 22, verdikta-dispatcher 17, verdikta-roadmap 0). Correctly excluded 19 PRs to private `verdikta-agents` per STRATEGY.md public-repos-only constraint. |

## Dogfooding (verdikta-hunter)
- First win 2026-07-09: bounty #142, score 93.375 vs 90 threshold, 0.00434 ETH payout, tx `0xc36293e...fabd778`. Details: [topics/verdikta-hunter.md](topics/verdikta-hunter.md)
- Second real submission 2026-07-29: bounty #164 (0.004 ETH reward, threshold 80%), prepare `0xb80d0ab2...131d307e`, start `0x5b789163...4d5265f6fc`, prepay 0.000240 ETH — status `PENDING_EVALUATION` as of 07-29, not yet settled.
- Protocol signal (via shiplog, 2026-07-27): bounty #153's rubric was hardened to require archive.org 7-day persistence proof after a hunter deleted a required post-payout deliverable — first observed case of a rubric tightening in direct response to hunter gaming; worth watching for a repeat pattern.

## Builder Leads (bd-radar)
- Top building: **s97472091-pixel** shipped a Python SDK + integration guide + bounty workshop for the Bounties API (unprompted), then kept escalating Jul7–16 with 3 case-study repos, a hosted `verdikta-playbook` site, a Medium deep-dive on a 99/100-scored bounty, and a bounty-#147 evidence repo — then went quiet 07-17 through 07-25 (9 days), before breaking the streak 2026-07-26 20:07 UTC with **`verdikta-agent`** — a complete autonomous bounty-hunting agent (monitor/viability-score/submit/track, real API + on-chain read) — their most ambitious artifact yet. **@AjAkmarudi72937** (previously flagged as possibly-scripted, then genuine amplifier) claimed "I built" that exact repo the same evening — strong evidence AjAkmarudi72937 and s97472091-pixel are the same operator running a GitHub+X pair — and also posted a citable "I tried to cheat a Verdikta bounty, the AI caught it" Medium writeup with on-chain proof (good priority-3 content material). Also: **aaronjmars/aeon-agent** (renamed from `aeon`, 10★ Aeon fork) built then accidentally dropped a verdikta-hunter skill — maintainer open to restoring post-refactor, still pushing automation-only commits as of 07-28, no human commit since 06-05, verdikta-hunter skill still not restored; **bingmokaka** shipped a tested PR fixing bounty-submission ABI bugs (2026-07-12). A bounty-farming boilerplate cluster (`Zetav1`) spread from `verdikta-docs` to a second repo (`verdikta-dispatcher`) on 2026-07-14 — watch, not yet a lead. **`NSPG13/agent-bounties`** (found 2026-07-16) — a direct, fast-shipping competitor (AI-agent bounty protocol on Base, 288+ PRs merged since 2026-07-08) whose repo contains a detailed writeup of Verdikta's own design pulled from our agent API/whitepaper — competitive intel, worth the operator's own read, still shipping as of 07-26. **Flag for engagement:** **@Project0_Z** now a 4-for-5 pattern of unprompted, organic advocacy (2026-07-16/17/26) — low engagement but high-quality, repeat signal; a reply/DM is a cheap, high-value engagement opp. **mumuzhong3** — confirmed integrating-class lead (2026-07-26): 2 real tested PRs (#27/#28) against `verdikta-applications` fixing issues #14/#16, both MERGEABLE, proactively asked about a payment path. `GH_READ_PAT` still 401/unset as of 07-29 (20 consecutive runs) — no functional impact, public API fallback covers all 5 watched repos. 07-29 (20th run): no new lead keys — top 3 unchanged; **@AjAkmarudi72937** posted a new analytical mention (07-28 14:45 UTC) framing Verdikta's rubric-scored receipts as agent-settlement dispute resolution — continuation of a tracked handle, not a new lead. Full detail: [topics/builder-leads.md](topics/builder-leads.md) (now caught up through the 20th run — the 07-25/16th-run gap noted previously has been backfilled).

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging
- GitHub token is missing `read:org` scope — github-monitor's "reviewer ghosted >72h" rule can't evaluate `reviewRequests` without it (no impact yet, no open PRs have pending review requests)
- digest, write-tweet, and github-monitor all hit `/tmp` writes and `rm` blocked mid-run (sandbox), leaving non-sensitive stray temp files (xAI payload/response JSON, char-count scripts, a composed notify body) in the repo root/`.runtmp/` — confirmed still present as of 2026-07-22, untracked/gitignored so invisible to `git status`; safe to delete but memory-flush can't (destructive-op gate excludes `rm`); needs a skill-side fix (write temp files under a repo-tracked scratch dir the skill itself cleans via its own allowed tools, not `/tmp`+`rm`)
- The Bash tool also hard-blocks plain shell `>` redirection to any file regardless of path (separate from the `$SECRET`-expansion guard) — digest (2026-07-22) worked around it by using the Write tool to author JSON payloads directly and `curl -o` (not shell redirect) for responses
- `cp` between two paths inside the same allowed working directory is also blocked (new observation, write-tweet 2026-07-28) — use the Write tool instead of `cp` when copying/saving drafts
- github-monitor's `.runtmp_age.py`/`.runtmp_notify.md` stray temp files (2026-07-29) don't match `.gitignore`'s `tmp_*`/`.*-tmp.md` patterns (wrong prefix — `.runtmp_` vs `tmp_`), so unlike other skills' stray files these actually show up as untracked in `git status`; needs either a gitignore pattern fix or the skill switched to the `tmp_*` convention other skills already use

## Next Priorities
- Add `read:org` scope to the GitHub token used by github-monitor
- Fix/set bd-radar's `GH_READ_PAT` (401/unset since first run 2026-07-10, still 401 through 2026-07-29 — 20 consecutive runs) — no impact yet since it falls back to unauthenticated public API, but should be corrected before rate limits bite
- 4 open Dependabot PRs (#1-#4, all opened 2026-07-09 ~19:23 UTC, this repo `nigelon11/verdikta-worker`) crossed the >24h stalled threshold as of 2026-07-11, still open and stalled (~484h as of 2026-07-30) — need review/merge per strategy priority 1 (keep repos healthy and shipping)
- `verdikta-applications#18` (bingmokaka, tested ETH-prepay fix, opened 2026-07-10) crossed the 48h-idle threshold 2026-07-18, still open (~341h since last update as of 2026-07-30) — a real, useful third-party contribution stalled on review; merge/review per strategy priority 1
- Draft "backlog workflow guidance" PR cluster opened 2026-07-14 ~18:48 UTC: `verdikta-docs#7` **merged 2026-07-22** (first resolution), leaving 3 still open/draft — `verdikta-applications#25`, `verdikta-arbiter#9` (still failing Gitleaks Secret Scan), `verdikta-dispatcher#5` — all confirmed past the 168h/7d age threshold (~365h as of 2026-07-30) and sitting in github-monitor's INFO tier (draft-capped, not ACT_NOW) — still need operator review/merge per strategy priority 1, especially `arbiter#9` given its real, unresolved Gitleaks CI failure
- `verdikta-applications#26` (operator's own rubricCid fix, opened 2026-07-21) crossed github-monitor's >48h INFO floor on 2026-07-24, still open with no CI configured and no reviews (~195h as of 2026-07-30) — lower urgency as an operator-owned PR, but now aging alongside the rest of the queue
- `verdikta-applications#27`/`#28` (mumuzhong3, opened 2026-07-24 ~18:56-19:00 UTC) — real fixes for open issues #14 (AWARDED bounty red error) and #16 (rubric validator missing jury-node checks), both MERGEABLE, no CI configured, no reviews yet; crossed github-monitor's 48h INFO floor 2026-07-27 (~112h old as of 2026-07-30) — a genuine third-party contribution, review/merge per strategy priority 1; confirmed as a builder lead by bd-radar (see Builder Leads above)
- Clean up stray non-sensitive temp files left in repo root/`.runtmp/` by digest/write-tweet/github-monitor sandbox workarounds (see Lessons Learned) — recurs most days when those skills run, though none present at this run's start (2026-07-30); low priority, not secret-bearing. github-monitor's variant (`.runtmp_*`) also needs a gitignore pattern fix since it doesn't match the existing `tmp_*` glob (see Lessons Learned).
- Bounty #164 (verdikta-hunter's second real submission, 2026-07-29) still `PENDING_EVALUATION` — watch for settlement/finalize on a future hunter run (see Dogfooding above)
- **Operator read recommended:** `NSPG13/agent-bounties` (found 2026-07-16 by bd-radar) is a direct, fast-shipping competitor on Base whose `docs/competitor-learning-plan.md` dissects Verdikta's own design in detail — see [topics/builder-leads.md](topics/builder-leads.md) for the summary and links.
