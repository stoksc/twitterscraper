FROM python:3.6-slim

WORKDIR /twitterscraper

ADD . /twitterscraper

RUN pip install -e .

CMD ["python", "app.py"]
