from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
is_continue = True
while is_continue:
    print("\n")
    keep_going = input("Good try!!! Do you want to try the game one more time!!")
    if keep_going.lower() == "yes":
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)

        quiz = QuizBrain(question_bank)
        while quiz.still_have_question():
            quiz.next_question()

        print("You've completed the quiz")
        print(f"Your final score is: {quiz.score}/{quiz.question_number}")

    else:
        is_continue = False
