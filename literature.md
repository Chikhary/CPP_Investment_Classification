# Literature Review

## 1. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — Lewis et al. (2020)

Lewis et al. shows that relying only on knowledge stored inside a language model can be limiting, especially when external factual information is needed. Their retrieval-augmented approach produced more factual and specific outputs than a parametric-only baseline. This motivated the use of Tavily in my project so the LLM can retrieve recent external information before producing its final forecast.

## 2. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — Yao et al. (2023)

ReAct shows that an LLM can alternate between reasoning and taking actions with external tools instead of producing an answer immediately.The authors found that combining reasoning with external information gathering can improve performance on knowledge-based tasks. This influenced the structure of my agent: at each step, Gemini chooses between a `search` action and a final `forecast` action, while previous observations are kept in the history.
