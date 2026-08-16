## Summary

Ran the memory-flush skill for 2026-08-16 (all-topic flush, no `${var}` scope):

**Promoted:**
- Bumped MEMORY.md "Last consolidated" to 08-16
- Refreshed all stalled-PR/issue hour counts in `topics/next-priorities.md` via live `gh` checks (no merges/closures since 08-15)
- Recounted committed scratch/tmp files: 156, up from 143 (+13) — investigated the jump (repo showed a single squashed commit with 813 files) and confirmed it's expected shallow-clone (`fetch-depth: 1`) behavior, not a real anomaly, so didn't file it as an issue
- Updated Builder Leads to bd-radar's 08-16/40th run (GH_READ_PAT unset streak → 40, `s97472091-pixel` quiet 4 days)
- Widened the verdikta-hunter no-run gap note to "07-30 through 08-16"

**Verified unchanged, no duplicate edits:** Recent Digests 08-16 row and mention-radar's Skills Built note were already self-updated by their own skills today; "Open Improvement PRs" and `memory/issues/INDEX.md` still empty/no-op.

**Files changed:** `memory/MEMORY.md`, `memory/topics/next-priorities.md`, `memory/logs/2026-08-16.md` (committed as `69e9d3a`).

**Follow-up needed:** the tmp-file cleanup PR and `GH_READ_PAT` fix are still outstanding (unchanged priorities); no new items requiring operator decision this run.
