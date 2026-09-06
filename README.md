The goal of this project is to build an LLM-based forecasting agent capable of estimating the probability of future events. The agent gathers relevant information from web sources, analyzes the available information, and produces a final probabilistic forecast.

Here is the backbone of the project:

```text
CPP_Investment_Classification/
│
├── README.md
├── AGENTS.md
├── spec.md
├── literature.md
│
├── src/
│   ├── main.py
│   ├── agent.py
│   ├── llm.py
│   └── tools.py
│
└── runs/
```

Here are the roles of each file:

* `main.py` — Entry point of the project that receives the forecasting question and launches the agent.
* `agent.py` — Contains the main forecasting agent loop, decision-making logic, and final forecast generation.
* `llm.py` — Handles communication with the Gemini language model and sends prompts to the LLM.
* `tools.py` — Contains the external tool used by the agent, Tavily, which performs web searches to gather relevant information.

### API Keys

Rename `.env_example` to `.env` and add your own API keys.

Tavily: https://app.tavily.com/home
Gemini: https://aistudio.google.com/app/api-keys

### Run the Project

To run the project, execute:

```bash
python src/main.py
```
