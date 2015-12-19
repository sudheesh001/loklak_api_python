## Python Loklak API
[![PyPI version](https://badge.fury.io/py/python-loklak-api.svg)](https://badge.fury.io/py/python-loklak-api) 
[![Build Status](https://travis-ci.org/loklak/python-loklak-api.svg?branch=master)](https://travis-ci.org/loklak/python-loklak-api)
--------------------------------------------

If you want to create an alternative twitter search portal, the only way would be to use the official twitter API to retrieve Tweets. But that interface needs an OAuth account and it makes your search portal completely dependent on Twitters goodwill. The alternative is, to scrape the tweets from the twitter html search result pages, but Twitter may still lock you out on your IP address. To circumvent this, you need many clients accessing twitter to scrape search results. This makes it neccessary to create a distributed peer-to-peer network of twitter scrapers which can all organize, store and index tweets. This solution was created with loklak.

#### What is Loklak ?
It is a server application which is able to collect messages from various sources, including twitter. The server contains a search index and a peer-to-peer index sharing interface.

--------------------------------------------

#### Why should I use this ?
If you like to be anonymous when searching things, want to archive tweets or messages about specific topics and if you are looking for a tool to create statistics about tweet topics, then you may consider loklak. With loklak you can do:
- collect and store a very, very large amount of tweets and similar messages
- create your own search engine for tweets
- omit authentication enforcment for API requests on the twitter plattform
- share tweets and tweet archives with other loklak users
- search anonymously on your own search portal
- create your own tweet search portal or statistical evaluations, i.e.:..
- use Kibana to analyze large amounts of tweets as source for statistical data.

--------------------------------------------

# Documentation of the API and Usage Examples

To use the loklak app, first an object of the loklak type needs to be created. Do the following to install the `pip` module and add it to your `requirements` for the application.

`pip install python-loklak-api`

Loklak once installed, can be used in the application as

`from loklak import Loklak`

To create a loklak object you can assign the `Loklak()` object to a variable.
`variable = Loklak()`

eg. `l = Loklak()`

### API Documentation

##### Status of the Loklak server
Using the object created above, `l.status()` returns a json of the status as follows

```json
{
  "index_sizes" : {
    "messages" : 48683271,
    "users" : 14948939,
    "queries" : 726,
    "accounts" : 53,
    "user" : 5072266,
    "followers" : 90,
    "following" : 72
  },
  "client_info" : {
    "RemoteHost" : "",
    "IsLocalhost" : "false",
    "Accept-Language" : "en-US,en;q=0.5",
    "Host" : "loklak.org",
    "Accept-Encoding" : "gzip, deflate",
    "X-Forwarded-For" : "",
    "X-Real-IP" : "",
    "Via" : "1.1 proxy14.nitw (squid/3.1.8)",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection" : "close",
    "Cache-Control" : "max-age=259200"
  }
}
```

##### Settings of the loklak server (strictly only for localhost clients)

Using the object created above `l.settings()` returns a json of the settings being used by the loklak server

##### Hello test - Check if the server is responding properly and is online

Using the object created above `l.hello()` returns a json response of the status of the server

When the server is online, the json should read
```json
{'status': 'ok'}
```

##### Peers - API To find out the loklak peers

Finding the list of loklak peers, use the object created above `l.peers()` which returns a json response containing all the peers connected to `loklak.org`

##### Users API

What this can do ?

- Fetch the details of one user
- Fetch the details of the user along with number of their followes and following
- Fetch only the followers / following of a particular user

Query Structure: `l.user(<username>,<followers count>,<following count>)`

`<username>` is a string, eg. `'loklak_app'`
`<followers count>` and `<following count>` is a numeric or a string or `None`

eg. `l.user('loklak_app')`
eg. `l.user('loklak_app',1000)` - 1000 followers of `loklak_app`
eg. `l.user('loklak_app',1000,1000)` - 1000 followers and following of `loklak_app`
eg. `l.user('loklak_app',None,1000)` - 1000 following of `loklak_app`

##### Accounts API
LOCALHOST ONLY, Loklak server running on port `localhost:9000`

To query the user account details of the data within the loklak server, use
`l.account('name')` where `'name'` is the screen_name of the user whose information is required.

To update the user details within the server, package a `json` object with the following parameters and other parameters which needs to be pushed to the server and use the `action=update` where `action` is the 2nd parameter of the `account()` api

`l.account('name','update','{ json object }')`

##### Search API

Public search API for the scraped tweets from Twitter.

Query structure: `search('querycontent','since date','until date', 'from a specific user')`

eg. l.search('doctor who')

A search result in json looks as follows.
```json
{
  "search_metadata" : {
    "startIndex" : "0",
    "itemsPerPage" : "100",
    "count" : "120",
    "query" : "doctor who"
  },
  "statuses" : [ {
    "created_at" : "2015-03-03T19:30:43.000Z",
    "screen_name" : "exanonym77s",
    "text" : "check #DoctorWho forums #TheDayOfTheDoctor #TheMaster @0rb1t3r http://www.thedoctorwhoforum.com/ https://pic.twitter.com/FvW6J9WMCw",
    "link" : "https://twitter.com/ronakpw/status/572841550834737152",
    "id_str" : "572841550834737152",
    "source_type" : "TWITTER",
    "provider_type" : "SCRAPED",
    "retweet_count" : 0,
    "favourites_count" : 0,
    "hosts" : [ "www.thedoctorwhoforum.com", "pic.twitter.com" ],
    "hosts_count" : 2,
    "links" : [ "http://www.thedoctorwhoforum.com/", "https://pic.twitter.com/FvW6J9WMCw" ],
    "links_count" : 2,
    "mentions" : [ "@0rb1t3r" ],
    "mentions_count" : 1,
    "hashtags" : [ "DoctorWho", "TheDayOfTheDoctor", "TheMaster" ],
    "hashtags_count" : 3,
    "without_l_len" : 62,
    "without_lu_len" : 62,
    "without_luh_len" : 21,
    "user" : {
      "name" : "Example User Anyone",
      "screen_name" : "exanonym77s",
      "profile_image_url_https" : "https://pbs.twimg.com/profile_images/567071565473267713/4hiyjKkF_bigger.jpeg",
      "appearance_first" : "2015-03-03T19:31:30.269Z",
      "appearance_latest" : "2015-03-03T19:31:30.269Z"
    }
  }, ...
  ]
}
```

Mentioning the Since and Until dates

eg. `l.search('sudheesh001', '2015-01-10', '2015-01-21')`

Which results in a json as follows
```json
{'search_metadata': {'client': '14.139.85.200',
                      'count': '3',
                      'count_backend': 0,
                      'count_cache': 3,
                      'count_twitter_all': 0,
                      'count_twitter_new': 0,
                      'hits': 3,
                      'itemsPerPage': '100',
                      'period': 103487501,
                      'query': 'sudheesh001 since:2015-01-10 until:2015-01-21',
                      'servicereduction': 'false',
                      'time': 2001},
 'statuses': [{'audio': [],
                'audio_count': 0,
                'classifier_language': 'english',
                'classifier_language_probability': 0.00043833465,
                'created_at': '2015-01-19T04:25:38.000Z',
                'favourites_count': 0,
                'hashtags': [],
                'hashtags_count': 0,
                'hosts': [],
                'hosts_count': 0,
                'id_str': '557031100065648640',
                'images': [],
                'images_count': 0,
                'link': 'https://twitter.com/sudheesh001/status/557031100065648640',
                'links': [],
                'links_count': 0,
                'mentions': ['imasaikiran', 'sudheesh001'],
                'mentions_count': 2,
                'place_context': 'ABOUT',
                'place_id': '',
                'place_name': '',
                'provider_hash': '1cadbfd3',
                'provider_type': 'REMOTE',
                'retweet_count': 0,
                'screen_name': 'sudheesh001',
                'source_type': 'TWITTER',
                'text': '@imasaikiran @sudheesh001 done !! \U0001f60a',
                'user': {'appearance_first': '2015-11-13T02:05:19.861Z',
                          'appearance_latest': '2015-11-13T02:05:19.861Z',
                          'name': 'SudheeshSinganamalla',
                          'profile_image_url_https': 'https://pbs.twimg.com/profile_images/500559201542762498/IvDEqWy1_bigger.jpeg',
                          'screen_name': 'sudheesh001',
                          'user_id': '390171807'},
                'videos': [],
                'videos_count': 0,
                'without_l_len': 36,
                'without_lu_len': 10,
                'without_luh_len': 10}
            ]}
```

Valid parameters for `since` and `until` can also be `None` or any `YMD` date format. Looking towards the future releases to resolve this to any date format.

The `from a specific user` parameter makes sure that the results obtained for the given query are only from a specific user.

`l.search('doctor who', '2015-01-10', '2015-01-21','0rb1t3r')`

##### Aggregations API

##### GeoLocation API

Loklak allows you to fetch required information about a country or city.

eg. `l.geocode(['Barcelona'])`
eg. `l.geocode(['place1','place2'])`
