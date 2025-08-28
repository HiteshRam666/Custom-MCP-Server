import httpx 
import json 
import os 
from dotenv import load_dotenv 
load_dotenv() 

api_key = os.getenv("BRAVE_API_KEY")

# Set up the request
headers = {
    "Accept": "application/json",
    "X-Subscription-Token": api_key
}

# Parameters for news search
params = {
    "q": "Bengal Riots in April 2025",  # Your search query for news topics
    "count": 10,        # Number of results to return
    "freshness": "week" # Time period (day, week, month)
}

# Brave Search API endpoint for news
url = "https://api.search.brave.com/res/v1/news/search"

async def brave_search_results(query: str) -> str:
    """Fetch search results from brave search engine"""
    headers = {
    "Accept": "application/json",
    "X-Subscription-Token": api_key}

    # Parameters for news search
    params = {
    "q": {query},  # Your search query for news topics
    "count": 10,        # Number of results to return
    "freshness": "week" # Time period (day, week, month)
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.search.brave.com/res/v1/news/search", headers=headers, params=params)
        return response.text 

if __name__ == "__main__":
    import asyncio 
    
    async def main():
        weather_data = await brave_search_results(query="Bengal Riots in April 2025")
        print(weather_data)

    asyncio.run(main())    