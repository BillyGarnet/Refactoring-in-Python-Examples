import unittest


def hello():
    return "Hello, World!"


class HelloWorldTests(unittest.TestCase):
    def test_response(self):
        self.assertEqual('Hello, World!', hello())