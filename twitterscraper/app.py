''' This module runs the the whole shebang. It gets a DB connection, starts a
stream listener, processes the tweets collected by it in 10-minute intervals
and
'''
import os
import sys

from .tools.analyze import analyze_tweets
from .tools.db import get_dynamodb_table
from .tools.files import block_until_file_exists, process_file
from .tools.retrieval import seperate_by_keyword, start_stream


AWS_AK, AWS_SK = os.environ['AWS_AK'], os.environ['AWS_SK']
KEYWORDS = sys.argv[1:]
FILE_PATH = os.path.join(os.getcwd(), 'data', 'interval{}.json')
TABLE_NAME = 'frameworks'


def main():
    table = get_dynamodb_table(table=TABLE_NAME,
                               access_key=AWS_AK,
                               secret_key=AWS_SK)
    start_stream(KEYWORDS)
    interval_number = 0
    while True:
        block_until_file_exists(FILE_PATH.format(interval_number + 1))
        cleaned_tweets = process_file(FILE_PATH.format(interval_number))
        for keyword in KEYWORDS:
            cleaned_keyword_tweets = seperate_by_keyword(keyword, cleaned_tweets)
            if cleaned_keyword_tweets:
                table.put_item(Item=analyze_tweets(keyword, cleaned_keyword_tweets))
        os.remove(FILE_PATH.format(interval_number))
        interval_number += 1


if __name__ == "__main__":
    main()
