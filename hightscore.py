# highscore.py
class HighScore:
    def __init__(self):
        self.high_score = float('inf')

    def update(self, score):
        if score < self.high_score:
            self.high_score = score

    def get_high_score(self):
        return self.high_score
