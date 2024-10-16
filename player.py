class Player:
    def make_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Please enter a valid number.")
