from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv

import pandas as pd

from utils.conf import OUTPUT_PATH

def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # connecting to reddit instance
    connection = connect_reddit()

    # extraction
    posts = extract_posts(connection, subreddit, time_filter, limit)

    # transformation
    posts_df = pd.DataFrame(posts)
    posts_df = transform_data(posts_df)

    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(posts_df, file_path)

    return file_path