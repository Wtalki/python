import csv

# Function to load flashcards from CSV file
def load_flashcards(filename):
    flashcards = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                flashcards[row['question']] = row['answer']
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return flashcards

# Function to run the flashcard quiz
def run_quiz(flashcards):
    score = 0
    total_questions = len(flashcards)

    print("\nWelcome to the Flashcard Quiz!")
    print("Answer the following questions:\n")

    for question, correct_answer in flashcards.items():
        user_answer = input(f"{question}\nYour answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}\n")

    # Display final score
    print(f"Quiz completed! Your score: {score}/{total_questions}")

# Main function to run the app
def main():
    filename = 'flashcards.csv'
    flashcards = load_flashcards(filename)

    if flashcards:
        run_quiz(flashcards)
    else:
        print("No flashcards available to quiz.")

# Run the app
main()
