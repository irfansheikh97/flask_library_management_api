import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_root_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)  # No root route defined
