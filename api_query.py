#coding=utf-8

import tweepy
import csv
import pandas as pd
import re

CONSUMER_KEY = "abc"
CONSUMER_SECRET_KEY = "abc"
ACCESS_TOKEN = "abc"
ACCESS_TOKEN_SECRET = "abc"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

csv_file = open('tweets.csv', 'a')
csv_writer = csv.writer(csv_file)

tweets = []

REMOVE_STRAYS = r'\\x\w{2}'
REMOVE_NEWLINES = r'\\n'


def clean_tweet(tweet):
	stray_filter = re.sub(REMOVE_STRAYS, "", tweet)
	newline_filter = re.sub(REMOVE_NEWLINES, " ", tweet)

	return newline_filter


for tweet in tweepy.Cursor(api.search, q='#pinkfloyd -filter:retweets', count=2, tweet_mode='extended', lang='en').items():
	unclean_tweet = str(tweet.full_text.encode('utf-8'))
	cleaned_tweet = clean_tweet(unclean_tweet)
	csv_writer.writerow([tweet.created_at, cleaned_tweet])
	tweets.append(cleaned_tweet)


df = pd.DataFrame(tweets)
df.to_csv(r"df.csv")

	
