class Quiz:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": "a",
            "What is 2 + 2?": "b",
            "What color is the sky?": "c"
        }
        self.options = {
            "What is the capital of France?": ["a) London", "b) Paris", "c) Berlin"],
            "What is 2 + 2?": ["a) 3", "b) 4", "c) 5"],
            "What color is the sky?": ["a) Green", "b) Yellow", "c) Blue"]
        }
        self.score = 0

    def take_quiz(self):
        for question in self.questions:
            print(question)
            for option in self.options[question]:
                print(option)
            answer = input("Your answer (a, b, or c): ")
            if answer.lower() == self.questions[question]:
                self.score += 1
                print("Correct!")
            else:
                print("Incorrect.")
        print(f"Your score: {self.score}/{len(self.questions)}")

def main():
    quiz = Quiz()
    quiz.take_quiz()

if __name__ == "__main__":
    main()
