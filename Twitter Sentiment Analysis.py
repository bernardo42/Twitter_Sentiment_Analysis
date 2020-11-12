import tweepy
from textblob import TextBlob

# step 1 - Authenticate
consumer_key = 'Your consumer_key'
consumer_secret = 'Your consumer_secret'
access_token='Your access_token'
access_token_secret='Your access_token_secret'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# step 2 - retrieve tweets
api = tweepy.API(auth)
public_tweets = api.search(q=['perasaan'], count=10)

all_polarity = 0
for tweet in public_tweets:
    print(tweet.text)
    # step 3 - perform sentiment analysis on tweets
    analysis = TextBlob(tweet.text)
    an = analysis.translate(from_lang='id', to='en')
    print("Subjectivity : ", an.sentiment.subjectivity)
    print("Polarity : ", an.sentiment.polarity)
    if(an.sentiment.polarity > 0):
        print('Positive')
    else:
        print('Negative')
    print('')