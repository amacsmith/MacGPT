import requests

def web_search(query: str, num_results: int = 5) -> list:
    """Simulate a web search using a public API."""
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    response = requests.get(url)
    data = response.json()
    return [
        {"title": result["Text"], "url": result["FirstURL"]}
        for result in data["RelatedTopics"][:num_results]
    ]