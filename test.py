import unittest
from hello import app
from flask import Flask
from flask_testing import LiveServerTestCase

class BasicTestCase(unittest.TestCase):
def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/hello', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')
       
class TestViews(TestCase):
    def test_some_json(self):
        response = self.client.get("/hello")
        self.assertEquals(response.json, dict(success=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')
