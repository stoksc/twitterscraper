from setuptools import setup, find_packages

setup(
    name='twitterscraper',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'boto3',
        'nltk',
        'tweepy',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
