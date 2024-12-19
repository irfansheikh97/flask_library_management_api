import unittest
from app import app
from auth import SECRET_TOKEN

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_success(self):
        credentials = {"username": "admin", "password": "password"}
        response = self.app.post('/auth/login', json=credentials)
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json)

    def test_login_failure(self):
        credentials = {"username": "admin", "password": "wrongpassword"}
        response = self.app.post('/auth/login', json=credentials)
        self.assertEqual(response.status_code, 401)

    def test_protected_route_with_token(self):
        headers = {"Authorization": f"Bearer {SECRET_TOKEN}"}
        response = self.app.get('/secure-data', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_protected_route_without_token(self):
        response = self.app.get('/secure-data')
        self.assertEqual(response.status_code, 403)
