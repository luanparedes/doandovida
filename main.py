from controller.screenmanagement import ScreenManagement
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

# Configuring window minimum size
Window.minimum_width, Window.minimum_height = (700, 500)

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
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'Gray'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.accent_hue = '300'
        self.theme_cls.theme_style = 'Dark'

        return ScreenManagement()


if __name__ == '__main__':
    MainProgram().run()
