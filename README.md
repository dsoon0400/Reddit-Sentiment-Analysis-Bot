
# Reddit Sentiment Analysis Bot

This repository contains a Python script that performs sentiment analysis on the top posts of a specified subreddit. The bot leverages the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool to analyze the emotional tone of posts, providing insights into the general sentiment of a subreddit.

## Features

- **Sentiment Analysis**: Analyzes the sentiment of posts using VADER, categorizing each post as positive, neutral, or negative.
- **Reddit API Integration**: Connects to Reddit's API to retrieve top posts from a specified subreddit.
- **OAuth 2.0 Authentication**: Uses secure OAuth 2.0 authentication for accessing Reddit data.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **PRAW (Python Reddit API Wrapper)**: Used to interact with Reddit's API.
- **VADER Sentiment Analysis**: Part of the `nltk` library.

### Install Dependencies

Run the following commands to install necessary libraries:
```bash
pip install praw
pip install nltk
```

### Setup Reddit API Credentials

1. Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps) and create a new application.
2. Note down the **Client ID**, **Client Secret**, and **User Agent**.
3. Set up a configuration file or include these details in the script as needed.

## Running the Bot

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/reddit_sentiment_analysis_bot.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd reddit_sentiment_analysis_bot
   ```

3. **Run the script**:
   ```bash
   python reddit_sentiment_bot.py
   ```

4. **Enter Subreddit**:
   - The script will prompt you to enter the name of the subreddit you want to analyze.

## Usage

- **Example**: Run the script, enter "news" as the subreddit, and receive a sentiment analysis of the top posts in r/news.
- **Output**: The bot will print the sentiment (positive, neutral, or negative) of each post and summarize the overall sentiment of the subreddit.

