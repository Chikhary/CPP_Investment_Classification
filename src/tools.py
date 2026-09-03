import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

api_key_tavily = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key= api_key_tavily)

def search_web(query:str):
    result = tavily_client.search(query=query,max_results=5)
    results = []

    for item in result["results"]:
        results.append({
            "title": item.get("title",None),
            "url": item.get("url",None),
            "content": item.get("content",None)
        })

    return results

if __name__ == "__main__":
    result = search_web("2026 US House election forecast")
    print(result)
