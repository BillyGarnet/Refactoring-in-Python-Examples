import unittest

from z_session_BowlingGame import BowlingGame


# http://www.bowlinggenius.com/
# to help check (test) your scores

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        global game
        game = BowlingGame()

    def throw_many(self, frame_qty, pins):
        for _ in range(frame_qty):
            game.hit(pins)
            game.hit(pins)

    def test_for_all_zeros(self):
        self.throw_many(10, 0)
        game.calculate_score()
        self.assertEqual(game.score, 0)

    def test_for_all_ones(self):
        self.throw_many(10, 1)
        game.calculate_score()
        self.assertEqual(game.score, 20)

    def test_for_spare_and_zeros(self):
        game.hit(6)
        game.hit(4)
        self.throw_many(9, 0)
        game.calculate_score()
        self.assertEqual(game.score, 10)

    def test_for_spare_and_one(self):
        game.hit(6)
        game.hit(4)
        game.hit(1)
        game.hit(0)
        self.throw_many(8, 0)
        game.calculate_score()
        self.assertEqual(game.score, 12)

    def test_for_strike_and_ones(self):
        game.hit(10)
        game.hit(1)
        game.hit(1)
        self.throw_many(8, 0)
        game.calculate_score()
        self.assertEqual(game.score, 14)

    def test_for_strike_and_spare(self):
        game.hit(10)
        game.hit(6)
        game.hit(4)
        self.throw_many(8, 0)
        game.calculate_score()
        self.assertEqual(game.score, 30)

    def test_for_strike_spare_and_ones(self):
        game.hit(10)
        game.hit(6)
        game.hit(4)
        self.throw_many(8, 1)
        game.calculate_score()
        self.assertEqual(game.score, 47)

    def test_for_two_strikes(self):
        game.hit(10)
        game.hit(10)
        self.throw_many(8, 0)
        game.calculate_score()
        self.assertEqual(game.score, 30)

    def test_for_two_strikes_and_ones(self):
        game.hit(10)
        game.hit(10)
        self.throw_many(8, 1)
        game.calculate_score()
        self.assertEqual(game.score, 49)

    def test_for_three_strikes(self):
        game.hit(10)
        game.hit(10)
        game.hit(10)
        self.throw_many(7, 0)
        game.calculate_score()
        self.assertEqual(game.score, 60)

    def test_for_perfect_game(self):
        for _ in range(12):
            game.hit(10)
        game.calculate_score()
        self.assertEqual(game.score, 300)
