import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys

sys.stdout.reconfigure(encoding='utf-8')

client_id = 'd5fvQl6EYX9fn7A1NokZcg'
client_secret = 'JJKNeQVbPvsClNlZ8ywpR1_NIzBaVw'
user_agent = "python:sentiment_analysis_bot:1.0 (by /u/LolliTek')"

headers = {
    'User-Agent': user_agent
}
data = {
    'grant_type': 'password',
    'username': 'Lollitek',
    'password': 'davidman132'
}
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

response = requests.post('https://www.reddit.com/api/v1/access_token',
                         headers=headers, data=data, auth=auth)

token = response.json().get('access_token')
headers['Authorization'] = f"bearer {token}"

#Initialize VADER
analyzer = SentimentIntensityAnalyzer()

#Prompt the user for the subreddit they want to search
subreddit_name = input("Enter the subreddit you want to search: ")

#Build the URL for the specified subreddit
subreddit_url = f'https://oauth.reddit.com/r/{subreddit_name}/top'

#Get the top posts from the specified subreddit
response = requests.get(subreddit_url, headers=headers, params={'limit': 30})

#Check if the subreddit is valid (response status code 200)
if response.status_code == 200:
    data = response.json()
        
    for post in data['data']['children']:
        title = post['data']['title']
        sentiment = analyzer.polarity_scores(title)
        
        if sentiment['compound'] >= 0.05:
            sentiment_str = "positive"
        elif sentiment['compound'] <= -0.05:
            sentiment_str = "negative"
        else:
            sentiment_str = "neutral"
            
        print(f"Title: {title} | Sentiment: {sentiment_str}")
else:
    print("Invalid Subreddit")
