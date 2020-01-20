import re

# regex definitions
REMOVE_LINKS		= "(https://t.co/)[\w\d]*|(t.co/)[\w\d]*" 
REMOVE_PUNCTUATIONS = "[.,;?\"\'()\[\]!]"
REPLACE_WITH_SPACE  = "[(\-)|(\/)|:]"
FIX_AMPS			= "&amp"
REMOVE_STRAYS 		= r'[^\x20-\x7e]' #creds to that guy on stackoverflow
REMOVE_NEWLINES 	= r'\\n'


def preprocess(tweet):
	"""
	Processes through the input tweet, and removes t.co links, and punctuations while fixing other
	encoding errors. Also converts the whole text to lowercase.
	"""
	tweet 			= tweet.lower()
	tweet_no_links 	= re.sub(REMOVE_LINKS, "", tweet)
	tweet_w_space 	= re.sub(REPLACE_WITH_SPACE, " ", tweet_no_links)
	tweet_no_punc	= re.sub(REMOVE_PUNCTUATIONS, "" , tweet_w_space)
	clean_tweet		= re.sub(FIX_AMPS, "&", tweet_no_punc)

	return clean_tweet


def clean_tweet(tweet):
	"""
	Removes the stray bytes from the mined tweets.
	"""
	tweet 			= tweet.decode('utf-8')
	stray_filter 	= re.sub(REMOVE_STRAYS, "", tweet)
	newline_filter 	= re.sub(REMOVE_NEWLINES, " ", stray_filter)

	return newline_filter


