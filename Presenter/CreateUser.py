from Model.Dao import Dao
from Model.Donator import Donator
from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField


class CreateUser(Screen):
    properties = []
    user = Donator()

    def __init__(self):
        super(CreateUser, self).__init__()
        self.name = 'newuser'

    def to_login_screen(self):
        self.parent.screen = 'login'

    def create_user_action(self):
        self.create_list_inputs()
        Dao.add_user(self, self.user)

    def create_user(self):
        self.user.email = self.ids.email.text
        self.user.password = self.ids.password.text if self.ids.password.text == self.ids.confirm.text else 'null'
        self.user.name = self.ids.name.text
        self.user.cpf = self.ids.cpf.text
        self.user.rg = self.ids.rg.text
        self.user.adress.cep = self.ids.cep.text
        self.user.adress.neighborhood = self.ids.neighborhood.text
        self.user.adress.street = self.ids.street.text
        self.user.adress.number = self.ids.number.text
        self.user.adress.complement = self.ids.complement.text
        self.user.adress.city = self.ids.city.text
        self.user.adress.estate = self.ids.estate.text
        self.user.tel = self.ids.tel.text
        self.user.cel = self.ids.cel.text
        self.user.height = self.ids.myheight.text
        self.user.weight = self.ids.myweight.text
        self.user.blood_type = self.ids.blood.text
