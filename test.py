import unittest
from loklak import Loklak
import os


class TestLoklak(unittest.TestCase):
    """"test class"""
    def setUp(self):
        """test proper setup"""
        self.loklak = Loklak()

    def test_hello(self):
        """test hello instance"""
        result = self.loklak.hello()
        self.assertEqual(result, {u'status': u'ok'})

    def test_geocode(self):
        """test geological features"""
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
            isinstance(result['locations']['Moscow']['place'], list)
        )

    def test_peers(self):
        """test finding peers"""
        result = self.loklak.peers()
        self.assertTrue('peers' in result)
        self.assertTrue(isinstance(result['peers'], list))
        self.assertTrue(len(result['peers']) >= 1)
        self.assertEqual(len(result['peers']), result['count'])

    def test_search(self):
        """test search result"""
        result = self.loklak.search('doctor who')
        self.assertTrue('error' in self.loklak.search())
        self.assertTrue('statuses' in result)
        self.assertTrue(isinstance(result['statuses'], list))
        self.assertTrue(len(result['statuses']) >= 1)
        self.assertEqual(len(result['statuses']), int(result['search_metadata']['count']))

    def test_status(self):
        """test status"""
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
        """test user"""
        result = self.loklak.user('dhruvRamani98')
        self.assertTrue('error' in self.loklak.user())
        self.assertTrue('user' in result)
        self.assertTrue('name' in result['user'])
        self.assertTrue('screen_name' in result['user'])

    def test_get_map(self):
        self.map_file = os.path.join(os.getcwd(), 'markdown.png')
        data = self.loklak.get_map(17.582729, 79.118320)
        self.assertTrue(data[:8] == '\211PNG\r\n\032\n'and (data[12:16] == 'IHDR'))
        with open(self.map_file, 'wb') as f:
            f.write(data)
        with open(self.map_file, 'rb') as f:
            file_contents = f.read()
        self.assertTrue(os.path.exists(self.map_file))
        self.assertEqual(data, file_contents)
        try:
            os.remove(self.map_file)
        except OSError as error:
            print(error)
    def test_aggregations(self):
        """test aggregations"""
        result = self.loklak.aggregations('sudheesh001','2015-01-10','2015-10-21',['mentions','hashtags'],10)
        data = result.json()
        self.assertEqual(result.status_code,200)
        self.assertTrue('aggregations' in data)
        self.assertTrue('hashtags' in data['aggregations'])
        self.assertTrue('mentions' in data['aggregations'])



if __name__ == '__main__':
    unittest.main()
