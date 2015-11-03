from loklak import Loklak
from pprint import pprint

# Create a loklak object
l = Loklak()

### API Usage

#######################################
#		   Usage and Testings         #
#######################################
# Loklak settings API
settings = l.settings()
pprint(settings)

# Loklak Status API

status = l.status()
pprint(status)

# Loklak Hello API

hello = l.hello()
pprint(hello)

# Loklak Peers API

peers = l.peers()
pprint(peers)

#######################################
# Users API

# User Query
user = l.user('sudheesh001')
pprint(user)
# User Query with followers and following list
user = l.user('sudheesh001', '1000', '1000')
pprint(user)
# User Query with followers only
user = l.user('sudheesh001', '1000')
pprint(user)
# User Query with following only
user = l.user('sudheesh001', None, '1000')
pprint(user)

user = l.user('')
pprint(user)

#######################################

# Search API Usage

### Aggregations

searchAggregation1 = l.aggregations('sudheesh001',None,None,['mentions','hashtags'],10)
pprint(searchAggregation1)

searchAggregation2 = l.aggregations('sudheesh001','2015-01-10','2015-10-21',['mentions','hashtags'],10)
pprint(searchAggregation2)

searchAggregation3 = l.aggregations('sudheesh001',None,'2015-10-21',['mentions','hashtags'],10)
pprint(searchAggregation3)

searchAggregation4 = l.aggregations('sudheesh001','2015-10-21',None,['mentions','hashtags'],10)
pprint(searchAggregation4)

searchAggregation5 = l.aggregations('sudheesh001',None,None,['mentions','hashtags'])
pprint(searchAggregation5)

### Search

search1 = l.search('sudheesh001')
pprint(search1)

search2 = l.search('sudheesh001','2015-01-10')
pprint(search2)

search3 = l.search('sudheesh001', None, '2015-01-10')
pprint(search3)

search4 = l.search('sudheesh001', '2015-01-10', None)
pprint(search4)

search5 = l.search('sudheesh001', '2015-01-10', '2015-01-21')
pprint(search5)

search6 = l.search('sudheesh001', '2015-01-10', '2015-01-21','sudheesh001')
pprint(search6)

###  account
account1 = l.account('name')
pprint(account1)

account2 = l.account('update','name','token','token_secret')
pprint(account2)

account3 = l.account('update','name','type')
pprint(account3)
