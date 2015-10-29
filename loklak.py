#!/usr/bin/env python
# encoding: utf-8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import copy
import math
import sys
import time
from collections import namedtuple
import requests
import json

class Loklak (object):
	baseUrl = 'http://loklak.org/api/'
	name = None
	followers = None
	following = None

	def status(self):
		statusAPI = 'status.json'
		Url = self.baseUrl+statusAPI
		r = requests.get(Url)
		if r.status_code == 200:
			return r.json()
		else:
			r = {}
			return json.dumps(r)

	def hello(self):
		helloAPI = 'hello.json'
		Url = self.baseUrl+helloAPI
		r = requests.get(Url)
		if r.status_code == 200:
			return r.json()
		else:
			r = {}
			return json.dumps(r)

	def peers(self):
		peersAPI = 'peers.json'
		Url = self.baseUrl+peersAPI
		r = requests.get(Url)
		if r.status_code == 200:
			return r.json()
		else:
			r = {}
			return json.dumps(r)

	def user(self, name = None, followers=None, following=None):
		userAPI = 'user.json'
		Url = self.baseUrl+userAPI
		self.name = name
		self.followers = followers
		self.following = following
		if name:
			params = {}
			params['screen_name'] = self.name
			if followers is not None:
				params['followers'] = self.followers
			if following is not None:
				params['following'] = self.following

			r = requests.get(Url, params=params)
			if r.status_code == 200:
				return r.json()
			else:
				r = {}
				return json.dumps(r)
		else:
			r = {}
			r['error'] = 'No user name given to query. Please check and try again'
			return json.dumps(r)

	def settings(self):
		settingsAPI = 'settings.json'
		Url = 'http://localhost:9000/api/'+settingsAPI
		r = requests.get(Url)
		if r.status_code == 200:
			return r.json()
		else:
			r = {}
			 r['error'] = 'This API has access restrictions: only localhost clients are granted.'
			return json.dumps(r)


def main():
	"""
		Command line interface
	"""
	import argparse
	import os
	import multiprocessing

	parser = argparse.ArgumentParser(description="Python wrapper around the loklak API.")
	parser.add_argument('-s', '--search', action='store_true', help='Search API Wrapper which helps to query loklak for JSON results.')
	parser.add_argument('-t', '--status', action='store_true', help='Status API Wrapper for the loklak status check.')
	parser.add_argument('-st', '--suggest', action='store_true', help='Suggestions API Wrapper , Works better with local loklak instance.')
	parser.add_argument('-c', '--crawler', action='store_true', help='Crawler API Wrapper on Loklak to crawl for tweets for a particular crawl depth.')
	parser.add_argument('-h', '--hello' , action='store_true', help='Loklak status check API.')
	parser.add_argument('-g', '--geocode', action='store_true', help='Geocode API for geolocation based information.')
	parser.add_argument('-p', '--peers', action='store_true', help='Loklak API for peers connected on the distributed network.')
	parser.add_argument('-pg', '--pushgeojson', action='store_true', help='Public API to push geojson objects to the loklak server.')
	parser.add_argument('-u', '--user', action='store_true', help='User API to show twitter user information.')
	parser.add_argument('-m', '--map', action='store_true', help='Map Visualization render using Loklak service.')
	parser.add_argument('-md', '--markdown', action='store_true', help='Markdown conversion API to render markdown as image using Loklak.')
	args = parser.parse_args()
