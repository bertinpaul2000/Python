class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_question(self):
        return self.question_number < 10

    def next_question(self):
        # ask the next question
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (true/false): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.user_score += 1
            print("You Got it Right")
        else:
            print("That's Wrong")
        print(f"The correct answer is \"{correct_answer}\".")
        print(f"Your current score is: {self.user_score}/{self.question_number}\n")


