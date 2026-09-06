The goal of this project is to build an LLM-based forecasting agent capable of estimating the probability of future events. The agent tries to gather relevant information from web sources, analyzes the available informations and produces a final probabilistic forecast.

Here is the backbone of the project:

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

Here are the roles of each 

main.py — Entry point of the project that receives the forecasting question and launches the agent.
agent.py — Contains the main forecasting agent loop, decision-making logic, and final forecast generation.
llm.py — Handles communication with the Gemini language model and sends prompts to the LLM.
tools.py — Contains external tools used by the agent, named Tavily, including web search for gathering relevant information.

Note: Change the name of .env_example for .env and put your own API keys. Here are the links:
Tavily: https://app.tavily.com/home
Gemini: https://aistudio.google.com/app/api-keys

To run the projet, execute this script:
python src/main.py
