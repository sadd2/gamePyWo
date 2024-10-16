# score.py
class Score:
    def __init__(self):
        self.attempts = 0

    def increment(self):
        self.attempts += 1

    def get_attempts(self):
        return self.attempts
