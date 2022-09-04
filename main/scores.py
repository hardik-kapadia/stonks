from flair.data import Sentence
from flair.models import TextClassifier
import flair
import numpy as np
import pandas as pd
import re
import nltk
from . import twitter
from .models import Tweet, stock
from . import get_stocks

from . import factor as fact
import datetime as DT

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')


def get_data(tweet):
    _data = {
        'id': tweet.tweet_id,
        'created_at': tweet.tweet_date,
        'text': tweet.tweet_body,
        'tweet_like_count': tweet.tweet_like_count,
        'tweet_rt_count': tweet.tweet_rt_count
    }
    return _data


class process:

    def __init__(self, df):
        self.df = df

    def noise_removal(self, sentence):

        for i in range(len(sentence)):
            sentence[i] = sentence[i].lower()
            sentence[i] = re.sub(r'\W', ' ', sentence[i])
            sentence[i] = re.sub(r'\d', ' ', sentence[i])  # removes digits
            sentence[i] = re.sub(r'\s+', ' ', sentence[i])  # removes spaces
            words = nltk.word_tokenize(sentence[i])
            new = []
            for word in words:
                if word not in stopwords.words('english'):
                    new.append(word)
            sentence[i] = ' '.join(new)
        return sentence[0]

    def lemmetization(self, tweet):
        df = self.df
        lem = WordNetLemmatizer()

        for i in range(len(df['text'])):
            words = nltk.word_tokenize(df['text'][i])
            words = [lem.lemmatize(word, pos='v') for word in words]
            df['text'][i] = ' '.join(words)

    def predictionsentiment(self, tweet):
        # print(f'Tweet senti....: ${tweet}')
        classifier = TextClassifier.load('en-sentiment')
        sentence = Sentence(tweet)
        print(tweet)
        classifier.predict(sentence)
        x = str(sentence.labels[0])
        # print(x)
        y = x.split(' ')
        # print(f'all of y :{y}')
        # print(f'last of y---: -- {y[-1]}')
        # print(f'second last of y---: -- {y[-2]}')
        z = float(y[-1][1:-1])
        if (str(y[-2]) == 'POSITIVE'):
            return z
        else:
            return (z*-1)


def get_initial_df(tweets):

    df = pd.DataFrame()

    for i in tweets:
        twit = get_data(i)
        df = df.append(twit, ignore_index=True)

    return df


def get_formatted_df(df):
    processor = process(df)
    df['text'] = df['text'].apply(lambda x: processor.noise_removal([x]))
    df['text'].apply(lambda x: processor.lemmetization(x))
    df['Probability'] = df['text'].apply(
        lambda x: processor.predictionsentiment(x))

    return df


def get_daily_scores(df, stock__):
    print(df)
    print('\n\n')
    print(stock__.history)


def get_score(_stock_):
    tweets = twitter.get_tweets(_stock_.words)
    df = get_initial_df(tweets)
    df = get_formatted_df(df)

    df['score'] = df['Probability'] * ((df['tweet_like_count'] * fact.LIKE_FACTOR) +
                                       (df['tweet_rt_count']*fact.RT_FACTOR))

    df2 = df.groupby(['created_at'])['score'].sum()

    df3 = df2.to_dict()

    print(df3)

    hist = _stock_.history
    hist['gain'] = hist['Close'] - hist['Open']

    print(hist)

    prediction = False

    latest_avg = 0
    try:
        latest_avg = (float(df3[str(DT.date.today())]) +
                      float(df3[str(DT.date.today() - DT.timedelta(days=1))]))
    except KeyError:
        print('Got thee error')
        latest_avg = float(
            df3[str(DT.date.today() - DT.timedelta(days=1))]) * 2

    print('\n\n Latest avg: ', latest_avg, '\n\n')
    prediction = latest_avg > 0
    count = 0

    avg = 0

    # mult = 1

    in_favour = 0
    against = 0

    for i, row in hist.iterrows():
        dt = str(i)[:10]
        gain = float(row['gain'])
        try:
            social_media_score = float(df3[dt])
        except KeyError:
            continue

        x = gain / social_media_score

        if x > 0:
            print('adding to favor')
            in_favour += 1
        else:
            print('adding t against')
            against += 1

        avg += abs(x)
        count += 1

        print(dt, gain, social_media_score, x)

    print('count is: ', count)
    print("and herrreeee's Johny: ", in_favour, against)

    if in_favour > against:
        mult = in_favour / count
    else:
        print('\n\nway down we go\n\n')
        mult = against/count
        mult *= -1

    avg = avg/count

    print('mult is', mult)

    result = latest_avg * avg * mult

    print('\n\n\n------------------\navg is', avg)

    print('Predicted gain:', result)

    closing_price = 0
    current_price = get_stocks.get_current_stock_price(_stock_.symbol)
    if (current_price == 0):
        m = hist['Close']
        closing_price = m[-1]
        current_price = closing_price

    print('Latest Price:', current_price)

    future_price = current_price + result
    print('Predicted Price: %.2f' % future_price)

    return result, future_price, current_price


# stt = get_stocks.get_stock('Tesla')
# get_score(stt[0])
