import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai_client = genai.Client(api_key=api_key)

def ask_to_llm(prompt: str):
    answer = genai_client.models.generate_content(model = "gemini-3.6-flash",contents = prompt)
    return answer.text

if __name__ == "__main__":
    answer = ask_to_llm("What is probability forecasting:")
    print(answer)    