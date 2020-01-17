#coding=utf-8

import tweepy
import csv
import pandas as pd
import re

#auth declarations
CONSUMER_KEY 		= "your-key-here"
CONSUMER_SECRET_KEY = "your-skey-here"
ACCESS_TOKEN 		= "your-token-here"
ACCESS_TOKEN_SECRET = "your-stoken-here"

#regex definitions
REMOVE_STRAYS 	= r'[^\x20-\x7e]' #creds to that guy on stackoverflow
REMOVE_NEWLINES = r'\\n'


tweets = []


def clean_tweet(tweet):
	tweet 			= tweet.decode('utf-8')
	stray_filter 	= re.sub(REMOVE_STRAYS, "", tweet)
	newline_filter 	= re.sub(REMOVE_NEWLINES, " ", stray_filter)

	return newline_filter


def get_tweets():
	for tweet in tweepy.Cursor(api.search, q='#pinkfloyd -filter:retweets', count=2, tweet_mode='extended', lang='en').items():
		tweets.append(tweet.full_text.encode('utf-8'))

	cleaned_tweets = []

	for line in tweets:
		cleaned_tweets.append(clean_tweet(line))

	return cleaned_tweets


if __name__ == "__main__":
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	tweet_list = get_tweets()

	df = pd.DataFrame(tweet_list)
	df.to_csv(r"df.csv")

