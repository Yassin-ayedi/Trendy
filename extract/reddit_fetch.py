import os
import logging
from utils import upload_to_datalake
import json
import praw
import pandas as pd
from datetime import datetime
import time
from tqdm import tqdm


def fetch_reddit():
    reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
    reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    reddit_user_agent = os.getenv("REDDIT_USER_AGENT")
    
    subreddits=["dataanalysis","datascience","dataengineering","datascience","businessanalysis","MachineLearning","programming","coding","aws","azure","googlecloud"]
    subreddit_to_job = {
    "programming": "Software Engineer",
    "coding": "Software Engineer",
    "aws": "Cloud Engineer",
    "azure": "Cloud Engineer",
    "googlecloud": "Cloud Engineer",
    }
    
    
    reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent=reddit_user_agent,
    ratelimit_seconds=5,  
    timeout=30
    )
    
    posts = []

    for subreddit_name in tqdm(subreddits):
        logging.info(f"Fetching posts from r/{subreddit_name}...")
        subreddit = reddit.subreddit(subreddit_name)


        for submission in subreddit.new(limit=50):  
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "job": subreddit_name,
                'score': submission.score,
                'num_comments': submission.num_comments,
                "total_awards": submission.total_awards_received,
                "date": submission.created_utc
            })
            time.sleep(1)  

    df = pd.DataFrame(posts)
    df['job'] = df['job'].map(subreddit_to_job).fillna(df['job'])

    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"reddit_posts_{timestamp}.json"
    json_data = df.to_json(orient="records", indent=2)

    # Upload to Data Lake (bronze)
    upload_to_datalake(json_data, file_name, filesystem_name="bronze/reddit")
    


