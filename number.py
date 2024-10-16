

import random
from config import LOWER_BOUND, UPPER_BOUND

class Number:
    def __init__(self):
        self.secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)

    def check_guess(self, guess):
        return guess == self.secret_number
