#!/usr/bin/env python
# encoding: utf-8
import sys
from loklak import Loklak

query = sys.argv[1]
l = Loklak()
print("Retrieving Tweets...")
tweets = l.search(query)

for tweet in tweets['statuses']:
	print('@'+str(tweet['screen_name'])+': '+str(tweet['text']))