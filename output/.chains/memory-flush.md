Committed. No notification needed here since memory-flush is an internal housekeeping skill (per its own spec, only logs — doesn't call `./notify`).

## Summary

Ran the `memory-flush` skill for 2026-08-21:

**Promoted:**
- New bd-radar lead **`Svector-anu/svectors-lab`** (integrating-class, Aeon fork that deliberately kept the verdikta-hunter skill after an upstream sync dropped it) into MEMORY.md's Builder Leads section, bumping tracked-lead count 8→9.
- Refreshed all stalled-PR/issue hour counts in Next Priorities via live `gh pr list`/`gh issue view` checks (worker Dependabot ~1036h/~499h, arbiter#9/dispatcher#5 ~917h, applications#8 ~3314h, dispatcher!6 ~555h).

**Pruned/updated:**
- Archived the 2026-08-13 Recent Digests row (aged past 7 days) to `topics/digest-history.md`.
- Confirmed no "Open Improvement PRs" section needed (still just the one false-positive dependabot PR) and `memory/issues/INDEX.md` still empty — no changes there.
- Widened the verdikta-hunter no-run gap and `GH_READ_PAT`/tmp-count day-counters to 08-21.

**Files modified:** `memory/MEMORY.md`, `memory/topics/next-priorities.md`, `memory/topics/digest-history.md`, `memory/logs/2026-08-21.md` — committed as `f362545`.

**Follow-up still open** (no action taken, per scope): repo scratch/tmp cleanup PR (156 files, 8th flat day), `GH_READ_PAT` unset (45 runs), `read:org` scope missing on github-monitor's token, bounty #164 settlement unconfirmed.
