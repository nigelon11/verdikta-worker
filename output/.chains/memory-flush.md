## Summary

Ran a second `memory-flush` for 2026-07-22, picking up activity from today's later skill runs (github-monitor, bd-radar, mention-radar, digest, write-tweet) that happened after the first flush earlier today.

Changes to `memory/MEMORY.md`:
- **Next Priorities**: refreshed live counters (GH_READ_PAT 401 now 13 runs, Dependabot PRs ~301h, `applications#18` ~160h), and resolved the open question from the prior flush — the 4-draft-PR cluster confirmed via `gh` and today's github-monitor run to have crossed the 168h/7d threshold and entered INFO tier (not ACT_NOW, still draft-capped per skill rule).
- **Builder Leads**: s97472091-pixel now 6th consecutive quiet day; aaronjmars/aeon-agent pushed again 07-22 (cron/token-report only, verdikta-hunter still not restored).
- **Lessons Learned**: added a new entry — the Bash tool also hard-blocks plain shell `>` redirection (separate from the secret-expansion guard), found by today's digest run.
- Checked Open Improvement PRs and `memory/issues/INDEX.md` — both unchanged, nothing to prune there.

Logged the promotion/pruning details to `memory/logs/2026-07-22.md` and committed both files (`404a0ec`). No follow-up actions needed — the flush itself doesn't resolve the underlying stalled PRs or the `GH_READ_PAT` fix; those remain operator action items as noted in Next Priorities.
