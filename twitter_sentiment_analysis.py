import tweepy
from textblob import TextBlob

# step 1 - Authenticate
consumer_key = 'rhCDHS4ke1Tbw0BZZathcNZAK'
consumer_secret = 'MrOn7y8XpLkBZsCpZlE8coDfKMwz2GnozHW6SVLb8AmIAeUxhu'
access_token='579672656-JmJvmbrNj2OPuq3ZTo5Fq7eHHzmhB8QYXTSifsdc'
access_token_secret='o2sDQqztwiOo4V9Nr8zCtXkLGKaNffsH2J9YYYrfec8eQ'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# step 2 - retrieve tweets
api = tweepy.API(auth)
public_tweets = api.search(q=['gedung'], count=10)

all_polarity = 0
for tweet in public_tweets:
    print(tweet.text)
    # step 3 - perform sentiment analysis on tweets
    analysis = TextBlob(tweet.text)
    an = analysis.translate(from_lang='id', to='en')
    print(an.sentiment)
    all_polarity += an.polarity
    print("")
    
if(all_polarity/100 > 0):
    print(all_polarity/100)
    print("")
    print('Positive')
else:
    print(all_polarity/100)
    print("")
    print('Negative')
