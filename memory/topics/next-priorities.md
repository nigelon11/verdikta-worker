---
type: Playbook
title: Next Priorities — detail
description: Full detail behind MEMORY.md's condensed Next Priorities list — stalled PR/issue tracking, repo scratch/tmp cleanup, bounty #164 settlement check
tags: [priorities, github-monitor, dogfooding, cleanup]
timestamp: 2026-08-16T23:44:54Z
---

# Next Priorities — detail

Condensed pointers live in [MEMORY.md](../MEMORY.md#next-priorities). Full detail below, updated by memory-flush each run.

## Stalled PRs/issues (per strategy priority 1)

- **Dependabot churn** (`nigelon11/verdikta-worker`, 2026-08-16 live check): `#9`/`#10` (opened 2026-08-01, ~379h old) not yet stalled; `#2`/`#3` (opened 07-09) remain open and are now the longest-stalled at **~916h**
- **`verdikta-applications#18`** (bingmokaka, tested ETH-prepay fix, opened 2026-07-10) crossed the 48h-idle threshold 2026-07-18, still open (~758h since last update as of 2026-08-16) — a real, useful third-party contribution stalled on review
- **Draft "backlog workflow guidance" PR cluster** opened 2026-07-14 ~18:48 UTC: `verdikta-docs#7` **merged 2026-07-22** (first resolution), leaving 3 still open/draft — `verdikta-applications#25`, `verdikta-arbiter#9` (still failing Gitleaks Secret Scan), `verdikta-dispatcher#5` — all past the 168h/7d age threshold (~783h as of 2026-08-16), sitting in github-monitor's INFO tier (draft-capped, not ACT_NOW); `arbiter#9` notable for its real, unresolved Gitleaks CI failure
- **`verdikta-applications#26`** (operator's own rubricCid fix, opened 2026-07-21) crossed github-monitor's >48h INFO floor on 2026-07-24, still open with no CI configured and no reviews (~612h as of 2026-08-16) — lower urgency as operator-owned, but aging alongside the rest of the queue
- **`verdikta-applications#27`/`#28`** (mumuzhong3, opened 2026-07-24 ~18:56-19:00 UTC) — real fixes for open issues #14 (AWARDED bounty red error) and #16 (rubric validator missing jury-node checks), both MERGEABLE, no CI configured, no reviews yet; crossed github-monitor's 48h INFO floor 2026-07-27 (~529h old as of 2026-08-16) — confirmed as a builder lead by bd-radar (see [builder-leads.md](builder-leads.md))
- **`verdikta-dispatcher!6`** (operator's own issue, opened 2026-07-29, "multi-identity operator failures under-penalized" oracle-selection concern) — surfaced by github-monitor 2026-07-30, still open and unaddressed (~435h as of 2026-08-16), long aged out of the 24h new-issue window but remains a watch item

## Repo scratch/tmp cleanup

Baseline 2026-08-04, re-checked daily. This repo (`verdikta-worker`) has scratch/tmp files committed to git — reproducible `git ls-files | grep -icE 'tmp'` count is **156** as of 2026-08-16, +13 vs 08-15 (growth resumed after 2 flat days; prior deltas: +19 on 08-11, +2 on 08-12, 0 on 08-13, +4 on 08-14, 0 on 08-15). See [MEMORY.md Lessons Learned](../MEMORY.md#lessons-learned) for the count-method history.

Spans bd-radar/digest/write-tweet/github-monitor/shiplog/mention-radar scratch output across `.runtmp/`, `.bdtmp/`, `.wttmp/`, `.ghmon-tmp/`/`ghmon-tmp/`, `tmp/`, `.aeon-tmp/`, `digest-tmp/`, `.mrtmp/`, and root-level loose files. None match existing `.gitignore` patterns. Scanned repeatedly, no secrets found — this is real repo bloat needing an actual cleanup PR (`git rm` the paths + fix whichever skill(s) run a broad `git add`/`git commit` that sweeps scratch dirs in, and/or extend `.gitignore` to cover `tmp/`, `*tmp/`, and `.*tmp*` naming). No cleanup PR opened as of 08-16.

## Bounty #164 settlement (dogfooding, per strategy priority 4)

Last known status `PENDING_EVALUATION` (2026-07-29); an official `@verdikta19633` post (08-03) states bounty #164 expired with 29 submissions and zero winners due to both jury models being invalid for the deployed class. No verdikta-hunter run 07-30 through 08-15 to confirm this is the same bounty and check settlement — if so, the 0.004 ETH prepay likely didn't settle. Run verdikta-hunter to confirm and, if so, file it as a dogfooding bug report. See [Dogfooding in MEMORY.md](../MEMORY.md#dogfooding-verdikta-hunter).

## Operator reads recommended

- `NSPG13/agent-bounties` (found 2026-07-16 by bd-radar) — direct, fast-shipping competitor on Base whose `docs/competitor-learning-plan.md` dissects Verdikta's own design in detail. See [builder-leads.md](builder-leads.md) for summary and links.
