# move fizzbuzz
import unittest

def fizzbuzz(number):

    return str(number)


class FizzBuzzTests(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual("1", fizzbuzz(1))