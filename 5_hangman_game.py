import random

# List of possible words
word_list = ["python", "hangman", "programming", "development", "computer"]

# Function to display the current state of the hangman
def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           -
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           -
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           -
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           -
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           -
        """
    ]
    return stages[tries]

# Function to run the game
def play_hangman():
    # Select a random word from the list
    word = random.choice(word_list)
    word_completion = ["_"] * len(word)  # List to track the word progress
    guessed = False
    guessed_letters = []  # Track letters guessed by the player
    guessed_words = []    # Track full words guessed by the player
    tries = 6  # Number of allowed incorrect guesses

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("Word: " + " ".join(word_completion))
    print("\n")

    # Main game loop
    while not guessed and tries > 0:
        guess = input("Guess a letter or the full word: ").lower()

        # Handle guessing a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter:", guess)
            elif guess not in word:
                print("Incorrect guess:", guess)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good guess:", guess)
                guessed_letters.append(guess)
                for i in range(len(word)):
                    if word[i] == guess:
                        word_completion[i] = guess
                if "_" not in word_completion:
                    guessed = True

        # Handle guessing the full word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word:", guess)
            elif guess != word:
                print("Incorrect guess:", guess)
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = list(word)

        # Handle invalid input
        else:
            print("Invalid input. Please enter a single letter or the full word.")

        # Display current state
        print(display_hangman(tries))
        print("Word: " + " ".join(word_completion))
        print("Incorrect guesses left:", tries)
        print("Guessed letters:", ", ".join(guessed_letters))
        print("\n")

    # End game message
    if guessed:
        print("Congratulations! You've guessed the word:", word)
    else:
        print("Game Over! The word was:", word)

# Run the game
play_hangman()
