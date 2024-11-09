quiz = {
    "what is the capital of france?":{
        "options":["A) Paris","B) Berlin","C) Madrid","D) Rome"],
        "answer":"A"
    },
    "What is 5 + 7 ?":{
        "options": ["A) 10", "B) 12", "C) 14", "D) 15"],
        "answer":"B"
    },
    "which planet is know a mokingbird?":{
        "options":["A) harper lee", "B) mark twin", "C) j.k. rowling", "D) ernest hemingwary"],
        "answer":"D"
    },
    "what is the larges ocean on earth?":{
        "options":["A) atalantic ocean","B) indian Ocean","C) arctic Ocean", "D) pecific Ocean"],
        "answer":"D"
    }
    
}
def conduct_quiz(quiz):
    score = 0
    total_questions = len(quiz)
    print("welcome to the quiz")
    print("please answer each questio by typing a, b, c, or d.")
    print()

    for question,data in quiz.items():
        print(question)
        for option in data["options"]:
            print(option)
        
        user_answer = input("your answer").upper()

        if user_answer == data["answer"]:
            print("correct!\n")
            score += 1
        else:
            print(f"incorrect. the correct answer was {data['answer']}.\n")

    print("Quiz Completed!")
    print(f"Your final score is: {score} out of {total_questions}")

conduct_quiz(quiz)
