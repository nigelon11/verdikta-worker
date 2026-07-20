Memory flush complete for 2026-07-20.

## Summary

Reviewed the last 3 days of logs (07-17 to 07-19) against `memory/MEMORY.md` and:

- **Bumped staleness counters:** `GH_READ_PAT` 401 (now 10 consecutive bd-radar runs), Dependabot PRs #1-#4 (~230h stalled), `verdikta-applications#18` (~86h idle since last update).
- **Updated Builder Leads pointer:** top lead s97472091-pixel now on a 3rd consecutive quiet day; noted aaronjmars/aeon-agent pushed again 07-19 but the verdikta-hunter skill is still not restored; NSPG13/agent-bounties still shipping. Full detail remains in `topics/builder-leads.md` (bd-radar owns that file directly).
- **New lesson logged:** digest and write-tweet runs on 07-18/07-19 both hit sandbox-blocked `/tmp`+`rm`, leaving non-sensitive stray temp files in the repo root/`.runtmp/` (confirmed still present on disk). Flagged as a Next Priority for a skill-side fix rather than attempting cleanup myself, since `rm` is outside memory-flush's granted tools.
- Confirmed no action needed on "Open Improvement PRs" (still just the false-positive Dependabot PR #2) or `memory/issues/INDEX.md` (still empty).
- Nothing found stale enough to remove from Dogfooding/Lessons Learned; no new Recent Digests row (3rd empty digest day in a row, nothing to promote).

Files changed: `memory/MEMORY.md`, new `memory/logs/2026-07-20.md`. Committed directly to `main` as `2a6cef8` (matches this repo's existing convention of direct commits for routine memory/log data, not code changes). No follow-up actions needed beyond the items already tracked in Next Priorities.
