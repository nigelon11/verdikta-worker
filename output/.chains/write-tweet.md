ℹ️ Farcaster capability check

No — there's currently no Farcaster posting capability wired up anywhere in this repo. Checked: no skill declares a Neynar/Warpcast API key or signer in `requires:`, no `FARCASTER_*` secret exists in aeon.yml or docs, and no code calls a casting endpoint. Farcaster shows up only as a passive search surface in mention-radar (read-only, for spotting external mentions of Verdikta).

All social output right now is X/Twitter, draft-only: write-tweet drafts tweets/threads/remixes, reply-maker drafts copy-paste replies — neither auto-posts, per STRATEGY.md's hard constraint that drafted content needs human approval.

To engage on Farcaster as @verdikta (or whichever handle), you'd need to: get a Neynar (or Warpcast) API key + signer, add it as a repo secret, and build a new skill (or extend write-tweet) declaring that key in `requires:`. Want me to draft that skill?