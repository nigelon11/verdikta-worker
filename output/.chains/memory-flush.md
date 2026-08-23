All memory-flush work is complete for 2026-08-23.

## Summary

Ran the memory-flush skill (no `${var}` topic filter, so a full sweep):

- **MEMORY.md**: bumped "Last consolidated" to 2026-08-23; archived the 08-15 Recent Digests row to `topics/digest-history.md`; refreshed Next Priorities with live `gh pr view`/`gh issue view` checks (worker Dependabot #2/#3 ~1084h, #9/#10 ~547h; `arbiter#9`/`dispatcher#5` ~965h; `applications#8` ~3362h; `dispatcher!6` ~603h — all states unchanged); recounted scratch/tmp files (156, flat, 10th flat day of 11); widened the verdikta-hunter no-run gap note to "07-30 through 08-23"; noted no recurrence of the notify-approval failure (08-23's digest was empty, no notify call attempted, so the 08-22 operator-decision item is still open).
- **topics/digest-history.md** / **topics/next-priorities.md**: bumped timestamps and synced detail to match.
- Verified no changes needed to the Open Improvement PRs check (`gh pr list --search "improve:"` still only the one false-positive dependabot PR), `memory/issues/INDEX.md` (still empty), or Builder Leads (bd-radar self-maintains that section, already current).
- No new Lessons Learned — no novel sandbox-blocking behavior in today's logs.
- Logged all promotions/checks to `memory/logs/2026-08-23.md` under `### memory-flush`.

MEMORY.md holds flat at 72 lines. Follow-up still needed from the operator: the 08-22 Vector/Apex Fusion digest item that never reached notify.
