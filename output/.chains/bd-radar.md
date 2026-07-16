## Summary

Ran the **bd-radar** skill (7th run) — swept GitHub (forks/issues across the 5 public `verdikta/*` repos + `gh search`), X (xAI search since 2026-07-13), and web (HN/Reddit/blog) for BD signal.

**Key finding:** a new competitive-intelligence signal — **`NSPG13/agent-bounties`**, a fast-shipping open-source AI-agent bounty protocol on Base (288 merged PRs since 2026-07-08) whose `docs/competitor-learning-plan.md` contains a detailed writeup of Verdikta's own design, pulled directly from our agent API and whitepaper. Not a partnership lead — flagged for the operator's own read.

No new `building`/`integrating` leads this run (so no self-notify, per the skill's quiet-by-default gating). **s97472091-pixel** (top tracked builder) shipped again — a new evidence repo for bounty #147, 7th consecutive run with fresh output. All other tracked leads (aaronjmars/aeon-agent, bingmokaka, @AjAkmarudi72937, @Fishhead8u) carried forward unchanged. `GH_READ_PAT` is still 401 — 7th consecutive run — falling back to the public GitHub API works fine, no functional gap yet.

**Files changed (committed as `3cc8a43`):**
- `output/articles/bd-radar-2026-07-16.md` — new ranked digest
- `memory/topics/bd-radar-leads.json` — added NSPG13 lead + updated s97472091-pixel signal
- `memory/topics/builder-leads.md` — added Competitive Intel section, appended run notes
- `memory/MEMORY.md` — updated Builder Leads summary + Next Priorities (flagged the competitor for operator review, bumped GH_READ_PAT count to 7)
- `memory/logs/2026-07-16.md` — `### bd-radar` log block

**Follow-up needed:** operator should read `NSPG13/agent-bounties`'s competitor-analysis doc, and `GH_READ_PAT` still needs fixing (7 straight failed runs).
