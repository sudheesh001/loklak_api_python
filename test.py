import unittest
from loklak import Loklak


class TestLoklak(unittest.TestCase):
    def setUp(self):
        self.loklak = Loklak()

    def test_hello(self):
        result = self.loklak.hello()
        self.assertEqual(result, {u'status': u'ok'})

    def test_geocode(self):
        result = self.loklak.geocode()
        self.assertEqual(result, '{}')

        result = self.loklak.geocode(places=['Moscow'])
        self.assertTrue('locations' in result)
        self.assertTrue('Moscow' in result['locations'])
        self.assertEqual(
            'Russian Federation',
            result['locations']['Moscow']['country']
        )
        self.assertEqual(
            'Russian Federation',
            result['locations']['Moscow']['country']
        )
        self.assertTrue(
            type(result['locations']['Moscow']['place']) == list
        )

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
        result_properties = [
            'messages', 'mps', 'users', 'queries',
            'accounts', 'user', 'followers', 'following'
        ]
        for prop in result_properties:
            self.assertTrue(
                prop in result['index_sizes'],
                msg='{} not found in index_sizes'.format(prop)
            )

        self.assertTrue('client_info' in result)
        client_properties = [
            'RemoteHost', 'IsLocalhost', 'Host',
            'Accept-Encoding', 'X-Forwarded-For', 'X-Real-IP',
            'User-Agent', 'Accept', 'Connection',
        ]
        for prop in client_properties:
            self.assertTrue(
                prop in result['client_info'],
                msg='{} not found in client info'.format(prop)
            )

    def test_user(self):
        result = self.loklak.user('dhruvRamani98')
        self.assertTrue('error' in self.loklak.user())
        self.assertTrue('user' in result)
        self.assertTrue('name' in result['user'])
        self.assertTrue('screen_name' in result['user'])


if __name__ == '__main__':
    unittest.main()
