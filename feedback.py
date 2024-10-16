


class Feedback:
    def congratulations(self):
        return "Congratulations! You've guessed the number!"

    def hint(self, guess, secret_number):
        if guess < secret_number:
            return "Too low! Try again."
        else:
            return "Too high! Try again."
