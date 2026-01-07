import unittest
import os


HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '5000'))
DEBUG = bool(os.getenv('DEBUG', True))

from app import app

class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_home_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_about_page_status_code(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_page_404_content(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Sorry the page is a lie.', response.data)

if __name__ == '__main__':
    unittest.main()