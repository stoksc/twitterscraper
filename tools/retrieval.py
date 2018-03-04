import json
import os
import time


import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

from tools.keys import CK, CS, AT, ATS


RATE_LIMIT_CODE = 420


class IntervalListener(StreamListener):
    def __init__(self, interval_length=60):
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
        if status_code == RATE_LIMIT_CODE:
            return False
        return True

    def write_to_file(self, data):
        with open(self.file_path.format(self.interval_number), 'a') as f:
            f.write(data)
            return True


def start_stream(hashtag=None):
    assert hashtag
    auth = OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)
    api = tweepy.API(auth)
    stream = tweepy.Stream(auth=api.auth,
                           listener=IntervalListener())
    stream.filter(track=[hashtag],
                  async=True)
    return stream


def clean_tweet(tweet):
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
