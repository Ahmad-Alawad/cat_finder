import unittest
import server

class IntegrationTest(unittest.TestCase):
    '''Testing our flask routes'''

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_home(self):
        result = self.client.get('/')
        self.assertIn("", result.data)



if __name__ == '__main__':
    unittest.main()
