from question_model import Question
from data import question_data


question_bank = []

for q in question_data:
    question = q["text"]
    answer = q["answer"]
    new_question = Question(text=question, answer=answer)
    question_bank.append(new_question)

