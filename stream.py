import json  
from twython import Twython, TwythonError, TwythonStreamer
import pymongo 

# Setup Authentification Settings
APP_KEY = 'YOURKEY' 
APP_SECRET = 'YOURSECRET' 

OAUTH_TOKEN = 'YOURTOKEN' 
OAUTH_TOKEN_SECRET = 'YOURTOKENSECRET'  

# Obtain an OAuth 2 Access Token
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

# Use the Access Token
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

# Setup a connection to mongodb
connection = pymongo.Connection('localhost', 27017)
db = connection.DATABASENAME

# Define a class to handle the stream
class Streamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            db.tweets.save(data) # Take the data in text and save it to the mongodb DATABASE.tweets
    
    def on_error(self, status_code, data):
        print status_code, data

# Start the stream
stream = Streamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(track = 'KEYWORDS') 
