import tweepy
from tweepy import OAuthHandler
import yaml
import json

with open("mining_config.yml", 'r') as keyfile:
    doc = yaml.load(keyfile)

consumer_key = doc["mysql"]["consumer_key"]
consumer_secret = doc["mysql"]["consumer_secret"]
access_token = doc["mysql"]["access_token"]
access_secret = doc["mysql"]["access_token_secret"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

while True:
    try:
        with open('twitter-data.json', 'w') as datafile:

            # Reading Timeline
            for status in tweepy.Cursor(api.home_timeline).items(10):
                # print(status.text) to just read and print
                # storing in JSON file
                json.dump(status._json, datafile)
                #print(status._json)
                #print('\n')

            # List of all followers
            for friend in tweepy.Cursor(api.friends).items():
                json.dump(friend._json, datafile)

            # List of all Tweets
            for tweet in tweepy.Cursor(api.user_timeline).item():
                json.dump(tweet._json, datafile)
        print('Complete.')
    except tweepy.RateLimitError:
        print('Rate Limit Reached.')
        break
