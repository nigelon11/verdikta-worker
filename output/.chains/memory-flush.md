Committed as `a4683aa`.

## Summary

Ran the `memory-flush` skill for 2026-08-04 (executed directly since it wasn't in the invokable skill list — read `skills/memory-flush/SKILL.md` and followed its steps).

**Changes to `memory/MEMORY.md`:**
- Bumped "Last consolidated" to 2026-08-04
- Live-refreshed all stalled-PR/issue hour counts in Next Priorities via `gh pr list`/`gh issue view` (Dependabot #2/#3 ~628h, applications#18 ~484h, draft cluster ~509h, applications#26 ~338h, applications#27/#28 ~269h, dispatcher!6 ~147h)
- **Fixed the scratch/tmp file count methodology**, which the prior flush (08-03) flagged as unreproducible — pinned a reproducible `git ls-files` command, giving **97** (documented in Lessons Learned). This is lower than the previously reported 108/115, but `git log` showed no actual deletions, so I noted explicitly this is a corrected baseline, not real cleanup, to avoid a false "shrinking" narrative later
- Widened the bounty #164 no-run gap note (Dogfooding + Next Priorities) to cover through 08-04

**Not promoted** (already self-maintained current by their own skills): bd-radar's Builder Leads paragraph and the digest's Recent Digests row both already reflected today's runs.

Logged the flush under `### memory-flush` in `memory/logs/2026-08-04.md` and committed both files (`a4683aa`). No follow-up actions needed beyond the existing Next Priorities items (dependabot review, stalled PR merges, tmp cleanup PR, bounty #164 settlement check).
