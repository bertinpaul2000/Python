from question_model import Question
from data import question_data, new_data
from quiz_brain import QuizBrain


question_bank = []
# for q_text in question_data:
#     question_text = q_text["text"]
#     question_answer = q_text["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

for q_text in new_data:
    question_text = q_text["question"]
    question_answer = q_text["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number}")