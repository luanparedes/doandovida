from View.LoginScreen import LoginScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class Screens(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        LoginScreen()
        print('teste')
