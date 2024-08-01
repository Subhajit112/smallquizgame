

class QuizBrain:
    def __init__(self,q_list):
        self.score = 0
        self.questionbank = q_list
        self.question_number = 0
        self.current_question= None

    def still_has_questions_left(self):
        return self.question_number < len(self.questionbank)
        
    def next_question(self):
        self.current_question = self.questionbank[self.question_number]
        self.question_number += 1
        return self.current_question.question
        
    def check_answer(self, user_answer):
            if user_answer.lower() == self.current_question.answer.lower():
                self.score +=1
                return True
            else:
                return False   