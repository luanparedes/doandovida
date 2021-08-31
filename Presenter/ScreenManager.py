from Presenter.LoginScreen import LoginScreen
from kivy.uix.screenmanager import ScreenManager


class Screens(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(LoginScreen())
