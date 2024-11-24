pip install tweepy textblob pandas 
import tweepy
from textblob import TextBlob
import pandas as pd

name: Python CI with Conda

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    # Checkout the repository
    - name: Checkout repository
     


# Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_SECRET = 'your_access_secret'

# Authenticate
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Search tweets
query = "Erasmus"  # Change this to any topic
tweets = api.search_tweets(q=query, lang="en", count=10)

# Analyze sentiment
data = []
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    data.append([tweet.text, sentiment])

# Save to CSV
df = pd.DataFrame(data, columns=["Tweet", "Sentiment"])
df.to_csv("tweets_sentiment.csv", index=False)
print("Sentiment analysis complete. Results saved to tweets_sentiment.csv.") 
