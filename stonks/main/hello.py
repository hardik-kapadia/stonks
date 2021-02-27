from flair.data import Sentence
from flair.models import TextClassifier
import flair
import numpy as np
import pandas as pd
import re
import nltk
import twitter
from models import Tweet, stock

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')


def get_data(tweet):
    _data = {
        'id': tweet.tweet_id,
        'created_at': tweet.tweet_date,
        'text': tweet.tweet_body,
        'tweet_like_count': tweet.tweet_like_count,
        'tweet_rt_count': tweet.tweet_rt_count
    }
    return _data


def noise_removal(sentence):

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


def lemmetization(tweet):
    lem = WordNetLemmatizer()

    for i in range(len(df['text'])):
        words = nltk.word_tokenize(df['text'][i])
        words = [lem.lemmatize(word, pos='v') for word in words]
        df['text'][i] = ' '.join(words)


def predictionsentiment(tweet):
    classifier = TextClassifier.load('en-sentiment')
    sentence = Sentence(tweet)
    classifier.predict(sentence)
    print(sentence)
    x = str(sentence.labels[0])
    y = x.split(' ')
    z = float(y[1][1:len(y[1])-1])
    if(str(y[0]) == 'POSITIVE'):
        return z
    else:
        return (z*-1)


tweets = twitter.get_tweets(['GME'])
print('No. of tweets:', len(tweets))

df = pd.DataFrame()

for i in tweets:
    twit = get_data(i)
    df = df.append(twit, ignore_index=True)

print(df)


df['text'] = df['text'].apply(lambda x: noise_removal([x]))

print('\n\n\nAfter noise\n\n\n')
print(df)
df['text'].apply(lambda x: lemmetization(x))
print('\n\n\nAfter Lemit\n\n\n')
print(df)

df['Probabilty'] = df['text'].apply(lambda x: predictionsentiment(x))

print('\n\n\nFinal\n\n\n')

print(df)
