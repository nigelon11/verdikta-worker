---
type: Reference
title: Builder Leads — bd-radar findings
description: High-intent third-party builders found by bd-radar, ranked by intent per STRATEGY.md priority 2 (find the builders).
tags: [bd-radar, leads, builders]
timestamp: 2026-07-12T00:00:00Z
---

# Builder Leads

Tracked in full (with dedup state) at `memory/topics/bd-radar-leads.json`. Human-readable summary of the highest-intent finds below.

## Building
- **s97472091-pixel ("pipsss")** — shipped a Python SDK (`verdikta-sdk`, `verdikta-sdk-v2`) + integration guide + bounty workshop for the Bounties API, all unprompted Jun30–Jul7 2026. Also opened PR #632 to `aaronjmars/aeon`'s verdikta-hunter skill and completed bounty #97. Highest-intent lead found so far.

## Integrating
- **aaronjmars/aeon** (10★ public Aeon framework fork) — built an in-tree verdikta-hunter skill Jul1–6 2026, accidentally dropped it in a restructure (PR #647). Maintainer replied to issue #681 ("will keep an eye on it once refactor lands", closed 2026-07-08). Worth a future nudge once their refactor lands.
- **bingmokaka** — [PR #18](https://github.com/verdikta/verdikta-applications/pull/18) to `verdikta-applications` (2026-07-10): fixed real ABI/flow bugs in the bounty-submission onboarding scripts (ETH-prepay alignment, stuck-submission diagnostics), tested, closes issue #17. Profile is a serial cross-ecosystem bounty hunter (17 forked repos across many bug-bounty/grant platforms), not a dedicated Verdikta builder — but a real, useful contribution to the flow other builders rely on. Found 2026-07-12.

## Mentioning (lower priority)
- **@AjAkmarudi72937** — organic-reading CN-language explainer posts about Verdikta's bounty flow (2026-07-07), also flagged by mention-radar as possibly scripted (low engagement, 6 near-identical posts in 2 min).
- **@Fishhead8u** — friction complaint about targeted-bounty pay/access (2026-07-08) — a real usability signal, not a lead.

## Notes
- bd-radar's `GH_READ_PAT` returned 401 (unset/invalid) on its first run (2026-07-10), still 401 as of its second (2026-07-11) and third (2026-07-12) runs — falls back to unauthenticated public GitHub API each time, which works fine for these public repos. No functional impact yet, but should be fixed to avoid rate-limit risk as watch scope grows.
- 2026-07-11 (2nd bd-radar run): 0 new leads — all 4 leads carried forward unchanged, no new activity. Two items noted for context, not scored as leads: (1) a bounty-farming spam pattern on `Zetav1`/`zp6` PRs against `verdikta-docs` (fake "Canonical Wallet"/star-verification boilerplate) — already filtered by bd-radar, isolated to those 2 accounts, watch for spread; (2) Verdikta's own `verdikta-bounties-onboarding` skill found mechanically mirrored across 5 OpenClaw skill marketplaces/aggregators — distribution-reach signal, not a new third-party build.
- 2026-07-12 (3rd bd-radar run): 1 new lead (bingmokaka, integrating). Three GitHub repo-name matches investigated and dropped as coincidental/empty (`ViKu7988/TechOn_Hackathon_VerdiktAI`, `VeRdiKT254/VERDIKTADDIKT`, `salvio1050/verdikta-zealy`). A Moltbook post reading like third-party "building with Verdikta" evangelism traced back to core-team member **yenachar**'s own AI-agent persona ("Mangosteen") — first-party, dropped. X: zero third-party mentions in the 3-day window (only the official account posted). Web: zero independent HN/Reddit/blog mentions, consistent with prior runs.
