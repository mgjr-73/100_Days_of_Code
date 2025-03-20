class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.list_length = (len(self.question_list))

    def still_has_questions(self):
        if self.list_length > 0:
            return True
        return False

        # instructor solution:
        # return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        self.list_length -= 1
        input(f"Q{self.question_number}: {question.text} True or False? ")





