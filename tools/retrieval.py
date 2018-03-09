''' This module handles all functionality to do with retrieving and preparing
tweets from Twitter's API via a tweepy StreamListener object.
'''
import os
import time

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener



CK, CS, AT, ATS = (
    os.environ['TWITTER_CK'],
    os.environ['TWITTER_CS'],
    os.environ['TWITTER_AT'],
    os.environ['TWITTER_ATS'],
)
RATE_LIMIT_CODE = 420


class IntervalListener(StreamListener):
    ''' This class extends tweepy.streaming's StreamListener and defines custom
    behavior of our StreamListener when tweets are received.
    '''
    def __init__(self, interval_length=30):
        self.start_time = time.time()
        self.interval_length = interval_length
        self.interval_number = 0
        self.file_path = os.path.join(os.getcwd(),
                                      'data',
                                      'interval{}.json')
        super(IntervalListener, self).__init__()

    def on_data(self, data):
        ''' Defines behavior of listener on receit of a status.'''
        if (time.time() - self.start_time) > self.interval_length:
            self.interval_number += 1
            self.start_time += self.interval_length
            self.file_path = os.path.join(os.getcwd(),
                                          'data',
                                          'interval{}.json')
        self.write_to_file(data)
        return True

    def on_error(self, status):
        ''' Defines behavior of listener on non-200 return; just continue
        unless we've hit the rate limit.'''
        if status == RATE_LIMIT_CODE:
            return False
        return True

    def write_to_file(self, data):
        ''' Writes data to the current file_path stored to save new data in.
        '''
        with open(self.file_path.format(self.interval_number), 'a') as f:
            f.write(data)
            return True


def start_stream(hashtags=None):
    ''' This function starts a stream listening for tweets with hashtag=w/e was
    passed in them. The behavior of the stream upon receiving a tweet is handled
    by the IntervalListener object passed to the stream.
    '''
    assert hashtags
    auth = OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    api = tweepy.API(auth)
    stream = tweepy.Stream(auth=api.auth,
                           listener=IntervalListener())
    stream.filter(track=hashtags,
                  async=True)
    return stream


def seperate_by_keyword(keyword: str, tweets: [dict]) -> [dict]:
    ''' This function takes a list of tweets and returns the tweets that
    contain the specified keyword
    '''
    filtered_tweets = []
    for tweet in tweets:
        if keyword in tweet['text']:
            filtered_tweets.append(tweet)
            continue
        if 'extended_tweet' in tweet:
            if keyword in tweet['extended_tweet']['full_text']:
                filtered_tweets.append(tweet)
    return filtered_tweets


def clean_tweet(tweet) -> dict:
    ''' Takes a tweepy tweet object and returns a dictionary that contains
    the information from the tweet that we actually need.
    '''
    if 'extended_tweet' in tweet:
        text = tweet['extended_tweet']['full_text']
    else:
        text = tweet['text']
    return {
        'user' : tweet['user']['screen_name'],
        'text' : text,
        'hashtags' : tweet['entities']['hashtags'],
    }
