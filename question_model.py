import random
from data import question_data
class Question:
    def __init__(self,question,correct_answer):
        self.question=question
        self.correct_answer=correct_answer

random_value=random.choice(question_data)
ques_1=Question(random_value["question"],random_value["correct_answer"])
