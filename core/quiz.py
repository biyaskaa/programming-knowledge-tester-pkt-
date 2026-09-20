class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_index = 0
        self.correct_count = 0

    def current_question(self):
        try:
            return self.questions[self.current_index]
        except:
            return None


    def submit_answer(self, answer_index):
        if answer_index == self.questions[self.current_index]['answer']: self.correct_count += 1
        self.current_index += 1

    def is_finished(self):
        return self.current_index == len(self.questions)

    def score(self):
        return self.correct_count, len(self.questions)