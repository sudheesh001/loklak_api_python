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
	q = None
	since = None
	until = None
	source = None
	count = None
	fields = None
	fromUser = None
	fields = None
	limit = None
	action = None
	data = {}

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

	def geocode(self, places=None):
		geoAPI = 'geocode.json'
		Url = self.baseUrl+geoAPI
		params = {}
		params['places'] = places
		r = requests.get(Url, params=params)
		if r.status_code == 200:
			return r.json()
		else :
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

	def search(self, q=None, since=None, until=None, fromUser=None):
		searchAPI = 'search.json'
		Url = self.baseUrl+searchAPI
		self.q = q
		self.since = since
		self.until = until
		self.fromUser = fromUser
		if q:
			params = {}
			params['q'] = self.q
			if since:
				params['q'] = params['q']+' since:'+self.since
			if until:
				params['q'] = params['q']+' until:'+self.until
			if fromUser:
				params['q'] = params['q']+' from:'+self.fromUser
			r = requests.get(Url, params=params)
			if r.status_code == 200:
				return r.json()
			else:
				r = {}
				r['error'] = 'Something went wrong, Looks like the server is down.'
				return json.dumps(r)
		else:
			r = {}
			r['error'] = 'No Query string has been given to run a query for'
			return json.dumps(r)

	def aggregations(self, q=None, since=None, until=None, fields=None, limit=None):
		aggregationsAPI = 'search.json'
		Url = self.baseUrl+aggregationsAPI
		self.q = q
		self.since = since
		self.until = until
		self.fields = fields # Array seperated values to be passed
		self.limit = limit
		if q:
			params = {}
			params['q'] = self.q
			if since:
				params['q'] = params['q']+' since:'+self.since
			if until:
				params['q'] = params['q']+' until:'+self.until
			if fields:
				fieldStringCSV = ''
				for i in self.fields:
					fieldStringCSV+=i+','
				params['fields'] = fieldStringCSV
			if limit:
				params['limit'] = self.limit
			if limit == None:
				limit = 6
				params['limit'] = self.limit
			params['count'] = 0
			params['source'] = 'cache'
			r = requests.get(Url, params=params)
			if r.status_code == 200:
				return r
			else:
				r = {}
				r['error'] = 'Something went wrong, Looks like the server is down.'
				return json.dumps(r)
		else:
			r = {}
			r['error'] = 'No Query string has been given to run an aggregation query for'
			return json.dumps(r)

	def account(self, name=None, action=None, data =None):
		accountAPI = 'account.json'
		Url = 'http://localhost:9000/api/'+accountAPI
		self.name = name
		self.data = data
		self.action = action
		# Simple GET Query
		headers = {
			'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
			'From': 'info@loklak.org'
		}
		if name:
			params = {}
			params['screen_name'] = self.name
			r = requests.get(Url, params=params, headers=headers)
			if r.status_code == 200:
				return r.json()
			else:
				r = {}
				r['error'] = 'Something went wrong, Looks query is wrong.'
				return json.dumps(r)
		# if action = update and data is provided, then make request
		elif self.action == 'update' and data:
			params = {}
			params['action']=self.action
			params['data']=self.data
			r = requests.post(Url, params=params, headers=headers)
			if r.status_code == 200:
				return r.json()
			else:
				r = {}
				r['error'] = 'Something went wrong, Looks query is wrong.'
				return json.dumps(r)
		else:
			r = {}
			r['error'] = 'No Query string has been given to run an query for account'
			return json.dumps(r)
