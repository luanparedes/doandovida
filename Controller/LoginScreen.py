from Model.Dao import Dao
from Controller.DialogAlerts import WrongLoginDialog
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    label_hyperlink = ObjectProperty()
    last_login = ObjectProperty()
    last_pass = ObjectProperty()

    def __init__(self, **kw):
        super(LoginScreen, self).__init__(**kw)
        self.name = 'login'

        self.remember_last_login()

    def to_mainpage_screen(self):
        login = self.ids.login_user.text
        password = self.ids.login_pass.text

        Dao.save_last_login(self, login, password)

        if Dao.verify_user(self, login.lower().strip(), password.strip()):
            self.parent.screen = 'mainpage'
        else:
            WrongLoginDialog()

    def to_newuser_screen(self):
        self.parent.screen = 'newuser'

    def remember_last_login(self):
        user = Dao.recover_last_login(self)

        try:
            self.last_login.text = user[0]
            self.last_pass.text = user[1]
        except:
            self.last_login.text = ""
            self.last_pass.text = ""
