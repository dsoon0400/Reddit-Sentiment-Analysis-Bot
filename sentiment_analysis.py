import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

sys.stdout.reconfigure(encoding='utf-8')

client_id = 'os.getenv("CLIENT_ID")' //Hidden keys
client_secret = 'os.getenv("CLIENT_SECRET")'
user_agent = "os.getenv("USER_AGENT")"

headers = {
    'User-Agent': user_agent
}
data = {
    'grant_type': os.getenv('REDDIT_GRANT_TYPE'),
    'username': os.getenv('REDDIT_USERNAME'),
    'password': os.getenv('REDDIT_PASSWORD')
}
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

response = requests.post('https://www.reddit.com/api/v1/access_token',
                         headers=headers, data=data, auth=auth)

token = response.json().get('access_token')
headers['Authorization'] = f"bearer {token}"

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Prompt the user for the subreddit they want to search
subreddit_name = input("Enter the subreddit you want to search: ")

# Prompt for the timeframe for sentiment trend analysis
days = int(input("Enter the number of days to analyze: "))

sentiment_scores = []
current_end_time = datetime.now(timezone.utc)

for day in range(days, 0, -1):
    # Calculate the timestamp for days ago
    start_time = current_end_time - timedelta(days=day)
    end_time = start_time + timedelta(days=1)

    # Build the URL for the specified subreddit
    subreddit_url = f'https://oauth.reddit.com/r/{subreddit_name}/top'
    
    # Get the top posts from the specified timeframe
    params = {'limit': 100, 't': 'day', 'before': int(end_time.timestamp())}
    response = requests.get(subreddit_url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        daily_sentiment = 0
        post_count = 0
        
        print(f"\nDay: {start_time.strftime('%Y-%m-%d')} ---------------------")
        for post in data['data']['children']:
            title = post['data']['title']
            sentiment = analyzer.polarity_scores(title)
            daily_sentiment += sentiment['compound']
            post_count += 1
            
            sentiment_str = "positive" if sentiment['compound'] >= 0.05 else "negative" if sentiment['compound'] <= -0.05 else "neutral"
            print(f"Title: {title} | Sentiment: {sentiment_str}\n")

        # Calculate the average sentiment for the day
        if post_count > 0:
            average_sentiment = daily_sentiment / post_count
            sentiment_scores.append(average_sentiment)
        else:
            sentiment_scores.append(0)  # No posts found for the day
    else:
        print("Error fetching data for the day")
        sentiment_scores.append(0)  # Error case

# Plot the sentiment trend
dates = [current_end_time - timedelta(days=i) for i in range(days, 0, -1)]
plt.figure(figsize=(10, 4))
plt.plot(dates, sentiment_scores, marker='o', linestyle='-', color='b')
plt.title(f"Sentiment Trend in /r/{subreddit_name} Over {days} Days")
plt.xlabel("Date")
plt.ylabel("Average Sentiment Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
