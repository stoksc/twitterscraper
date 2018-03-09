![Build Status](https://travis-ci.org/stoksc/twitterscraper.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/stoksc/twitterscraper/badge.svg?branch=master)](https://coveralls.io/github/stoksc/twitterscraper?branch=master)
### twitterscraper

Listens for tweets of a given hashtag, analyzes them, and stores the restores in DynamoDB.

##### Getting Started
To get started, clone this repository (`git clone https://github.com/stoksc/twitterscraper`).

Then make a new Python3.6 Virtual Environment with `virtualenv` (`virtualenv -p python3.6 venv`), activate it (`source venv/bin/activate`), and install the package with `pip install .`.

After this, you'll need to set some environment variables for the program to use. Specifically, you need `AWS_AK, AWS_SK, TWITTER_CK, TWITTER_CS, TWITTER_AT, TWITTER_ATS` which are your AWS access key and secret key (IAM users with DynamoDB full access) and your Twitter API consumer key, consumer secret, access token and access token secret.

Then just run the program followed by the keywords you want to track:

`python twitterscraper/app.py keyword1 keyword2`

They some poorly selected metadata from the tweets will be stored every 10-minutes into a DynamoDB table.

##### Built With

- [boto3](https://boto3.readthedocs.io/en/latest/) - Boto is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of Amazon services like S3 and EC2. Boto provides an easy to use, object-oriented API as well as low-level direct service access..
- [tweepy](http://docs.tweepy.org/en/v3.6.0/) - Python3 wrapper for the Twitter API.
- [nltk](https://www.nltk.org/) - NLTK is a leading platform for building Python programs to work with human language data.

##### Author

* [stoksc](https://github.com/stoksc)
