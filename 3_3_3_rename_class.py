# Everytime we read this we have to figure out what it means
class ProcessResult(object):
    def __init__(self):
        self.first_ball = 0
        self.second_ball = 0

    def comment_code(self, first_ball, second_ball):

        first_ball += 3
        return self.calculate_total(first_ball, second_ball)

    def calculate_total(self, first_ball, second_ball):
        return first_ball + second_ball
