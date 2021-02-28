import tweepy

from . import config as conf
from . import factor as fact

from .models import Tweet

# from datetime import date
import datetime as DT


def get_date(x: int):
    today = DT.date.today()

    s_date = today - DT.timedelta(days=x)
    e_date = today - DT.timedelta(days=x - 1)

    return str(s_date), str(e_date)


def get_tweets(words):

    auth = tweepy.OAuthHandler(conf.COSUMER_KEY, conf.CONSUMER_SECRET)
    auth.set_access_token(conf.ACCESS_TOKEN, conf.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    query = ""

    for word in words:
        query += word+" OR "
    query = query[:-3]

    tweets_list = []

    date_s, date_e = get_date(2)
    print('This is the one: ', date_s)

    tweets = tweepy.Cursor(api.search, q=query, lang="en",
                           since=date_s, tweet_mode='extended', result_type='popular').items(8)

    tweets_list.extend(get_proper_tweets(tweets))

    for i in range(1, 10):

        date_s, date_e = get_date(i)

        # print("date: ", date_s, date_e)

        tweets = tweepy.Cursor(api.search, q=query, lang="en",
                               since=date_s, until=date_e, tweet_mode='extended', result_type='popular').items(4)

        tweets_list.extend(get_proper_tweets(tweets))

    count = 1

    return tweets_list


def get_proper_tweets(tweets):

    tweet_list = []

    for tweet in tweets:

        tweet_id = tweet.id
        user = tweet.user
        likes = tweet.favorite_count
        rts = tweet.retweet_count

        if(int(likes) == 0 and int(rts) == 0):
            continue

        user_id = user.id_str
        name = user.screen_name

        try:
            text = tweet.retweeted_status.full_text
            likes = tweet.retweeted_status.favorite_count
            rts = tweet.retweeted_status.retweet_count
        except AttributeError:
            text = tweet.full_text
            likes = tweet.favorite_count
            rts = tweet.retweet_count

        tweet_date = tweet.created_at
        tweet_date = str(tweet_date)[:10]

        _tweet = Tweet(tweet_id, name, user_id, text, likes, rts, tweet_date)
        tweet_list.append(_tweet)
    return tweet_list


# get_tweets(['GME'])
