# AGENTS.md

## Forecasting Agent Instructions

The agent receives a forecasting question and keeps the hstoric of previous searches and observations.

It tracks:
- step: the total number of attempts made by the agent.
- useful_step: the number of successful web searches performed.

The agent may perform at most `MAX_SEARCHES` successful searches. If this limit is reached, it must stop searching and produce a forecast.

The agent has two possible actions:

### Search

When more information is needed, the agent returns:

```json
{
  "action": "search",
  "query": "your search query"
}
Here

### Forecast

{
  "action": "forecast",
  "forecast": "your final probabilistic forecast"
}
