# Twitter Sentiment Analysis Tool

This project performs sentiment analysis on real-time tweets using the Twitter API and the TextBlob library. The analysis categorizes the sentiment of tweets into **Positive**, **Negative**, or **Neutral**. Additionally, sentiment trends are visualized over time using Plotly, providing an interactive way to explore tweet sentiment based on specific topics.

## Features

- **Real-time sentiment analysis** of tweets via the Twitter API.
- Sentiment classification into Positive, Negative, or Neutral using TextBlob.
- **Date filtering** to gather tweets from the past week.
- **Interactive sentiment visualization** using Plotly for sentiment trends over time.
- **CSV export** of tweet text and sentiment data for further analysis.

## Requirements

- Python 3.x
- pip

### Python Libraries

To run this project, you need the following Python libraries:

- `tweepy`
- `pandas`
- `textblob`
- `plotly`
- `matplotlib`

Install them by running:

```bash
pip install tweepy pandas textblob plotly matplotlib
