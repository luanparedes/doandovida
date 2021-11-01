from controller.enums import OS
from model.quiz import Quiz
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy.properties import StringProperty, NumericProperty


class QuizPage(MDBottomNavigationItem):

    # Properties
    question = StringProperty()
    answer1 = StringProperty()
    answer2 = StringProperty()
    answer3 = StringProperty()

    question_size = NumericProperty()
    answers_size = NumericProperty()

    def __init__(self, **kwargs):
        super(QuizPage, self).__init__(**kwargs)

        self.quiz = Quiz()
        self.show_question()
        self.os_differences()

    # Actions
    def show_answer(self):
        # TODO creating action
        pass

    # Privates
    def show_question(self):
        question = self.quiz.show_next_question()

        self.question = question[0]
        self.answer1 = question[1]
        self.answer2 = question[2]
        self.answer3 = question[3]

    def os_differences(self):
        if OS.is_android.value or OS.is_ios.value:
            self.question_size = 32
            self.answers_size = 24
        else:
            self.question_size = 24
            self.answers_size = 18
