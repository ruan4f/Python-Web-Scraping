import csv
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = ""
consumer_secret = ""
access_token = "-"
access_token_secret = ""

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'PaulistaoFem'
tweet_id = '1324821820206469122'

replies=[]

status = api.get_status(1324821820206469122, tweet_mode="extended")

print(status)


