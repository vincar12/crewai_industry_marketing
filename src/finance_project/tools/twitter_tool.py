import tweepy
import os
from langchain.tools import tool
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TwitterTools:
    client = tweepy.Client(
        bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
        wait_on_rate_limit=True
    )

    @staticmethod
    @tool('fetch_tweets')
    def fetch_tweets(query: str, limit: int = 10) -> str:
        """
        Fetches recent tweets containing a specific keyword.
        """
        try:
            tweets = TwitterTools.client.search_recent_tweets(
                query=query,
                max_results=limit,
                tweet_fields=["created_at"]
            )
            return tweets
        except tweepy.TooManyRequests:
            print("Rate limit exceeded. Sleeping for 60 seconds...")
            time.sleep(60)
            return TwitterTools.fetch_tweets(query, limit)

if __name__ == "__main__":
    print(TwitterTools.fetch_tweets("electric vehicles"))
