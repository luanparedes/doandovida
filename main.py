from controller.screenmanagement import ScreenManagement
from model.dao import Dao
from kivymd.app import MDApp
from kivy.lang import Builder

#_version__ = '1.0.1510'

# Register KV files
Builder.load_file('view/MainScreen.kv')
Builder.load_file('view/LoginScreen.kv')
Builder.load_file('view/CreateUser.kv')
Builder.load_file('view/Settings.kv')
Builder.load_file('view/InfoBloodCenterCard.kv')
Builder.load_file('view/AboutCard.kv')
Builder.load_file('view/AboutDonationPage.kv')
Builder.load_file('view/CustomMap.kv')
Builder.load_file('view/HomePage.kv')
Builder.load_file('view/QuizPage.kv')


class MainProgram(MDApp):
    def build(self):
        self.title = 'Doando Vida - Ajude quem precisa!'
        self.icon = 'Assets/logo.png'
        self.theme_cls.primary_palette = Dao.get_saved_config(Dao())[1]
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '300'
        self.theme_cls.theme_style = Dao.get_saved_config(Dao())[0]

        return ScreenManagement()


if __name__ == '__main__':
    MainProgram().run()
