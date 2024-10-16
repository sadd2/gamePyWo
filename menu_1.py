from game import Game
from rules import Rules

class Menu:
    def show(self):
        print("Welcome to the Number Guessing Game!")
        while True:
            print("\n1. Start Game")
            print("2. View Rules")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                game = Game()
                game.start()
            elif choice == '2':
                Rules.show_rules()
            elif choice == '3':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")
