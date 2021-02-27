import tweepy
import config as conf
import factor as fact
import models

from datetime import date

def get_date():
    today = date.today()

    c_date = str(today)[:-1]
    a = int(str(today)[-1:]) - 7

    c_date += str(a)

    return c_date


def get_tweets(words):

    auth = tweepy.OAuthHandler(conf.COSUMER_KEY, conf.CONSUMER_SECRET)
    auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    query = ""

    for word in words:
        query += word+" OR "
    query = query[:-3]
    
    date_s = get_date()

    tweets = tweepy.Cursor(api.search, q=query, lang="en",
                           since=date_s, tweet_mode='extended').items(20)
    
    print(type(tweets))
    
    return tweets

