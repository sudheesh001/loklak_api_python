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

if __name__ == '__main__':
    unittest.main()
