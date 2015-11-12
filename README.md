## Python Loklak API
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


##### Aggregations API