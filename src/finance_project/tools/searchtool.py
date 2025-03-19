import requests
import json
import os
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

# Load API keys at import time
load_dotenv()

class SearchTools:

    @tool('search internet')
    def search_internet(query: str) -> str:
        """
        Use this tool to search the internet for information. 
        This tool returns 5 results from Google Search Engine.
        """
        return SearchTools.search(query)
    
    @tool('open website')
    def open_website(url: str) -> str:
        """
        Use this tool to open a website and get the contents.
        """
        loader = WebBaseLoader(url)
        return loader.load()
    
    @tool('dataset search')
    def dataset_search(query: str) -> str:
        """
        Use this tool to search open datasets related to the query.
        Queries public sources like World Bank, OECD, Kaggle, and Google Dataset Search.
        """
        sources = [
            "site:data.worldbank.org", 
            "site:stats.oecd.org", 
            "site:kaggle.com/datasets",
            "site:datasetsearch.research.google.com"
        ]
        modified_query = f"{query} {' OR '.join(sources)}"
        return SearchTools.search(modified_query)


    def search(query, limit=10):

        url = "https://google.serper.dev/search"

        payload = json.dumps({
        "q": query,
        "num": limit
        })
        headers = {
        'X-API-KEY': os.getenv("SERPER_API_KEY"),
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json().get("organic", [])

        string = []
        for result in results:
            string.append(f"{result['title']}\n{result['snippet']}\n{result['link']}")

        return f"Search results for '{query}':\n\n" + "\n".join(string)
