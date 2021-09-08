from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class LoginScreen(Screen):
    label_hyperlink = ObjectProperty()

    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)
        self.name = 'login'

    def to_newuser_screen(self):
        self.parent.screen = 'newuser'
