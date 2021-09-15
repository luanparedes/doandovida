from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField


class CreateUser(Screen):
    def __init__(self):
        super(CreateUser, self).__init__()
        self.name = 'newuser'
