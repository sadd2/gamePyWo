

import random
from player import Player
from number import Number
from feedback import Feedback
from config import LOWER_BOUND, UPPER_BOUND

class Game:
    def __init__(self):
        self.player = Player()
        self.number = Number()
        self.feedback = Feedback()

    def start(self):
        print(f"I'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}.")
        while True:
            guess = self.player.make_guess()
            if self.number.check_guess(guess):
                print(self.feedback.congratulations())
                break
            else:
                print(self.feedback.hint(guess, self.number.secret_number))
