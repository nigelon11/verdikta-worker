---
type: Playbook
title: Next Priorities — detail
description: Full detail behind MEMORY.md's condensed Next Priorities list — stalled PR/issue tracking, repo scratch/tmp cleanup, bounty #164 settlement check
tags: [priorities, github-monitor, dogfooding, cleanup]
timestamp: 2026-08-22T23:40:00Z
---

# Next Priorities — detail

Condensed pointers live in [MEMORY.md](../MEMORY.md#next-priorities). Full detail below, updated by memory-flush each run.

## Digest delivery failure (2026-08-22)

Today's digest lead item — Apex Fusion Foundation's Vector (staked-jury + bonded-escrow settlement layer, closest public analog to Verdikta's own model found to date) plus a NeoSoul $11M raise as a secondary item — was drafted but never sent. `./notify` returned "This command requires approval" on two attempts in-run and the skill gave up rather than retry, per its own log note flagging this as a run anomaly for skill-health. The draft body was held at `.digest-body-tmp.md` (untracked, repo root) but that file no longer exists as of this flush — the only surviving record is the full write-up in [memory/logs/2026-08-22.md](../logs/2026-08-22.md). Operator should either manually review/post that content or wait for skill-health to file an issue on the notify-approval failure; `memory/issues/INDEX.md` is still empty as of this run so nothing has been auto-filed yet.

## Stalled PRs/issues (per strategy priority 1)

**2026-08-19 — major queue clearance.** Operator merged 4 long-stalled `verdikta-applications` PRs in one session (18:37–19:59 UTC): `#25` (backlog workflow guidance, part of the cross-repo draft cluster), `#26` (own rubricCid fix), `#4` (classMap jury models), and mumuzhong3's `#27`/`#28` (closing issues #14/#16 — first third-party PR merged into a public verdikta-applications repo). `#2` closed unmerged (superseded by nginx/build changes elsewhere). Live-checked via `gh pr view --json state,mergedAt,closedAt` per PR.

**2026-08-20 — `verdikta-applications#18` closed as superseded, not rejected.** bingmokaka's tested ETH-prepay fix (opened 2026-07-10, ~830h stalled) was closed 2026-08-20T02:37:46Z after the operator (`yenachar`) hand-reapplied the identical logic to `main` in commit `ac45954` — credited "direction is exactly right," but the branch's `_lib.js` carried CRLF line endings (repo is LF) that inflated an ~8-line logic change into a 718-line diff, plus UTF-8→ASCII glyph mangling, so it was reapplied by hand instead of merged. Drops off the stalled-review watch list; see [builder-leads.md](builder-leads.md) for the full comment trail.

Remaining open:
- **Dependabot churn** (`nigelon11/verdikta-worker`, 2026-08-22 live check): `#9`/`#10` (opened 2026-08-01, ~523h old) not yet stalled; `#2`/`#3` (opened 07-09) remain open and are the longest-stalled at **~1060h**
- **Draft "backlog workflow guidance" PR cluster**: `verdikta-docs#7` merged 2026-07-22, `verdikta-applications#25` merged 2026-08-19 — 2 of 4 resolved. Remaining: `verdikta-arbiter#9` (still failing Gitleaks Secret Scan) and `verdikta-dispatcher#5`, both ~941h as of 2026-08-22, sitting in github-monitor's INFO tier (draft-capped, not ACT_NOW); `arbiter#9` notable for its real, unresolved Gitleaks CI failure
- **`verdikta-applications#8`** (operator's own bundle-submit-flow skill PR, opened 2026-04-05) — still open, not merged; ~3338h since open, crossed back into github-monitor's INFO tier on 08-22 (now >48h since its last push)
- **`verdikta-dispatcher!6`** (operator's own issue, opened 2026-07-29, "multi-identity operator failures under-penalized" oracle-selection concern) — surfaced by github-monitor 2026-07-30, still open and unaddressed (~579h as of 2026-08-22), long aged out of the 24h new-issue window but remains a watch item

## Repo scratch/tmp cleanup

Baseline 2026-08-04, re-checked daily. This repo (`verdikta-worker`) has scratch/tmp files committed to git — reproducible `git ls-files | grep -icE 'tmp'` count is **156** as of 2026-08-22, flat vs 08-21 (9th flat day of the last 10; prior deltas: +19 on 08-11, +2 on 08-12, 0 on 08-13, +4 on 08-14, 0 on 08-15, +13 on 08-16, 0 on 08-17 through 08-22). See [MEMORY.md Lessons Learned](../MEMORY.md#lessons-learned) for the count-method history.

Spans bd-radar/digest/write-tweet/github-monitor/shiplog/mention-radar scratch output across `.runtmp/`, `.bdtmp/`, `.wttmp/`, `.ghmon-tmp/`/`ghmon-tmp/`, `tmp/`, `.aeon-tmp/`, `digest-tmp/`, `.mrtmp/`, and root-level loose files. None match existing `.gitignore` patterns. Scanned repeatedly, no secrets found — this is real repo bloat needing an actual cleanup PR (`git rm` the paths + fix whichever skill(s) run a broad `git add`/`git commit` that sweeps scratch dirs in, and/or extend `.gitignore` to cover `tmp/`, `*tmp/`, and `.*tmp*` naming). No cleanup PR opened as of 08-21.

## Bounty #164 settlement (dogfooding, per strategy priority 4)

Last known status `PENDING_EVALUATION` (2026-07-29); an official `@verdikta19633` post (08-03) states bounty #164 expired with 29 submissions and zero winners due to both jury models being invalid for the deployed class. No verdikta-hunter run 07-30 through 08-22 to confirm this is the same bounty and check settlement — if so, the 0.004 ETH prepay likely didn't settle. Run verdikta-hunter to confirm and, if so, file it as a dogfooding bug report. See [Dogfooding in MEMORY.md](../MEMORY.md#dogfooding-verdikta-hunter).

## Operator reads recommended

- `NSPG13/agent-bounties` (found 2026-07-16 by bd-radar) — direct, fast-shipping competitor on Base whose `docs/competitor-learning-plan.md` dissects Verdikta's own design in detail. See [builder-leads.md](builder-leads.md) for summary and links.
