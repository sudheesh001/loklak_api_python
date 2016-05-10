#!/usr/bin/env python
# encoding: utf-8
"""The module that handles the main interface of loklak"""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import json
import re
import requests


class Loklak(object):
    """The fields for the Loklak object"""
    baseUrl = 'http://loklak.org/'
    name = None
    followers = None
    following = None
    query = None
    since = None
    until = None
    source = None
    count = None
    fields = None
    from_user = None
    fields = None
    limit = None
    action = None
    data = {}

    def __init__(self, baseUrl='http://loklak.org/'):
        baseUrl = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', baseUrl)
        try:
            if baseUrl[0]:
                if baseUrl[0] != 'http://loklak.org/':
                    url_test = self.hello()
                    if url_test['status'] == 'ok':
                        self.baseUrl = baseUrl[0]
                else:
                    self.baseUrl = baseUrl[0]
        except IndexError:
            pass

    def getBaseUrl(self):
        return self.baseUrl

    def status(self):
        """Returns the status of the server"""
        status_application = 'api/status.json'
        url_to_give = self.baseUrl+status_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return json.dumps(return_to_user)

    def hello(self):
        """Gives a hello"""
        hello_application = 'api/hello.json'
        url_to_give = self.baseUrl+hello_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return json.dumps(return_to_user)

    def geocode(self, places=None):
        """Gives the geocode"""
        geo_application = 'api/geocode.json'
        url_to_give = self.baseUrl+geo_application
        params = {}
        params['places'] = places
        return_to_user = requests.get(url_to_give, params=params)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return json.dumps(return_to_user)

    def get_map(self, latitude, longitude, width=500, height=500,
                zoom=8, text=""):
        """Returns a map of size 500x500"""
        map_application = 'vis/map.png'
        params = {'text': text, 'mlat': latitude, 'mlon': longitude,
                  'width': width, 'height': height, 'zoom': zoom}
        return_to_user = requests.get(self.baseUrl + map_application,
                                      params=params, stream=True)
        if return_to_user.status_code == 200:
            return return_to_user.raw.read()
        else:
            return ''

    def get_markdown(self, text, color_text="000000", color_bg="ffffff",
                     padding="10", uppercase="true"):
        """Returns a map of size 500x500"""
        map_application = 'vis/markdown.png'
        params = {'text': text, 'color_text': color_text, 'color_background': color_bg,
                  'padding': padding, 'uppercase': uppercase}
        return_to_user = requests.get(self.baseUrl + map_application,
                                      params=params, stream=True)
        if return_to_user.status_code == 200:
            return return_to_user.raw.read()
        else:
            return ''

    def peers(self):
        """Gives the peers of a user"""
        peers_application = 'api/peers.json'
        url_to_give = self.baseUrl+peers_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return json.dumps(return_to_user)

    def user(self, name=None, followers=None, following=None):
        """User information, including who they are following, and
        who follows them"""
        user_application = 'api/user.json'
        url_to_give = self.baseUrl+user_application
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

            return_to_user = requests.get(url_to_give, params=params)
            if return_to_user.status_code == 200:
                return return_to_user.json()
            else:
                return_to_user = {}
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('No user name given to query. Please '
                                       'check and try again')
            return json.dumps(return_to_user)

    def settings(self):
        """Gives the settings of the application"""
        settings_application = 'api/settings.json'
        url_to_give = self.baseUrl + settings_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return_to_user['error'] = 'This API has access restrictions: \
            only localhost clients are granted.'
            return json.dumps(return_to_user)

    def search(self, query=None, since=None, until=None, from_user=None, count=None):
        """Handles the searching"""
        search_application = 'api/search.json'
        url_to_give = self.baseUrl+search_application
        self.query = query
        self.since = since
        self.until = until
        self.from_user = from_user
        self.count = count
        if query:
            params = {}
            params['query'] = self.query
            if since:
                params['query'] = params['query'] + ' since:'+self.since
            if until:
                params['query'] = params['query'] + ' until:'+self.until
            if from_user:
                params['query'] = params['query'] + ' from:'+self.from_user
            if count:
                params['count'] = self.count
            return_to_user = requests.get(url_to_give, params=params)
            if return_to_user.status_code == 200:
                return return_to_user.json()
            else:
                return_to_user = {}
                return_to_user['error'] = ('Something went wrong, Looks like'
                                           ' the server is down.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('No Query string has been'
                                       ' given to run a query for')
            return json.dumps(return_to_user)

    def suggest(self, query=None, count=None, order=None, orderby=None,since=None, until=None):
        suggest_application = 'api/suggest.json'
        url_to_give = self.baseUrl+suggest_application
        params  = {}
        if query:
            params['query'] = query
        if count:
            params['count'] = count
        if order:
            params['order'] = order
        if since:
            params['since'] = since
        if until:
            params['until'] = until
        print(params)
        return_to_user = requests.get(url_to_give, params=params)
        print(return_to_user.url)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else :
            return_to_user = {}
            return_to_user['error'] = ('Something went wrong, looks like the server is down.')
            return json.dumps(return_to_user)

    def aggregations(self, query=None, since=None, until=None,
                     fields=None, limit=6, count=0):
        """Gives the aggregations of the application"""
        aggregations_application = 'api/search.json'
        url_to_give = self.baseUrl+aggregations_application
        self.query = query
        self.since = since
        self.until = until
        self.fields = fields
        self.limit = limit
        self.count = count
        if query:
            params = {}
            params['query'] = self.query
            if since:
                params['query'] = params['query']+' since:'+self.since
            if until:
                params['query'] = params['query']+' until:'+self.until
            if fields:
                if isinstance(fields, list):
                    params['fields'] = ','.join(self.fields)
                else:
                    params['fields'] = self.fields

            params['count'] = self.count
            params['source'] = 'cache'
            return_to_user = requests.get(url_to_give, params=params)
            if return_to_user.status_code == 200:
                return return_to_user
            else:
                return_to_user = {}
                return_to_user['error'] = ('Something went wrong, '
                                           'Looks like the server is down.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = 'No Query string has been given to run an\
             aggregation query for'
            return json.dumps(return_to_user)

    def account(self, name=None, action=None, data=None):
        """Displays users account"""
        account_application = 'account.json'
        url_to_give = 'http://localhost:9000/api/'+account_application
        self.name = name
        self.data = data
        self.action = action
        # Simple GET Query
        headers = {
            'User-Agent': ('Mozilla/5.0 (Android 4.4; Mobile; rv:41.0)'
                           ' Gecko/41.0 Firefox/41.0'),
            'From': 'info@loklak.org'
        }
        if name:
            params = {}
            params['screen_name'] = self.name
            return_to_user = requests.get(url_to_give, params=params,
                                          headers=headers)
            if return_to_user.status_code == 200:
                return return_to_user.json()
            else:
                return_to_user = {}
                return_to_user['error'] = ('Something went wrong, '
                                           'Looks query is wrong.')
                return json.dumps(return_to_user)
        # if action = update and data is provided, then make request
        elif self.action == 'update' and data:
            params = {}
            params['action'] = self.action
            params['data'] = self.data
            return_to_user = requests.post(url_to_give,
                                           params=params, headers=headers)
            if return_to_user.status_code == 200:
                return return_to_user.json()
            else:
                return_to_user = {}
                return_to_user['error'] = ('Something went wrong,'
                                           ' Looks query is wrong.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('No Query string has been given'
                                       ' to run an query for account')
            return json.dumps(return_to_user)
