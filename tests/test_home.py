import unittest

from app import app


class HomeTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_home(self):
        response = self.client().get('/home')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
