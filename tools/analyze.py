''' This module provides functions for analyzing tweets.

TODO:
  * structure is there, make the actual content better
'''

import re
import time

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')
MODEL = SentimentIntensityAnalyzer()
REGEX_STR = r'<[^>]+>|(?:@[\w_]+)|(?:\#+[\w_]+[\w\'_\-]*[\w_]+)|\
http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|\
(?:%[0-9a-f][0-9a-f]))+|(?:(?:\d+,?)+(?:\.?\d+)?)'


def analyze_tweets(keyword: str, tweets: dict) -> dict:
    ''' This function takes a group of tweets and returns statistics
    on them like average sentiment and related hashtags
    '''
    return {
        'framework' : keyword,
        'unix_time' : int(time.time()),
        'number_of_tweets' : len(tweets),
        'sentiment' : str(average_sentiment(tweets)),
        'related_hashtag' : most_related_hashtags(tweets),
    }


def most_related_hashtags(tweets: dict) -> dict:
    ''' Function takes a list of tweets (represented as dictionaries) and
    returns the hashtags that appear most frequently.
    '''
    occurences = {}
    for tweet in tweets:
        for hashtag in tweet['hashtags']:
            hashtag = hashtag['text'].lower()
            if hashtag in occurences:
                occurences[hashtag] += 1
            else:
                occurences[hashtag] = 1
    return occurences


def average_sentiment(tweets: dict) -> float:
    ''' Function takes a list of tweets and returns the average
    sentiment of them.
    '''
    tweet_texts = clean_text(tweets)
    total = 0
    for tweet_text in tweet_texts:
        total += MODEL.polarity_scores(tweet_text)['compound']
    return total/len(tweets)


def clean_text(tweets: dict) -> [str]:
    ''' Takes a dictionary with a text attribute and returns plain text, cleaned
    of emojis, totally safe strings.
    '''
    return [re.sub(REGEX_STR, '', tweet['text']) for tweet in tweets]
