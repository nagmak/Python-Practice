#! python3

# Import methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import yaml

with open("twitter_config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# Variables with user credentials to access the Twitter API
access_token = cfg["mysql"]["access_token"]
access_token_secret = cfg["mysql"]["access_token_secret"]
consumer_key = cfg["mysql"]["consumer_key"]
consumer_secret = cfg["mysql"]["consumer_secret"]

# Prints received tweets to stdout

class StdOutListener(StreamListener):
    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    # Twitter authentication + connection to Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Filter Twitter Streams to capture data with keyword: Hackathon
    stream.filter(track=['hackathon'])
