# 1000,   M
# 500,    D
# 100,    C
# 50,     L
# 10,     X
# 5,      V
# 1,      I
import unittest


def convert(number):
    roman = ""

    conversion = [(10, "X"), (5, "V"), (1, "I")]
    for arabic_numeral, roman_numeral in conversion:
        while number >= arabic_numeral:
            roman += roman_numeral
            number -= arabic_numeral

    return roman


class RomanNumeralsTest(unittest.TestCase):
    def test_for_1(self):
        self.assertEqual(convert(1), "I")

    def test_for_2(self):
        self.assertEqual(convert(2), "II")

    def test_for_3(self):
        self.assertEqual(convert(3), "III")

    def test_for_5(self):
        self.assertEqual(convert(5), "V")

    def test_for_10(self):
        self.assertEqual(convert(10), "X")

    def test_for_20(self):
        self.assertEqual(convert(20), "XX")

    def test_for_30(self):
        self.assertEqual(convert(30), "XXX")