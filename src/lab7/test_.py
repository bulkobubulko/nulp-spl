import unittest
from spotify_api import get_token, get_auth_token  

class TestLab7(unittest.TestCase):
    def test_get_token(self):
        token = get_token()
        self.assertIsNotNone(token)
        self.assertIsInstance(token, str)
        self.assertGreater(len(token), 0)
        
    def test_get_auth_token(self):
        token = get_token()
        headers = get_auth_token(token)
        self.assertIsNotNone(headers)
        self.assertIsInstance(headers, dict)
        self.assertIn('Authorization', headers)
        self.assertIn('Bearer', headers['Authorization'])
        self.assertIn(token, headers['Authorization'])
        
if __name__ == '__main__':
    unittest.main()