import tweepy

import calc.config as conf
import calc.factor as fact

from models import Tweet

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
                           since=date_s, tweet_mode='extended').items(50)

    tweets_list = get_proper_tweets(tweets)

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

        print("\nhere's the text:", text, '\n\n')

        _tweet = Tweet(tweet_id, name, user_id, text, likes, rts, tweet_date)
        tweet_list.append(_tweet)
    return tweet_list
