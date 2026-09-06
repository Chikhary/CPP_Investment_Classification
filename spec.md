# spec.md

## System Objective

The goal of the system is to answer forecasting questions by combining an LLM with external web search. The agent gathers recent information, reasons over the retrieved evidence, and returns a final probabilistic forecast.

## Workflow

The system follows this process:

1. A forecasting question is provided to the agent.
2. Gemini receives the question and the history of previous observations.
3. The agent chooses between two actions:
   - `search`: generate a query and retrieve recent information using Tavily.
   - `forecast`: return the final probabilistic prediction.
4. Successful search results are added to the history and reused in the next reasoning step.
5. The number of successful searches is limited by `MAX_SEARCHES`.
6. Once the search limit is reached, the agent must produce a forecast.

## Components

- `main.py`: receives the user question and launches the agent.
- `agent.py`: manages the forecasting loop, search decisions, errors, and final output.
- `llm.py`: handles communication with Gemini.
- `tools.py`: handles web search through Tavily.

## Outputs

For each run, the system saves:

- a `trace` file containing the question, search history, and final forecast.
- a `forecast` file containing the question and final forecast.

Both files are stored in the `runs/` directory.
## Models and External Services

- Gemini model: The exact model used in `llm.py`.
- Tavily API for web search.

## Failure Handling

The system handles invalid JSON responses, LLM API failures, search API failures, and unknown agent actions. If the agent cannot complete the forecast normally, it returns an explicit stopping message.
