ℹ️ Digest — 2026-08-16

*AI agents that transact onchain — 2026-08-16*

_TL;DR: Quiet day — the one hard signal is a formal security audit showing all 15 major x402 payment facilitators, including Coinbase, have unpatched trust-layer holes spanning 99% of tracked transaction volume._

1. *x402 security audit finds 31 vulnerabilities across 15 facilitators covering 99% of volume*
   A peer-reviewed study tested 15 x402 payment facilitators — Coinbase, Thirdweb, PayAI, Mogami, and others — and found every one violated at least one security rule, surfacing 31 distinct vulnerabilities across free-shopping, asset-theft, service-denial, and gas-abuse attack classes. Findings were presented at USENIX Security Symposium and republished Aug 13; Coinbase (77M+ transactions, ~$27M volume, the dominant facilitator by far) has acknowledged and partially patched issues via HackerOne.
   Why it matters: x402 is the payment rail most agent-payment teams build on — a trust gap this wide at the settlement layer is exactly the failure mode an AI-judged dispute/escrow layer is built to catch.
   https://cryptoslate.com/coinbase-and-14-other-x402-facilitators-failed-security-tests-built-for-the-coming-ai-agent-economy/

_Quiet news day otherwise — nothing else cleared the bar._