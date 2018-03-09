''' This module handles any file management needed by run.py on the bottom
level.
'''
import json
import os
import time

from .retrieval import clean_tweet


def block_until_file_exists(file_path: str) -> None:
    ''' Blocks the calling thread of execution until the file at file_path
    exists.
    '''
    while not os.path.exists(file_path):
        time.sleep(1)


def process_file(file_path: str) -> dict:
    ''' Reads a file full of JSON entries and picks them out, one by one,
    appending them to an array to return.
    '''
    cleaned_tweets = []
    with open(file_path, 'r') as data_file:
        for entry in data_file:
            tweet = json.loads(entry)
            cleaned_tweets.append(clean_tweet(tweet))
    return cleaned_tweets
