import os
from dotenv import load_dotenv 
import httpx 
load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")

async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no")
        return response.text 

if __name__ == "__main__":
    import asyncio 
    async def main():
        weather_data = await fetch_weather("london")
        print(weather_data) 
    asyncio.run(main())
