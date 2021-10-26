from Controller.ScreenManagement import ScreenManagement
from Model.Dao import Dao
from kivymd.app import MDApp
from kivy.lang import Builder

#_version__ = '1.0.1510'

# Register KV files
Builder.load_file('View/MainScreen.kv')
Builder.load_file('View/LoginScreen.kv')
Builder.load_file('View/CreateUser.kv')
Builder.load_file('View/Settings.kv')
Builder.load_file('View/InfoBloodCenterCard.kv')
Builder.load_file('View/AboutCard.kv')


class MainProgram(MDApp):
    def build(self):
        self.title = 'Doando Vida - Ajude quem precisa!'
        self.icon = 'Assets/logo.png'
        self.theme_cls.primary_palette = Dao.get_saved_config(Dao())[1]
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.primary_hue = '700'
        self.theme_cls.accent_hue = '300'
        self.theme_cls.theme_style = Dao.get_saved_config(Dao())[0]

        return ScreenManagement()

if __name__ == '__main__':
    MainProgram().run()
