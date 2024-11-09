import random 
choices = ["rock","paper","scissors"]

def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "it's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "you win!"
    else:
        return "computer wins!"

def play_game():
    print("welcome to rock, paper, scissors!")

    while True:
        user_choice = input("enter rock, paper, scissors or 'quit to stop playint: ").lower()

        if user_choice == "quit":
            print("thanks for playing")
            break

        if user_choice not in choices:
            print("invalid choice. please try again")
            continue

        computer_choice = random.choice(choices)
        print(f"compute chose: {computer_choice}")

        result = determine_winner(user_choice,computer_choice)
        print(result + "\n")
play_game()

