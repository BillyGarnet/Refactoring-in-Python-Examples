import unittest

from session_FizzBuzz import fizzbuzz


class FizzBuzzTests(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_for_2(self):
        self.assertEqual(fizzbuzz(2), "2")

    def test_for_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_for_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_for_6(self):
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_for_10(self):
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_for_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
