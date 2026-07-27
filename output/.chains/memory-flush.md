Committed. Per skill guidance, this run had material updates (not a no-op `MEMORY_FLUSH_OK` with nothing to do), so no separate notification is needed — memory-flush doesn't notify per CLAUDE.md's "notify only on signal" rule and the skill itself has no notify step.

## Summary

Ran the memory-flush skill, consolidating the 07-25→07-27 log tail into `memory/MEMORY.md`:
- Bumped "Last consolidated" to 2026-07-27.
- Archived the 8 oldest Recent Digests rows (07-09→07-17) to new `memory/topics/digest-history.md`, trimming MEMORY.md from 66→61 lines (was over the ~50-line index target).
- Added a new Dogfooding entry: bounty #153's rubric was hardened (archive.org 7-day persistence proof) after a hunter deleted a required deliverable — surfaced by today's shiplog run.
- Refreshed all Next Priorities PR-age counts via live `gh pr view`/`gh pr list` checks and updated the `applications#27`/`#28` line to reflect today's github-monitor tier crossing (48h INFO floor, ~51h old).
- Fixed a stale GH_READ_PAT streak count in Next Priorities (17/07-26) that had drifted out of sync with Builder Leads (18/07-27) — both now agree.
- Confirmed "Open Improvement PRs" search and `memory/issues/INDEX.md` unchanged (no action needed); stray `.runtmp*` temp files present but match the already-documented sandbox pattern.

Files changed: `memory/MEMORY.md`, `memory/logs/2026-07-27.md`, `memory/topics/digest-history.md` (new). Committed directly as `chore(cron): memory-flush success` (47bc106), consistent with other cron skill runs. No follow-up actions needed — this is a self-contained memory-hygiene pass.
