# AGENTS.md

## Forecasting Instructions

The agent is instructed to act as a forecasting agent and to prioritize the most recent available information. For each question, it receives the previous observations and must choose between two actions: searching for more information or returning a final probabilistic forecast.

The agent may perform up to `MAX_SEARCHES` searches. Once this limit is reached, it must stop searching and produce a final forecast. All responses must be returned as valid JSON only.

## Agent Actions

### Search

When more information is needed, the agent generates a web search query:

```json
{
  "action": "search",
  "query": "your search query"
}
