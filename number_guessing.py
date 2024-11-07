# import random

# def number_guessing_game():
#     target_number = random.randint(1,100)
#     max_attempts = 10
#     attempts = 0

#     print("Welcome to the Number Guessing Game!")
#     print(f"I have chosen a number between 1 and 100 you have {max_attempts} attempts to guess it")

#     while attempts < max_attempts:
#         try:
#             guess = int(input("enter your guess: "))
#             attempts += 1

#             if guess < target_number:
#                 print("too low Try again")
#             elif guess > target_number:
#                 print("too high try again")
#             else:
#                 print(f"congratulations you guessed the number {target_number} correctly in {attempts} attempts")
#                 break

#         except ValueError:
#             print("please enter a vlid integer.")
#         if attempts == max_attempts:
#             print(f"sorry you've used all (max_attempts) attempts. the number was {target_number}.")
# number_guessing_game()





# number guessing game difficulty level
import random


class NumberGuessingGame:
    def __init__(self):
        self.target_number = 0
        self.max_attempts = 0
        self.attempts = 0
        self.score = 100
        self.guesses = [] # list of guesses
    
    def set_difficulty(self):
        print("\nchoose difficulty level:")
        print("1. easy (1 - 50 , 15 attempts)")
        print("2. medium (1-100, 10 attempts)")
        print("3. hard (1-200, 5 attempts)")
        choice = input("enter choice(1-3): ")

        if choice == '1':
            self.target_number = random.randint(1,50)
            self.max_attempts = 15
        elif choice == '2':
            self.target_number = random.randint(1,100)
            self.max_attempts = 10
        elif choice == '3':
            self.target_number = random.randint(1,200)
            self.max_attempts = 5
        else:
            print("Invalid choice. Defaulting to Medium")
            self.target_number = random.randint(1,100)
            self.max_attempts = 10
        print(f"\nA number of has been choosen. you have {self.max_attempts} attempts to guess it!")
    
    def give_hint(self,guess):
        if abs(self.target_number - guess) <=5:
            print("you're very close!")
        elif abs(self.target_number -guess) <= 10:
            print("you're getting warm")
    def play_game(self):
        self.set_difficulty()
        while self.attempts < self.max_attempts:
            try:
                guess = int(input("\n Enter your guess: "))
                if guess in self.guesses:
                    print("you've already guessed that number!")
                    continue
                
                self.attempts += 1
                self.guesses.append(guess)

                if guess < self.target_number:
                    print("too low")
                    self.give_hint(guess)
                    self.score -= 10
                elif guess > self.target_number:
                    print("too high!")
                    self.give_hint(guess)
                    self.score -=10
                else:
                    print(f"congratulations you've guessed it in {self.attempts} attempts.")
                    print(f"your final sc ore is {self.score} points")
                    break
            except ValueError:
                print("please enter a valid integer")
            
            if self.attempts == self.max_attempts:
                print(f"\n you've run out of attempts! the number was{self.target_number}.")
                print(f"your final score is {self.score} points.")
        self.play_again()
    def play_again(self):
        choice = input("\ndo yo want to play again (y/n):").lower()
        if choice == 'y':
            self.reset_game()
            self.play_game()
        else:
            print("thanks for playing")
    def reset_game(self):
        self.target_number = 0
        self.max_attempts = 0
        self.attempts = 0
        self.guesses = []
game = NumberGuessingGame()
game.play_game()


