import unittest
import sys

sys.path.append("../")
from app import app

class HomeTests(unittest.TestCase):
    def setup(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status, 200)


if __name__ == '__main__':
    unittest.main()
