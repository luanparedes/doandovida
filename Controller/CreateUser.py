from Model.Dao import Dao
from Model.Donator import Donator
from Controller.DialogAlerts import AlreadyHaveEmailDialog
from kivy.uix.screenmanager import Screen


class CreateUser(Screen):
    user = Donator()

    def __init__(self):
        super(CreateUser, self).__init__()
        self.name = 'newuser'

    def to_login_screen(self):
        self.parent.screen = 'login'

    def create_user_action(self):
        dao = Dao()
        self.create_user()
        dao.add_user(self.user)

    def create_user(self):
        self.user.email = self.ids.email.text
        self.user.password = self.ids.password.text
        self.user.name = self.ids.name.text
        self.user.cpf = self.ids.cpf.text
        self.user.rg = self.ids.rg.text
        self.user.adress.cep = self.ids.cep.text
        self.user.adress.neighborhood = self.ids.neighborhood.text
        self.user.adress.street = self.ids.street.text
        self.user.adress.number = int(self.ids.number.text)
        self.user.adress.complement = self.ids.complement.text
        self.user.adress.city = self.ids.city.text
        self.user.adress.state = self.ids.state.text
        self.user.tel = self.ids.tel.text
        self.user.cel = self.ids.cel.text
        self.user.height = float(self.ids.myheight.text)
        self.user.weight = int(self.ids.myweight.text)
        self.user.blood_type = self.ids.blood.text

    def on_verify_email(self):
        if self.ids.email.text != '':
            if Dao.verify_email(self, self.ids.email.text):
                AlreadyHaveEmailDialog()
