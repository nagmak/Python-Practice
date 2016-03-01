#! python3

# Import methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables with user credentials to access the Twitter API
access_token = "507100158-jOzjXuEgDfVuTYwxbt4MR4vzUCepeHAqCA9Vgp7Y"
access_token_secret = "Jdhzdo30uiB6JPTPK6MLgoq6rEu7E55MushHE8YYk2GeG"
consumer_key = "lIvH5Y3rCJ9j8nQcidLBtvKUW"
consumer_secret = "hxHCV6exazbl72NgKmU6uU2lkgpsSpWAxf1732Guc8jKIlLzEf"

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
