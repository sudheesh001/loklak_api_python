import unittest
from loklak import Loklak


class TestLoklak(unittest.TestCase):
    def setUp(self):
        self.loklak = Loklak()
    
    def test_hello(self):
        result = self.loklak.hello()
        self.assertEqual(result, {u'status': u'ok'})
    
    def test_peers(self):
        result = self.loklak.peers()
        self.assertTrue('peers' in result)
        self.assertTrue(type(result['peers']) == list)
        self.assertTrue(len(result['peers']) >= 1)
        self.assertEqual(len(result['peers']), result['count'])
        
     def test_search(self):
        result = self.loklak.search('doctor who')
        self.assertTrue('error' in self.loklak.search())
        self.assertTrue('statuses' in result)
        self.assertTrue(type(result['statuses']) == list)
        self.assertTrue(len(result['statuses']) >= 1)
        self.assertEqual(len(result['statuses']), int(result['search_metadata']['count']))

    def test_status(self):
        result = self.loklak.status()
        self.assertTrue('index_sizes' in result)
        self.assertTrue('messages' in result['index_sizes'])
        self.assertTrue('mps' in result['index_sizes'])
        self.assertTrue('users' in result['index_sizes'])
        self.assertTrue('queries' in result['index_sizes'])
        self.assertTrue('accounts' in result['index_sizes'])
        self.assertTrue('user' in result['index_sizes'])
        self.assertTrue('followers' in result['index_sizes'])
        self.assertTrue('following' in result['index_sizes'])
        
        self.assertTrue('client_info' in result)
        self.assertTrue('RemoteHost' in result['client_info'])
        self.assertTrue('IsLocalhost' in result['client_info'])
        self.assertTrue('Accept-Language' in result['client_info'])
        self.assertTrue('If-Modified-Since' in result['client_info'])
        self.assertTrue('Host' in result['client_info'])
        self.assertTrue('Accept-Encoding' in result['client_info'])
        self.assertTrue('X-Forwarded-For' in result['client_info'])
        self.assertTrue('X-Real-IP' in result['client_info'])
        self.assertTrue('Via' in result['client_info'])
        self.assertTrue('User-Agent' in result['client_info'])
        self.assertTrue('Accept' in result['client_info'])
        self.assertTrue('Connection' in result['client_info'])
        self.assertTrue('Cache-Control' in result['client_info'])


    def test_user(self):
        result = self.loklak.user('dhruvRamani98')
        self.assertTrue('error' in self.loklak.user())
        self.assertTrue('user' in result)
        self.assertTrue('name' in result['user'])
        self.assertTrue('screen_name' in result['user'])


if __name__ == '__main__':
    unittest.main()
