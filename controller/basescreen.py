from model.donator import Donator
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from datetime import datetime as dt
import datetime


class BaseScreen:
    #Properties
    user_name = StringProperty('')
    user_mail = StringProperty('')
    user_age = StringProperty('')
    user_gender = StringProperty('')
    user_weight = StringProperty('')
    user_is_active = BooleanProperty(False)

    quiz_points = StringProperty('0')
    energy = StringProperty('5')
    date = StringProperty('')
    next_donation = StringProperty('')

    def __init__(self):
        self.user = Donator()
        self.user.get_user_info()

        self.user_name = self.user.name
        self.user_mail = self.user.email
        self.user_age = '32'
        self.user_gender = self.user.gender
        self.user_weight = str(self.user.weight)

        self.date = f'{self.user.time.day} - {self.user.time.month} - {self.user.time.year}'
        self.quiz_points = str(self.user.quiz_points)
        self.energy = str(self.user.energy)
        self.next_donation = '3 - 2 - 2022' #self.verify_next_donation_date()

    def verify_next_donation_date(self):
        data = f'{self.user.time.day}-{self.user.time.month}-{self.user.time.year}'
        pass
