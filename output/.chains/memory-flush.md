## Summary

Ran the `memory-flush` skill (no topic filter — full scan):

**Promoted / updated in `memory/MEMORY.md`:**
- Bumped "Last consolidated" to 2026-08-02.
- Archived the 07-25 Recent Digests row to `topics/digest-history.md` (table was at 8 rows, kept last 7 inline).
- **Key finding:** live `gh pr list` check showed Dependabot `#1`/`#4` (stalled since 07-09, previously flagged in Next Priorities) were auto-closed 08-01 and superseded by new grouped PRs `#9`/`#10`; `#2`/`#3` remain open and are now the longest-stalled (~557h). Rewrote that Next Priorities line to reflect the churn instead of the stale "#1-#4" framing.
- Refreshed all other stalled-PR/issue hour counts (`applications#18` ~413h, draft cluster ~437h, `applications#26` ~267h, `applications#27`/`#28` ~184h, `dispatcher!6` ~75h) against current time.
- Escalated the tmp/scratch-file cleanup item — committed count grew from 103 (07-30) to **108** (08-02), still no cleanup PR opened.
- Confirmed "Open Improvement PRs" is still just a false-positive text match (now PR `#10` instead of `#2`) — no section needed.
- Verified `memory/issues/INDEX.md` still empty; Builder Leads/Dogfooding/Lessons Learned already current (no promotion needed).

**Files changed:** `memory/MEMORY.md`, `memory/topics/digest-history.md`, new `memory/logs/2026-08-02.md`. Not committed manually — the `aeon.yml` workflow auto-commits after a successful run.

**Follow-up for the operator:** the Dependabot PR set and the growing (108-file) tmp/scratch bloat both need real action — the details are in Next Priorities.
