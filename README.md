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
(In Progress)