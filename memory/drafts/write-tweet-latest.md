---
type: Reference
---

## Tweet Drafts: AI agents exploiting other AI agents (Pillar Security / Google ADK)

### Tier 1 — One-liner
**1a. Hot take**
> A bot with more permissions than the human filing the issue was always going to end badly.

**1b. Observation**
> Google's own AI agents trust each other more than they trust the humans that built them.

### Tier 2 — Two-punch
**2a. Data drop**
> A low-privilege triage bot got tricked into invoking a high-privilege CI agent — from a GitHub comment. Google deleted three workflows after.

**2b. Reframe**
> Everyone's worried about prompt injection tricking an AI into saying something dumb. The real risk is one AI agent tricking another into acting.

### Tier 3 — Paragraph
**3a. Narrative**
> A public GitHub issue, a comment, and a triage bot with just enough trust in its coworker. That's all it took for Pillar Security to get a low-privilege AI agent to hijack a high-privilege one inside Google's own ADK. The exploit chain was three agents deep.

**3b. Structural critique**
> The bug wasn't in either agent's model — it was in the handoff. Google's ADK let a public bot delegate to a privileged one with no re-check of who actually asked. Multi-agent systems inherit the trust of their weakest link, not their strongest.

### Tier 4 — Long tweet
**4a. Data drop**
> Pillar Security's Google ADK finding, in three steps: 1) a public-facing issue-triage agent reads a GitHub comment containing a prompt injection. 2) that injection tells it to invoke a second, privileged agent meant only for internal CI/CD. 3) the privileged agent complies — no human, no re-auth, no scope check between the two. Google pulled three workflows once they found it. This is what people mean when they say agent orchestration is a new attack surface, not just a new feature.

**4b. Reframe**
> The instinct after reading about the Google ADK agent-to-agent exploit is to blame the model that got prompt-injected. Wrong target. The model did exactly what it was built to do — read text, act on instructions. The actual failure was letting a low-trust agent's output become a high-trust agent's input without a boundary in between. That's not an LLM problem. That's a systems-design problem, and it's the same one every agent-to-agent protocol has to solve before it can be trusted with anything that moves money or state.

### Tier 5 — Thread opener
**5a. Structural critique**
> Google just shipped the clearest proof yet that 'my agent trusts your agent' isn't a security model. A public bot got prompt-injected, then triggered a privileged one. Here's the exploit chain — and why it generalizes to every multi-agent system being built right now:
---
- The setup: Google ADK let a low-privilege, public-facing triage agent delegate tasks to a high-privilege internal agent
- The trigger: a single GitHub issue comment carrying a prompt injection — no exploit tooling needed
- The escalation: the privileged agent acted on the delegated instruction with no re-check of the original requester
- The fix: Google deleted three workflows — a patch, not a redesign
- The generalization: any system where agents delegate based on output alone, not verified identity/intent, has this exact hole

**5b. Thesis-first**
> Multi-agent AI systems have a trust problem nobody's pricing in: trusting another agent's output means trusting whoever last got that agent to say something. Google's own ADK just proved it in production. Here's what happened, and what it means:
---
- Pillar Security found a public triage agent could be prompt-injected via a GitHub comment
- That injection got it to invoke a second, privileged agent with no identity re-check
- The privileged agent complied — first documented real-world agent-exploiting-agent case
- Google's fix so far: delete three workflows, not redesign the trust boundary
- The lesson for builders: verify the requester, not just the request — every hop

---

Best overall: **4a** — most concrete, walks the exact exploit chain step by step, gives builders something they can actually use.
Best per tier: 1a (one-liner) · 2a (two-punch) · 3b (paragraph) · 4a (long tweet) · 5b (thread opener)
