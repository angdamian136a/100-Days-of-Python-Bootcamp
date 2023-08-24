class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.questions_list = q_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question_ta = self.questions_list[self.question_number]
        self.question_number += 1
        user_response = input("Q.{}: {} (True/False)?: ".format(self.question_number, question_ta.text))
        self.check_answer(user_response, question_ta.answer)

    def check_answer(self, u_response, q_answer):
        if u_response.lower() == q_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, you got it wrong.")
        print("The correct answer was: {}".format(q_answer))
        print("Your current score is: {}/{}.".format(self.score, self.question_number))
        print("\n")



