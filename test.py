from loklak import Loklak
from pprint import pprint

# Create a loklak object
l = Loklak()

### API Usage
#######################################
#		   Usage and Testings         #
#######################################

# Loklak Status API

status = l.status()
pprint(status)

# Loklak Hello API

hello = l.hello()
pprint(hello)

# Loklak Peers API

peers = l.peers()
pprint(peers)

# Users API

user = l.user('sudheesh001')
pprint(user)

user = l.user('')
pprint(user)