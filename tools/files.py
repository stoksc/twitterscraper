import json
import os
import time

from tools.retrieval import clean_tweet


def block_until_file_exists(file_path):
    while not os.path.exists(file_path):
        time.sleep(1)


def process_file(file_path):
    cleaned_tweets = []
    with open(file_path, 'r') as f:
        for entry in f:
            tweet = json.loads(entry)
            cleaned_tweets.append(clean_tweet(tweet))
    return cleaned_tweets
