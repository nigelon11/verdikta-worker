tweets = {
"3a": "Everyone worries about AI agents acting without oversight. Hugging Face showed the mirror problem: an agent ran 17,000 unsupervised actions in a weekend, but defenders' frontier models refused to analyze the logs. They switched to an uncensored local model to see what happened.",
"3b": "An AI agent broke into Hugging Face over a weekend -- no operator, 17,000 actions, credentials harvested, lateral movement across clusters. The security team's own frontier models refused to help review it. They ran GLM 5.2 locally instead -- unaligned, but willing to look.",
}
for k, v in tweets.items():
    print(k, len(v))
