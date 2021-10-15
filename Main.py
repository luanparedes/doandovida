from kivymd.app import MDApp
from Controller.ScreenManagement import ScreenManagement
from kivy.lang import Builder

__version__ = '1.0.1510'

# Register KV files
Builder.load_file('View/MainScreen.kv')
Builder.load_file('View/LoginScreen.kv')
Builder.load_file('View/CreateUser.kv')
Builder.load_file('View/Settings.kv')
Builder.load_file('View/InfoBloodCenterCard.kv')


class MainProgram(MDApp):
    def build(self):
        self.title = 'Doando Vida - Ajude quem precisa!'
        self.icon = 'Assets/logo.png'
        self.create_settings()
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.accent_palette = 'Indigo'
        self.theme_cls.primary_hue = '300'
        self.theme_cls.theme_style = 'Dark'

        return ScreenManagement()


if __name__ == '__main__':
    MainProgram().run()
