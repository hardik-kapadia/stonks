from django.db import models
# Create your models here.


class stock:
    def __init__(self, name, symbol, history, country):
        self.name = name
        self.symbol = symbol
        self.history = history
        self.words = [symbol, self.name.split(' ')[0]]
        self.country = country


class Tweet:

    def __init__(self, tweet_id, tweet_user_name, tweet_user_id, tweet_body, tweet_like_count, tweet_rt_count, tweet_date):
        self.tweet_id = tweet_id
        self.tweet_user_name = tweet_user_name
        self.tweet_user_id = tweet_user_id
        self.tweet_body = tweet_body
        self.tweet_like_count = tweet_like_count
        self.tweet_rt_count = tweet_rt_count
        self.tweet_date = tweet_date

    def set_score(self, score):
        self.score = score
