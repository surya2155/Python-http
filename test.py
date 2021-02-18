import unittest
from hello import app
class BasicTestCase(unittest.TestCase):
def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')
