from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank=[]
random.shuffle(question_data)

for question in question_data[0:5]:
    ques = Question(question["question"], question["correct_answer"])
    question_bank.append(ques)
quiz_brain=QuizBrain(question_bank)
if quiz_brain.still_has_question():
    quiz_brain.next_question(question_bank)

