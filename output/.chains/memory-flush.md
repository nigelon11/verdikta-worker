Committed. The remaining untracked files (`notify`, `notify-jsonrender`, `.notify-sent-hashes`) are the standard runtime tool scripts documented in CLAUDE.md, not scratch output — correctly left alone.

## Summary

Ran the `memory-flush` skill (topic-agnostic, `${var}` empty) against the last 3 days of logs (2026-07-31 → 2026-08-02):

**Promoted to MEMORY.md:**
- Added `mention-radar` to the Skills Built table (new skill, first ran 2026-08-02, quiet).
- Updated Builder Leads paragraph with bd-radar's 24th run (08-02) summary, replacing the stale 23rd-run text; confirmed `topics/builder-leads.md` is already self-maintained and current.
- Refreshed all stalled-PR/issue hour counts in Next Priorities via live `gh` checks (Dependabot #2/#3 ~581h now longest-stalled; `#9`/`#10` ~43h, not yet stalled; `applications#18` ~437h; draft cluster ~461h; `applications#26` ~291h; `applications#27`/`#28` ~208h; `dispatcher!6` ~99h).
- Escalated the committed-scratch-file count (108 → 115) — confirmed the newly-seen untracked `notify`/`notify-jsonrender`/`.notify-sent-hashes` are the documented tool scripts, not part of that bloat.

**Pruned:** archived the oldest Recent Digests row (07-26) to `topics/digest-history.md` to keep the inline table at 7 rows.

**Unchanged (checked, no action needed):** Open Improvement PRs section, `memory/issues/INDEX.md` (still empty), Lessons Learned.

Logged the promote/prune summary to `memory/logs/2026-08-03.md` and committed all changes (`c8b66b1`).
