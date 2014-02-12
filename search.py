import json

import sys

import os

import twython

from twython import Twython



APP_KEY = 'YOURAPPKEY'

APP_SECRET = 'YOURAPPSECRET'



OAUTH_TOKEN = 'YOURTOKEN'

OAUTH_TOKEN_SECRET = 'YOURTOKENSECRET'



twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

results = twitter.search(q='KEYWORD', geocode='LOCATION', count=1000)

f = open(os.path.expanduser("PATHTOTWEETS/tweets.txt"), 'w')

sys.stdout = f

for tweet in results['statuses']:
    print tweet['user']['screen_name'].encode('utf-8')
    if tweet['place']: print tweet['place']['name']
    print tweet['created_at'].encode('utf-8')
    print tweet['text'].encode('utf-8'), "\n"
