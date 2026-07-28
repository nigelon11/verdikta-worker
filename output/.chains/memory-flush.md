## Summary

Ran `memory-flush` for 2026-07-28 (no topic filter — flushed all recent activity):

**Promoted:**
- Refreshed Builder Leads and Next Priorities with live `gh pr`/`gh pr list` checks (not stale log numbers): Dependabot #1-#4 ~460h, `applications#18` ~316h, draft cluster ~341h, `applications#26` ~170h, `applications#27`/`#28` ~87h.
- Bumped GH_READ_PAT 401 streak to 19 consecutive runs and added bd-radar's 19th-run summary (no new leads).
- Two new Lessons Learned: `cp` is blocked by the Bash permission layer (use Write instead); `memory/topics/builder-leads.md` has stalled at its 07-25/16th-run entry even though bd-radar is now on run 19 — the detail file is drifting behind MEMORY.md's own summary. Added a matching Next Priorities line for this.

**Pruned:**
- Removed the resolved "verdikta-hunter executor allowlist" lesson (already fixed in `b73a317`).
- Archived the 2026-07-21 Recent Digests row to `topics/digest-history.md`.
- Confirmed "Open Improvement PRs" (still just the Dependabot false-positive) and `memory/issues/INDEX.md` (still empty) need no changes.

**Files changed:** `memory/MEMORY.md`, `memory/topics/digest-history.md`, `memory/logs/2026-07-28.md` — committed as `0740af8`.

Follow-up needed: operator should confirm whether bd-radar's `builder-leads.md` upkeep is worth a skill fix, and the long-standing GH_READ_PAT/read:org-scope/stalled-PR items remain open.
