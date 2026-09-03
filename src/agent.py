import json
from llm import ask_to_llm
from tools import search_web

MAX_STEPS = 5


def clean_json_response(answer: str):
    answer = answer.strip()

    if answer.startswith("```json"):
        answer = answer[len("```json"):]

    if answer.startswith("```"):
        answer = answer[len("```"):]

    if answer.endswith("```"):
        answer = answer[:-3]

    return answer.strip()


def run_agent(question: str):

    history = []

    step = 0
    useful_step = 0

    while step < 10 * MAX_STEPS and useful_step < MAX_STEPS:

        print(f"\n------------- we are at step {step + 1} -------------\n")

        prompt = f"""
You are a forecasting agent.

Question:
{question}

Previous observations:
{json.dumps(history, indent=2)}

You have two possible actions:

1. SEARCH

Return:
{{
    "action": "search",
    "query": "your search query"
}}

2. FORECAST

Return:
{{
    "action": "forecast",
    "forecast": "your final probabilistic forecast"
}}

Return ONLY valid JSON.
"""

        # 1. Ask Gemini
        try:
            answer = ask_to_llm(prompt)
        except Exception as e:
            print(f"LLM call failed: {e}")
            step += 1
            continue

        # 2. Parse Gemini response
        cleaned_answer = clean_json_response(answer)

        try:
            decision = json.loads(cleaned_answer)
        except json.JSONDecodeError:
            print("Gemini did not return valid JSON.")
            step += 1
            continue

        # 3. Execute Gemini's decision
        if decision.get("action") == "search":

            query = decision.get("query")

            try:
                search_result = search_web(query)
            except Exception as e:
                print(f"Search tool failed: {e}")
                step += 1
                continue

            history.append({
                "action": "search",
                "query": query,
                "search_result": search_result
            })

            useful_step += 1
            step += 1

        elif decision.get("action") == "forecast":

            return decision.get("forecast")

        else:
            print("Gemini returned an unknown action.")
            step += 1

    return (
        f"Agent stopped after {useful_step} useful steps "
        f"and {step} total attempts."
    )