from Model.Dao import Dao
from Presenter.DialogAlerts import WrongLoginDialog
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class LoginScreen(Screen):
    label_hyperlink = ObjectProperty()

    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)
        self.name = 'login'

    def to_mainpage_screen(self):
        if Dao.verify_user(self, "luan.simas.paredes@gmail.com".lower(), "Paredes@10102017"):
            self.parent.screen = 'mainpage'
        else:
            WrongLoginDialog()

    def to_newuser_screen(self):
        self.parent.screen = 'newuser'
