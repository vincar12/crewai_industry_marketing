from dotenv import load_dotenv
import os
import requests
from langchain.tools import tool

# Load the .env file
load_dotenv()

class NewsAPITool:
    API_KEY = os.getenv("NEWSAPI_KEY")

    @tool("fetch_news")
    def fetch_news(query: str, limit: int = 10) -> list:
        """
        Fetches recent news articles related to a specific query.
        """
        if not NewsAPITool.API_KEY:
            return ["Error: API key is missing. Make sure NEWSAPI_KEY is set."]

        url = "https://newsapi.org/v2/everything"
        params = {
            "q": query,
            "apiKey": NewsAPITool.API_KEY,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": limit,
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code != 200:
                return [f"Error: {data.get('message', 'Failed to fetch news')}"]

            articles = data.get("articles", [])
            return [
                {
                    "title": article["title"],
                    "source": article["source"]["name"],
                    "url": article["url"],
                    "published_at": article["publishedAt"]
                }
                for article in articles
            ]

        except requests.RequestException as e:
            return [f"Request error: {str(e)}"]
