import requests
from langchain.tools import tool
from dotenv import load_dotenv
from finance_project.tools.searchtool import SearchTools  # Import your existing search tools

# Load API keys at import time
load_dotenv()

class FilteredSearchTool:

    # List of known non-paywalled sites
    non_paywalled_sites = [
        "site:reuters.com", 
        "site:bloomberg.com", 
        "site:gov", 
        "site:forbes.com", 
        "site:marketwatch.com"
    ]

    @tool('filtered search')
    def filtered_search(query: str) -> str:
        """
        Searches the internet while prioritizing non-paywalled sources.
        It filters results from major financial news sites and government sources.
        """
        # Modify the search query to prioritize non-paywalled sources
        modified_query = f"{query} {' OR '.join(FilteredSearchTool.non_paywalled_sites)}"
        print(f"Searching with query: {modified_query}")
        
        # Perform the search using your existing search function
        search_results = SearchTools.search(modified_query)

        # Filter out paywalled links
        filtered_results = []
        for result in search_results.split("\n\n"):  # Each result is separated by double newline
            if result.strip():
                lines = result.split("\n")
                url = lines[-1].strip()  # The last line is the URL
                if not FilteredSearchTool.is_paywalled(url):  # Check if the URL is paywalled
                    filtered_results.append(result)

        return "\n\n".join(filtered_results) if filtered_results else "No non-paywalled results found."

    @staticmethod
    def is_paywalled(url: str) -> bool:
        """
        Checks if a website is paywalled by looking for keywords in the page content.
        """
        paywalled_keywords = ["subscribe", "premium", "paywall", "membership"]
        try:
            # Send a request to the website
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5)

            # Check if the page contains words that indicate a paywall
            if any(keyword in response.text.lower() for keyword in paywalled_keywords):
                print(f"Skipping paywalled site: {url}")
                return True
        except requests.exceptions.RequestException:
            # If there's an error (timeout, 403, etc.), assume it's paywalled
            print(f"Failed to fetch {url}, assuming paywalled.")
            return True
        
        return False
