#!/usr/bin/env python
# encoding: utf-8
"""The module that handles the main interface of loklak."""
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import json
import re
import requests
from xmljson import badgerfish as bf
from json import dumps
import csv


class Loklak(object):
    """The fields for the Loklak object.

    Additionaly, it contains methods that can be used for accessing
    the Loklak API services like geocode, markdown, etc.

    """

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
        """Constructor of the Loklak class.

        Args:
            baseUrl (str): Base URL for accessing the APIs (default=http://loklak.org).

        """
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
        """Return the string value of baseUrl."""
        return self.baseUrl

    def status(self):
        """Retrieve a json response about the status of the server."""
        status_application = 'api/status.json'
        url_to_give = self.baseUrl+status_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return json.dumps(return_to_user)

    def xmlToJson(self, xmlData = None):
        """Convert XML to JSON as the service."""
        jsonData = ''
        if xmlData:
            jsonData = dumps(bf.data(fromstring(xmlData)))
        return jsonData

    def csvToJson(self, csvData = None, fieldnamesList = None):
        """Convert CSV to JSON as the service."""
        jsonData = ''
        if csvData:
            data = csv.DictReader( csvData, fieldnames = fieldnamesList)
            jsonData = json.dumps( [ row for row in data ] )
            return out

    def hello(self):
        """Retrieve a json response about the basic status of the server."""
        hello_application = 'api/hello.json'
        url_to_give = self.baseUrl+hello_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return json.dumps(return_to_user)

    def geocode(self, places=None):
        """Provide geocoding of place names to location coordinates.

        Args:
            places (list): A list of place names.

        Examples:
            >>> l.geocode(['Barcelona'])
            {u'locations': {u'Barcelona': {u'country': u'Spain',
                                           u'country_code': u'ES',
                                           u'location':[2.15898974899153,
                                                        41.38879005861875],
            ...

        Returns:
            json: The geocoding results based on the given place(s) name.

        """
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
        """Visualize map using Loklak service.

        Args:
            latitude (float):   Latitude value.
            longtitude (float): Longitude value.
            width (int):        Width (default=500).
            height (int):       Height (default=500).
            zoom (int):         Zoom value (default=8).
            text (str):         Value of text like Hello.

        Returns:
            bytes: An encoded map image.

        """
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
        """Provide an image with text on it.

        Args:
            text (str):     Text to be printed, markdown possible.
            color_text:     6-character hex code for the color.
            color_bg:       6-character hex code for the color.
            padding:        Space around text.
            uppercase:      <true|false> by default true. If true the text is printed UPPERCASE.

        Returns:
            bytes: An encoded image.

        """
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
        """Retrieve the peers of a user."""
        peers_application = 'api/peers.json'
        url_to_give = self.baseUrl+peers_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return json.dumps(return_to_user)

    def push(self, data=None):
        """Push servlet for twitter like messages.

        Note:
            The API of this function has a restrictions
            which only localhost clients are granted.

        Args:
            data: A search result object.

        Returns:
            json: Status about the message is pushed or not.

        """
        push_application = 'api/push.json'
        url_to_give = self.baseUrl + push_application
        headers = {
            'User-Agent': ('Mozilla/5.0 (Android 4.4; Mobile; rv:41.0)'
                           ' Gecko/41.0 Firefox/41.0'),
            'From': 'info@loklak.org'
        }
        if data:
            self.data = data
            params = {}
            params['data'] = json.dumps(self.data)
            return_to_user = requests.post(url_to_give, data=params)
            if return_to_user:
                return return_to_user.json()
            else:
                return_to_user = {}
                return_to_user['error'] = ('Something went wrong,'
                                           ' looks like the query is wrong.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('Something went wrong,'
                                       ' looks like the data is not correct.')
            return json.dumps(return_to_user)


    def user(self, name=None, followers=None, following=None):
        """Retrieve Twitter user information.

        Args:
            name (str):         Twitter screen name of the user.
            followers (int):    Followers of the user.
            following (int):    Accounts the user is following.

        Returns:
            json: User information, including who they are following, and who follows them.

        """
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
            return_to_user['error'] = ('No user name given to query. Please'
                                       ' check and try again')
            return json.dumps(return_to_user)

    def settings(self):
        """Retrieve the settings of the application.

        Note:
            The API of this function has a restrictions
            which only localhost clients are granted.

        Returns:
            json: The settings of the application.

        """
        settings_application = 'api/settings.json'
        url_to_give = self.baseUrl + settings_application
        return_to_user = requests.get(url_to_give)
        if return_to_user.status_code == 200:
            return return_to_user.json()
        else:
            return_to_user = {}
            return_to_user['error'] = ('This API has access restrictions:'
                                        ' only localhost clients are granted.')
            return json.dumps(return_to_user)

    def susi(self, query=None):
        """Retrieve Susi query response.

        Args:
            query (str): Query term.

        Returns:
            json: Susi response.

        """
        susi_application = 'api/susi.json'
        url_to_give = self.baseUrl + susi_application
        self.query = query
        if query:
            params = {}
            params['q'] = self.query
            return_to_user = requests.get(url_to_give, params=params)
            if return_to_user.status_code == 200:
                return return_to_user.json()
            else:
                return_to_user = {}
                return_to_user['error'] = ('Looks like there is a problem in susi replying.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('Please ask susi something.')
            return json.dumps(return_to_user)

    def search(self, query=None, since=None, until=None, from_user=None, count=None):
        """Handle the searching.

        Args:
            query (str):        Query term.
            since (str):        Only messages after the date (including the date), <date>=yyyy-MM-dd or yyyy-MM-dd_HH:mm.
            until (str):        Only messages before the date (excluding the date), <date>=yyyy-MM-dd or yyyy-MM-dd_HH:mm.
            from_user (str):    Only messages published by the user.
            count (int):        The wanted number of results.

        Returns:
            json: Search results from API.

        """
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
                return_to_user['error'] = ('Something went wrong, looks like'
                                           ' the server is down.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('No Query string has been'
                                       ' given to query for an account')
            return json.dumps(return_to_user)

    def suggest(self, query=None, count=None, order=None, orderby=None,since=None, until=None):
        """Retrieve a list of queries based on the given criteria.

        Args:
            query (str):     To get a list of queries which match; to get all latest: leave query empty.
            count (int):     Number of queries.
            order (str):     Possible values: desc, asc; default: desc.
            orderby (str):   A field name of the query index schema, i.e. retrieval_next or query_count.
            since (str):     Left bound for a query time.
            until (str):     Right bound for a query time.

        Returns:
            json: A list of queries in the given order.

        """
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
            return_to_user['error'] = ('Something went wrong,'
                                        ' looks like the server is down.')
            return json.dumps(return_to_user)

    def aggregations(self, query=None, since=None, until=None,
                     fields=None, limit=6, count=0):
        """Give the aggregations of the application.

        Args:
            query (str):    Query term.
            since (str):    Only messages after the date (including the date), <date>=yyyy-MM-dd or yyyy-MM-dd_HH:mm.
            until (str):    Only messages before the date (excluding the date), <date>=yyyy-MM-dd or yyyy-MM-dd_HH:mm.
            fields (str):   Aggregation fields for search facets, like "created_at,mentions".
            limit (int):    A limitation of number of facets for each aggregation.
            count (int):    The wanted number of results.

        Returns:
            json: Aggregations of the application.

        """
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
                return_to_user['error'] = ('Something went wrong,'
                                           ' looks like the server is down.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('No Query string has been given to run'
                                        'query for aggregations')
            return json.dumps(return_to_user)

    def account(self, name=None, action=None, data=None):
        """Provide the storage and retrieval of the user account data.

        Note:
            The API of this function has a restrictions which only localhost
            clients are granted. If you want to retrieve the user account
            information, just fill the 'name' argument, and do not fill any
            args.

            If you want to store one or more account objects, fill the
            'action' argument with "update" then submit that object
            (these objects) inside the 'data' argument.

            The data object must have this following form:
            {
              "screen_name"           : "test",        // primary key for the user
              "source_type"           : "TWITTER",     // the application which created the token, by default "TWITTER"
              "oauth_token"           : "abc",         // the oauth token
              "oauth_token_secret"    : "def",         // the oauth token_secret
              "authentication_first"  : "2015-06-07T09:39:22.341Z",        // optional
              "authentication_latest" : "2015-06-07T09:39:22.341Z",        // optional
              "apps"                  : {"wall" : {"type" : "horizontal"}} // any json
            }

        Args:
            name (str):     Twitter screen name of the user.
            action (str):   Proper values are either <empty> or 'update'.
            data (str):     An object to store (if you set action=update, you must submit this data object).

        Returns:
            json: Information about user's account if the 'action' argument is empty (retrieving).

        """
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
                return_to_user['error'] = ('Something went wrong,'
                                           ' looks like the query is wrong.')
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
                                           ' looks like the query is wrong.')
                return json.dumps(return_to_user)
        else:
            return_to_user = {}
            return_to_user['error'] = ('No Query string has been given'
                                       ' given to query for an account')
            return json.dumps(return_to_user)
