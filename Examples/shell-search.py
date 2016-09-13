#!/usr/bin/env python
# encoding: utf-8
"""This module contains an example of retrieving tweets using search() function and print them in the console."""
import sys
from loklak import Loklak

query = sys.argv[1]
l = Loklak()
print("Retrieving Tweets...")
tweets = l.search(query)

for tweet in tweets['statuses']:
	print('@'+str(tweet['screen_name'])+': '+str(tweet['text']))