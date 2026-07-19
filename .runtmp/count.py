tweets = {
"1a": "Nobody pays a stranger to write your docs. They do it because the product just worked.",
"1b": "The best growth metric isn't signups. It's an unpaid case study nobody asked for.",
"2a": "A developer shipped an SDK, a workshop, and three case-study repos for our bounty API — unprompted. That's the whole PMF signal, right there.",
"2b": "Growth teams spend six figures chasing the exact thing one bored developer will build for free the moment your onboarding doesn't suck.",
"3a": "Everyone measures adoption by signups and star counts. Wrong metric. The real signal is unprompted labor — someone building tooling around your API that nobody requested and you'd have gladly paid for. That's not marketing. That's proof the thing actually works.",
"3b": "One developer found our AI-judged bounty API, scored a submission, then went and wrote an SDK, ran an integration workshop, and published a deep-dive on the scoring model — none of it requested. Nobody greenlit a campaign. It happened because the API did what the docs said.",
"4a": "Watched a developer go from first bounty submission to full advocate in under two weeks: an SDK wrapper, an integration workshop, three case-study repos, a hosted playbook site, and a Medium deep-dive on a 99/100-scored submission. Nobody asked for any of it — no content bounty, no DM, no partnership deck. That's what real developer pull looks like, versus what most 'growth' actually is: paid placements, quote-tweet swaps, engagement pods that die the day the budget does. If you want to know whether a dev tool has product-market fit, stop counting followers. Count the unprompted repos.",
"4b": "How do you actually know a dev tool has product-market fit, versus just a good marketing budget? Followers can be bought. Quote-tweets can be arranged. An unprompted SDK, workshop deck, and three case-study repos from a developer who owes you nothing — that can't be. We watched exactly that happen around a bounty API this month, with zero outreach on our end. The tell isn't attention. It's unpaid labor spent making your thing easier for the next person to use.",
"5a": "The realest product-market-fit signal in dev tools isn't adoption. It's when a stranger starts doing your marketing team's job for free.",
"5b": "Most 'organic growth' stories are staged. This one wasn't — and the paper trail is just a string of public GitHub commits.",
}
for k, v in tweets.items():
    print(k, len(v))
