from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    question = q["text"]
    answer = q["answer"]
    new_question = Question(text=question, answer=answer)
    question_bank.append(new_question)


q = QuizBrain(question_bank)

while q.still_has_questions():
    q.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {q.score}/{q.question_number}")


# instructor code
# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
#
# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
#
# quiz = QuizBrain(question_bank)
#
# while quiz.still_has_questions():
#     quiz.next_question()
#
# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")