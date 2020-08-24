def pythonic_examples(game=None):

    # instead of
    for x in range(0, 3):
        print(x)

    # do this
    for x in range(3):
        print(x)

    for i in range(10):
        game.hit(25)
        game.hit(10)
    self.assertEqual(game.calculate_score, 350)

    # use _ instead of i since it isn't used in loop
    for _ in range(10):
        game.hit(25)
        game.hit(10)
    self.assertEqual(game.calculate_score, 350)