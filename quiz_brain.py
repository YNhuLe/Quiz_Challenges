class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_have_question(self):
        return self.question_number < len(self.question_list)

    correct_format = True

    def check_input(self, cu_question):
        while True:
            user_answer = input(f"Q.{self.question_number}: {cu_question.text} (True/False): ")

            if user_answer.lower() in ["false", "true"]:
                return user_answer
            else:
                print("Please give the correct answer either 'true' or 'false'")

    def next_question(self):
        if self.still_have_question():
            current_question = self.question_list[self.question_number]
            user_answer = self.check_input(current_question)
            self.check_answer(user_answer, current_question.answer)
            self.question_number += 1
        else:
            print("No more question. Quiz completed.")

    # def next_question(self):
    #     current_question = self.question_list[self.question_number]
    #     self.question_number += 1
    #     self.check_input(self.question_number, current_question)
    #     user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    #
    #     self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are right!")

        else:
            print("You are wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
