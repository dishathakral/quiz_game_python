class QuizBrain:
    def __init__(self,qlist,question_number=0,score=0):
        self.question_number=question_number
        self.question_list=qlist
        self.score=score
    # function next question
    def next_question(self,qlist):#it get next question along with it check answer and give score
        for question in qlist:
            self.question_number+=1
            print(f'Q{self.question_number} {question.question}')
            solution = input("your answer:").lower()
            if solution == question.correct_answer.lower():
                print("7 CRORE!!!!")
                self.score+=1
            else:
                print(f"WRONG! The correct answer is: {question.correct_answer}")
            print(f"your current score is {self.score}/{self.question_number}\n")
        print(f"you have completed the quiz.your final score is {self.score}/5")

    def still_has_question(self):
        if self.question_number<5:
            return True
        else:
            return False
