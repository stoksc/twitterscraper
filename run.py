import json
import os
import time

import tweepy
from tweepy import Stream

from tools.analyze import analyze_tweets
from tools.db import get_dynamodb_table
from tools.files import block_until_file_exists, process_file
from tools.keys import AWS_AK, AWS_SK
from tools.retrieval import start_stream, clean_tweet


HASHTAG = 'python'
FILE_PATH = os.path.join(os.getcwd(), 'data', 'interval{}.json')


def main():
    table = get_dynamodb_table(table=HASHTAG,
                               access_key=AWS_AK,
                               secret_key=AWS_SK)
    start_stream(HASHTAG)
    interval_number = 0
    while True:
        block_until_file_exists(FILE_PATH.format(interval_number + 1))
        cleaned_tweets = process_file(FILE_PATH.format(interval_number))
        table.put_item(Item=analyze_tweets(interval_number, cleaned_tweets))
        interval_number += 1


if __name__ == "__main__":
    main()