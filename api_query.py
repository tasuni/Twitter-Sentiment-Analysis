import tweepy
import csv
import pandas as pd
import re
import tweet_preprocess as tp

CONSUMER_KEY = "your-key-here"
CONSUMER_SECRET_KEY = "your-skey-here"
ACCESS_TOKEN = "your-token-here"
ACCESS_TOKEN_SECRET = "your-stoken-here"


class TweepyHandler:
	def set_auth(self, consumer_key, consumer_secret_key, access_token, access_token_secret):
		"""
		Setup the auth keys and access tokens for the api instance
		"""
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
		auth.set_access_token(access_token, access_token_secret)
		api = tweepy.API(auth)

		return api


	def get_tweets(self, hashtag, api):
		"""
		Get 1000 cleaned preprocessed tweets from the created API instance
		"""
		tweet_count = 0
		tweets = []

		# Get 1k tweets
		for tweet in tweepy.Cursor(api.search, q= f'#{hashtag} -filter:retweets', count=1000, tweet_mode='extended', lang='en').items():
			tweets.append(tweet.full_text.encode('utf-8'))
			tweet_count += 1

			if tweet_count == 1000:
				break

		# Clean the obtained tweets
		cleaned_tweets = []

		for line in tweets:
			cleaned_tweets.append(tp.preprocess(tp.clean_tweet(line)))
		return cleaned_tweets


if __name__ == "__main__":
	Tweep = TweepyHandler()
	tweep = Tweep.set_auth(CONSUMER_KEY, CONSUMER_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	tweet_list = Tweep.get_tweets("pinkfloyd", tweep)

	df = pd.DataFrame(tweet_list)
	df.to_csv(r"df.csv")

