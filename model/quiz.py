from model.dao import Dao
from random import randint


class Quiz:
    def __init__(self):
        self.question = None
        self.answer1 = None
        self.answer2 = None
        self.answer3 = None
        self.right_answer = None

        self.all_questions = []
        self.showed_before = []

        self.get_all_questions()

    def get_all_questions(self):
        questions = Dao.take_all_questions(Dao())

        for question in questions:
            self.question = question[1]
            self.answer1 = question[2]
            self.answer2 = question[3]
            self.answer3 = question[4]
            self.right_answer = question[5]

            self.all_questions.append([self.question, self.answer1, self.answer2, self.answer3, self.right_answer])

    def show_next_question(self):
        number = randint(0, len(self.all_questions)-1)

        if number in self.showed_before:
            self.show_next_question()

        self.showed_before.append(number)
        
        return self.all_questions[number]
