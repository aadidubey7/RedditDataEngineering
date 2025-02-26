import sys

import praw
from praw import Reddit

import pandas as pd
import numpy as np

from utils.conf import POST_FIELDS, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def connect_reddit() ->  Reddit:
    try:
        reddit = praw.Reddit(
            client_id = 'rIFJ_lsQSHPmtkqeK25Nog',
            client_secret = 'pja-RxOmo9QbwP8pn7iVF1kASVV7HQ',
            user_agent = 'aditya-dev'
        )
        print("Connected to reddit")
        return reddit
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    posts_list = []
    for post in posts:
        post_dict = vars(post)
        post = { key: post_dict[key] for key in POST_FIELDS }
        posts_list.append(post)

    return posts_list

def transform_data(posts_df: pd.DataFrame):
    posts_df['created_utc'] = pd.to_datetime(posts_df['created_utc'], unit='s')
    posts_df['over_18'] = np.where((posts_df['over_18'] == True), True, False)
    posts_df['author'] = posts_df['author'].astype(str)
    edited_mode = posts_df['edited'].mode()
    posts_df['edited'] = np.where(posts_df['edited'].isin([True, False]),
                                  posts_df['edited'], edited_mode).astype(bool)
    posts_df['num_comments'] = posts_df['num_comments'].astype(int)
    posts_df['score'] = posts_df['score'].astype(int)
    # posts_df['upvote_ratio'] = posts_df['upvote_ratio'].astype(int)
    # posts_df['selftext'] = posts_df['selftext'].astype(str)
    posts_df['title'] = posts_df['title'].astype(str)

    return posts_df

def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)

