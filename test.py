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