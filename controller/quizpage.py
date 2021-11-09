from controller.basescreen import BaseScreen
from controller.enums import OS
from model.quiz import Quiz
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty


class QuizPage(MDBottomNavigationItem, BaseScreen):
    # Properties
    question = StringProperty()
    answer1 = StringProperty()
    answer2 = StringProperty()
    answer3 = StringProperty()
    txt = StringProperty()

    question_size = NumericProperty()
    answers_size = NumericProperty()

    def __init__(self, **kwargs):
        super(QuizPage, self).__init__(**kwargs)

        self.quiz = Quiz()
        self.show_question()
        self.os_differences()

        self.bind(energy=self.update_energy_counter)

    # Actions
    def get_started(self, value):
        self.remove_widget(self.ids.get_started)
        self.remove_widget(self.ids.btn_get_started)

    # Privates
    def show_question(self):
        question = self.quiz.show_next_question()

        #self.energy = self.energy - 1

        if question is None:
            self.remove_widget(self.ids.quiz_game)
            self.remove_widget(self.ids.btn_answer)
            self.show_label_no_questions()
            return

        self.question = question[0]
        self.answer1 = question[1]
        self.answer2 = question[2]
        self.answer3 = question[3]

    def show_label_no_questions(self):
        label = MDLabel(text='Não temos perguntas novas nesse momento!')
        self.add_widget(label)

    def update_energy_counter(self, value):
        self.txt = str(self.energy - 1)

    def os_differences(self):
        if OS.is_android.value or OS.is_ios.value:
            self.question_size = 32
            self.answers_size = 24
        else:
            self.question_size = 24
            self.answers_size = 18
