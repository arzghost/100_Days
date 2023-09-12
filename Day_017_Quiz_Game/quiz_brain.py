class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.question} (True/False): '.replace('&quot;', '"').replace("&#039;", "'"))
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.capitalize() == correct_answer.capitalize() or user_answer[0].lower() == correct_answer.lower()[0]:
            print('You got it right!')
            self.score += 1
        else:
            print('That is wrong.')
        print(f'Your current score: {self.score}/{self.question_number}\n')
